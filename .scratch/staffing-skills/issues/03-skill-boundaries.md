# Skill boundaries

Type: grilling
Status: resolved
Blocked by: none
Map: [Staffing skills suite](../map.md)

## Question

How is the suite cut into skills?

Candidate cuts: one skill per artifact (four) plus a shared reference for conventions and sources of truth; a single staffing skill with modes; or another cut.

Decide:

- The cut, including which skill owns the Oportunidad status summary (shaped in [Oportunidad status summary](10-opportunity-status-summary.md)) and the per-Posición comparison table (new outputs from [Disk layout of the chain](02-chain-disk-layout.md)).
- Note from [JD structure](04-jd-structure.md): the JD step runs per Oportunidad and also writes `opportunity.md` from the Propuesta and P&L, and the suite has a level-equivalence reference table.
- How shared conventions (glossary terms, the no-verdict rule, language, sources of truth, disk layout) reach every skill without being duplicated.
- Each skill's trigger description: what you say that should invoke it, and what must not.

Load `writing-for-agents` for this ticket.

From [Scorecards: dimensions and scale](06-scorecards.md): the Dimensiones and the `Proposed:` marker are shared conventions every skill uses.

From [Unified Guía de entrevista](07-interview-guide.md):
- No blank Scorecards are written any more. Decide which skill builds the evidence per Dimensión from the transcript (a Scorecard step, or the Debrief skill, depending on [Unified Debrief](08-debrief.md)).
- Decide where the question bank lives inside the suite: pluggable content per platform and per track, read by the Guía skill.

From [Unified Debrief](08-debrief.md):
- The Debrief skill builds the evidence per Dimensión from the transcripts, inside the Debrief. There is no Scorecard step and no Scorecard file. Still for this ticket: whether a standalone action is needed at all, e.g. to draft one Entrevista's Calificaciones before the others arrive.
- The Debrief is one per Candidato and is updated after each Entrevista, keeping the hiring lead's Resolutions and Decisions.

From [Oportunidad status summary](10-opportunity-status-summary.md):
- The Resumen de estado is read-only over the whole Oportunidad: it reads `opportunity.md`, every `jd.md` and `shortlist.md`, and each Candidato's `match-evaluation.md`, `interviews/` and `debrief.md`, and writes only `status-<YYYY-MM-DD>.md`. Decide which skill owns it, or whether it is its own.
- The comparison table is not part of it: it stays an on-request output for the hiring lead, not stored. Decide which skill produces it.
- Trigger wording to tell apart: "status of <Oportunidad>" / "todos los candidatos revisados para <Oportunidad>" (Resumen de estado) vs "compare the Candidatos for <Posición>" (comparison table).

From [Acceptance cases](09-acceptance-cases.md):
- The skills resolve the tree root (`opportunities/`, `people/`) from the working directory, never from a fixed path, so that acceptance runs write into a sandbox.
- Each skill's skill-creator evals point at `~/Workspace/leadership/staffing/tests/acceptance/<handle>/`. The handles are English.
- [Debrief inputs outside the suite's shape](12-debrief-inputs-outside-the-suite-shape.md) may add an action, such as importing an old Debrief, that this cut has to place.

From [Debrief inputs outside the suite's shape](12-debrief-inputs-outside-the-suite-shape.md):
- No import action is needed. A Candidato in progress at cutover enters at their next step; the hiring lead copies the old files into the suite's tree and the skills identify them by content.
- The Debrief skill offers to run the Evaluación de match when there is none, as the Guía skill does. Decide how one skill offers another's action.

From [Handbook gaps for JDs](11-handbook-gaps-for-jds.md):
- The JD skill reads two suite references: the level equivalence table and a folder with the HR versions of the Descripciones de cargo, converted to Markdown. Decide where they live. They sit next to each other and are copied into the suite, unlike the handbook, which is read in place.

## Answer

Grilled 2026-10-22 (Q1–Q13) and 2026-10-27 (the rest, with Q13 and Q14 asked again after the tickets closed in between). No term added to [GLOSSARY.md](../../../GLOSSARY.md).

**Facts that shaped the answer** (checked 2026-10-27 with Claude Code 2.1.311 on a mock tree outside the workspace, since removed)

- Claude Code loads `.claude/skills/` and `CLAUDE.md` from the start directory and every parent, also outside a git repo. A session started in `tests/runs/<handle>/` sees the suite's skills.
- A folder without `SKILL.md` inside `.claude/skills/` is ignored silently, and the docs say nothing about it. `synced` and `anthropic-skills` are reserved names there.
- `${CLAUDE_SKILL_DIR}` is the skill's own folder. `${CLAUDE_PROJECT_DIR}` is the start directory, not the folder that holds `.claude/`.
- `human-resources` is a plugin synced from claude.ai, with id `human-resources@synced`. Setting `"human-resources@synced": false` in `enabledPlugins` removes it. Outside a git repo, though, Claude Code reads a project `.claude/settings.json` only from the start directory itself. `skillOverrides` does not reach plugin skills. `permissions.deny` blocks a skill but leaves it listed.

**The cut**

Five skills, one per artifact, all model-invoked, all in this project's `staffing/.claude/`. Nothing is global: the suite works only in this project, for staffing.

| Skill | Writes | Also owns |
|---|---|---|
| `staffing-jd` | `opportunity.md` and every `jd.md` | adding or changing a Posición, updating a JD, listing the evaluations a JD update made stale |
| `staffing-match` | `people/<p>/`, `<op>--<pos>/`, `match-evaluation.md` | a batch of CVs, re-evaluation, the comparison table (on request, not stored), `shortlist.md` edits as dictated |
| `staffing-interview-guide` | `interviews/<YYYY-MM-DD>/interview-guide.md` | the question bank |
| `staffing-debrief` | `debrief.md` | the Calificaciones built from transcripts |
| `staffing-status` | `status-<YYYY-MM-DD>.md` | nothing else: read-only over the whole Oportunidad |

- A new action goes to the skill that owns the file it writes. A new skill appears only for an artifact with no owner. No import action is needed ([Debrief inputs outside the suite's shape](12-debrief-inputs-outside-the-suite-shape.md)).
- No standalone action drafts one Entrevista's Calificaciones: the Debrief is incremental from the first Entrevista.
- Only the hiring lead decides `shortlist.md`. Claude edits it only as dictated, through `staffing-match`.
- Each skill exports its own artifact through one shared converter (`npx md-to-pdf`).

**Match batches**

- For a batch without Posiciones named, the skill proposes a person → Posición table, sorted alphabetically and never saved. The hiring lead confirms it in one round, which also asks whether each person is internal or external (external by default). A person on two Posiciones is two Candidatos. An unassigned CV gets no folder and is listed in the final report.
- In a batch, one subagent per Candidato sees only that person's files and the JD. A single CV is evaluated directly.
- Files are grouped per person and copied, under their original names, to `people/<p>/`. An existing person's folder is reused, and the skill asks when unsure.

**Shared reference**

- `.claude/shared/`, outside the skills scan: `conventions.md`, `disk-layout.md`, `dimensions.md`, `level-equivalence.md`, `export.md` plus its script, and `hr-job-descriptions/<role>-<level>.md`, the HR Descripciones de cargo converted to Markdown.
- Each `SKILL.md` reads them as `${CLAUDE_SKILL_DIR}/../../shared/<file>`, never through `${CLAUDE_PROJECT_DIR}`, which breaks when a session starts in a subfolder.
- A two-line workspace `CLAUDE.md` only points to `.claude/shared/` and to `GLOSSARY.md`.

**Inside a skill folder**

- `SKILL.md` holds the steps and the rules every branch needs.
- `template.md`, next to it, holds the artifact's template and is read at the writing step.
- Material only some branches reach sits in sibling files behind a pointer: the Guía skill's `question-bank/platforms/<platform>.md` and `question-bank/tracks/<track>.md`, the match skill's instructions for a batch subagent.

**Conventions every skill follows** (in `conventions.md`)

- **Required and offered inputs.** Each skill's input list marks every input as required or offered.
  - Required and missing: the skill stops and offers to run the skill that produces it. Examples: the Guía with no Evaluación de match, the match skill with no `jd.md`.
  - Offered and missing: the skill offers once, goes on when declined, and says in its artifact what is missing. Example: the Debrief with no Evaluación de match.
  - `staffing-status` neither stops nor offers: it reports what is pending as facts.
- **Offering another skill's action.** The offer is one yes/no question that names the skill. On yes, the current skill invokes the other through the Skill tool in the same session, then resumes the step that needed it with the new artifact.
- **Kept inputs.** Every input is kept next to what it feeds and identified by content: files under their original names, pasted text as `pasted-<YYYY-MM-DD>.md`. `staffing-jd` keeps the Propuesta, the P&L and any brief or supplied JD in `opportunities/<op>/`, so the P&L, with its rates, lives there.
- **Tree root.** The root is the first folder, from the working directory upward, that holds `opportunities/` or `people/`. When there is none, a skill that writes asks once before creating them, naming the path. `staffing-status` creates nothing and says it found no tree.

**JD update**

- Updating a JD lists the Candidatos whose Evaluación de match went stale (`jd_updated` differs from the JD's `updated`) and offers to run `staffing-match` on them: a batch, one subagent per Candidato. It never re-evaluates on its own.

**Trigger descriptions**

Drafts, each opening on the glossary term the hiring lead uses, one trigger per branch, positive. The final wording comes out of skill-creator's description optimization.

```
staffing-jd: JDs and opportunity.md for an Oportunidad, from its Propuesta and P&L,
  a brief or a supplied JD. Use when starting an Oportunidad, adding or changing a
  Posición, updating a JD, or exporting one to PDF.

staffing-match: Evaluación de match of Candidatos against a Posición's JD, from CVs,
  profiles and internal history. Use when evaluating one CV or a batch, re-evaluating
  after a JD change, comparing a Posición's Candidatos, editing its Shortlist as
  dictated, or exporting an evaluation.

staffing-interview-guide: Guía de entrevista for one Entrevista of one Candidato,
  usable by any Entrevistador, delegated ones included. Use when preparing or planning
  an Entrevista, splitting a Posición across Entrevistas, or writing interview
  questions for a Candidato.

staffing-debrief: Debrief of a Candidato's Entrevistas from transcripts, notes and
  Scorecards, with Proposed Calificaciones per Dimensión. Use after an Entrevista,
  when another one is added, when rating or scoring a Candidato, or exporting it.

staffing-status: Resumen de estado of an Oportunidad for management: each Candidato's
  Etapa per Posición and what is pending. Use when asked for an Oportunidad's status,
  which Candidatos were reviewed or are pending, or a status update for dirección.
```

| Look-alike request | Skill |
|---|---|
| "compare the Candidatos for <Posición>" | `staffing-match` |
| "todos los candidatos revisados para <Oportunidad>" | `staffing-status` |
| "build the scorecard for X", "rate X" | `staffing-debrief` |
| "interview questions for <Posición>" with no Candidato | `staffing-interview-guide`, which asks for the Candidato |

- What must not trigger a skill lives in its trigger evals, not in its description: Spanish and English phrasings for every branch, with negatives drawn from the look-alikes above and from the `human-resources` requests.

**Plugin collision**

- `human-resources`' `interview-prep` and `recruiting-pipeline` collide with the Guía and status triggers. `"human-resources@synced": false` goes in `enabledPlugins` of `staffing/.claude/settings.json` only, never at user level.
- Sessions start at `staffing/`. Acceptance runs in `tests/runs/<handle>/` get the same file, through `--settings` or a `.claude/settings.json` in the run folder, whichever skill-creator's runner accepts.

**Acceptance runs**

- The sandbox is `tests/runs/<handle>/`, with no git: Plan B is dropped and the map's "no git here" holds. The run setup creates empty `opportunities/` and `people/` in it, so the tree root resolves there.
- Each skill's evals point at `tests/acceptance/<handle>/`, with English handles ([Acceptance cases](09-acceptance-cases.md)).
- The first build step is a smoke check with `claude -p` from a run folder: the `staffing-*` skills are listed, no `human-resources:*` skill is, and a skill reads a file from `../../shared/`.

**Handed to other tickets**

- [Disk layout of the chain](02-chain-disk-layout.md): amended with kept inputs, `pasted-<YYYY-MM-DD>.md`, the tree root rule and dictated Shortlist edits.
- [Acceptance cases](09-acceptance-cases.md): amended with the sandbox path, its setup and its settings.
- [Handbook gaps for JDs](11-handbook-gaps-for-jds.md): amended with the path of the Descripciones de cargo folder.
