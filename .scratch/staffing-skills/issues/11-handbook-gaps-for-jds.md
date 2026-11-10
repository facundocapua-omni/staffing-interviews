# Handbook gaps for JDs

Type: grilling
Status: resolved
Blocked by: none
Map: [Staffing skills suite](../map.md)

## Question

When the handbook cannot supply a JD's base, where does it come from, and how does the JD skill say so?

Decide:

- The missing rows of the level equivalence fixed in [JD structure](04-jd-structure.md): Globant "Lead" and the old Omni Experience Senior I/II (7 and 8 years). Check first whether an official Globant ↔ Omni equivalence exists.
- DXP roles the handbook lacks (Software Architect, for which an old JD exists) and platforms it lacks (Sitecore, used in the `tl-interviews` case). Options: the old JDs, a base specific to the Posición, or adding them to the handbook first.
- How a JD and `opportunity.md` flag a Posición whose base is incomplete, so recruiting never gets requirements Claude invented.

[Scorecards: dimensions and scale](06-scorecards.md) depends on this answer: when the handbook lacks the platform or role, a Scorecard's sub-areas and expectations come only from the JD's Requisitos.

From [Acceptance cases](09-acceptance-cases.md): once this is answered, the Sitecore Tech Leader case (`tl-interviews/brandon-gallagher/`, CV in `tl-interviews/`) becomes the acceptance case for a platform or role outside the handbook. Add it to that ticket's case table, with variant checks drawn from this answer.

## Answer

Grilled 2026-10-22/23. Terms added to [GLOSSARY.md](../../../GLOSSARY.md): Descripción de cargo and Presales. JD was refined to say where its Requisitos come from.

> **Amended by [Skill boundaries](03-skill-boundaries.md)** (2026-10-27). The Descripciones de cargo folder is `.claude/shared/hr-job-descriptions/<role>-<level>.md`, next to `.claude/shared/level-equivalence.md`.

**Facts that shaped the answer**

- No official Globant ↔ Omni ↔ handbook level equivalence exists anywhere on disk, so the suite's table is the only one. Globant's P&L template (`Params` sheet) has its own band of years per seniority.
- Globant's technical roles stop at Sr 3, and above them come SME, Tech Manager and Tech Director. "Lead" is the only seniority of a few practice roles that are not technical, such as Cultural Hacking Lead.
- Omni's old Experience Senior I/II (ranks 7–8, 7 and 8 years) continues the individual-contributor (IC) path after Senior II. It runs parallel to Tech Lead I/II and manages no one. In the handbook, L8 *is* Tech Leader, so no IC level exists above L7.
- The handbook's `Expert` is the old "Architect" renamed. It is defined as a standing regional technical authority, not a per-project seat, and has no years and no `By platform`.
- Two Software Architect documents disagree. The hiring lead's 2024 draft asks for 5 years and Adobe Commerce. HR's version in `~/Downloads/ENGINEERING/LEADS/` asks for 11 years at rank 9.
- Sitecore is not mentioned in the handbook or in any old Descripción de cargo. In the tl case, the hiring lead gave the stack (XM Cloud + Next.js).

**Level equivalence** (replaces the table in [JD structure](04-jd-structure.md))

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
- Globant's `Lead` has no row. It only appears on practice roles, which are not DXP technical roles, so the intake rules give them no JD.
- Years come from the HR job descriptions, not from the Globant P&L band. The two differ only on Sr 3 (8–10 vs 7+), and that difference gets no flag.
- When a P&L has "Architect" as the Client's Role Name on a Sr 3 developer line, the intake asks whether the Posición is an Expert or a Tech Leader.

**Where a JD's Requisitos come from**

- Two kinds of source feed a JD:
  - **Base**, generic to a role and level: the handbook and the Descripciones de cargo.
  - **Posición-specific**: the Propuesta, Presales, a JD the hiring lead supplies, and the hiring lead's intake answers.
- The base has three parts: role, level and platform. Each part is filled from the first source in this order that covers it:
  1. the handbook;
  2. a Descripción de cargo of the same role (and, for the platform part, of the same platform), only for what the handbook does not cover;
  3. Claude's proposals in the intake round.
- From a Descripción de cargo the skill takes:
  - its knowledge and requirements;
  - its years;
  - its responsibilities, which feed "What the person will do".
- It never takes the KPIs, the reporting line, the authority or the English level. English follows the suite's B2 rule.
- Claude proposes platform Requisitos from its own knowledge only in the intake round, as questions marked `Proposed:`. Only what the hiring lead confirms is written, with origin `hiring lead`. Anything not confirmed is written to no file.
- A JD the hiring lead supplies for a Posición is a Posición-specific source and sits above the base.
  - Its Requisitos carry origin `supplied JD`, and the base fills in whatever the supplied JD does not cover.
  - When it contradicts the base (years, English, a level Must have), the intake round shows the contradiction and the hiring lead chooses. Nothing is resolved silently.
  - `opportunity.md` records who supplied it: the hiring lead, the client or Presales.
  - The `jd.md` anonymises the client even when the supplied JD names it.
  - A Descripción de cargo the hiring lead hands in for a Posición counts as a supplied JD. The tag follows who chose it for the Posición, not the file's format.
- **Software Architect:**
  - Must haves come from the handbook's `Expert`. The 11 years and the responsibilities come from HR's version.
  - HR's stack list (Java, Python, Node.js, .NET…) stays out, because it is not the Propuesta's platform. The platform comes from the Propuesta and the mechanism above.
  - Flag "Expert is a regional role in the handbook; project scope from the Propuesta".
  - The 5-year draft is not a source.
- **Sitecore Tech Leader:** the role (Leader) and the level (L8) come from the handbook. The platform part comes from the Propuesta, when there is one, and from the proposals the hiring lead confirms.

**Origins** (replaces the list in [JD structure](04-jd-structure.md))

- The origins are `handbook role`, `handbook level`, `handbook platform`, `HR job description` (formerly "old JD (years)"), `Propuesta`, `presales`, `supplied JD`, `hiring lead` and `suite rule`. Claude is never an origin.
- `presales` marks a Requisito that Presales states outside the Propuesta and the P&L: its notes, a message the hiring lead pastes, or its answer to a forwarded intake question. The skill never infers it: a Requisito is `presales` only when the hiring lead says so. What the Propuesta says keeps the origin `Propuesta`.

**Input without a Propuesta or P&L**

- Any Oportunidad, not only one with an internal client, may come with only the hiring lead's material: a supplied JD or a brief. For example, a running project needs a new Tech Leader.
- The level is then asked in the intake round, and `opportunity.md` is still written.
- The client is anonymised unless it is internal.

**How an incomplete base is flagged**

- `opportunity.md`: a flag on the Posición in the P&L lines → Posiciones table, such as `Off-handbook platform: Sitecore` or `Off-handbook role: <role>`. The "priced as Sr 3" and "Expert is a regional role" flags above go in the same table.
- `jd.md` (the Markdown source): a note at the top that says which part of the base is missing and where those Requisitos came from.
- The PDF export for recruiting strips the note, as it strips the origin tags. Recruiting only sees confirmed Requisitos.

**Where the Descripciones de cargo live**

- The HR versions the suite uses are copied into the suite as Markdown, in a reference folder next to the level table. Drafts are not copied.
- They are frozen documents, so the handbook's "read, never copied" rule does not apply to them. This means the skill does not depend on `~/Downloads` at run time.
- [Skill boundaries](03-skill-boundaries.md) sets the path. The conversion is execution that follows the spec.

**Acceptance cases** (added to [Acceptance cases](09-acceptance-cases.md); inputs under `~/Workspace/leadership/`)

| Handle | Skill | Inputs | Variant checks |
|---|---|---|---|
| `jd-off-handbook` | JD | A brief converted from §1 of `tl-interviews/brandon-gallagher/interview-guide.md`: a Tech Leader for a Sitecore project already in flight, with a demanding client. No Propuesta or P&L. The intake answers come from that session: the XM Cloud + Next.js stack, and the person leads the team. | Asks for no Propuesta or P&L. Proposes the Sitecore stack in the intake marked `Proposed:`, and writes only what was confirmed, with origin `hiring lead`. Role and level come from the handbook (Leader, L8). `opportunity.md` has `Off-handbook platform: Sitecore` and `jd.md` has the note at the top; neither is in the PDF. |
| `guide-off-handbook` | Guía | The reviewed JD from `jd-off-handbook`; an Evaluación de match fixture from the CV `tl-interviews/T. Brandon Gallagher_Sitecore (1).pdf`; three Entrevistadores: the hiring lead (leadership), the Managing Director and a Sitecore Expert (technical block) | Says the handbook does not cover Sitecore and no question bank does either, and draws the technical questions from the JD's Requisitos. The Sitecore Expert owns the technical block, and its briefing works without the hiring lead's context. |

- The Evaluación de match is only a fixture, produced by the match skill from the CV. The match skill only reads the JD, so a gap in the handbook changes nothing for it. There is no Debrief case, because no transcript exists.
- Variant checks added to existing cases:
  - `jd-expedia`: the intake asks whether line 4 (AEM Backend, Sr 3) leads people. The hiring lead adds the answer to the answers fixture when the case is built.
  - `jd-internal-client`: the Director's Descripción de cargo counts as a supplied JD. Its Requisitos carry `supplied JD`, and the handbook's `director` role fills in what it does not cover.
- Mutated cases, one per new stop-and-ask rule:
  - `jd-supplied-contradiction`: `jd-internal-client` with the supplied document's years edited to contradict the table. The intake shows the contradiction, and the skill writes nothing for that Requisito until the hiring lead answers.
  - `jd-architect-line`: `jd-expedia` with "Architect" as the Client's Role Name on line 4. The intake asks whether it is Expert or Tech Leader. On a second run with the answer "Expert":
    - Must haves come from `Expert`.
    - The 11 years and the responsibilities carry `HR job description`.
    - The "Expert is a regional role" flag is present.
- Not covered by a past case: the `presales` origin. The spec says so.

**Handed to other tickets**

- [JD structure](04-jd-structure.md): amended with the level table, the origins, the supplied JD and the input without a Propuesta or P&L.
- [Acceptance cases](09-acceptance-cases.md): amended with the cases above.
- [Skill boundaries](03-skill-boundaries.md): the path of the Descripciones de cargo reference folder, next to the level table.
- [Scorecards: dimensions and scale](06-scorecards.md) and [Unified Guía de entrevista](07-interview-guide.md) need no change. When the handbook lacks the platform, expectations and technical questions still come from the JD's Requisitos, whatever base the JD got.
