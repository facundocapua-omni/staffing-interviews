---
name: staffing-jd
description: JDs and opportunity.md for an Oportunidad, from its Propuesta and P&L, a brief or a supplied JD. Use when starting an Oportunidad (a proposal deck or pricing sheet to staff, "armar los JDs"), adding or changing a Posición, updating a JD, or exporting one to PDF.
---

# staffing-jd

Writes an Opportunity's `opportunity.md` and the `jd.md` of each of its Positions. A JD is the recruiting brief: recruiting sources Candidates from it, and every later skill evaluates them against it. One run covers the whole Opportunity, never a single Position.

On every branch, read first:

- `${CLAUDE_SKILL_DIR}/../../shared/conventions.md`: language, the hiring lead decides, `Proposed:`, inputs, tree root, client name.
- `${CLAUDE_SKILL_DIR}/../../shared/disk-layout.md`: paths, slugs, frontmatter.

## Inputs

| Input | Mark |
|---|---|
| The Proposal (usually a deck) and the P&L; in their place, the hiring lead's material: a brief or a supplied JD, as files or pasted text | Required. With none of them, stop and ask for it: no skill produces them. |
| Presales' own statements: its notes, a message the hiring lead pastes, its answer to a forwarded intake question | Optional |
| The handbook, `level-equivalence.md`, `hr-job-descriptions/` (all in `${CLAUDE_SKILL_DIR}/../../shared/` except the handbook) | Reference |

Read a deck or a `.docx` as text with `markitdown <file>` (`textutil -convert txt -stdout <file>` also works for `.docx`), and a P&L with `openpyxl` on its Labor Estimate and SOW sheets. Convert on stdout or in your scratchpad: the tree holds only the kept originals and the artifacts.

## New Opportunity

### 1. Root and kept inputs

Resolve the tree root (conventions), starting with `ls -d opportunities people` in the working directory: the folders may be empty, which Glob does not show. Read enough of the inputs to name the Opportunity `<client>-<project>`, then copy every input into `opportunities/<op>/` under its original name, and save pasted text as `pasted-<YYYY-MM-DD>.md`. Copy, never move: the originals stay where the hiring lead left them. When the inputs do not name the client or the project, ask in the intake round and keep the inputs right after the answers.

Done when every input sits in `opportunities/<op>/`.

### 2. Intake analysis

Read every input and draft the analysis that becomes `opportunity.md`:

- the context: client, project, workstreams, dates, stack signals, locations;
- the P&L lines → Positions table: one row per Labor Estimate line, mapped through the intake rules and the Requirement sources below. Without a P&L, one row per Position the material describes;
- the inconsistencies found.

Done when every line has a row, and every row either gets a JD, gets none with its reason, or waits on a question of the round.

### 3. Intake round

Show the hiring lead the analysis and one round of numbered questions, in Spanish. Ask each of these that applies:

- every inconsistency found (e.g. a SOW vs Labor Estimate gap, a role label against the Proposal's platform, a workstream outside the Labor Estimate);
- for every Sr 3 line, whether the person leads people;
- for a Sr 3 line whose Client's Role Name is "Architect", whether the Position is an Expert or a Tech Leader;
- the level of each Position, when there is no P&L;
- for a level whose row names two HR job descriptions (Tech Lead I / II, Experience Senior I / II), which one sets the years;
- every contradiction between a supplied JD and the base (years, English, a level Must have), with both values side by side;
- who supplied each supplied JD: the hiring lead, the client or Presales. Ask even when the message seems to say: the tag follows the answer, never a guess;
- for a Position across several platforms, whether it needs each one or at least one of them, and which go to Nice to have;
- whether the client is internal, when the material does not say;
- the headcount, start and location of each Position, when the inputs leave them open;
- Claude's platform Requirements, when neither the handbook nor an HR job description covers the platform. Write each in English, prefixed `Proposed:`, exactly as it would land in the JD, so the hiring lead confirms the very wording; offer each as Must have or Nice to have.

Then stop and wait for the answers. Done when the round is sent.

### 4. Write

Write `opportunity.md` and every `jd.md` of the Opportunity in this run, from `${CLAUDE_SKILL_DIR}/template.md`, with today as `updated`.

- A Requirement whose question is still unanswered is written nowhere. `opportunity.md` records the question as open, with what waits on it; the hiring lead closes it later through Update a JD. The round is not repeated.
- A `Proposed:` Requirement the hiring lead did not confirm reaches no file. A confirmed one carries `hiring lead`, and loses the prefix.
- An answer that leaves something out of the Position applies to the whole JD: no Requirement, responsibility, keyword or screening point brings it back.
- Logistics come from the inputs or an answer. A value an open question bears on reads "To be confirmed"; the section is always there.
- `opportunity.md` names no person: a line already assigned reads "no: already assigned to a named person".

Done when every Position marked for a JD has its `jd.md`, and each one passes this check:

- Must have is a short filter (see Requirement sources), and every "Not a fit if" line negates one Must have at its strength;
- two tiers only, Must have and Nice to have, with no weights;
- every Requirement and every line of "What the person will do" closes with at least one origin tag;
- English is B2, or B1 where the hiring lead granted the exception for a role that does not face the client;
- no allocation (FTE, months, gaps between months), and no rate, cost, margin or salary;
- the client is anonymised, unless it is internal: search the file for the client's name, brands, domains and internal product names (a design system's name, a team's name), and replace each with a description.

### 5. Offer the export

Ask one yes/no question: export the JDs to PDF? On yes, go to Export.

## Add or change a Position

The same intake rules and sources, for that one Position: a round with only the questions that apply to it, then its `jd.md` and its row in `opportunity.md`, whose `updated` changes. Changing a Position that already has a JD also follows Update a JD.

## Update a JD

1. Rewrite `jd.md` with today's `updated`, under the same rules. A change that raises a question goes through a round first.
2. List the stale Candidates: every `people/*/<op>--<position>/match-evaluation.md` whose `jd_updated` differs from the new `updated`, in alphabetical order.
3. When the list is not empty, offer once to run `staffing-match` on them as a batch, one subagent per Candidate. Re-evaluating is the hiring lead's request: on no, end with the list.

## Export

Read `${CLAUDE_SKILL_DIR}/../../shared/export.md` and run its script on each `jd.md`. The script strips the origin tags and the off-handbook note, which is why `template.md` fixes their form. Done when each PDF sits next to its source.

## Intake rules

- **Only DXP technical lines get a JD.** A P&L lists the whole priced team: lines already assigned to a person, structure or governance lines, and practice roles (Globant `Lead`) get none. A technical line whose role the handbook lacks is flagged `Off-handbook role: <role>` and asked about in the round.
- **Seniority** comes from the Labor Estimate, never from the client-facing SOW sheet, and maps to a level through `level-equivalence.md`. A gap between the two sheets is a flag in `opportunity.md`, never in the JD.
- **Platform and technical Requirements** come from the technology the Proposal defines. A P&L role label ("AEM Backend Developer") is only today's catalog name.
- **Workstreams staffed by the same people** fold their needs into the same JD.
- **Seats:** lines with the same handbook role, level, platform and location are one Position, with their seats as its headcount.
- **Allocation** (FTE curves, gaps between months) stays out of the JD: a JD sources a profile.
- **English:** B2 minimum for every Position; B1 only as an exception for a role that does not face the client.
- **A migration's source platform:** familiarity with it enters as Nice to have.
- **Without a Proposal or P&L** (any Opportunity, e.g. a running project that needs a new Tech Leader, and always an internal client): ask the level in the round, write `opportunity.md` all the same, and anonymise the client unless it is internal.

## Requirement sources

**The base** is generic to a role and level, in three parts: role, level and platform. Fill each part from the first source in this order that covers it:

1. The handbook (`~/Workspace/martech/structure/src/content/docs/`):
   - role: the `### Must have` of `roles/<role>.md`;
   - level: the level's row in `career-paths/<track>.md`, with `reference/career-levels.md` (for L8, its Tech Leader or Expert focus);
   - platform: the platform's entry under the role's `### By platform`. A leadership role has none: read `technologies/<platform>.md`, and pitch the platform part at the role (leading delivery or architecture on the platform), never its stack layer by layer.
2. An HR job description of the same role (and of the same platform, for the platform part), only for what the handbook does not cover. `hr-job-descriptions/README.md` maps levels to files and says which sections to take.
3. Claude's `Proposed:` Requirements in the intake round. Only what the hiring lead confirms is written, with origin `hiring lead`.

Years always come from `level-equivalence.md`, with origin `HR job description`: the handbook has none.

**Position-specific** Requirements come from the Proposal, Presales, a supplied JD and the hiring lead's answers.

**Must have is the filter** recruiting applies: each line is something it can check in a CV or a screening call, and lacking it rules the Candidate out. A recruiter reads it in one pass, so it usually stays under a dozen lines:

- Fold related items into one line that keeps every tag of what it folds: "Code review and mentoring of the Developers on the team `[handbook role]` `[handbook level]`".
- The level's scope enters as the one line that states it ("Has led a project's technical delivery end to end, managing the Developers"); its focus items (branching strategy, executive reporting) describe the job and go to "What the person will do".
- A supplied JD's list of soft skills folds the same way, into a line or two.

**A supplied JD** sits above the base:

- Its Requirements carry `supplied JD`, translated into English; the base fills in whatever it does not cover.
- A contradiction with the base goes to the round, and the hiring lead chooses. Nothing is resolved silently, and the Requirement waits until the answer.
- An HR job description the hiring lead hands in for a Position counts as a supplied JD: the tag follows who chose it for the Position, not the file's format. From any HR job description, take only the sections the README names.

**Software Architect** (an Expert Position): the Must haves come from the handbook's `expert` role; the 11 years and the responsibilities from `software-architect.md`, with origin `HR job description`. Its stack list stays out: the platform comes from the Proposal and the order above. Flag the row `Expert is a regional role in the handbook; project scope from the Propuesta`. The hiring lead's 2024 draft (5 years) is not a source.

**An off-handbook platform** (e.g. a Sitecore Tech Leader): the role and level come from the handbook (Leader, L8); the platform part from the Proposal when there is one, and from the proposals the hiring lead confirms. The handbook does not cover the platform: say so, and invent no stack.

### Flags for an incomplete base

- `opportunity.md`: a flag on the Position's row, `Off-handbook platform: <platform>` or `Off-handbook role: <role>`. The `priced as Sr 3, IC Position mapped to L7` and `Expert is a regional role…` flags go in the same column.
- `jd.md`: the off-handbook note at the top (form in `template.md`), saying which part of the base is missing and where those Requirements came from.

## Origins

`handbook role`, `handbook level`, `handbook platform`, `HR job description`, `Propuesta`, `presales`, `supplied JD`, `hiring lead`, `suite rule`. Claude is never an origin.

- A Requirement is `presales` only when the hiring lead says it comes from Presales. What the Proposal says keeps `Propuesta`.
- English carries `suite rule`, plus `supplied JD` when a supplied JD states it.
- Tags close the line, one per source that backs it: `` `[handbook platform]` `[Propuesta]` ``.

Search keywords, screening and "Not a fit if" restate the Must haves and Nice to haves for recruiting and add no Requirement of their own, so they carry no tags.
