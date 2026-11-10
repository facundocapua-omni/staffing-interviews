# Debrief inputs outside the suite's shape

Type: grilling
Status: resolved
Blocked by: none
Map: [Staffing skills suite](../map.md)

## Question

What do the Debrief, and the Guía of a later Entrevista, do with inputs that do not have the shape the suite gives them?

[Acceptance cases](09-acceptance-cases.md) converted past cases into fixtures because nothing on disk has the suite's shape. Real use will produce the same mismatches. Decide:

- **Evidence from a question that is not in the Guía.** Entrevistadores improvise and follow threads. Decide how such evidence is cited when it has no Qn, and which column it goes to.
- **A Scorecard an Entrevistador brings in another shape.** It may use other dimensions, or a numeric or Hire / No Hire scale, as the old aem and td Scorecards do. Decide how it fills the Dimensión rows that [Unified Debrief](08-debrief.md) says a brought Scorecard fills verbatim.
- **A Debrief with no Evaluación de match,** e.g. a Candidato interviewed without one. Options: the skill stops, it offers to run the evaluation, or it goes on without the Points to probe section.
- **Candidatos in progress at cutover,** e.g. one waiting for another Entrevista who has an old guide, old Scorecards and an old Debrief. Decide whether they finish in the old workspace or enter the suite, and if they enter, how the next Guía reads their old Debrief.

Once decided, say which case in [Acceptance cases](09-acceptance-cases.md) gets a variant check for each answer, e.g. `debrief-pending-update` for cutover.

The answer may add an action, such as importing an old Debrief, that [Skill boundaries](03-skill-boundaries.md) has to place.

## Answer

Grilled 2026-10-22/23. Term refined in [GLOSSARY.md](../../../GLOSSARY.md): Scorecard (any shape; only ratings on the suite's scale are Calificaciones).

**Facts that shaped the answer**

- In progress at cutover:
  - aem: six Candidatos with a CV or profile and an old guide (March–July 2026), with no interview evidence.
  - react: one Candidato with only a take-home report.
  - tl: one Candidato with only a guide (the Sitecore case).
  - td: only Gustavo Hurtado has interview evidence: a transcript, two old 1–5 Scorecards with a recommendation, and an old Debrief with "another round" ticked.
- Gemini "Notes by Gemini" files hold a verbatim transcript, with a timestamp about every minute and speaker labels that are sometimes wrong (the Candidato appears under another surname).

**Evidence from a question that is not in the Guía**

- A question that follows the thread of a Guía question is cited `<YYYY-MM-DD> · Qn follow-up`.
- Any other question is cited `<YYYY-MM-DD> · off-guide [hh:mm:ss]`, with the transcript's timestamp and the question as asked, in one line. A later Entrevista's Guía uses the question as asked so it does not repeat it.
- Claude never invents a question id: ids belong to the Guía.
- The column follows the rule in [Unified Debrief](08-debrief.md): the owner of the block where the evidence arose, per the Guía's agenda. It counts like any other evidence.

**An Entrevista with no suite Guía** (an old guide at cutover, or an Entrevista held without asking for one)

- No Guía is written after the fact: that would be a plan that never existed.
- Every citation is `<YYYY-MM-DD> · [hh:mm:ss]` with the question as asked. The sources line says "No Guía: cited by timestamp". When the transcript has no timestamps, the question as asked identifies the citation on its own.
- An old guide is read for context only and is never cited.
- With one Entrevistador, there is one column. With several, the skill asks the hiring lead once who led each block or stretch of time.

**A Scorecard an Entrevistador brings in another shape**

- A rating is copied verbatim, with no prefix, only when both hold:
  - its scale is the suite's (Below / Meets / Exceeds / Not assessed);
  - its dimension maps one-to-one to a Dimensión. The names need not match. A dimension that means the same thing is copied under the Dimensión's name, and the subsection shows the mapping, since Claude made it: *"from <Entrevistador>'s 'Visión Arquitectónica'"*.
- Anything else is never converted: a number, a Hire / No Hire, a dimension covering two Dimensiones (td's "Stakeholders y Delivery"), or two of its dimensions landing on one Dimensión.
  - The rating is quoted verbatim, in its own scale and under its own name, attributed, as evidence in the matching Dimensión's subsection.
  - The column is Claude's `Proposed:` from the transcript.
- With no transcript, Claude proposes from the Scorecard's written evidence, `Proposed:`, citing it. Never from the number alone.
- A Scorecard with bare numbers and no written evidence or transcript is lower-fidelity evidence. Under the [Unified Debrief](08-debrief.md) rule, the skill first asks the hiring lead to fill the gap, for example by asking the Entrevistador to rate on the suite's scale or to add the evidence. Without a clear answer the row is `Proposed: Not assessed`, with the original rating quoted and the limit stated in that Entrevista's sources.
- A dimension with no Dimensión to map to is listed verbatim in that Entrevistador's sources line as "not mapped to a Dimensión".
- A recommendation in a brought Scorecard is left out, for the reason given in [Scorecards: dimensions and scale](06-scorecards.md): it anchors the Decision. The sources line says "recommendation left out"; the original file stays for the hiring lead.

**A Debrief with no Evaluación de match**

- The Debrief skill offers to run it and does not stop.
- Run after the Entrevista, the evaluation still reads documents only, never the transcript. Its Puntos a indagar may well come out Not probed, which is what happened. Running it now also spares a later Entrevista's Guía, which stops without one.
- When the hiring lead declines, the Debrief goes on:
  - Points to probe reads "No Evaluación de match: no Puntos a indagar were set".
  - Not covered lists only Dimensiones.
- An old candidate profile from the per-stack workspaces is not an Evaluación de match.

**Candidatos in progress at cutover**

- Every one of them enters the suite. Nobody finishes in an old workspace, so only one process is maintained.
- There is no batch migration. A Candidato enters at their next step: a new Entrevista or a Debrief. Until then their old folder is not touched.
- **Without interview evidence:** they start from scratch with an Evaluación de match, then a Guía. The old guide is not reused.
- **With interview evidence:**
  1. Their Oportunidad and Posición must exist in the suite first, from the JD skill run on the old JD (the internal-client path).
  2. The hiring lead copies the files into the suite's tree, without moving them: the transcript and old Scorecards into `interviews/<YYYY-MM-DD>/`, the CV into the Candidato folder. The skills identify them by content, so no import action is needed. The old workspace stays as it is until it is archived, which is out of scope.
  3. The Debrief is rebuilt from the primary evidence: the transcript, with no Guía (see above), and the old Scorecards as brought Scorecards in another shape.
  4. The old Debrief's prose is never translated or carried over.
  5. Its ticked Decision is not copied. Nobody can tell for sure who ticked it, and Claude fills nothing in the Decision. The Decision list starts empty, the sources line names the old Debrief, and the skill asks the hiring lead to write their decision again.
  6. A later Guía then reads the rebuilt Debrief like any other.

**Evidence from outside an Entrevista** (a follow-up email, a reference, an internal Candidato's manager's opinion)

- It is not a Debrief source. The Debrief's sources stay the ones [Unified Debrief](08-debrief.md) set: interview evidence, the English result and the take-home report.
- The hiring lead may cite it in their own Justification or Resolution.
- When it changes what the documents show, the Evaluación de match is run again as a new document. The Debrief never re-evaluates it.

**Speaker labels in the transcript**

- When the content and the Guía's `interviewers` make the speaker clear, Claude corrects the label without asking and states it once in the sources: *"speaker label 'X' is the Candidato"*.
- When it stays ambiguous who said something, e.g. two Entrevistadores under one label, it is lower-fidelity evidence: the skill asks the hiring lead first and, without a clear answer, states the limit.

**Acceptance cases**

| Answer | Case | Variant checks |
|---|---|---|
| Question not in the Guía | New mutated case `debrief-off-guide`: `debrief-single-leadership` with one or two questions removed from its converted Guía | That evidence is cited `off-guide [hh:mm:ss]` with the question as asked, in the block owner's column; no invented id. |
| No Evaluación de match | `debrief-single-leadership` (it has no match among its inputs) | Offers to run the evaluation. When declined, Points to probe reads "No Evaluación de match…". |
| Scorecard in another shape, recommendation, no Guía, cutover | New real case `debrief-cutover`: Gustavo Hurtado's raw folder (`td-interviews/Evaluaciones/In Progress/Gustavo_Hurtado/`) as it stands: old guide unconverted, 1–5 Scorecards with a recommendation, old Debrief | Citations by timestamp with "No Guía" in the sources. The 1–5 ratings are quoted in their scale, never converted. "Recommendation left out". The Decision is empty and the old Debrief is only named in the sources. |
| Evidence from outside an Entrevista | `debrief-pair-degraded` | The Candidate Profile in the folder is not cited as Debrief evidence. |
| Speaker labels | `debrief-pending-update` | The sources line states that the mislabelled speaker is the Candidato. |

- `debrief-cutover` is kept apart from `debrief-pending-update`, whose calibration compares Claude's `Proposed:` column with those same old Scorecards; feeding them in as inputs would spoil it.

**Handed to other tickets**

- [Unified Debrief](08-debrief.md): amended, a brought Scorecard fills a column verbatim only on the suite's scale with a one-to-one mapping; off-guide and no-Guía citation forms.
- [Acceptance cases](09-acceptance-cases.md): amended, two new cases (`debrief-off-guide`, `debrief-cutover`) and three variant checks on existing cases.
- [Skill boundaries](03-skill-boundaries.md): no import action is needed; the Debrief skill offers to run the Evaluación de match, as the Guía skill does.
