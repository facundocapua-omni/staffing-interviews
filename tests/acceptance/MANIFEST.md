# Acceptance inputs: manifest

Copied on 2026-10-27 (spec §6 step 2) from the sources in spec §5.6. This file is for the build, not a case input: never hand it to a skill.

## Folder roles inside a case

| Folder | Holds | Handed to the skill under test |
|---|---|---|
| `inputs/` | the material the hiring lead would give the skill | yes |
| `answers/` | the hiring lead's scripted replies to the skill's question rounds | only as replies, when the skill asks |
| `fixture-sources/` | raw material that becomes a fixture once converted or run, then reviewed | no |
| `fixtures/` | frozen, reviewed outputs of earlier cases (§5.3); created during step 3 | yes |
| `calibration/` | old Scorecards compared qualitatively with Claude's `Proposed:` column (§5.3) | never |

## Cases

| Handle | Copied now | Still to come (step 3) |
|---|---|---|
| `jd-expedia` | `inputs/`: Proposal deck (55 slides), P&L. `answers/intake-round-1.md`: round 1 answers, verbatim from the intake prototype | The answer on whether line 4 leads people. Answer 4 in round 1 carries an older level table (Sr 3 → L8 with no lead question): the hiring lead decides whether it stays |
| `jd-internal-client` | `inputs/`: the DXP Technology Director JD (Spanish `.docx`) | none |
| `jd-off-handbook` | `inputs/brief.md`, converted from §1 of `tl-interviews/brandon-gallagher/interview-guide.md` (the project context and the hiring lead's focus; the handbook's Tech Leader expectations left out, since the skill reads them from the handbook); `answers/intake-answers.md` | none |
| `match-internal-prior` | `inputs/`: CV, earlier AEM Debrief, Soft and Tech Scorecards (the internal history) | `fixtures/`: the reviewed backend JD from `jd-expedia` |
| `match-takehome` | `inputs/`: CV, take-home report | `fixtures/`: the reviewed frontend JD from `jd-expedia` |
| `match-external-leadership` | `inputs/`: CV | `fixtures/`: the reviewed JD from `jd-internal-client` |
| `guide-pair` | nothing: every input is a fixture | `fixtures/`: reviewed `match-internal-prior` and its JD. Request: two Interviewers, one soft, one technical |
| `guide-takehome` | `inputs/`: take-home report | `fixtures/`: reviewed `match-takehome` and its JD |
| `guide-second-interview` | nothing: every input is a fixture | `fixtures/`: reviewed `match-external-leadership`, the second-run Debrief of `debrief-pending-update`. Request: the DXP Director as the only Interviewer |
| `guide-off-handbook` | `fixture-sources/`: the Sitecore CV, for the match fixture | `fixtures/`: reviewed JD from `jd-off-handbook`; the Match evaluation produced from the CV. Request: three Interviewers (the hiring lead on leadership, the Managing Director, a Sitecore Expert on the technical block) |
| `debrief-single-leadership` | `inputs/`: Gemini transcript. `fixture-sources/`: old guide. `calibration/`: Leadership and Technical Scorecards | `fixtures/`: the old guide converted to a Guía (§5.3), the reviewed JD from `jd-internal-client`. No Match evaluation, by design |
| `debrief-pending-update` | `inputs/`: Gemini transcript. `fixture-sources/`: old guide. `calibration/`: Leadership and Technical Scorecards | `fixtures/`: the converted Guía, the reviewed JD from `jd-internal-client`, the reviewed `match-external-leadership`. Between its two runs the hiring lead writes an "Another interview" Decision and a Resolution |
| `debrief-pair-degraded` | `inputs/`: Gemini notes, Candidate Profile. `fixture-sources/`: old guide | `fixtures/`: the converted Guía; the Match evaluation produced from the Candidate Profile; the JD from `staffing-jd` run on a brief (AEM Developer, L5), and that brief, which the hiring lead supplies |
| `debrief-cutover` | `inputs/`: the raw folder as it stands, all 7 files (transcript, unconverted old guide, 1–5 Scorecards with a recommendation, old Debrief, Candidate Profile, CV) | none |

## Built at run time, nothing copied

Mutated cases are built in the run sandbox from their base case by removing, adding or editing one input (§5.1):

| Handle | Base case | Mutation |
|---|---|---|
| `jd-supplied-contradiction` | `jd-internal-client` | the supplied JD's years edited to contradict `level-equivalence.md` |
| `jd-architect-line` | `jd-expedia` | "Architect" as the Client's Role Name on P&L line 4; a second run answers "Expert" |
| `guide-missing-match` | a Guía case | its Match evaluation removed |
| `guide-stale-match` | a Guía case | `jd_updated` older than the JD's `updated` |
| `debrief-off-guide` | `debrief-single-leadership` | one or two questions removed from its converted Guía |
| `debrief-stale-match` | a Debrief case | `jd_updated` older than the JD's `updated` |
| `debrief-missing-english` | a Debrief case | no English result |
| `debrief-missing-interviewer` | a Debrief case | an Interviewer in `interviewers` with no transcript, Scorecard or notes |
| `debrief-export-pending` | a Debrief case | export requested while the latest Decision is empty |

The `status-*` cases run over a tree assembled from the frozen fixtures of every earlier case (§4.5), once those exist.

The run setup (sandbox, settings, read grant) is in spec §5.2.
