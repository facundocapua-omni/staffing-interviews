# Staffing skills suite: spec

Assembled 2026-10-27 from the [Staffing skills suite map](map.md) once no tickets remained. Each section links the tickets that hold its reasoning. Where a ticket and this spec differ, the spec holds: it applies every amendment between tickets. Domain terms are those in [GLOSSARY.md](../../GLOSSARY.md).

A few calls no ticket made had to be made while assembling. Each is marked *(call N)* where it applies and listed in [§7](#7-calls-made-while-assembling); the hiring lead confirmed them on 2026-10-27.

**Reading order for a build session:** §1–§3, then the section in §4 of the skill being built, then §5 for its cases. §6 is the build order.

## 1. The suite

Five model-invoked skills, one per artifact, chained JD → Evaluación de match → Guía de entrevista → Debrief, plus the Resumen de estado that reads them all. They live in `staffing/.claude/skills/` and work only in this project. ([Skill boundaries](issues/03-skill-boundaries.md))

| Skill | Writes | Also owns | Read by |
|---|---|---|---|
| `staffing-jd` | `opportunity.md` and every `jd.md` | adding or changing a Posición; updating a JD; listing the evaluations a JD update made stale | recruiting (JD as PDF); `opportunity.md` stays with the hiring lead |
| `staffing-match` | `people/<p>/`, `<op>--<pos>/`, `match-evaluation.md` | a batch of CVs; re-evaluation; the comparison table (on request, not stored); `shortlist.md` edits as dictated | the hiring lead; shareable as PDF |
| `staffing-interview-guide` | `interviews/<YYYY-MM-DD>/interview-guide.md` | the question bank | every Entrevistador, delegated ones included (as PDF) |
| `staffing-debrief` | `debrief.md` | the Calificaciones built from transcripts | the hiring lead, their managers and recruiting |
| `staffing-status` | `status-<YYYY-MM-DD>.md` | nothing else: read-only over the whole Oportunidad | management (dirección) |

- A new action goes to the skill that owns the file it writes. A new skill appears only for an artifact with no owner.
- `candidate-takehome-review` stays as it is, outside the chain. The hiring lead copies its report into the Candidato folder, where it is an optional input.
- The suite replaces the per-stack workspaces (`aem-`, `tl-`, `react-`, `td-interviews`). Stack specifics are pluggable content (the question bank), not separate skills.
- An Entrevista may be run by the hiring lead, a pair, or a delegated team member.

**Out of scope**

- Packaging as a plugin for other leads: this is a personal suite.
- Publishing a JD externally, or a client-facing version.
- Integrations: ATS, HRIS, meeting recorders.
- Interviews run by the client.
- Redesigning `candidate-takehome-review`.
- Spanish versions of the templates.
- A portfolio status across Oportunidades; purging a person's data (status snapshots are never scrubbed).
- Anything after the hiring lead's decision: offer, acceptance, onboarding, an internal's assignment.
- Writing the handbook's `evaluation-criteria/` pages and archiving the per-stack workspaces: execution after the build (§6).

## 2. Project setup

```
staffing/                          # sessions start here
  CLAUDE.md                        # two lines: points to .claude/shared/ and GLOSSARY.md
  GLOSSARY.md
  .claude/
    settings.json                  # "enabledPlugins": { "human-resources@synced": false }
    shared/                        # §3; outside the skills scan
    skills/
      staffing-jd/                 # SKILL.md, template.md
      staffing-match/              # SKILL.md, template.md, batch-subagent.md
      staffing-interview-guide/    # SKILL.md, template.md, question-bank/platforms/<platform>.md,
                                   #   question-bank/tracks/<track>.md
      staffing-debrief/            # SKILL.md, template.md
      staffing-status/             # SKILL.md, template.md
  opportunities/  people/          # the tree (§3.2)
  tests/
    acceptance/<handle>/           # case inputs and frozen fixtures (§5)
    runs/<handle>/                 # one sandbox per run (§5)
```

**Inside a skill folder**

- `SKILL.md` holds the steps and the rules every branch needs.
- `template.md` holds the artifact's template and is read at the writing step. `staffing-jd`'s holds both `opportunity.md` and `jd.md`.
- Material only some branches reach sits in a sibling file behind a pointer: the question bank, the batch subagent's instructions.
- Shared files are read as `${CLAUDE_SKILL_DIR}/../../shared/<file>`.

**Platform facts** (checked 2026-10-27 on Claude Code 2.1.311; they shaped this layout)

- Claude Code loads `.claude/skills/` and `CLAUDE.md` from the start directory and every parent, also outside a git repo. A session started in `tests/runs/<handle>/` sees the suite.
- A folder inside `.claude/skills/` without a `SKILL.md` is ignored silently. `synced` and `anthropic-skills` are reserved names there.
- `${CLAUDE_SKILL_DIR}` is the skill's own folder. `${CLAUDE_PROJECT_DIR}` is the start directory, not the folder holding `.claude/`, so it breaks when a session starts in a subfolder.
- Outside a git repo, a project `.claude/settings.json` is read only from the start directory. `skillOverrides` does not reach plugin skills; `permissions.deny` blocks a skill but leaves it listed.
- The `human-resources` plugin (`human-resources@synced`, synced from claude.ai) collides with the Guía and status triggers through `interview-prep` and `recruiting-pipeline`. It is disabled in `staffing/.claude/settings.json` only, never at user level.
- *(Smoke check, 2026-10-27.)* `${CLAUDE_SKILL_DIR}/../../shared/` resolves correctly, but from `tests/runs/<handle>/` it lies outside the working directory, so `claude -p` denies the Read. A session started in `staffing/` needs no grant.

**Sources of truth**

- The handbook, `~/Workspace/martech/structure/src/content/docs/`, is read in place and never copied: `roles/`, `reference/career-levels.md`, `reference/tracks.md`, `career-paths/<track>.md`, `technologies/<platform>.md`, `evaluation-criteria/`. A Posición may add Requisitos of its own.
- The HR Descripciones de cargo are the exception: they are frozen, so the suite keeps converted copies (§3.5).
- The question bank lives in the suite, not in the handbook, because Candidatos internos can read the handbook.

## 3. Shared reference

Each subsection is the content of one file in `.claude/shared/`. The build words it for the agent (`writing-for-agents`).

### 3.1 `conventions.md`

([Skill boundaries](issues/03-skill-boundaries.md), [Scorecards](issues/06-scorecards.md), [Disk layout](issues/02-chain-disk-layout.md))

**Language**

- Chat with the hiring lead in Spanish. Skills and every deliverable are in English; Spanish only on explicit request.
- Deliverables use each glossary term's English name (Opportunity, Position, Must have, Nice to have, Candidate, Match evaluation, Evidence level, Point to probe, Interview, Interview guide, Interviewer, Rating, Dimension, Discrepancy, Stage, Status summary). Chat uses the Spanish one. Fixed lines the tickets wrote with Spanish terms take the English names *(call 9)*.
- Quotes stay in their original language, followed by an English translation in brackets *(call 10)*.

**The hiring lead decides**

- Claude gives evidence and clearly marked proposals. Every judgment field is the hiring lead's: the Decision and its calibrated level, a Discrepancia's Resolution, the Shortlist and its order.
- No artifact carries a verdict, recommendation, ranking, score, total, average, weight, threshold, count of Requisitos or Dimensiones ("8/11"), growth velocity, risk level, or a summary that concludes. A threshold is a verdict reached by arithmetic; importance comes from the Must have / Nice to have tiers and from the hiring lead.
- Wherever Claude lists Candidatos, they are in alphabetical order. Only the Shortlist has another order, the hiring lead's.
- Explanations are factual (different questions asked, different coverage), never a hypothesis about a person.
- When in doubt, ask instead of concluding.

**Marking what Claude wrote**

- In a document where humans also write, every value Claude proposes carries the prefix `Proposed:` (e.g. `Proposed: Meets`). It survives a PDF export and needs no colour or extra column. Claude never removes it. The hiring lead confirms a value by removing the prefix or changing the value.
- A document Claude writes entirely (the Evaluación de match, the Guía) says so once in its header instead.
- Claude's own proposals for a JD's Requisitos appear only in the intake round, marked `Proposed:`. What the hiring lead does not confirm is written to no file.

**Inputs**

Each skill's input table marks every input as one of:

- **Required.** When missing, the skill stops and offers to run the skill that produces it, or asks for it when no skill does.
- **Offered.** When missing, the skill offers once, goes on when declined, and says in its artifact what is missing.
- **Optional.** Read when present, never asked for *(call 1)*.

`staffing-status` neither stops nor offers: it reports what is missing as pending facts.

An offer is one yes/no question that names the skill. On yes, the current skill invokes the other through the Skill tool in the same session, then resumes the step that needed it with the new artifact.

**Kept inputs**

- Every input is kept next to what it feeds and identified by content, never by name: files under their original names, pasted text as `pasted-<YYYY-MM-DD>.md` (with a numeric suffix on collision, *call 8*).
- Where each goes:
  - Propuesta, P&L, brief, supplied JD → `opportunities/<op>/` (so the P&L, with its rates, lives there).
  - CV, public profile, internal history → `people/<p>/`.
  - Take-home report copy, recruiting's screening notes, English result → the Candidato folder `<op>--<pos>/` *(call 8)*.
  - Transcript, notes, brought Scorecards → `interviews/<YYYY-MM-DD>/`.

**Tree root**

- The root is the first folder, from the working directory upward, that holds `opportunities/` or `people/`. It is never a fixed path, so acceptance runs write into their sandbox.
- When there is none, a skill that writes asks once before creating both, naming the path. `staffing-status` creates nothing and says it found no tree.

**Staleness**

- An Evaluación de match is stale when its `jd_updated` differs from its JD's `updated`. Every skill that reads one says so. Re-evaluating is always the hiring lead's request.

**Client name**

- `opportunity.md` and the status summary name the real client. The JD and the Guía anonymise it ("a US-based global travel company"), even when a supplied JD names it, unless the client is internal.

**Salary** is recorded nowhere in the suite.

**Export** is on request, through the shared converter (§3.6).

### 3.2 `disk-layout.md`

([Disk layout](issues/02-chain-disk-layout.md), amended by [Unified Debrief](issues/08-debrief.md), [Status summary](issues/10-opportunity-status-summary.md) and [Skill boundaries](issues/03-skill-boundaries.md))

```
<root>/
  opportunities/<client>-<project>/
    opportunity.md                        # staffing-jd
    <Propuesta, P&L, brief, supplied JD>  # kept inputs, any name
    status-<YYYY-MM-DD>.md (+ .pdf)       # staffing-status; earlier dates kept
    <position-slug>/
      jd.md (+ jd.pdf)                    # staffing-jd
      shortlist.md                        # the hiring lead's; Claude edits it only as dictated
  people/<first>-<last>/
    <CV, public profile, internal history>          # any name, identified by content
    <op>--<position>/                               # one Candidato
      match-evaluation.md (+ .pdf)                  # staffing-match
      debrief.md (+ .pdf)                           # staffing-debrief, one per Candidato
      <take-home report copy, screening notes, English result>
      interviews/<YYYY-MM-DD>/                      # one per Entrevista
        interview-guide.md (+ .pdf)                 # staffing-interview-guide
        <transcript, notes, brought Scorecards>     # one file per Entrevistador, any name
```

- Person-first: everything about a person sits in `people/<p>/`, including an internal Candidato's earlier Debriefs in their other Candidato folders. `opportunities/` holds no personal data except Shortlist names and status summaries.
- The same person in two Posiciones is two Candidato folders under one person folder.
- A second Entrevista is another `interviews/<YYYY-MM-DD>/` with its own Guía. The Debrief stays one per Candidato.
- No status folders, no pipeline CSV, no separate candidate profile. The CV analysis lives only in the Evaluación de match; the Etapa is derived from which files exist (§4.5).

**Naming**

- Folders and files are in English. Generated artifacts have fixed names; inputs keep any name.
- Slugs are kebab-case ASCII: Oportunidad `<client>-<project>`, Posición from its title, person `<first>-<last>`. A numeric suffix only on collision. Dates are ISO.
- A Candidato folder is `<op>--<position>`: the Oportunidad slug, a double dash, the Posición slug.

**Frontmatter** (the path is the link skills follow; the frontmatter makes a forwarded or exported file self-describing)

| Artifact | Fields |
|---|---|
| `opportunity.md` | `opportunity`, `updated` *(call 5)* |
| `jd.md` | `opportunity`, `position`, `updated` *(call 5)* |
| `match-evaluation.md` | `opportunity`, `position`, `person`, `candidate_kind: internal \| external`, `date`, `jd_updated` |
| `interview-guide.md` | the same five, plus `interviewers` |
| `debrief.md` | the same five with `date` as the last update, plus `interviewers` (every Entrevistador across the Entrevistas) and `interviews` (the Entrevista dates, which are their folder names) |
| `status-<YYYY-MM-DD>.md` | `opportunity`, `date` |

**`shortlist.md`** is an ordered list, one Candidato per line: `<n>. <person-slug>: <note>` *(call 6)*.

### 3.3 `dimensions.md`

([Scorecards](issues/06-scorecards.md), amended by [Unified Guía](issues/07-interview-guide.md) and [Unified Debrief](issues/08-debrief.md))

**Scale.** A Calificación is Below, Meets or Exceeds the Posición's career level, or Not assessed. It is a word, never a number.

**Dimensiones.** Deliverables use these names and definitions verbatim.

| Block | Dimension | Definition |
|---|---|---|
| Soft | Communication | Explains ideas clearly, in a structure the listener can follow, for technical and non-technical audiences. |
| Soft | Problem Solving | Breaks an unfamiliar problem down, weighs options and trade-offs, and reaches an approach they can defend. |
| Soft | Collaboration | Works with others toward a shared result, credits the team, and handles disagreement constructively. |
| Soft | Growth Mindset | Learns from mistakes and feedback, is honest about gaps, and keeps skills current. |
| Soft | Ownership | Takes responsibility for outcomes end to end, including follow-through when things go wrong. |
| Soft | English | Understands and expresses technical and day-to-day content in English at the level the Posición requires. |
| Technical | Platform knowledge | Depth on the Posición's platform and its stack, across the sub-areas from the handbook or the JD. |
| Technical | Architecture & design | Designs solutions that fit the problem, weighing scalability, maintainability and trade-offs. |
| Technical | Code quality & practices | Produces and reviews work to team standards: testing, reviews, tooling, performance. |
| Technical | Debugging & troubleshooting | Finds and fixes problems methodically, including unfamiliar ones, with the right diagnostic tools. |
| Technical | Stack breadth | Works competently beyond their main layer: adjacent frontend, backend, devops and integrations. |
| Leadership | People leadership & mentoring | Grows and guides a team through mentoring, review and feedback, leading rather than doing everything themselves. |
| Leadership | Stakeholder & client management | Manages expectations, scope and difficult conversations with clients and internal stakeholders. |
| Leadership | Delivery ownership | Drives commitments to completion on time and at quality, tracked with KPIs. |

- Every Posición gets the 6 soft and the 5 technical Dimensiones.
- Leadership roles (Tech Leader L8, Expert, Manager, Director) add the 3 leadership Dimensiones and keep the full technical core, measured against their role: for a Director, Meets in Code quality means setting standards, not writing code.
- English is rated against the level the JD sets: B2 minimum, B1 as the exception. The Entrevista does not assess it; its result reaches the hiring lead separately. This is the one exception to "only interview evidence counts".

**What Meets means** (what changes by track and level; the Dimensiones themselves do not)

- The rubric lives in the handbook's `evaluation-criteria/`: soft and leadership in one shared page, the technical core one page per track. Skills only read it.
- While a rubric page is missing or `Pending`, individual-contributor tracks read `career-paths/<track>.md` and `reference/career-levels.md`, and leadership roles read `roles/<role>.md`. The artifact says "rubric pending: using career-paths" (or "using roles" for a leadership role, *call 14*).
- Platform knowledge's sub-areas come from `technologies/<platform>.md` (Stack by layer) and from the Posición's own Requisitos. They are collected as evidence and never rated one by one.
- When the handbook lacks the platform or the role (Sitecore, Software Architect), sub-areas and expectations come only from the JD's Requisitos. The skill says the handbook does not cover it and never invents a stack.

**Rating rules** (wherever a Calificación is proposed)

- Only interview evidence counts, never the CV.
- Not covered in the Entrevista: Not assessed, never a default value.
- Asked and followed up with no concrete example: Below, because that is evidence.
- A confident wrong answer counts against the Candidato more than an honest gap.
- No usable evidence: Not assessed, never inferred.

**Flags.** The lists are prompts, not a checklist: only what was observed is written, each flag with its evidence, and others may be added. The Guía draws its "Watch for" signals from them; the Debrief records them.

- Red: consistently bashes previous employers · cannot give specific examples · defensive when challenged · resistance to learning · takes all credit without mentioning the team · asks no questions · confident wrong answer.
- Green: honest about gaps and proposes how to address them · explains complex concepts clearly · discusses challenges respectfully · asks thoughtful questions about the team · acknowledges mistakes and lessons learned · enthusiastic about the domain · mentions helping others grow.

### 3.4 `level-equivalence.md`

([Handbook gaps for JDs](issues/11-handbook-gaps-for-jds.md); no official equivalence exists, so this table is the only one)

| Globant P&L | Handbook | HR job description | Years |
|---|---|---|---|
| Mid Level | L5 Semi Senior Advanced | Semi Senior II | 4 |
| Sr | L6 Senior Level 1 | Senior I | 5 |
| Sr Level 2 | L7 Senior Level 2 | Senior II | 6 |
| Sr 3, leads people | L8 Senior Level 3 (Tech Leader) | Tech Lead I / II | 7+ / 10+ |
| Sr 3, does not lead people | L7 Senior Level 2 | Experience Senior I / II | 7 / 8 |
| Subject Matter Expert | Expert | Software Architect | 11 |
| Manager | Tech Manager | Technical Manager | 11 |
| Director | Director | DXP Technology Director | 13 |

- For every Sr 3 line, the intake round asks whether the person leads the team. When they do not, `opportunity.md` flags "priced as Sr 3, IC Posición mapped to L7".
- When a P&L has "Architect" as the Client's Role Name on a Sr 3 line, the intake round asks whether the Posición is an Expert or a Tech Leader.
- Globant's `Lead` has no row: it appears only on practice roles, which are not DXP technical roles and get no JD.
- Years come from the HR job descriptions, not from the Globant P&L band. The two differ only on Sr 3 (8–10 vs 7+), and that gets no flag.
- The Debrief's calibrated level uses the handbook column. Only the hiring lead writes it.

### 3.5 `hr-job-descriptions/`

([Handbook gaps for JDs](issues/11-handbook-gaps-for-jds.md))

- The HR versions of the Descripciones de cargo the suite uses, converted to Markdown as `<role>-<level>.md`. Drafts are not copied. The list to convert is in §6.
- They are frozen documents, the one exception to "read, never copied", so no skill depends on `~/Downloads` at run time.
- From a Descripción de cargo a skill takes its knowledge and requirements, its years, and its responsibilities (which feed "What the person will do"). Its KPIs, reporting line, authority and English level stay out; English follows the suite's B2 rule.

### 3.6 `export.md` and its script

([Skill boundaries](issues/03-skill-boundaries.md), [JD structure](issues/04-jd-structure.md), [Unified Debrief](issues/08-debrief.md))

- One shared converter, `npx md-to-pdf`. Each skill exports its own artifact, on request: `jd.md`, `match-evaluation.md`, `interview-guide.md`, `debrief.md`, `status-<YYYY-MM-DD>.md`.
- The PDF sits next to its source, with the same name and the `.pdf` extension.
- It has the same content as the source, `Proposed:` prefixes included, with one exception: the JD's export strips the origin tags and the off-handbook note, so recruiting sees only confirmed Requisitos.
- The Debrief's export first checks the latest Decision. When it is empty, the skill warns and asks before exporting.
- *(Built 2026-10-27.)* The script is `.claude/shared/export-pdf.mjs`. `export.md` fixes the exact form of the origin tags and of the off-handbook note (a blockquote opening with `> **Off-handbook:**`), which `staffing-jd`'s template must follow for the strip to work. The frontmatter opens every PDF as a table, except the JD's and the Guía's, whose `opportunity` slug would name the client they anonymise (hiring lead, 2026-10-27).

## 4. Skills

Each section holds the skill's trigger draft, inputs, steps, rules, template and acceptance. The trigger drafts open on the glossary term the hiring lead uses, with one trigger per branch; the final wording comes out of skill-creator's description optimization, and what must not trigger lives in the trigger evals (§5.5).

| Look-alike request | Skill |
|---|---|
| "compare the Candidatos for <Posición>" | `staffing-match` |
| "todos los candidatos revisados para <Oportunidad>" | `staffing-status` |
| "build the scorecard for X", "rate X" | `staffing-debrief` |
| "interview questions for <Posición>" with no Candidato | `staffing-interview-guide`, which asks for the Candidato |

### 4.1 `staffing-jd`

([JD structure](issues/04-jd-structure.md), [Handbook gaps for JDs](issues/11-handbook-gaps-for-jds.md), [Acceptance cases](issues/09-acceptance-cases.md); prototypes in [prototypes/04-jd/](prototypes/04-jd/), whose tags and labels predate the final origins)

**Trigger draft**

```
JDs and opportunity.md for an Oportunidad, from its Propuesta and P&L, a brief or a
supplied JD. Use when starting an Oportunidad, adding or changing a Posición, updating
a JD, or exporting one to PDF.
```

**Inputs**

| Input | Mark |
|---|---|
| Propuesta (usually a deck) and P&L, or in their place the hiring lead's material: a brief or a supplied JD, as files or pasted text | Required: with none of them, the skill stops and asks |
| Presales' own statements: its notes, a message the hiring lead pastes, its answer to a forwarded intake question | Optional |
| The handbook, `level-equivalence.md`, `hr-job-descriptions/` | Reference |

**Steps** (one run per Oportunidad, never per Posición)

1. Resolve the tree root and keep the inputs in `opportunities/<op>/`.
2. Read the inputs and draft the intake analysis: the context, the P&L lines → Posiciones table with its flags, and the inconsistencies found.
3. Show it with one round of questions to the hiring lead. The round asks:
   - every inconsistency found (e.g. a SOW vs Labor Estimate gap, a role label against the Propuesta's platform, a workstream outside the Labor Estimate);
   - for every Sr 3 line, whether the person leads people;
   - for a Sr 3 line whose Client's Role Name is "Architect", whether the Posición is an Expert or a Tech Leader;
   - the level of each Posición, when there is no P&L;
   - each contradiction between a supplied JD and the base (years, English, a level Must have);
   - who supplied each supplied JD: the hiring lead, the client or Presales;
   - Claude's `Proposed:` platform Requisitos, when neither the handbook nor a Descripción de cargo covers the platform.
4. Write `opportunity.md` (the intake analysis plus the answers) and every `jd.md` of the Oportunidad, in the same run. A Requisito whose question is still unanswered is written nowhere.
5. Offer the PDF export of the JDs.

**Other actions**

- **Add or change a Posición:** the same rules, for that Posición; `opportunity.md`'s table is updated.
- **Update a JD:** rewrite it with a new `updated`. Then list the Candidatos whose Evaluación de match went stale and offer to run `staffing-match` on them as a batch, one subagent per Candidato. The skill never re-evaluates on its own.
- **Export a JD:** §3.6.

**Intake rules**

- Only DXP technical lines get a JD. A P&L lists the whole priced team: lines already assigned to a person, structure or governance lines, and practice roles (Globant `Lead`) get none.
- Seniority comes from the P&L's Labor Estimate, never from its client-facing SOW sheet, and maps to a level through `level-equivalence.md`. A gap between the two sheets is a flag in `opportunity.md`, not in the JD.
- Platform and technical Requisitos come from the technology the Propuesta defines. A P&L role label ("AEM Backend Developer") is only today's catalog name.
- Workstreams staffed by the same people fold their needs into the same JD.
- Allocation (FTE curves, gaps between months) stays out of the JD: a JD sources a profile.
- English: B2 minimum for every Posición; B1 only as an exception for a role that does not face the client.
- Familiarity with a migration's source platform enters as Nice to have.
- **Without a Propuesta or P&L** (any Oportunidad, e.g. a running project that needs a new Tech Leader, and always an internal client): the level is asked in the round, `opportunity.md` is still written, and the client is anonymised unless it is internal.

**Where Requisitos come from**

- **Base**, generic to a role and level, in three parts: role, level and platform. Each part comes from the first source in this order that covers it:
  1. the handbook: the role's Must have, the level's scope in its career path, the platform's `### By platform`;
  2. a Descripción de cargo of the same role (and of the same platform, for the platform part), only for what the handbook does not cover;
  3. Claude's `Proposed:` Requisitos in the intake round. Only what the hiring lead confirms is written, with origin `hiring lead`.
- Years always come from `level-equivalence.md`: the handbook has none.
- **Posición-specific:** the Propuesta, Presales, a supplied JD, the hiring lead's answers.
- **A supplied JD** sits above the base:
  - its Requisitos carry `supplied JD`, and the base fills in whatever it does not cover;
  - a contradiction with the base goes to the round, and the hiring lead chooses: nothing is resolved silently;
  - a Descripción de cargo the hiring lead hands in for a Posición counts as a supplied JD. The tag follows who chose it for the Posición, not the file's format.
- **Software Architect:** the Must haves come from the handbook's `Expert`; the 11 years and the responsibilities from HR's Software Architect, with origin `HR job description`. HR's stack list stays out: the platform comes from the Propuesta and the order above. Flag: "Expert is a regional role in the handbook; project scope from the Propuesta". The hiring lead's 2024 draft (5 years) is not a source.
- **Off-handbook platform** (e.g. a Sitecore Tech Leader): the role (Leader) and level (L8) come from the handbook; the platform part from the Propuesta when there is one, and from the proposals the hiring lead confirms.

**Origins**

- `handbook role`, `handbook level`, `handbook platform`, `HR job description`, `Propuesta`, `presales`, `supplied JD`, `hiring lead`, `suite rule`. Claude is never an origin.
- A Requisito is `presales` only when the hiring lead says it comes from Presales. What the Propuesta says keeps `Propuesta`.
- In `jd.md`, each Requisito ends with its tags in backticks, e.g. `` `[handbook platform]` `[Propuesta]` ``, one per source that backs it *(call 4)*.

**Flags for an incomplete base**

- `opportunity.md`: a flag on the Posición's row, such as `Off-handbook platform: Sitecore` or `Off-handbook role: <role>`. The "priced as Sr 3" and "Expert is a regional role" flags go in the same column.
- `jd.md`: a note at the top saying which part of the base is missing and where those Requisitos came from. The PDF strips it.

**Template: `opportunity.md`** (the only artifact besides the status summary that names the real client)

1. Frontmatter.
2. Context: client, project, workstreams, dates, stack signals, locations.
3. Sources read, and who supplied each supplied JD.
4. P&L lines → Posiciones: one row per P&L line with the line (role · seniority · location), the Posición (handbook role · level · platform), headcount, start, whether it gets a JD, and flags *(call 7)*.
5. Inconsistencies found.
6. Intake answers.

**Template: `jd.md`** (the recruiting brief)

1. Frontmatter.
2. Off-handbook note, only when the base is incomplete.
3. Title (role · level · platform) and location.
4. A one-line summary.
5. **Must have**, as a checklist, each item with its origins.
6. **Nice to have**, each item with its origins.
7. What the person will do.
8. Search keywords.
9. Screening: questions with what a good answer mentions, and/or points to check in the CV or profile.
10. Not a fit if.
11. Logistics: location, remote, start, full-time.

Two tiers only, labelled as the handbook does ("Must have", "Nice to have"), with no numeric weights.

**Acceptance**

Rule checks, on every case (plus §5.4):

- only two tiers, Must have and Nice to have;
- every Requisito carries its origin;
- English is B2 (B1 only as the exception);
- no allocation;
- the client is anonymised in every `jd.md`, unless the client is internal.

| Case | Variant checks |
|---|---|
| `jd-expedia` | An intake analysis and one question round before writing. P&L lines 1–3 get no JD. Seniority comes from the Labor Estimate, with the SOW gap as a flag in `opportunity.md`. Lines 10, 11 and API are flagged and get no invented Requisitos. The round asks whether line 4 (AEM Backend, Sr 3) leads people. |
| `jd-internal-client` | Asks for no Propuesta or P&L. Asks for the level in the intake. Writes an English JD from a Spanish source. The Director's Descripción de cargo counts as a supplied JD: its Requisitos carry `supplied JD`, and the handbook's `director` role fills in what it does not cover. |
| `jd-off-handbook` | Asks for no Propuesta or P&L. Proposes the Sitecore stack in the intake marked `Proposed:` and writes only what was confirmed, with origin `hiring lead`. Role and level come from the handbook (Leader, L8). `opportunity.md` has `Off-handbook platform: Sitecore` and `jd.md` has the note at the top; neither is in the PDF. |
| `jd-supplied-contradiction` (mutated) | The intake shows the contradiction, and nothing is written for that Requisito until the hiring lead answers. |
| `jd-architect-line` (mutated) | The intake asks whether line 4 is an Expert or a Tech Leader. On a second run answered "Expert": the Must haves come from `Expert`, the 11 years and the responsibilities carry `HR job description`, and the "Expert is a regional role" flag is present. |

### 4.2 `staffing-match`

([Evaluación de match rubric](issues/05-match-evaluation-rubric.md), [Skill boundaries](issues/03-skill-boundaries.md))

**Trigger draft**

```
Evaluación de match of Candidatos against a Posición's JD, from CVs, profiles and
internal history. Use when evaluating one CV or a batch, re-evaluating after a JD
change, comparing a Posición's Candidatos, editing its Shortlist as dictated, or
exporting an evaluation.
```

**Inputs**

| Input | Mark |
|---|---|
| The Posición's `jd.md` | Required: offers `staffing-jd` |
| A document about the person: a CV or a public profile (a LinkedIn profile alone is enough) | Required: asks for it |
| For a Candidato interno: project history, prior feedback, earlier Debriefs and Scorecards in `people/<p>/` | Optional |
| A copy of the take-home report | Optional |
| Recruiting's screening notes | Optional |

**Steps** (one CV)

1. Resolve the tree root. Find the person's folder or create `people/<first>-<last>/`, reusing an existing one and asking when unsure, and keep the files there under their original names.
2. When the Candidato folder `<op>--<pos>/` does not exist, ask whether the person is internal or external (external by default, *call 15*) and create it.
3. Read the JD and every source. Split the JD's Requisitos into atomic rows.
4. Give each row its Nivel de evidencia and citation. Record the Logistics, the career timeline and the credibility observations. Derive the Puntos a indagar.
5. Write `match-evaluation.md` from the template. Offer the PDF export.

**Batch**

- When the Posiciones are not named, the skill proposes a person → Posición table, in alphabetical order and never saved. The hiring lead confirms it in one round, which also asks whether each person is internal or external (external by default).
- A person on two Posiciones is two Candidatos. An unassigned CV gets no folder and is listed in the final report.
- Files are grouped per person and kept in `people/<p>/` as in step 1.
- One subagent per Candidato sees only that person's files and the JD, and follows `batch-subagent.md`. A single CV is evaluated directly.
- The final report lists the evaluations written, alphabetically, and the unassigned CVs.

**Re-evaluation** happens only on request: after a JD update (offered by `staffing-jd`), or when a new document changes what the documents show. The new evaluation replaces `match-evaluation.md` with the new `jd_updated` and `date`. Before writing, the skill says that levels the hiring lead corrected in place will be replaced, and asks. After writing, it lists in chat every Requisito whose Nivel de evidencia differs from the previous file, so the hiring lead can reapply their corrections; in a batch, the final report carries that list per Candidato *(call 3)*.

**Comparison table** (on request, shown in chat, never stored)

- One row per Requisito, in the JD's order and with its tier, plus the Logistics rows.
- One column per Candidato, in alphabetical order, never ordered by fit.
- Each cell holds the Nivel de evidencia.
- No totals or counts.
- A column whose evaluation is stale is marked in its header.

**Shortlist.** Claude edits `shortlist.md` only as the hiring lead dictates, writing exactly the order and notes dictated, and creates it when missing.

**What is assessed**

- Every Must have and every Nice to have in the JD gets one row, in the JD's order, with its tier.
- A line with several parts ("5+ years in frontend, 2+ with React in production") is split into atomic rows (1a, 1b) that point back to the JD line.
- "What the person will do" is not assessed: those are not Requisitos.
- "Not a fit if" is not assessed separately. When the CV hits one, it is a credibility observation.

**Nivel de evidencia** (a vocabulary distinct from the Calificación, on purpose)

| Level | When |
|---|---|
| Evidenced | A concrete project or role shows it: what, where, how long. |
| Claimed | Stated (skills list, summary) but no project backs it. |
| Partial | Evidence of something adjacent (Sanity instead of Contentful, Pages Router only), or of one part of a compound Requisito. |
| No evidence | Not mentioned. Absence from a CV is not proof the Candidato lacks it. |
| Not met | The documents show the Candidato falls short: 3 years against 5+, a whole career in Angular. |

**Sources and citation**

- Sources: CV, public profile, the take-home report, recruiting's screening notes.
- Every level cites its evidence (quote and file); only No evidence may go without one.
- Evidence carries its period ("React, 2016–2018"). Its age is shown, never weighted.
- Interview evidence never enters here: it belongs to the Debrief. The skill reads documents only, even when run after an Entrevista.

**Candidato interno**

- The extra sources in `people/<p>/` are cited with their date and Posición. They weigh no more than the CV, but can reach Evidenced through observed work rather than claims.
- A Calificación from an earlier Entrevista is cited as a dated fact, never carried over as a Calificación.
- When internal evidence contradicts the CV, the contradiction is flagged.
- Prior feedback is not treated as sensitive: the evaluation can be shared.

**Logistics** holds facts: location, work mode, availability or start date, notice period. It is checked against the JD's Logistics. No salary.

**Puntos a indagar** (the hand-off to the Guía)

- What becomes one:
  - every Must have that is not Evidenced (Claimed, Partial, No evidence, and Not met in case the hiring lead interviews anyway);
  - every Nice to have that is Claimed or Partial;
  - every credibility observation.
- Each carries: the Requisito row and its tier; the Nivel de evidencia; the quote it rests on; what to verify, worded as a doubt, not a question; the Dimensión or Dimensiones it lands on.
- Order: Must have first, then Nice to have; within each, Claimed → Partial → No evidence. This orders the interview plan; it is not a judgment.
- No questions are written here: the Guía owns timing and coverage.

**Template: `match-evaluation.md`**

1. Header:
   - the frontmatter;
   - the fixed line *"Evidence from documents only, before any interview. Not a hiring recommendation."*;
   - a line saying the Evidence levels are Claude's reading of the sources;
   - the list of sources read.
2. Requirements: a table with id, Requisito, tier, Nivel de evidencia, and evidence (quote · file · period).
3. Logistics, checked against the JD.
4. Career timeline: facts only (roles, companies, dates, duration).
5. Credibility observations not tied to a Requisito: timeline gaps, inflated titles, certifications without projects, a "Not a fit if" hit.
6. Points to probe.

No Gaps section (the Points to probe open with the Must haves), no summary and no conclusion. No `Proposed:` on the levels: the header covers them, and the hiring lead corrects a level by editing it in place. Also left out: "seniority (your assessment)", a "working hypothesis", comparable precedents or any comparison between Candidatos, counts or percentages, a computed growth velocity.

**Acceptance**

Rule checks, on every case (plus §5.4):

- one row per atomic Requisito, in the JD's order, with its tier;
- every Nivel de evidencia is cited, except No evidence;
- evidence carries its period;
- the fixed "Not a hiring recommendation" header line;
- no summary, conclusion, velocity or salary;
- the Puntos a indagar follow the order rule.

| Case | Variant checks |
|---|---|
| `match-internal-prior` | Earlier Calificaciones are cited as dated facts, never carried over. AEM in place of Contentful is Partial. A contradiction between the CV and internal evidence is flagged. |
| `match-takehome` | The take-home report is a cited source. Years below the JD's are Not met. |
| `match-external-leadership` | External Candidato in a leadership role. The Puntos a indagar land on the leadership Dimensiones. |

### 4.3 `staffing-interview-guide`

([Unified Guía de entrevista](issues/07-interview-guide.md), amended by [Unified Debrief](issues/08-debrief.md) and [Debrief inputs outside the suite's shape](issues/12-debrief-inputs-outside-the-suite-shape.md))

**Trigger draft**

```
Guía de entrevista for one Entrevista of one Candidato, usable by any Entrevistador,
delegated ones included. Use when preparing or planning an Entrevista, splitting a
Posición across Entrevistas, or writing interview questions for a Candidato.
```

**Inputs**

| Input | Mark |
|---|---|
| The Posición's `jd.md` | Required: offers `staffing-jd` |
| The Candidato's `match-evaluation.md` | Required: offers `staffing-match`. When stale, the Guía says so and goes on. |
| The Entrevistadores, the blocks each owns, and the date | Required: asked in one round before writing |
| For a later Entrevista, the Debrief of the earlier ones | Offered: offers `staffing-debrief`. When declined, the Guía reads the earlier Guías so it repeats no question, and its header says it cannot target the Dimensiones left Not assessed or the open Discrepancias *(call 2)* |
| A copy of the take-home report in the Candidato folder | Optional |
| The question bank | Reference |

The Guía never reads the CV: the CV analysis lives only in the Evaluación de match, whose only source may be a public profile. A request with no Candidato ("interview questions for <Posición>") gets a question asking which Candidato.

**Steps**

1. Resolve the tree root and the Candidato folder, check the inputs, and ask the round.
2. Set what the Entrevista measures: the Posición's Dimensiones and what Meets means (§3.3), Platform knowledge's sub-areas, the Puntos a indagar in their order and, for a later Entrevista, the Dimensiones still Not assessed and the open Discrepancias.
3. Fit the hour: at least one main question per Dimensión and every Punto a indagar on a Must have. When that does not fit, say so and propose what moves to another Entrevista. The hiring lead chooses between another Entrevista and listing those Dimensiones as not covered.
4. Write the questions.
5. Write `interviews/<YYYY-MM-DD>/interview-guide.md` from the template. Offer the PDF export, which is what a delegated Entrevistador receives.

**Format**

- Every Entrevista lasts one hour, for every Posición, leadership roles included.
- Blocks in a fixed order: Opening → Background & motivation → Soft → Technical → Leadership (leadership roles only) → Candidate questions → Closing.
- The agenda gives each block its minutes and an owner from `interviewers`, with one line saying both are a starting split for the Entrevistadores to adjust.
- A later Entrevista of the same Candidato reads the Debrief and any brought Scorecards. It targets the Dimensiones left Not assessed and the open Discrepancias (empty Resolution), and repeats no question already asked, off-guide questions included.

**Questions**

- Numbered across the whole Guía, Q1…Qn. The ids are stable; everything written after the Entrevista cites them.
- Each question has:
  - the main question;
  - follow-ups;
  - **Listen for:** what a strong answer mentions at the Posición's level;
  - **Watch for** (optional): signals specific to that question;
  - the Dimensiones it gives evidence for;
  - its origin: handbook, JD Requisito, Punto a indagar, take-home, or question bank.
- No model answers in prose and no per-question Below/Meets/Exceeds anchors: anchors belong to the rubric, per Dimensión.
- **Technical questions** are suggested prompts the technical Entrevistador adapts. They come from Platform knowledge's sub-areas (`technologies/<platform>.md`), the JD's Requisitos, and the level's scope in `career-paths`. When the handbook lacks the platform, they come only from the JD's Requisitos, and the Guía says so.
- **Take-home:** its report's follow-up questions enter the Technical block, adapted, with origin `take-home`, plus a "walk me through your submission" question.

**Question bank**

- `question-bank/platforms/<platform>.md` and `question-bank/tracks/<track>.md`, read for the Posición's platform and track. Bank questions have the shape above.
- When no bank covers the platform or track, the Guía generates the questions and says the bank is missing.
- The bank grows only by a deliberate edit.

**Coverage**

- Every Dimensión has at least one main question, or is listed as "Not covered in this interview", so its Not assessed is planned, not accidental.
- A coverage table maps each Dimensión to its question numbers. English reads "Assessed separately".

**Puntos a indagar**

- They arrive in the evaluation's order; credibility observations not tied to a Requisito come after the Nice to haves.
- Each becomes a question or a follow-up, worded neutrally so the Candidato does not feel targeted, and asked in the block where it fits: the timeline in Background & motivation, an unexplained career gap at the Closing, once and neutrally.
- A table at the top maps each Punto a indagar to where it is asked, and a list gives what the Entrevista tests, in priority order.
- A Must have that is not Evidenced is probed early in its block, and the briefing states it neutrally: *"The match evaluation found no evidence for Must have <X>; this interview should collect it."* *(call 9)*
- Whether to hold the Entrevista is the hiring lead's call before asking for the Guía. The Guía plans the Entrevista it was asked for.

**Usable without the hiring lead's context**

- **Briefing:** the Posición (role · level · platform); the project, with the client anonymised; what is being tested, in priority order; what the Calificaciones are measured against (the rubric link, or "rubric pending: …").
- **Interviewer tips** (fixed):
  - Ask for STAR examples.
  - Ask "what did *you* do?".
  - Let the Candidato talk 70–80% of the time.
  - Give an honest exit on technical questions: "I'd rather know the edges than hear a guess."
  - No personal topics.
  - Don't name the client.
  - "Form your own view of the Candidate before discussing them with other Interviewers." *(call 16)*
- **What you can tell the candidate:** the logistics from the JD.
- **Opening script:** tells the Candidato the call is recorded and transcribed, and asks for consent. Without consent, the Entrevistador takes minimal notes per block, the only case in which anyone takes notes.
- An English phrasebook only on request.

**The transcript is the evidence.** The Guía has no notes template and writes no blank Scorecards. Only the Guía goes out to a delegated Entrevistador; only the transcript comes back, dropped in the Entrevista's folder under any name.

The Guía is in English whatever language the Entrevista is held in, and carries no `Proposed:`: its header says Claude wrote it.

**Template: `interview-guide.md`** *(section order: call 12)*

1. Header: the frontmatter; a line saying Claude wrote this plan; the stale-match warning, when it applies; any handbook or question-bank gap.
2. Briefing, with the neutral line for each Must have not Evidenced.
3. Agenda: blocks, minutes, owners, and the "starting split" line.
4. What this interview tests, in priority order, and the Points to probe → where asked table.
5. Coverage table.
6. Interviewer tips.
7. Questions, by block, Q1…Qn, starting with the Opening script and its consent line.
8. What you can tell the candidate.

**Acceptance**

Rule checks, on every case (plus §5.4):

- every Dimensión has a main question, or is listed as "Not covered in this interview";
- a coverage table;
- English reads "Assessed separately";
- questions are numbered Q1…Qn;
- no notes template and no blank Scorecards;
- never suggests declining the Candidato;
- the client is anonymised;
- the header says Claude wrote it.

| Case | Variant checks |
|---|---|
| `guide-pair` | An owner per block. A table maps each Punto a indagar to its question. A Must have that is not Evidenced is probed early and briefed neutrally. |
| `guide-takehome` | Take-home questions carry origin `take-home`. Adds "walk me through your submission". |
| `guide-second-interview` | Targets the Not assessed Dimensiones and the open Tensions. Repeats no question from the first Entrevista. Has a leadership block. Its briefing works without the hiring lead's context. |
| `guide-off-handbook` | Says the handbook does not cover Sitecore and no question bank does either, and draws the technical questions from the JD's Requisitos. The Sitecore Expert owns the technical block, and its briefing works without the hiring lead's context. |
| `guide-missing-match` (mutated) | Stops and offers to run `staffing-match`. |
| `guide-stale-match` (mutated) | Warns that the evaluation is stale against the JD. |

### 4.4 `staffing-debrief`

([Unified Debrief](issues/08-debrief.md), amended by [Debrief inputs outside the suite's shape](issues/12-debrief-inputs-outside-the-suite-shape.md); [Scorecards](issues/06-scorecards.md))

**Trigger draft**

```
Debrief of a Candidato's Entrevistas from transcripts, notes and Scorecards, with
Proposed Calificaciones per Dimensión. Use after an Entrevista, when another one is
added, when rating or scoring a Candidato, or exporting it.
```

**Inputs**

| Input | Mark |
|---|---|
| The Posición's `jd.md` | Required: offers `staffing-jd` |
| Per Entrevista and Entrevistador: the transcript (the main evidence), or a Scorecard or notes they bring | When an Entrevistador in `interviewers` has none of them, the skill asks whether to wait or go on without them; it never drafts a partial Debrief silently |
| Per Entrevista: its Guía (question ids, block owners) | Optional: without one, citations go by timestamp |
| The Candidato's `match-evaluation.md` | Offered: offers `staffing-match`. When stale, the header says so and its Puntos a indagar are used as they stand. |
| The English result, provided separately | Offered: asks for it; if it never arrives, English is Not assessed |
| A copy of the take-home report | Optional: cited in Evidence for / against and in Discrepancias, never the basis of a Calificación |
| The existing `debrief.md` | Its Resolutions and Decisions are kept |

**Not a source:** evidence from outside an Entrevista (a follow-up email, a reference, an internal Candidato's manager's opinion), an old candidate profile from the per-stack workspaces, and an old Debrief's prose. The hiring lead may cite outside evidence in their own Justification or Resolution. When it changes what the documents show, the Evaluación de match is run again; the Debrief never re-evaluates it.

**Steps**

1. Resolve the tree root and the Candidato folder. List the Entrevistas (`interviews/<YYYY-MM-DD>/`) and the evidence in each. Check the inputs and ask for what is missing in one round.
2. Read each transcript. Fix speaker labels the content makes clear, and check fidelity. For lower-fidelity evidence, ask the hiring lead to fill the gap first.
3. Build the Calificaciones table, one column per Entrevistador per Entrevista, and the evidence per Dimensión.
4. Write the Discrepancias, the outcome of each Punto a indagar, and the remaining sections.
5. Write or update `debrief.md`: Claude's sections are rewritten; Resolutions and Decisions already written are kept verbatim, and the skill asks before touching them.
6. Offer the PDF export (§3.6).

**One Debrief per Candidato**

- One `debrief.md` consolidates every Entrevista the Candidato had for the Posición and is updated after each one.
- A planned split of the Posición's coverage and an "Another interview" decision are handled alike: one more Entrevista in the same document.
- No standalone action drafts one Entrevista's Calificaciones: the Debrief is incremental from the first Entrevista.

**Calificaciones**

- A table with one row per Dimensión of the Posición and one column per Entrevistador per Entrevista. No consolidated column.
- **A brought Scorecard** fills its column verbatim, with no prefix (a `Proposed:` left in it stays), only when both hold:
  - its scale is the suite's (Below / Meets / Exceeds / Not assessed);
  - each of its dimensions maps one-to-one to a Dimensión. Names may differ; the subsection then shows the mapping, since Claude made it: *"from <Interviewer>'s '<their dimension>'"*.
- Anything else is never converted: a number, a Hire / No Hire, a dimension covering two Dimensiones, or two dimensions landing on one Dimensión.
  - The rating is quoted verbatim, in its own scale and under its own name, attributed, as evidence in the matching Dimensión's subsection.
  - The column is Claude's, `Proposed:`, from the transcript. With no transcript, Claude proposes from the Scorecard's written evidence, citing it, never from a number alone.
  - A Scorecard with bare numbers and neither written evidence nor a transcript is lower-fidelity evidence: the skill first asks the hiring lead to fill the gap (e.g. have the Entrevistador rate on the suite's scale or add the evidence). Without a clear answer the row is `Proposed: Not assessed`, with the original rating quoted and the limit stated in that Entrevista's sources.
  - A dimension with no Dimensión to map to is listed verbatim in that Entrevistador's sources line as "not mapped to a Dimension".
  - A recommendation in it is left out, because it anchors the Decision. The sources line says "recommendation left out"; the original file stays for the hiring lead.
- **Otherwise** Claude proposes the column from the transcript, every value `Proposed:`, following the rating rules in §3.3. No Scorecard file is written first.
- **Columns:** evidence goes to the owner of the block where it arose, per the Guía's agenda. When a block has two owners, Claude proposes once and the column carries both names: never two values from the same transcript. With no Guía and several Entrevistadores, the skill asks the hiring lead once who led each block or stretch of time.
- Under the table, one subsection per Dimensión: each column's Calificación with its quotes and citations.
- **English row:** the result provided (level, who provided it, when), the level the JD sets (B2, or B1 as the exception), and a `Proposed:` Calificación against it.
- **Confirming:** the hiring lead confirms a `Proposed:` Calificación by editing it, checking with the block owner when it is someone else. A delegated Entrevistador only returns the transcript and needs no access to these files. A Calificación still unconfirmed at Decision time shows as such.
- `Proposed:` marks Calificaciones only. Everything else Claude writes is covered by the header line.

**Citations**

- `<YYYY-MM-DD> · Qn` for a Guía question.
- `<YYYY-MM-DD> · Qn follow-up` for a question that follows the thread of a Guía question.
- `<YYYY-MM-DD> · off-guide [hh:mm:ss]` for any other question, with the question as asked, in one line. It counts like any other evidence, in the column of the block's owner.
- For an Entrevista with no suite Guía: `<YYYY-MM-DD> · [hh:mm:ss]` with the question as asked, and the sources line says "No Guía: cited by timestamp". Without timestamps, the question as asked identifies the citation on its own.
- Question ids belong to the Guía: Claude never invents one, and never writes a Guía after the fact. An old guide is read for context only and never cited.

**Fidelity and speakers**

- Lower-fidelity evidence: a degraded or partial transcript, minimal notes taken because the Candidato did not consent to recording, a speaker that stays ambiguous (e.g. two Entrevistadores under one label), a Scorecard of bare numbers. The skill first asks the hiring lead to fill the gap. Without a clear answer, it states the limit per Entrevista in the sources and in the evidence of every Calificación that rests on it.
- When the content and the Guía's `interviewers` make a speaker clear, Claude corrects the label without asking and states it once in the sources: *"speaker label 'X' is the Candidate"*.

**Discrepancias**

- A Discrepancia is any difference between columns on the same Dimensión (Meets vs Exceeds counts), opposite outcomes on the same Punto a indagar, or a red flag from one Entrevistador against a green flag from another on the same behaviour.
- Rated vs Not assessed is coverage, listed under Not covered; a flag only one Entrevistador saw is attributed to them.
- Each shows each side's evidence and a blank **Resolution** that only the hiring lead fills. An open Discrepancia is one with an empty Resolution; a later Guía targets those.
- **Single Entrevistador** (across every Entrevista): the same template with one column. The section is **Tensions in the evidence**, about tensions inside that Entrevistador's own evidence, e.g. between the CV and what the Entrevista showed. The header carries the fixed line *"One interviewer: no independent second view."* *(call 9)*
- When the Entrevistadores agree, the section says None.

**Points to probe: what the interview showed**

- Every Punto a indagar, in the evaluation's order, records Confirmed, Contradicted, Inconclusive or Not probed, with the transcript quote and who asked.
- The Contradicted credibility points are the inconsistencies between the CV and the answers.
- With no Evaluación de match (offer declined), the section reads *"No match evaluation: no points to probe were set."* *(call 9)* and Not covered lists only Dimensiones.

**Decision** (first in the document, so managers and recruiting read it before the evidence)

- A dated list, newest first, filled only by the hiring lead. Claude never ticks or pre-fills anything in it.
- Each entry:
  - **Outcome:** Advance / Advance with conditions / Another interview / Do not advance. The same for Candidatos internos and externos; Advance for an internal is a placement.
  - **Justification.**
  - **Calibrated level,** in the handbook's vocabulary through `level-equivalence.md`. Claude never proposes it.
  - **Conditions,** or the reason for another Entrevista.
  - **Next steps.**
  - **Decided by / date.**
- An empty latest entry means the decision is pending.
- The Debrief never edits the Shortlist: the hiring lead updates it after deciding.

**Cutover inputs** (a Candidato from a per-stack workspace, §6)

- Old Scorecards are brought Scorecards in another shape; an old guide is context only.
- An old Debrief is named in the sources line and nothing more: its prose is never translated or carried over, and its ticked Decision is not copied. The Decision list starts empty, and the skill asks the hiring lead to write their decision again.

**Template: `debrief.md`**

1. Header:
   - the frontmatter;
   - what the Calificaciones are measured against: role or track, the Posición's level, the rubric link or "rubric pending: …";
   - the line *"Drafted by Claude from <sources>. Resolution and Decision are the hiring lead's."*;
   - the single-Entrevistador line, when it applies;
   - the sources read per Entrevista, with any fidelity limit, label correction, unmapped dimension or "recommendation left out";
   - the stale-match warning, when it applies.
2. Decision.
3. Ratings, with the evidence per Dimensión.
4. Discrepancies (or Tensions in the evidence), each with its Resolution.
5. Points to probe: what the interview showed.
6. Strengths and Concerns shared across Entrevistadores.
7. Flags: red and green, each attributed to who saw it.
8. Evidence for / Evidence against: both lists required, each item cited; no balance or summary.
9. Gaps and support: each gap tied to a Requisito or Dimensión, with the support it suggests.
10. Not covered: Dimensiones still Not assessed after every Entrevista and Puntos a indagar not probed, stating that absence of evidence is not evidence.

Left out: averages, totals and any consolidated Calificación; growth velocity; onboarding risk level and time to productivity as Claude's estimates (the hiring lead may write them in the Decision); hypotheses about why Entrevistadores disagree; a "Previous rounds" section.

**Acceptance**

Rule checks, on every case (plus §5.4):

- the Decision is empty, with nothing pre-ticked;
- `Proposed:` on every Calificación Claude writes;
- Not assessed instead of inference;
- every Discrepancia (or Tension) has a blank Resolution;
- no average, consolidated column, velocity or risk level;
- quotes appear in their original language followed by an English translation;
- both Evidence for and Evidence against are present.

| Case | Variant checks |
|---|---|
| `debrief-single-leadership` | One column, a "Tensions in the evidence" section and the single-Entrevistador line. Covers the three leadership Dimensiones. Spanish quotes are followed by an English translation. Offers to run the Evaluación de match; when declined, Points to probe reads "No match evaluation…". |
| `debrief-pending-update` | Run twice. The second run keeps the hiring lead's Decision and Resolution verbatim and asks before touching them. The sources line states which mislabelled speaker is the Candidato. |
| `debrief-pair-degraded` | Internal Candidato with two Entrevistadores. Asks the hiring lead to fill the gap first. States the fidelity limit per Entrevista and in every Calificación that rests on it. Uses Not assessed instead of inference. The Candidate Profile in the folder is not cited as Debrief evidence. |
| `debrief-cutover` | Citations by timestamp, with "No Guía" in the sources. The 1–5 ratings are quoted in their scale, never converted. "Recommendation left out". The Decision is empty and the old Debrief is only named in the sources. |
| `debrief-off-guide` (mutated) | Evidence from a removed question is cited `off-guide [hh:mm:ss]` with the question as asked, in the block owner's column; no invented id. |
| `debrief-stale-match` (mutated) | The header says the evaluation is stale; its Puntos a indagar are used as they stand. |
| `debrief-missing-english` (mutated) | Asks for the English result; when none arrives, English is Not assessed. |
| `debrief-missing-interviewer` (mutated) | Asks whether to wait for the Entrevistador or go on. |
| `debrief-export-pending` (mutated) | Warns that the latest Decision is empty and asks before exporting. |

### 4.5 `staffing-status`

([Oportunidad status summary](issues/10-opportunity-status-summary.md))

**Trigger draft**

```
Resumen de estado of an Oportunidad for management: each Candidato's Etapa per Posición
and what is pending. Use when asked for an Oportunidad's status, which Candidatos were
reviewed or are pending, or a status update for dirección.
```

**Inputs.** It reads `opportunity.md`, every `jd.md` (and whether its `jd.pdf` exists), every `shortlist.md`, and, for each Candidato folder `people/*/<op>--*/`, `match-evaluation.md`, `interviews/` and `debrief.md`. It writes only `status-<YYYY-MM-DD>.md`. It neither stops nor offers: whatever is missing becomes a pending item.

**Steps**

1. Resolve the tree root. With no tree, say so and create nothing.
2. Read the files above and derive each Candidato's Etapa and the pending items.
3. Write `opportunities/<op>/status-<YYYY-MM-DD>.md`. Earlier dates are kept; a second run on the same day overwrites that day's file.
4. Offer the PDF export.

**Audience and format.** One document, for management; the hiring lead reads it too and may edit the `.md` before exporting. It is always a picture of the present: no comparison with an earlier summary, and no free section. One Oportunidad per summary. PDF, not Excel: there is nothing to compute, and a spreadsheet invites sorting by columns, a ranking by another name.

**Etapa** (derived from the files, never stored)

| Stage | When |
|---|---|
| Not evaluated | The Candidato folder exists without `match-evaluation.md`. |
| Evaluated | `match-evaluation.md` exists, and no Entrevista is planned. |
| Interview planned | An `interviews/<YYYY-MM-DD>/` has its Guía and no transcript. |
| Interviewed | An Entrevista has a transcript whose date is not yet in the Debrief's `interviews`. |
| Debriefed | The Debrief covers every Entrevista with a transcript, and its latest Decision entry is empty. |
| Decided | The Debrief's latest Decision entry is filled in. |

- With several Entrevistas, the stage of the latest one is shown with its number ("Interview 2 planned").
- A latest Outcome of *Another interview* stays Decided until the next Guía exists, with the pending item "Another interview decided, not planned"; then it is "Interview 2 planned".
- Being on the Shortlist is not an Etapa: it is a column, since a Candidato may be interviewed before being shortlisted.
- The summary ends at the hiring lead's decision; it never says a seat is covered.

**Pending items** (facts, each with "since <date>" and no computed waiting time)

- No JD, or a JD not exported.
- No Candidates.
- An Evaluación de match stale against the JD.
- An Entrevista whose date has passed with no transcript.
- A transcript the Debrief does not cover yet.
- Decision pending.
- English result missing.
- Evaluated Candidatos neither on the Shortlist nor decided.
- Another interview decided, not planned.

Open Discrepancias and Calificaciones still `Proposed:` stay inside the Debrief: they are the hiring lead's work, and in front of management they hint at how a Candidato did.

**What the summary holds, and nothing more**

- Process facts: Etapas, dates, Shortlist positions, the hiring lead's recorded Outcomes, pending items. Process counts (Candidatos per Etapa, decisions recorded) are allowed: they count stages, not evidence.
- About a Candidato: only the name, internal or external, availability, and the hiring lead's latest Decision entry.
- Never: Calificaciones (proposed or confirmed); Niveles de evidencia, Puntos a indagar or credibility observations; counts of Requisitos or Dimensiones; other CV content; salary; the notes in `shortlist.md`; the comparison table (a Requisito × Candidato matrix in front of management invites counting cells); any wording that judges a Candidato ("strong profile", "risky").

**Template: `status-<YYYY-MM-DD>.md`** (names the real client)

1. Header:
   - the frontmatter;
   - client, project and dates, from `opportunity.md`;
   - the fixed line *"Status derived from the files on <date>. Not a hiring recommendation."*
2. Overview: one line per Posición, in `opportunity.md`'s order, with role · level · platform, headcount, the start date needed (from `opportunity.md`, *call 7*), Candidatos per Etapa, and the decisions recorded.
3. Per Posición:
   - the JD's `updated` date and whether it was exported;
   - a table of every Candidato of the Posición, including those off the Shortlist and those already Decided: the shortlisted ones first in the hiring lead's order, then the rest alphabetically;
   - its pending items.

Columns of the Candidato table:

- **Candidate:** name, internal or external. A person who is a Candidato in two Posiciones appears in both, with "also Candidate for <Posición>".
- **Shortlist:** the hiring lead's position (#1, #2…) or "—".
- **Stage.**
- **Last change:** a date.
- **Available from:** from the Evaluación de match's Logistics, next to the Posición's start date, with no judgment ("at risk") added.
- **Decision:** the latest entry as Outcome · Calibrated level · date · Decided by. Justification, Conditions and Next steps stay in the Debrief.

**Acceptance** *(call 11)*

The acceptance ticket gave this skill no case. Its cases run over a tree assembled from the frozen fixtures of the other skills' cases, so nothing is invented. Mutated cases each add or remove one file to reach what that tree lacks.

Rule checks, on every case (plus §5.4):

- every Candidato of each Posición appears, shortlisted ones first in the Shortlist's order, then the rest alphabetically;
- each Etapa matches the files;
- pending items are facts with "since <date>";
- no Calificación, Nivel de evidencia, Punto a indagar, Shortlist note or Requisito count;
- the client is named.

| Case | Variant checks |
|---|---|
| `status-sandbox` | The Candidato with an "Another interview" Decision and a second Guía shows "Interview 2 planned". A Candidato with a Debrief and an empty Decision shows Debriefed, with the pending item "Decision pending". |
| `status-not-evaluated` (mutated) | The Candidato folder without its Evaluación de match shows Not evaluated. |
| `status-interviewed` (mutated) | The transcript no Debrief covers shows Interviewed, with the pending item "A transcript the Debrief does not cover yet". |
| `status-shortlist` (mutated) | Shortlisted Candidatos come first, in the hiring lead's order, then the rest alphabetically. No Shortlist note appears. |

## 5. Acceptance

([Acceptance cases](issues/09-acceptance-cases.md), amended by [Handbook gaps for JDs](issues/11-handbook-gaps-for-jds.md), [Debrief inputs outside the suite's shape](issues/12-debrief-inputs-outside-the-suite-shape.md) and [Skill boundaries](issues/03-skill-boundaries.md))

### 5.1 What a case is

- Each case has input files, a request to the skill, and checks. They map one-to-one to skill-creator's `evals/evals.json` (prompt, files, assertions). On top of that, the hiring lead reviews each output qualitatively.
- There is no golden output: writing the expected document would be writing the deliverable.
- Checks come in two layers: **rule checks**, written once per skill and applied to every case of it (in §4 and §5.4), and **variant checks**, one to three per case, for what that case exercises (in §4).
- Content checks (e.g. which Nivel de evidencia a given Requisito gets) are not in the spec: the hiring lead writes them at build time from the first reviewed output.
- The real past decision is never a check, since it would steer the skill toward a verdict. The hiring lead may use it as a lens in the qualitative review: does the evidence surface what drove it?
- A **mutated case** is built in the sandbox from a real case by removing, adding or editing one input: one per stop-and-ask rule, and for `staffing-status` one per Etapa or ordering rule its assembled tree lacks.

### 5.2 Runs

- The sandbox is `tests/runs/<handle>/`, with no git. The run setup creates empty `opportunities/` and `people/` in it, so the tree root resolves there, and gives it `staffing/.claude/settings.json` (which disables `human-resources`) through `--settings` or a settings file in the run folder, whichever skill-creator's runner accepts.
- Each skill's evals point at `tests/acceptance/<handle>/`, which holds copies of the inputs and the frozen fixtures. Copies are needed because the origins are volatile (`~/Downloads`) or will be archived (the per-stack workspaces). `tests/acceptance/MANIFEST.md` says what each case folder holds and what is still to come.
- *(Smoke check, 2026-10-27.)* A run also needs a read grant on the suite, scoped to the run: `--allowedTools 'Read(~/Workspace/leadership/staffing/.claude/**)'` next to `--settings ../../../.claude/settings.json`. The grant stays out of `settings.json`. User-level plugins load in runs as well: `remember` writes `.remember/` into the sandbox and carries memory between runs of a handle, and `learning-output-style` changes the chat. Whether the run settings disable them is decided with the runner in step 3.

### 5.3 Fixtures

Fixtures convert what exists and never invent.

- An old guide becomes the Entrevista's Guía: its questions are numbered Q1…Qn in the order they were asked, and each block gets its owner.
- An Evaluación de match is produced by the match skill from the CV; for `debrief-pair-degraded`, from the Candidate Profile, the only source.
- A JD comes from a JD case's output, or from the JD skill run on the hiring lead's material.
- Old Scorecards are inputs only in `debrief-cutover`; elsewhere they serve calibration only.
- When a case's input is another case's output, the hiring lead first reviews and corrects that output, and it is then frozen as a fixture, so cases do not drift with each other.

**Calibration** (qualitative, not pass/fail, since the scales differ): `debrief-single-leadership` and `debrief-pending-update` are also run with the transcript only, and Claude's `Proposed:` column is compared with the hiring lead's old Scorecards from the same Entrevista. `debrief-cutover` is kept apart from `debrief-pending-update` because feeding those Scorecards in as inputs would spoil this comparison.

### 5.4 Rule checks for every skill

- No verdict, recommendation, ranking, count or total.
- The deliverable is in English.
- Nothing is written outside the sandbox.

### 5.5 Trigger evals

- Spanish and English phrasings for every branch of each trigger.
- Negatives drawn from the look-alikes in §4 and from the `human-resources` requests (`interview-prep`, `recruiting-pipeline`).

### 5.6 Case table

This is the only place in the spec that names a person or a source path; the rest cites cases by handle and copies no quotes, CV content or real outcomes. Paths are under `~/Workspace/leadership/` unless stated.

| Handle | Skill | Inputs |
|---|---|---|
| `jd-expedia` | JD | Propuesta `~/Downloads/[Globant - Expedia_TPA] SF Contentful Migration - October 2026 (1).pptx` (55 slides) and P&L `~/Downloads/[TPA Expedia] Contentful Migration Proposal - Pricing Sheet V4 _AI PODs_.xlsx`; question-round answers from the [intake prototype](prototypes/04-jd/PROTOTYPE-01-intake-analysis.md), plus the answer on whether line 4 leads people, added when the case is built |
| `jd-internal-client` | JD | `td-interviews/DXP TECHNOLOGY DIRECTOR - JOB DESCRIPTION (2).docx` (Spanish) |
| `jd-off-handbook` | JD | A brief converted from §1 of `tl-interviews/brandon-gallagher/interview-guide.md`: a Tech Leader for a Sitecore project already in flight, with a demanding client; no Propuesta or P&L. Intake answers from that session: the XM Cloud + Next.js stack, and the person leads the team |
| `jd-supplied-contradiction` | JD | `jd-internal-client` with the supplied document's years edited to contradict the level table |
| `jd-architect-line` | JD | `jd-expedia` with "Architect" as the Client's Role Name on line 4; a second run answers "Expert" |
| `match-internal-prior` | Match | Daniel Carrasco Herrera: CV plus the earlier AEM Debrief and Scorecards (`aem-interviews/Evaluaciones/Completed/Daniel Carrasco Herrera/`), against the reviewed backend JD from `jd-expedia` |
| `match-takehome` | Match | Jhon Garces: CV plus take-home report (`react-interviews/candidatos/jhon-garces/`), against the reviewed frontend JD from `jd-expedia` |
| `match-external-leadership` | Match | Gustavo Hurtado: CV (`td-interviews/Evaluaciones/In Progress/Gustavo_Hurtado/`), against the reviewed JD from `jd-internal-client` |
| `guide-pair` | Guía | The reviewed `match-internal-prior` and its JD; two Entrevistadores, one soft and one technical |
| `guide-takehome` | Guía | The reviewed `match-takehome`, its JD and the take-home report |
| `guide-second-interview` | Guía | The reviewed `match-external-leadership` and `debrief-pending-update`; the DXP Director as the only Entrevistador |
| `guide-off-handbook` | Guía | The reviewed JD from `jd-off-handbook`; an Evaluación de match fixture produced from the CV `tl-interviews/T. Brandon Gallagher_Sitecore (1).pdf`; three Entrevistadores: the hiring lead (leadership), the Managing Director, and a Sitecore Expert (technical block) |
| `guide-missing-match` | Guía | A Guía case with its Evaluación de match removed |
| `guide-stale-match` | Guía | A Guía case with `jd_updated` older than the JD's `updated` |
| `debrief-single-leadership` | Debrief | Jose David Restrepo: Gemini transcript plus the converted old guide (`td-interviews/Evaluaciones/Completed/Jose_David_Restrepo/`); JD from `jd-internal-client`; no Evaluación de match |
| `debrief-pending-update` | Debrief | Gustavo Hurtado: Gemini transcript plus the converted old guide; JD from `jd-internal-client`; match from `match-external-leadership`. Run twice; between runs the hiring lead writes an "Another interview" Decision and a Resolution |
| `debrief-pair-degraded` | Debrief | Swaroop Kumar Reddy: Gemini notes plus the converted old guide plus the Candidate Profile (`aem-interviews/Evaluaciones/Completed/Swaroop Kumar Reddy/`); match from the Candidate Profile; JD from the JD skill run on a brief (AEM Developer, L5) |
| `debrief-cutover` | Debrief | Gustavo Hurtado's raw folder as it stands (`td-interviews/Evaluaciones/In Progress/Gustavo_Hurtado/`): the transcript, the old guide unconverted, 1–5 Scorecards with a recommendation, the old Debrief |
| `debrief-off-guide` | Debrief | `debrief-single-leadership` with one or two questions removed from its converted Guía |
| `debrief-stale-match` | Debrief | A Debrief case with `jd_updated` older than the JD's `updated` |
| `debrief-missing-english` | Debrief | A Debrief case with no English result |
| `debrief-missing-interviewer` | Debrief | A Debrief case where an Entrevistador in `interviewers` has no transcript, Scorecard or notes |
| `debrief-export-pending` | Debrief | A Debrief case with export requested while the latest Decision is empty |
| `status-sandbox` | Status | A tree assembled from the frozen outputs of the JD, match, Guía and Debrief cases (JDs, Evaluaciones de match, Guías, transcripts and Debriefs, including the second run of `debrief-pending-update` and the Guía of `guide-second-interview`); one run per Oportunidad in it |
| `status-not-evaluated` | Status | `status-sandbox` with one Evaluación de match removed |
| `status-interviewed` | Status | `status-sandbox` with one Debrief removed and its transcripts kept |
| `status-shortlist` | Status | `status-sandbox` with a `shortlist.md` the hiring lead writes for one Posición |

### 5.7 Not covered by a past case

- A second Entrevista inside the Debrief: covered by the first live Candidato who has two.
- The `presales` origin.

## 6. Build order

The skills are built in chain order, because each skill's cases take the reviewed output of the one before as fixtures.

0. **Smoke check.** Write `staffing/.claude/settings.json`, the two-line `CLAUDE.md`, one file in `.claude/shared/`, and a stub `SKILL.md` per `staffing-*` skill. From `tests/runs/smoke/` (with empty `opportunities/` and `people/`), run `claude -p` with the settings and check that the `staffing-*` skills are listed, no `human-resources:*` skill is, and a skill reads a file from `../../shared/`.
1. **Shared reference.** Write the files of §3, and the export script. Convert to Markdown, in `hr-job-descriptions/`, the HR versions in `~/Downloads/ENGINEERING/` that the level table names *(call 13)*:
   - `BACK END DEVELOPER/`, `FRONT END DEVELOPER/` and `AEM DEVELOPER/` (back end and front end): Semi Senior II, Senior I, Senior II, Experience Senior I, Experience Senior II;
   - `LEADS/`: Technical Lead I and II, Software Architect, Technical Manager, DXP Technology Director.

   Named e.g. `backend-senior-i.md`, `aem-frontend-experience-senior-ii.md`, `technical-lead-ii.md`, `software-architect.md`.
2. **Acceptance inputs.** Copy each case's inputs (§5.6) into `tests/acceptance/<handle>/`.
3. **Skills,** each with skill-creator: `SKILL.md`, `template.md`, sibling files, evals pointing at its cases, trigger evals, then description optimization. After each skill, the hiring lead reviews its outputs, corrects and freezes the ones later cases use, and writes the content checks.
   1. `staffing-jd`.
   2. `staffing-match`, on the reviewed JDs. It also produces the match fixtures for `debrief-pair-degraded` and `guide-off-handbook`.
   3. `staffing-interview-guide`. Seed the question bank first from the existing banks: aem's Top 20, td's Top 21, react's guide and tl's ad hoc questions, in the shape of §4.3.
   4. `staffing-debrief`.
   5. `staffing-status`, over a tree assembled from the frozen fixtures of the earlier cases (§4.5).
4. **Cutover,** once the suite is live ([Debrief inputs outside the suite's shape](issues/12-debrief-inputs-outside-the-suite-shape.md)):
   - Every Candidato in progress enters the suite, at their next step: a new Entrevista or a Debrief. Nobody finishes in an old workspace, and there is no batch migration; an old folder is untouched until its Candidato's next step.
   - Without interview evidence (at cutover: six aem Candidatos with an old guide, one react Candidato with only a take-home report, the tl Sitecore Candidato): an Evaluación de match from scratch, then a Guía. The old guide is not reused.
   - With interview evidence (at cutover: the `debrief-cutover` Candidato only):
     1. The Oportunidad and Posición are created first, with `staffing-jd` on the old JD (the internal-client path).
     2. The hiring lead copies, without moving, the transcript and old Scorecards into `interviews/<YYYY-MM-DD>/` and the CV into the person's folder. The skills identify them by content; no import action is needed.
     3. `staffing-debrief` rebuilds the Debrief from the primary evidence (§4.4, cutover inputs).
     4. A later Guía reads the rebuilt Debrief like any other.

After the build, and outside it: writing the handbook's `evaluation-criteria/` pages (until then the skills fall back as in §3.3), and archiving the per-stack workspaces.

## 7. Calls made while assembling

No ticket answered these; each was needed to make the spec buildable. The hiring lead confirmed all of them on 2026-10-27, as written here.

1. **A third input mark, Optional** (read when present, never asked for), for the take-home report, screening notes, internal history, a Guía in the Debrief, and Presales statements. [Skill boundaries](issues/03-skill-boundaries.md) marks every input required or offered, which would make each skill ask for a take-home report on every run.
2. **The Debrief of earlier Entrevistas is an offered input of a later Guía:** when an earlier Entrevista has a transcript but no Debrief, the Guía offers to run `staffing-debrief`. When declined, it reads the earlier Guías so it repeats no question, and says what it cannot target.
3. **Re-evaluation replaces `match-evaluation.md`,** after saying that levels the hiring lead corrected in place will be replaced, and asking. Afterwards it lists the Requisitos whose level changed against the previous file.
4. **Origin tags are written `` `[origin]` `` after each Requisito,** like the prototype's tags but with the final origin names, so the export can strip them.
5. **Frontmatter of `opportunity.md` and `jd.md`:** `opportunity`, `updated`, plus `position` on the JD. The Disk layout's fields (`person`, `candidate_kind`) do not apply to them.
6. **`shortlist.md` is an ordered list,** `<n>. <person-slug>: <note>`, so `staffing-status` can read the positions.
7. **`opportunity.md`'s table carries headcount and start per Posición,** which the status Overview needs; the intake asks them when there is no P&L.
8. **Where Candidato-level inputs are kept:** the take-home report copy, screening notes and the English result go to the Candidato folder; a second `pasted-<YYYY-MM-DD>.md` on the same day takes a numeric suffix.
9. **Fixed lines use English terms:** "The match evaluation found no evidence for Must have <X>…", "No match evaluation: no points to probe were set.", "One interviewer: no independent second view." The tickets wrote them with the Spanish terms.
10. **Quotes in their original language plus an English translation** apply to every deliverable that quotes (the Evaluación de match included), not only the Debrief.
11. **`staffing-status` had no case.** Its cases run over a tree assembled from the other cases' frozen fixtures, plus mutated cases for what that tree lacks (§4.5).
12. **Section order of the Guía.** [Unified Guía](issues/07-interview-guide.md) fixes the contents but not the order.
13. **Which Descripciones de cargo are converted,** and their file names (§6 step 1).
14. **"rubric pending: using roles"** for a leadership role, which reads `roles/<role>.md`, not `career-paths`.
15. **Internal or external is asked for a single CV too,** not only in a batch.
16. **The interviewer tip** "Confirm Claude's proposed Calificaciones before discussing with other Entrevistadores" became "Form your own view of the Candidate before discussing them with other Interviewers", because [Unified Debrief](issues/08-debrief.md) moved confirmation to the hiring lead.
