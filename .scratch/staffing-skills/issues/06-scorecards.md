# Scorecards: dimensions and scale

Type: grilling
Status: resolved
Blocked by: 01
Map: [Staffing skills suite](../map.md)

## Question

What Soft and Technical scorecards does the whole suite use?

Decide:

- The dimensions and the scale, unifying the existing AEM scorecards (Technical 1–5, Soft) with whatever the other per-stack workspaces used. Start from the conflicts listed in [Inventory existing staffing material](01-inventory-existing-staffing-material.md).
- How technical dimensions vary by track (frontend, backend, devops, qa, leadership roles) and by platform.
- Whether dimension definitions live in `martech/structure/src/content/docs/evaluation-criteria/` (pending in the handbook today) or inside the suite.
- How a score Claude proposes is told apart from a score an Entrevistador confirmed.
- If the suite generates scorecards, their file names inside the interview folder (see [Disk layout of the chain](02-chain-disk-layout.md)).

Both the Guía de entrevista and the Debrief measure against these dimensions.

## Answer

Grilled 2026-10-21. Terms resolved in [GLOSSARY.md](../../../GLOSSARY.md): Scorecard, Dimensión, Calificación.

> **Amended by [Unified Guía de entrevista](07-interview-guide.md)** (2026-10-21). Where the two disagree, these points win:
> - **No blank Scorecards.** The Guía no longer writes `scorecard-<interviewer-slug>.md` files. Entrevistadores take no notes; Claude builds the Calificaciones from the call's transcript, marked `Proposed:` and citing the Guía's question ids, and each Entrevistador confirms their own. A Scorecard an Entrevistador brings is still accepted. Whether the transcript-based evidence is a Scorecard per Entrevistador or goes straight into the Debrief: [Unified Debrief](08-debrief.md).
> - **English is provided separately.** It stays a soft Dimensión, but the Entrevista does not assess it: its result reaches the hiring lead separately. The skill asks for it when it is missing; if it never arrives, it is Not assessed. This is the one exception to "only interview evidence counts".

> **Amended by [Unified Debrief](08-debrief.md)** (2026-10-22). Where the two disagree, these points win:
> - **A Scorecard is what an Entrevistador brings.** The suite writes no Scorecard files. Claude's transcript-based Calificaciones (`Proposed:`, citing `<YYYY-MM-DD> · Qn`, attributed to the block owner) live in the Debrief's Calificaciones table, one column per Entrevistador per Entrevista.
> - **The hiring lead confirms.** A `Proposed:` Calificación is confirmed when the hiring lead edits it, checking with the block owner when it is someone else. A Scorecard an Entrevistador brings is theirs and carries no prefix.

**The Scorecard**

- One Entrevistador's Calificaciones for one interview, soft and technical in one file. It is optional: the Debrief also works from a transcript or notes alone.
- The suite writes one blank per Entrevistador listed in the Guía's `interviewers`, at the same time as the Guía: `interviews/<YYYY-MM-DD>/scorecard-<interviewer-slug>.md`. A filled Scorecard that comes back under another name or format is identified by content.
- Frontmatter: the Disk layout fields (`opportunity`, `position`, `person`, `candidate_kind`, `date`) plus `interviewer`, singular.
- At the top it states what it rates against: role or track, the Posición's career level, and a link to the handbook rubric, or "rubric pending: using career-paths". A delegated Entrevistador can then tell what Meets means without asking.
- Body:
  - Per Dimensión: the Calificación and its evidence (quotes, and the question it came from).
  - For Platform knowledge, a checklist of sub-areas to collect evidence on. The sub-areas are not rated one by one.
  - Red and green flags.
  - Notes per question.
- Left out:
  - A recommendation (Strong Hire … Strong No Hire), even from a human Entrevistador: it anchors the Debrief, and in the aem CSV it had already drifted into free text.
  - "Does the level match the CV?": comparing with the CV is the Debrief's job, since the Debrief has the Evaluación de match.
  - Round, per-question ratings, averages.

**Scale**

- A Calificación is Below, Meets or Exceeds the Posición's career level, or Not assessed. It is a word, not a number.
- No averages, totals, weights or thresholds anywhere in the suite: a threshold is a verdict reached by arithmetic. Importance comes from the JD's Requisito excluyente / Plus tiers and from the hiring lead.
- Missing evidence:
  - Not covered in the interview: Not assessed, never a default value.
  - Asked and followed up with no concrete example: rated (Below), because that is evidence.
- Only interview evidence counts, never the CV.
- A confident wrong answer counts against the Candidato more than an honest gap.
- The historical aem 1–5 scorecards are not converted.

**Dimensiones** (deliverables use these names and definitions verbatim)

| Block | Dimensión | Definition |
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
- Leadership roles (Tech Leader L8, Expert, Manager, Director) add the 3 leadership Dimensiones. They keep the full technical core, measured against their role: for a Director, Meets in Code quality means setting standards, not writing code.
- English is rated against the English level the JD sets: B2 minimum, B1 as an exception (see [JD structure](04-jd-structure.md)).
- What changes by track and level is what Meets means, not the Dimensiones themselves:
  - Individual-contributor tracks read `career-paths/<track>.md` and `reference/career-levels.md`.
  - Leadership roles read `roles/<role>.md`.
- Platform knowledge's sub-areas come from `technologies/<platform>.md` (Stack by layer) and from the Posición's own Requisitos.
- When the handbook lacks the platform or the role (Sitecore, Software Architect), the sub-areas and expectations come only from the JD's Requisitos. The skill says the handbook does not cover it and never invents a stack.

**Flags**

- The lists are prompts, not a checklist. The Entrevistador writes down only what they observed, each flag with its evidence, and may add others.
- Red:
  - Consistently bashes previous employers
  - Cannot give specific examples
  - Defensive when challenged
  - Resistance to learning
  - Takes all credit without mentioning the team
  - Asks no questions
  - Confident wrong answer
- Green:
  - Honest about gaps and proposes how to address them
  - Explains complex concepts clearly
  - Discusses challenges respectfully
  - Asks thoughtful questions about the team
  - Acknowledges mistakes and lessons learned
  - Enthusiastic about the domain
  - Mentions helping others grow
- aem's "Inconsistencies between CV and answers" moves to the Debrief.

**Where the definitions live**

- The names and one-line definitions are fixed here and carried into the spec.
- The full rubric (what Meets means at each level) lives in the handbook's `evaluation-criteria/`. Its template is adapted to these Dimensiones: soft and leadership in one shared file, the technical core one file per track.
- Skills only read the rubric.
- While a rubric page is `Pending`, the skill falls back to `career-paths`, `career-levels` and `roles`, and says the rubric is missing.
- Writing those handbook pages is execution after the spec.

**Proposed vs confirmed**

- When Claude fills a Scorecard from an Entrevistador's notes or transcript, every Calificación it writes carries the prefix `Proposed:` (e.g. `Proposed: Meets`).
- The Calificación is confirmed when the Entrevistador removes the prefix or changes the value. A Calificación without the prefix is the Entrevistador's.
- `Proposed:` marks Claude's proposals in documents where humans also write (Scorecard, Debrief). It survives a PDF export and needs no colour or extra column.
- A document written entirely by Claude, such as the Evaluación de match, says so once in its header instead (refined in [Evaluación de match rubric](05-match-evaluation-rubric.md)).

**Handed to other tickets**

- Questions map to these 14 Dimensiones, and the blank Scorecards are written with the Guía: [Unified Guía de entrevista](07-interview-guide.md).
- These go to [Unified Debrief](08-debrief.md):
  - the `Proposed:` marker, with proposed Calificaciones read as Claude's;
  - the comparison of the CV with what the interview showed;
  - no Entrevistador recommendation to consolidate, and no averages.
- Which skill writes the blank Scorecards, and the Dimensiones and `Proposed:` as shared conventions: [Skill boundaries](03-skill-boundaries.md).
- When the handbook lacks a platform or role, the Scorecard follows whatever base the JD gets: [Handbook gaps for JDs](11-handbook-gaps-for-jds.md).
