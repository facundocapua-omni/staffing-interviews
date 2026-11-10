#!/usr/bin/env python3
"""Mechanical rule checks for staffing-jd runs (spec §4.1 Acceptance, §5.4).

    check_jd.py <run-dir> [client-term ...] [--people name ...]

Reads the sandbox the runner left in <run-dir> and prints one JSON object per check
({text, passed, evidence}), for grading.json. Client terms are the names, brands and
domains that must not appear in a jd.md (pass none for an internal client); people are
names that must not appear in opportunity.md.
"""
import json
import re
import sys
from pathlib import Path

ORIGINS = ["handbook role", "handbook level", "handbook platform", "HR job description",
           "Propuesta", "presales", "supplied JD", "hiring lead", "suite rule"]
TAG = r"`\[(?:%s)\]`" % "|".join(re.escape(o) for o in ORIGINS)
TAGGED_LINE = re.compile(r"(?:\s*%s)+\s*$" % TAG)
TAGGED_SECTIONS = ("must have", "nice to have", "what the person will do")
ALLOCATION = re.compile(r"\bFTE\b|\ballocation\b|\b0\.5\b|\bM\d{1,2}\b|\bmonths? \d", re.I)
MONEY = re.compile(r"\$\s?\d|\bUSD\b|\brate card\b|\bhourly rate\b|\bsalary\b|\bmargin\b", re.I)


def sections(md: str) -> dict[str, list[str]]:
    out, current = {}, None
    for line in md.splitlines():
        h = re.match(r"^##\s+(.*)", line)
        if h:
            current = h.group(1).strip().lower()
            out[current] = []
        elif current is not None:
            out[current].append(line)
    return out


def check(text: str, passed: bool, evidence: str) -> dict:
    return {"text": text, "passed": passed, "evidence": evidence}


def main() -> None:
    run_dir = Path(sys.argv[1])
    args = sys.argv[2:]
    people = args[args.index("--people") + 1:] if "--people" in args else []
    client_terms = args[:args.index("--people")] if "--people" in args else args
    sandbox = run_dir / "sandbox"
    jds = sorted((sandbox / "opportunities").rglob("jd.md"))
    results = [check("At least one jd.md was written", bool(jds),
                     ", ".join(str(j.relative_to(sandbox)) for j in jds) or "none")]

    tiers, untagged, english, alloc, money, named, long_must, no_logistics = [], [], [], [], [], [], [], []
    for jd in jds:
        rel = jd.relative_to(sandbox / "opportunities")
        # The frontmatter's slug names the client on purpose; the export drops it (export.md).
        md = re.sub(r"\A---\n.*?\n---\n", "", jd.read_text(), flags=re.S)
        secs = sections(md)
        extra = [s for s in secs if re.search(r"plus|bonus|preferred|optional|required|knock", s)]
        if "must have" not in secs or extra:
            tiers.append(f"{rel}: sections {list(secs)}")
        for name in TAGGED_SECTIONS:
            for line in secs.get(name, []):
                if re.match(r"^\s*[-*]|^\s*\d+\.", line) and not TAGGED_LINE.search(line):
                    untagged.append(f"{rel} [{name}]: {line.strip()[:90]}")
        must = [l for l in secs.get("must have", []) if re.match(r"^\s*[-*]", l)]
        if len(must) > 12:
            long_must.append(f"{rel}: {len(must)} lines")
        if "logistics" not in secs:
            no_logistics.append(str(rel))
        eng = [l for l in md.splitlines() if re.search(r"english", l, re.I)]
        if not any(re.search(r"\bB2\b", l) for l in eng) or any(re.search(r"\b(C1|C2)\b", l) for l in eng):
            english.append(f"{rel}: {eng[:2]}")
        alloc += [f"{rel}: {l.strip()[:90]}" for l in md.splitlines() if ALLOCATION.search(l)]
        money += [f"{rel}: {l.strip()[:90]}" for l in md.splitlines() if MONEY.search(l)]
        for term in client_terms:
            named += [f"{rel}: '{term}' in {l.strip()[:80]}" for l in md.splitlines() if term.lower() in l.lower()]

    results += [
        check("Every jd.md has only the Must have and Nice to have tiers, with no weights", not tiers,
              "; ".join(tiers) or "Must have / Nice to have only"),
        check("Every Requirement and responsibility line closes with at least one origin tag", not untagged,
              "; ".join(untagged[:8]) or "all tagged"),
        check("Every jd.md sets English at B2", not english, "; ".join(english) or "B2 found in every jd.md"),
        check("Every jd.md keeps Must have to a short filter (12 lines or fewer)", not long_must,
              "; ".join(long_must) or "all within 12"),
        check("Every jd.md has a Logistics section", not no_logistics, "; ".join(no_logistics) or "all present"),
        check("No jd.md carries allocation (FTE, months)", not alloc, "; ".join(alloc[:5]) or "none found"),
        check("No jd.md carries rates, costs or salary", not money, "; ".join(money[:5]) or "none found"),
    ]
    if client_terms:
        results.append(check(f"No jd.md names the client ({', '.join(client_terms)})", not named,
                             "; ".join(named[:6]) or "none found"))

    if people:
        opp = "\n".join(f.read_text() for f in (sandbox / "opportunities").rglob("opportunity.md"))
        hits = [p for p in people if p.lower() in opp.lower()]
        results.append(check(f"opportunity.md names no person ({', '.join(people)})", not hits,
                             ", ".join(hits) or "none found"))

    timing = json.loads((run_dir / "timing.json").read_text())
    outside = [f for t in timing["turns"] for f in t["writes_outside_sandbox"]]
    results.append(check("No file is written outside the sandbox", not outside, "; ".join(outside) or "none"))

    turn1 = (run_dir / "turn-1.jsonl").read_text()
    early = re.findall(r'"file_path":\s*"([^"]*jd\.md)"', turn1)
    results.append(check("Turn 1 writes no jd.md before the answers", not early, ", ".join(early) or "none"))

    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
