# Acceptance cases

Type: grilling
Status: resolved
Blocked by: 04, 05, 07, 08
Map: [Staffing skills suite](../map.md)

## Question

Which real past cases serve as each skill's acceptance example in the spec, and what must the skill's output on that case show?

Start from the cases listed under "Complete real cases" in the [inventory findings](../research/01-existing-staffing-material.md#complete-real-cases-acceptance-candidates). Decide:

- One or more cases per skill (JD, Evaluación de match, Guía de entrevista, Debrief), covering at least one Candidato interno and one single-Entrevistador case. For the JD skill, the Expedia AEM → Contentful Propuesta + P&L used in [JD structure](04-jd-structure.md) is a ready case (its intake answers are in the prototype).
- What each case checks against the decided template and rules (e.g. no verdict, evidence marked as missing rather than guessed).
- How the spec cites a case without copying personal data into it.

From [Unified Debrief](08-debrief.md), cases that exercise its variants:
- `aem/Evaluaciones/Completed/Amol Pandit/`: Candidato interno, single Entrevistador, a degraded transcript (lower-fidelity evidence).
- `td/Evaluaciones/Completed/Jose_David_Restrepo/`: single Entrevistador, a leadership role (the 3 leadership Dimensiones).
- `td/Evaluaciones/In Progress/Gustavo_Hurtado/`: decision pending another Entrevista (the dated Decision list, a second Entrevista column).
- Each must show: no verdict or pre-ticked Decision, `Proposed:` on every Calificación Claude writes, Not assessed instead of inference, and Discrepancias with an empty Resolution.

## Answer

Grilled 2026-10-22. Term refined in [GLOSSARY.md](../../../GLOSSARY.md): Oportunidad (its client may be internal). The case folders were inventoried the same day.

> **Amended by [Debrief inputs outside the suite's shape](12-debrief-inputs-outside-the-suite-shape.md)** (2026-10-23). Two Debrief cases are added and three get one more variant check; the case table there holds them:
> - New mutated case `debrief-off-guide` (from `debrief-single-leadership`) and new real case `debrief-cutover` (Gustavo Hurtado's raw folder, old Scorecards as inputs, kept apart from `debrief-pending-update`'s calibration).
> - Variant checks added to `debrief-single-leadership` (no Evaluación de match), `debrief-pair-degraded` (no evidence from outside an Entrevista) and `debrief-pending-update` (speaker labels).

> **Amended by [Handbook gaps for JDs](11-handbook-gaps-for-jds.md)** (2026-10-23). The Sitecore Tech Leader leaves "Not covered by a past case"; the case table there holds the additions:
> - New real cases `jd-off-handbook` (a brief with no Propuesta or P&L) and `guide-off-handbook` (three Entrevistadores, no question bank for Sitecore). Brandon Gallagher's Evaluación de match is a fixture only.
> - New mutated cases `jd-supplied-contradiction` (from `jd-internal-client`) and `jd-architect-line` (from `jd-expedia`).
> - Variant checks added to `jd-expedia` (the intake asks whether the Sr 3 line leads people) and `jd-internal-client` (the Descripción de cargo counts as `supplied JD`).
> - Still not covered by a past case: the `presales` origin.

> **Amended by [Skill boundaries](03-skill-boundaries.md)** (2026-10-27). The sandbox is `tests/runs/<handle>/`, with no git: Claude Code finds the suite's skills from there. The run setup creates empty `opportunities/` and `people/` in it, so the tree root (the first folder upward holding either) resolves to the run folder. Each run gets `staffing/.claude/settings.json`, which disables `human-resources`, through `--settings` or a settings file in the run folder. The first build step is a smoke check from a run folder.

**Facts that corrected the question**

- `Amol Pandit/` has no transcript in its folder. The degraded transcript is Swaroop Kumar Reddy's: Gemini notes with unreadable stretches.
- No case has two Entrevistas on disk. Gustavo Hurtado's second round never happened.
- Only four cases have a transcript: Jose David Restrepo, Gustavo Hurtado and Jhon Garces (Spanish, one Entrevistador each) and Swaroop (English, two Entrevistadores, internal, no CV).
- Nothing on disk has the suite's shape:
  - old guides have blocks but no Q ids or block owners;
  - old Scorecards use other dimensions and a Hire / No Hire scale;
  - no case has an Evaluación de match.
- The Expedia Oportunidad had no Candidatos.
- The td cases are the company's own Technology Director role: an Oportunidad with an internal client.

**What a case is**

- Each case has three parts: input files, the request to the skill, and checks. These map one-to-one to skill-creator's `evals/evals.json` (prompt, files, assertions). On top of that, the hiring lead reviews the output qualitatively.
- There is no golden output: writing the expected document would be writing the deliverable.
- Checks come in two layers:
  - **Rule checks:** written once per skill from its decided template and applied to every case of that skill (listed below).
  - **Variant checks:** one to three per case, for what that case exercises (in the case table).
- Content checks, such as which Nivel de evidencia a given Requisito gets, are not in the spec. Writing them means reading the case. The hiring lead writes them at build time from the first reviewed output.
- The real past decision is never a check, since it would steer the skill toward a verdict. Every Debrief case checks that the Decision is empty. The hiring lead may use the real decision as a lens in the qualitative review: does the evidence surface what drove it?
- **Calibration** (qualitative, not pass/fail, since the scales differ): `debrief-single-leadership` and `debrief-pending-update` are also run with the transcript only. Claude's `Proposed:` column is then compared with the hiring lead's old Scorecards from the same Entrevista.

**Where cases live**

- Every case has an English handle.
- The spec cites cases by handle in its body. A single table maps each handle to its folder and origin (the case table below). No names appear outside that table, and the spec copies no quotes, CV content or real outcomes.
- Each case folder `~/Workspace/leadership/staffing/tests/acceptance/<handle>/` holds copies of the inputs and the fixtures. Copies are needed because the origins are volatile (`~/Downloads`) or will be archived (the per-stack workspaces).
- Runs write to a sandbox, never to the real `opportunities/` or `people/`. A test Evaluación de match saved there would create a Candidato who does not exist. So the skills resolve the tree root from the working directory.

**Fixtures** (they convert what exists, never invent)

- An old guide becomes the Entrevista's Guía: its questions are numbered Q1…Qn in the order they were asked, and each block gets its owner.
- An Evaluación de match is produced by the match skill from the CV. For Swaroop, it is produced from the Candidate Profile, his only source.
- A JD comes either from a JD case's output or from the JD skill run on the hiring lead's material.
- Old Scorecards are not inputs. They are used only for calibration.
- When a case's input is another case's output, the hiring lead first reviews and corrects that output. It is then frozen as a fixture, so cases do not drift with each other.

**Cases**

| Handle | Skill | Inputs (origin under `~/Workspace/leadership/` unless stated) | Variant checks |
|---|---|---|---|
| `jd-expedia` | JD | Propuesta `~/Downloads/[Globant - Expedia_TPA] SF Contentful Migration - October 2026 (1).pptx` (55 slides) and P&L `~/Downloads/[TPA Expedia] Contentful Migration Proposal - Pricing Sheet V4 _AI PODs_.xlsx`; question-round answers from the [intake prototype](../prototypes/04-jd/PROTOTYPE-01-intake-analysis.md) | Intake analysis and one question round before writing. P&L lines 1–3 get no JD. Seniority comes from the Labor Estimate, with the SOW gap as a flag in `opportunity.md`. Lines 10, 11 and API are flagged and get no invented Requisitos. |
| `jd-internal-client` | JD | `td-interviews/DXP TECHNOLOGY DIRECTOR - JOB DESCRIPTION (2).docx` (Spanish) | Asks for no Propuesta or P&L. Asks for the level in the intake. Writes an English JD from a Spanish source. |
| `match-internal-prior` | Match | Daniel Carrasco Herrera: CV plus his earlier AEM Debrief and Scorecards (`aem-interviews/Evaluaciones/Completed/Daniel Carrasco Herrera/`), against the reviewed backend JD from `jd-expedia` | Earlier Calificaciones are cited as dated facts, never carried over. AEM in place of Contentful is Partial. A contradiction between the CV and internal evidence is flagged. |
| `match-takehome` | Match | Jhon Garces: CV plus take-home report (`react-interviews/candidatos/jhon-garces/`), against the reviewed frontend JD from `jd-expedia` | The take-home report is a cited source. Years below the JD's are Not met. |
| `match-external-leadership` | Match | Gustavo Hurtado: CV (`td-interviews/Evaluaciones/In Progress/Gustavo_Hurtado/`), against the reviewed JD from `jd-internal-client` | External Candidato in a leadership role. The Puntos a indagar land on the leadership Dimensiones. |
| `guide-pair` | Guía | Reviewed `match-internal-prior` and its JD; two Entrevistadores, one soft and one technical | An owner per block. A table maps each Punto a indagar to its question. A Must have that is not Evidenced is probed early and briefed neutrally. |
| `guide-takehome` | Guía | Reviewed `match-takehome`, its JD and the take-home report | Take-home questions carry origin `take-home`. Adds "walk me through your submission". |
| `guide-second-interview` | Guía | Reviewed `match-external-leadership` and `debrief-pending-update`; the DXP Director as the only Entrevistador | Targets the Not assessed Dimensiones and the open Tensions. Repeats no question from the first Entrevista. Has a leadership block. Its briefing works without the hiring lead's context. |
| `debrief-single-leadership` | Debrief | Jose David Restrepo: Gemini transcript plus the converted old guide (`td-interviews/Evaluaciones/Completed/Jose_David_Restrepo/`); JD from `jd-internal-client` | One column, a "Tensions in the evidence" section and the single-Entrevistador line. Covers the three leadership Dimensiones. Spanish quotes are followed by an English translation. |
| `debrief-pending-update` | Debrief | Gustavo Hurtado: Gemini transcript plus the converted old guide; JD from `jd-internal-client`; match from `match-external-leadership`. Run twice; between runs the hiring lead writes an "Another interview" Decision and a Resolution. | The second run keeps that Decision and Resolution verbatim and asks before touching them. |
| `debrief-pair-degraded` | Debrief | Swaroop Kumar Reddy: Gemini notes plus the converted old guide plus the Candidate Profile (`aem-interviews/Evaluaciones/Completed/Swaroop Kumar Reddy/`); match from the Candidate Profile; JD from the JD skill run on a brief (AEM Developer, L5) | Internal Candidato with two Entrevistadores. Asks the hiring lead to fill the gap first. States the fidelity limit per Entrevista and in every Calificación that rests on it. Uses Not assessed instead of inference. |

**Rule checks per skill** (every case of that skill)

- **Every skill:**
  - no verdict, recommendation, ranking, count or total;
  - the deliverable is in English;
  - nothing is written outside the sandbox.
- **JD:**
  - only two tiers, Must have and Nice to have;
  - every Requisito carries its origin;
  - English is B2 (B1 only as the exception);
  - no allocation;
  - the client is anonymised in every `jd.md`, unless the client is internal.
- **Evaluación de match:**
  - one row per atomic Requisito, in the JD's order, with its tier;
  - every Nivel de evidencia is cited, except No evidence;
  - evidence carries its period;
  - the fixed "not a hiring recommendation" header line;
  - no summary, conclusion, velocity or salary;
  - the Puntos a indagar follow the order rule.
- **Guía de entrevista:**
  - every Dimensión has a main question, or is listed as "Not covered in this interview";
  - a coverage table;
  - English reads "Assessed separately";
  - questions are numbered Q1…Qn;
  - no notes template and no blank Scorecards;
  - never suggests declining the Candidato;
  - the client is anonymised;
  - the header says Claude wrote it.
- **Debrief:**
  - the Decision is empty, with nothing pre-ticked;
  - `Proposed:` on every Calificación Claude writes;
  - Not assessed instead of inference;
  - every Discrepancia (or Tension) has a blank Resolution;
  - no average, consolidated column, velocity or risk level;
  - quotes appear in their original language followed by an English translation;
  - both Evidence for and Evidence against are present.

**Mutated cases** (one per stop-and-ask rule, built in the sandbox from a real case by removing or editing one input)

- `guide-missing-match`: no Evaluación de match. The skill stops and offers to run it.
- `guide-stale-match` and `debrief-stale-match`: `jd_updated` is newer than the evaluation. The Guía warns; the Debrief says so in its header and uses the Puntos a indagar as they stand.
- `debrief-missing-english`: no English result. The skill asks for it; if none arrives, English is Not assessed.
- `debrief-missing-interviewer`: an Entrevistador in `interviewers` has no transcript, Scorecard or notes. The skill asks whether to wait or go on.
- `debrief-export-pending`: export is requested while the latest Decision is empty. The skill warns and asks first.

**Not covered by a past case** (the spec says so)

- A second Entrevista inside the Debrief: covered by the first live Candidato who has two.
- A platform or role outside the handbook: the Sitecore Tech Leader in `tl-interviews/brandon-gallagher/` (CV in `tl-interviews/`) becomes a case once [Handbook gaps for JDs](11-handbook-gaps-for-jds.md) is resolved.

**Decided here because the cases need it: an Oportunidad with an internal client**

- The JD skill's input is whatever material the hiring lead has, as files or pasted text: an existing JD or a brief, in place of the Propuesta and P&L.
- The level, which otherwise comes from the Labor Estimate, is asked in the intake round.
- Nothing is anonymised, because the client is the employer.
- `opportunity.md` is still written.
- No new term is added.

**Handed to other tickets**

- [JD structure](04-jd-structure.md): amended with the internal-client input.
- [Skill boundaries](03-skill-boundaries.md): the skills resolve the tree root from the working directory, and each skill's evals point at `tests/acceptance/<handle>/`.
- [Handbook gaps for JDs](11-handbook-gaps-for-jds.md): the Sitecore Tech Leader case waits on it.
- New ticket [Debrief inputs outside the suite's shape](12-debrief-inputs-outside-the-suite-shape.md): what the fixtures hide in real use.
