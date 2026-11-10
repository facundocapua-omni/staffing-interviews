#!/usr/bin/env python3
"""Run one acceptance case of a staffing-* skill in its own sandbox, one turn at a time (spec §5.2).

    run_case.py <evals.json> <handle> <run-dir> setup
    run_case.py <evals.json> <handle> <run-dir> turn <n> [--reply-file <file> | --text <text>]

`setup` builds <run-dir>/sandbox: empty opportunities/ and people/, so the tree root
resolves there, and the case's input files copied into inbox/, mutated when the case
says so. Turn 1 sends the case's prompt; a later turn resumes the same session with a
reply (the hiring lead's answers). Each turn saves its stream to turn-<n>.jsonl, its
final message to outputs/chat-turn-<n>.md, and copies every artifact the sandbox now
holds into outputs/ for the eval viewer.

Runs load only project settings plus staffing/.claude/settings.json, so user-level
plugins (remember, the learning output style) stay out of the sandbox.
"""
import json
import re
import shutil
import subprocess
import sys
import time
import zipfile
from pathlib import Path

STAFFING = Path(__file__).resolve().parent.parent
ACCEPTANCE = STAFFING / "tests" / "acceptance"
HANDBOOK = Path.home() / "Workspace/martech/structure/src/content/docs"
MODEL = "claude-opus-5-5"
REPLY_MARK = "<!-- reply -->"

# Per-command rules: auto mode refuses a run with Bash allowed whole. They still deny
# some compound commands and file names with brackets; writes_outside() checks after
# every turn that nothing landed outside the sandbox.
ALLOWED_TOOLS = [
    "Read", "Glob", "Grep", "Write", "Edit", "Skill",
    f"Read({STAFFING}/.claude/**)", f"Read({STAFFING}/GLOSSARY.md)", f"Read({HANDBOOK}/**)",
    "Bash(markitdown:*)", "Bash(textutil:*)", "Bash(python3:*)", "Bash(node:*)",
    "Bash(ls:*)", "Bash(cp:*)", "Bash(mkdir:*)", "Bash(find:*)", "Bash(grep:*)",
    "Bash(head:*)", "Bash(tail:*)", "Bash(wc:*)", "Bash(date:*)", "Bash(cat:*)",
    "Bash(cd:*)", "Bash(pwd)", "Bash(dirname:*)", "Bash(test:*)",
]


def rewrite_zip_member(path: Path, member: str, edit) -> None:
    """Replace one XML member of an Office file in place, leaving every other member untouched."""
    tmp = path.with_suffix(path.suffix + ".tmp")
    with zipfile.ZipFile(path) as src, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as dst:
        for item in src.infolist():
            data = src.read(item.filename)
            if item.filename == member:
                new = edit(data.decode("utf-8"))
                if new == data.decode("utf-8"):
                    raise SystemExit(f"mutation changed nothing in {member}")
                data = new.encode("utf-8")
            dst.writestr(item, data)
    tmp.replace(path)


def docx_years_8(inbox: Path) -> None:
    """jd-supplied-contradiction: the supplied JD asks 8 years, against 13 in level-equivalence.md."""
    (docx,) = inbox.glob("*.docx")

    def edit(xml: str) -> str:
        at = xml.index("Años de experiencia")
        head, tail = xml[:at], xml[at:]
        tail = re.sub(r"(<w:t[^>]*>)1(</w:t>)", r"\g<1>8\2", tail, count=1)
        tail = re.sub(r"(<w:t[^>]*>)3(</w:t>)", r"\1\2", tail, count=1)
        return head + tail

    rewrite_zip_member(docx, "word/document.xml", edit)


def xlsx_line4_architect(inbox: Path) -> None:
    """jd-architect-line: "Architect" as the Client's Role Name on P&L line 4 (Labor Estimate row 13)."""
    (xlsx,) = inbox.glob("*.xlsx")
    rewrite_zip_member(
        xlsx, "xl/worksheets/sheet5.xml",
        lambda xml: xml.replace('<c r="E13" s="278"/>',
                                '<c r="E13" s="278" t="inlineStr"><is><t>Architect</t></is></c>', 1),
    )


MUTATIONS = {"docx_years_8": docx_years_8, "xlsx_line4_architect": xlsx_line4_architect}


def load_case(evals_path: Path, handle: str) -> dict:
    evals = json.loads(evals_path.read_text())["evals"]
    return next(e for e in evals if e["handle"] == handle)


def setup(case: dict, run_dir: Path) -> None:
    sandbox = run_dir / "sandbox"
    if sandbox.exists():
        raise SystemExit(f"{sandbox} exists: use a fresh run dir")
    for sub in ("opportunities", "people", "inbox"):
        (sandbox / sub).mkdir(parents=True)
    for rel in case["files"]:
        shutil.copy2(ACCEPTANCE / rel, sandbox / "inbox" / Path(rel).name)
    if case.get("mutation"):
        MUTATIONS[case["mutation"]](sandbox / "inbox")
    (run_dir / "outputs").mkdir(exist_ok=True)
    (run_dir / "eval_metadata.json").write_text(json.dumps({
        "eval_id": case["id"], "eval_name": case["handle"],
        "prompt": case["prompt"], "assertions": case.get("expectations", []),
    }, indent=2, ensure_ascii=False))


def reply_text(path: Path) -> str:
    text = path.read_text()
    return text.split(REPLY_MARK, 1)[1].strip() if REPLY_MARK in text else text.strip()


def collect(run_dir: Path) -> None:
    """Copy every artifact under the sandbox tree into outputs/, path flattened with '__'."""
    sandbox, outputs = run_dir / "sandbox", run_dir / "outputs"
    for f in sorted((sandbox / "opportunities").rglob("*")) + sorted((sandbox / "people").rglob("*")):
        if f.is_file() and f.suffix in (".md", ".pdf"):
            shutil.copy2(f, outputs / "__".join(f.relative_to(sandbox).parts))
    listing = sorted(str(p.relative_to(sandbox)) for p in sandbox.rglob("*") if p.is_file())
    (outputs / "tree.txt").write_text("\n".join(listing) + "\n")


def writes_outside(since: float) -> list[str]:
    """Files under staffing/ (outside tests/runs/) or the handbook modified since the turn began."""
    hits = []
    for root in (STAFFING, HANDBOOK):
        for f in root.rglob("*"):
            if "tests/runs" in str(f) or ".remember" in f.parts:
                continue
            try:
                if f.is_file() and f.stat().st_mtime > since:
                    hits.append(str(f))
            except OSError:
                pass
    return hits


def turn(case: dict, run_dir: Path, n: int, text: str) -> None:
    session_file = run_dir / "session.json"
    # The prompt goes through stdin: a reply opening with "- " would parse as an option.
    cmd = [
        "claude", "-p", "--model", MODEL,
        "--output-format", "stream-json", "--verbose",
        "--setting-sources", "project,local",
        "--settings", str(STAFFING / ".claude/settings.json"),
        "--permission-mode", "acceptEdits",
        "--allowedTools", *ALLOWED_TOOLS,
    ]
    if n > 1:
        cmd += ["--resume", json.loads(session_file.read_text())["session_id"]]
    began = time.time()
    stream = run_dir / f"turn-{n}.jsonl"
    with stream.open("w") as out:
        proc = subprocess.run(cmd, cwd=run_dir / "sandbox", input=text, stdout=out,
                              stderr=subprocess.PIPE, text=True)
    result = next((json.loads(l) for l in reversed(stream.read_text().splitlines())
                   if l.startswith("{") and json.loads(l).get("type") == "result"), None)
    if result is None:
        raise SystemExit(f"turn {n}: no result event (exit {proc.returncode}): {proc.stderr[-2000:]}")
    session_file.write_text(json.dumps({"session_id": result["session_id"]}))
    (run_dir / "outputs" / f"chat-turn-{n}.md").write_text(result.get("result") or "")
    timing_file = run_dir / "timing.json"
    timing = json.loads(timing_file.read_text()) if timing_file.exists() else {"turns": []}
    usage = result.get("usage", {})
    timing["turns"].append({
        "turn": n, "duration_ms": result.get("duration_ms"), "cost_usd": result.get("total_cost_usd"),
        "num_turns": result.get("num_turns"), "is_error": result.get("is_error"),
        "output_tokens": usage.get("output_tokens"),
        "permission_denials": result.get("permission_denials", []),
        "writes_outside_sandbox": writes_outside(began),
    })
    timing["total_duration_seconds"] = round(sum((t["duration_ms"] or 0) for t in timing["turns"]) / 1000, 1)
    timing_file.write_text(json.dumps(timing, indent=2))
    collect(run_dir)
    print(json.dumps(timing["turns"][-1], indent=2))


def main() -> None:
    evals_path, handle, run_dir, action = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3]), sys.argv[4]
    case = load_case(evals_path, handle)
    run_dir.mkdir(parents=True, exist_ok=True)
    if action == "setup":
        setup(case, run_dir)
        return
    n = int(sys.argv[5])
    if n == 1:
        text = case["prompt"]
    elif sys.argv[6] == "--reply-file":
        text = reply_text(ACCEPTANCE / sys.argv[7])
    else:
        text = sys.argv[7]
    turn(case, run_dir, n, text)


if __name__ == "__main__":
    main()
