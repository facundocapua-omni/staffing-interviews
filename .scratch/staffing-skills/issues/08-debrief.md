# Unified Debrief

Type: grilling
Status: resolved
Blocked by: 06
Map: [Staffing skills suite](../map.md)

## Question

What single Debrief replaces the per-stack ones?

Decide:

- Its inputs: transcripts, scorecards from other Entrevistadores, your notes, the Evaluación de match, and an optional take-home report.
- How several scorecards are consolidated (consensus, discrepancies), and the single-Entrevistador variant used for internal diagnostics (see the `aem-interviews` project memory).
- How Claude's proposals are marked against the dimensions in [Scorecards: dimensions and scale](06-scorecards.md).
- Where the decision lives and what is left blank for you, given that your managers and recruiting read it.

Start from the Debrief conflicts listed in the [inventory findings](../research/01-existing-staffing-material.md#debrief): verdict field, scorecards vs transcript as input, variants, audience, and level vocabulary.

From [Scorecards: dimensions and scale](06-scorecards.md):
- Scorecards are optional inputs. Calificaciones are Below / Meets / Exceeds / Not assessed, with no averages or thresholds.
- A Calificación prefixed `Proposed:` is Claude's, not the Entrevistador's. Mark the Debrief's own proposals the same way.
- Scorecards carry no recommendation, so there is none to consolidate.
- Comparing the CV with what the interview showed belongs here, including the "Inconsistencies between CV and answers" flag.

From [Unified Guía de entrevista](07-interview-guide.md):
- Entrevistadores take no notes: the call's transcript is the main evidence. The Guía writes no blank Scorecards any more. Claude builds the evidence per Dimensión from the transcript, with `Proposed:` Calificaciones that cite the Guía's question ids (Q1…Qn), attributing each block to its owner in the Guía's agenda. Still for this ticket: whether that evidence is a Scorecard per Entrevistador or goes straight into the Debrief. A Scorecard or notes an Entrevistador brings are still accepted.
- An Entrevista lasts one hour, and covering a Posición may take more than one, each with its own folder and Guía. Decide here whether there is one Debrief per Entrevista or one consolidated across a Candidato's Entrevistas.
- English is not assessed in the Entrevista: its result is provided to the hiring lead separately. When it is missing, the skill asks for it. If it never arrives, English is Not assessed. Show it against the level the JD sets.
- A later Entrevista's Guía reads the previous Debrief and targets the Dimensiones left Not assessed and the open discrepancies. The Debrief must make both easy to find.

## Answer

Grilled 2026-10-21/22. Terms resolved in [GLOSSARY.md](../../../GLOSSARY.md): Debrief (one per Candidato), Discrepancia (a Tension with a single Entrevistador); Punto a indagar and Scorecard refined.

> **Amended by [Debrief inputs outside the suite's shape](12-debrief-inputs-outside-the-suite-shape.md)** (2026-10-23). Where the two disagree, these points win:
> - **A brought Scorecard fills a column verbatim only on the suite's scale, with a one-to-one mapping to a Dimensión** (names may differ; the subsection shows the mapping). Any other rating is quoted as evidence, never converted, and the column is Claude's `Proposed:`. A recommendation in it is left out.
> - **Citations without a question id:** `<YYYY-MM-DD> · Qn follow-up`, `<YYYY-MM-DD> · off-guide [hh:mm:ss]` with the question as asked, or `<YYYY-MM-DD> · [hh:mm:ss]` for an Entrevista with no Guía.
> - **No Evaluación de match:** the skill offers to run it and goes on without it when the hiring lead declines.

**One Debrief per Candidato**

- One `debrief.md` per Candidato consolidates every Entrevista they had for the Posición: `people/<p>/<op>--<pos>/debrief.md` (+ `debrief.pdf`), next to `match-evaluation.md`, not inside `interviews/<YYYY-MM-DD>/`. This amends [Disk layout of the chain](02-chain-disk-layout.md).
- It is updated after each Entrevista. Claude's sections are rewritten; Resolutions and Decisions already written are kept, and the skill asks before touching them.
- A planned split of the Posición's coverage and an "Another interview" decision are handled alike: one more Entrevista in the same document.
- Frontmatter: the Disk layout fields with `date` as the last update, plus `interviewers` (every Entrevistador across the Entrevistas) and `interviews` (the Entrevista dates, which are their folder names).

**Inputs**

- Per Entrevista: the transcript (the main evidence) and its Guía (question ids Q1…Qn and the owner of each block).
- A Scorecard or notes an Entrevistador brings, identified by content.
- The Evaluación de match, for its Puntos a indagar. When it is stale against the JD (`jd_updated`), the header says so and its Puntos are used as they stand; it is never re-evaluated.
- The English result, provided separately. When it is missing the skill asks for it; if it never arrives, English is Not assessed.
- The optional take-home report: cited in Evidence for / against and in Discrepancias, never the basis of a Calificación. What the Candidato said about it in an Entrevista is interview evidence.
- An Entrevistador in `interviewers` with no transcript, Scorecard or notes: the skill asks whether to wait or go on without them. It never drafts a partial Debrief silently.
- Lower-fidelity evidence (a degraded or partial transcript, minimal notes taken because the Candidato did not consent to recording): the skill first asks the hiring lead to fill the gap. When there is no clear answer, it states the limit per Entrevista in the sources and in the evidence of every Calificación that rests on it. A Dimensión with no usable evidence is Not assessed, never inferred.

**Calificaciones and their evidence**

- A table with one row per Dimensión of the Posición and one column per Entrevistador per Entrevista. No consolidated column, no averages.
- A column comes verbatim from a Scorecard the Entrevistador brought: it is theirs, so it carries no prefix (a `Proposed:` left in it stays). Otherwise Claude proposes the column from the transcript, every value `Proposed:`. No Scorecard file is written first.
- Evidence goes to the column of the owner of the block where it arose, per the Guía's agenda. When a block has two owners, Claude proposes once and the column carries both names: it never proposes two values from the same transcript.
- Under the table, one subsection per Dimensión: each column's Calificación with its quotes, cited as `<YYYY-MM-DD> · Qn`.
- The hiring lead confirms a `Proposed:` Calificación by editing it (removing the prefix or changing the value), checking with the block owner when it is someone else. A delegated Entrevistador only returns the transcript and needs no access to these files. Claude never removes a `Proposed:`, so a Calificación still unconfirmed at Decision time shows as such. This amends [Scorecards: dimensions and scale](06-scorecards.md) ("each Entrevistador confirms their own").
- English row: the result provided (level, who provided it, when), the level the JD sets (B2, or B1 as the exception) and a `Proposed:` Calificación against it.
- `Proposed:` marks Calificaciones only. Everything else Claude writes is covered by one header line: *"Drafted by Claude from <sources>. Resolution and Decision are the hiring lead's."*

**Discrepancias**

- A Discrepancia is:
  - any difference between columns on the same Dimensión (Meets vs Exceeds counts);
  - opposite outcomes on the same Punto a indagar;
  - a red flag from one Entrevistador against a green flag from another on the same behaviour.
- Not a Discrepancia: rated vs Not assessed (that is coverage, listed under Not covered), or a flag only one Entrevistador saw (it is attributed to them).
- Each shows each side's evidence and a blank **Resolution** that only the hiring lead fills. The only explanation allowed is factual (different questions asked, different coverage), never a hypothesis about the Entrevistadores.
- An open Discrepancia is one with an empty Resolution. A later Entrevista's Guía targets those.
- **Single Entrevistador** (across every Entrevista): the same template with one column. The section is called **Tensions in the evidence**, about tensions inside that Entrevistador's own evidence, e.g. between the CV and what the Entrevista showed. The header carries the fixed line *"One Entrevistador: no independent second view."*
- No "light" variant: when the Entrevistadores agree, the section says None.

**CV vs Entrevista**

- Every Punto a indagar from the Evaluación de match, in its order, records what the Entrevistas showed: Confirmed, Contradicted, Inconclusive or Not probed, with the transcript quote and who asked.
- aem's "Inconsistencies between CV and answers" flag is the list of Contradicted credibility points.

**Decision**

- A dated list, newest first, filled only by the hiring lead. Claude never ticks or pre-fills anything in it.
- Each entry:
  - **Outcome:** Advance / Advance with conditions / Another interview / Do not advance. The same for Candidatos internos and externos: Advance for an internal is a placement. No Strong/Weak gradient, since the Shortlist orders Candidatos.
  - **Justification.**
  - **Calibrated level,** in the handbook's vocabulary (L5…L8, or the role) through the suite's level-equivalence table ([JD structure](04-jd-structure.md)). Claude never proposes it.
  - **Conditions,** or the reason for another Entrevista.
  - **Next steps.**
  - **Decided by / date.**
- An empty latest entry means the decision is pending.

**Document** (`debrief.md`, in English)

1. **Header:**
   - the frontmatter;
   - what the Calificaciones are measured against: role or track, the Posición's level, the rubric link or "rubric pending: using career-paths";
   - the "Drafted by Claude" line;
   - the single-Entrevistador line, when it applies;
   - the sources read per Entrevista, with any fidelity limit;
   - the stale-match warning, when it applies.
2. **Decision** (the hiring lead's; first, so managers and recruiting read it before the evidence).
3. **Calificaciones,** with the evidence per Dimensión.
4. **Discrepancies** (or **Tensions in the evidence**), each with its Resolution.
5. **Points to probe: what the interview showed.**
6. **Strengths** and **Concerns** shared across Entrevistadores.
7. **Flags:** red and green, each attributed to who saw it.
8. **Evidence for / Evidence against:** both lists required, each item cited; no balance or summary.
9. **Gaps and support:** each gap tied to a Requisito or Dimensión, with the support it suggests.
10. **Not covered:** Dimensiones still Not assessed after every Entrevista and Puntos a indagar not probed, stating that absence of evidence is not evidence. A later Entrevista's Guía targets these.

- Quotes stay in their original language, followed by an English translation in brackets.

**Left out**

- Averages, totals and any consolidated Calificación.
- Growth Velocity: it judges potential (same reason as in [Evaluación de match rubric](05-match-evaluation-rubric.md)).
- Onboarding "Risk level" and "Time to productivity" as Claude's estimates: verdicts under another name. The hiring lead may write them in the Decision.
- Hypotheses about why Entrevistadores disagree.
- A "Previous rounds" section: replaced by the Entrevista columns and the dated Decision list.

**Export and Shortlist**

- Exported as PDF on request next to its source, with the same content. When the latest Decision is empty, the skill warns and asks before exporting.
- The Debrief never edits the Shortlist: the hiring lead updates it after deciding.

**Handed to other tickets**

- [Disk layout of the chain](02-chain-disk-layout.md): amended, `debrief.md` moves to the Candidato folder.
- [Scorecards: dimensions and scale](06-scorecards.md): amended, a Scorecard exists only when an Entrevistador brings one; Claude's transcript-based Calificaciones live in the Debrief; the hiring lead confirms them.
- [Skill boundaries](03-skill-boundaries.md): the Debrief skill builds the evidence per Dimensión from the transcripts; there is no separate Scorecard step.
- [Oportunidad status summary](10-opportunity-status-summary.md): what it reads from a Debrief.
- [Acceptance cases](09-acceptance-cases.md): real cases that exercise the variants.
