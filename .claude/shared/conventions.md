# Conventions

Rules every `staffing-*` skill follows on every run. Domain terms are defined in `GLOSSARY.md`, at the suite root (two folders above this one).

## Language

- Chat with the hiring lead in Spanish, using each glossary term's Spanish name (Posición, Candidato, Evaluación de match).
- Write skills and every deliverable in English, using each term's English name: Opportunity, Position, Requirement, Must have, Nice to have, Candidate, Match evaluation, Evidence level, Point to probe, Interview, Interview guide, Interviewer, Rating, Dimension, Discrepancy, Stage, Status summary. Write a deliverable in Spanish only when the hiring lead asks for it.
- Quote a source in its original language, followed by an English translation in brackets.

## The hiring lead decides

Claude supplies evidence and clearly marked proposals. Every judgment is the hiring lead's: the Decision and its calibrated level, a Discrepancy's Resolution, the Shortlist and its order.

- An artifact carries evidence only. It holds no verdict, recommendation, ranking, score, total, average, weight, threshold, count of Requirements or Dimensions ("8/11"), growth velocity, risk level, or summary that concludes. A threshold is a verdict reached by arithmetic: importance comes from the Must have / Nice to have tiers and from the hiring lead.
- List Candidates in alphabetical order. Only the Shortlist has another order, the hiring lead's.
- Explain a difference by facts (different questions asked, different coverage), never by a hypothesis about a person.
- When in doubt, ask the hiring lead instead of concluding.

## Marking what Claude wrote

- In a document where humans also write, every value Claude proposes carries the prefix `Proposed:` (e.g. `Proposed: Meets`). The prefix survives a PDF export and needs no colour or extra column. The hiring lead confirms a value by removing the prefix or changing the value; Claude leaves every `Proposed:` in place.
- A document Claude writes entirely (the Match evaluation, the Interview guide) says so once, in its header, instead.
- Claude's own proposals for a JD's Requirements appear only in the intake round, marked `Proposed:`. Only what the hiring lead confirms reaches a file.

## Inputs

Each skill's input table marks every input as one of:

- **Required.** When missing, stop and offer to run the skill that produces it; when no skill does, ask for it.
- **Offered.** When missing, offer once. When declined, go on and say in the artifact what is missing.
- **Optional.** Read it when present; never ask for it.

`staffing-status` neither stops nor offers: it reports what is missing as pending items.

An offer is one yes/no question that names the skill. On yes, invoke that skill through the Skill tool in the same session, then resume the step that needed it with the new artifact.

## Kept inputs

- Keep every input next to what it feeds, in the folder `disk-layout.md` gives it.
- Identify an input by its content, never by its name. Files keep their original names. Pasted text is saved as `pasted-<YYYY-MM-DD>.md`, and a second one on the same day takes a numeric suffix (`pasted-<YYYY-MM-DD>-2.md`).

## Tree root

- The root is the first folder, from the working directory upward, that holds `opportunities/` or `people/`. Resolve it on every run, never as a fixed path, so an acceptance run writes inside its sandbox.
- When no folder qualifies, a skill that writes asks once before creating both `opportunities/` and `people/`, naming the path. `staffing-status` creates nothing and says it found no tree.

## Staleness

A Match evaluation is stale when its `jd_updated` differs from its JD's `updated`. Every skill that reads one says so. Re-evaluating happens only at the hiring lead's request.

## Client name

`opportunity.md` and the Status summary name the real client. The JD and the Interview guide anonymise it ("a US-based global travel company"), even when a supplied JD names it, unless the client is internal.

## Sources

- The handbook, `~/Workspace/martech/structure/src/content/docs/`, is read in place and never copied: `roles/<role>.md`, `reference/career-levels.md`, `reference/tracks.md`, `career-paths/<track>.md`, `technologies/<platform>.md`, `evaluation-criteria/`. A Position may add Requirements of its own.
- The HR job descriptions are the exception: read the frozen copies in `hr-job-descriptions/`, never the originals.

## Salary and export

- Salary stays out of every file the suite writes.
- Export to PDF only on request, as `export.md` says.
