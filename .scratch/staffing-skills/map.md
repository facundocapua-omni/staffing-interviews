# Staffing skills suite

Label: wayfinder:map
Tracker: local markdown — tickets in [issues/](issues/)

## Destination

A spec at `.scratch/staffing-skills/spec.md` for a personal suite of four chained skills (JD → Evaluación de match → Guía de entrevista → Debrief), plus a status summary per Oportunidad, giving each skill's inputs, output, template and rules, plus the shared conventions, ready to build each skill with `skill-creator`. The spec is assembled from this map's decisions once no tickets remain.

Assembled 2026-10-27: [spec.md](spec.md). Its §7 lists 16 calls made while assembling that no ticket answered, all confirmed by the hiring lead the same day. Next: build step 0, the smoke check (spec §6).

## Notes

- Domain: staffing client-project Posiciones for the DXP technical team. Use the terms in [GLOSSARY.md](../../GLOSSARY.md) and update it when a term is resolved.
- Grilling tickets load `grilling` + `domain-modeling`; tickets that decide skill wording or boundaries also load `writing-for-agents`.
- Sources of truth: `~/Workspace/martech/structure` (roles, career levels, tracks, platforms) is read by the skills, never copied; a Posición may add requirements of its own. The old HR Descripciones de cargo are the exception: frozen, so the suite keeps a copy ([Handbook gaps for JDs](issues/11-handbook-gaps-for-jds.md)). Existing house templates: `~/Workspace/leadership/aem-interviews/Templates/` (EN).
- Claude never decides: no verdict anywhere in the suite. Claude gives evidence and clearly marked proposals; the hiring lead decides.
- Language: chat in Spanish; skills and every deliverable in English, Spanish only on explicit request.
- Inputs are files and pasted text only.
- The suite replaces the per-stack workspaces (`aem-`, `tl-`, `react-`, `td-interviews`); stack specifics become pluggable content, not separate skills.
- Skills live in `~/Workspace/leadership/staffing/.claude/skills/`. `candidate-takehome-review` stays as-is, outside the chain; its report is an optional input.
- An interview may be run by the hiring lead, a pair, or a delegated team member.
- No git here: research findings live in [research/](research/) next to this map and are linked from their ticket.

## Decisions so far

<!-- one line per closed ticket: [title](issues/NN-slug.md): gist -->

- [Inventory existing staffing material](issues/01-inventory-existing-staffing-material.md): four diverging workspaces, a common core per artifact type with listed conflicts, the Evaluación de match is new, the handbook lacks years, Nice-to-have, evaluation criteria and interview material.
- [Disk layout of the chain](issues/02-chain-disk-layout.md): person-first tree (`opportunities/` for Posiciones, JDs and Shortlists; `people/<p>/<op>--<pos>/` per Candidato with one folder per interview); Candidato is the person×Posición pair; no pipeline CSV; Markdown source with exports for what is shared.
- [JD structure](issues/04-jd-structure.md): one run per Oportunidad from Propuesta + P&L → intake questions → `opportunity.md` + every `jd.md`; recruiting-brief skeleton with Excluyente/Plus Requisitos tagged by origin, client anonymised, Globant→handbook level table.
- [Scorecards: dimensions and scale](issues/06-scorecards.md): a Scorecard only when an Entrevistador brings one (Claude's transcript-based Calificaciones live in the Debrief, amended by the Guía and the Debrief); Calificación is Below/Meets/Exceeds the Posición's level or Not assessed, with no numbers, averages or recommendation; 6 soft + 5 technical Dimensiones for every Posición, plus 3 leadership ones for leadership roles; rubric in the handbook's `evaluation-criteria/`; Claude's Calificaciones are marked `Proposed:`; English is a result provided separately.
- [Evaluación de match rubric](issues/05-match-evaluation-rubric.md): one row per atomic Requisito with a Nivel de evidencia (Evidenced/Claimed/Partial/No evidence/Not met), each with a cited quote; documents only, no interview evidence; Logistics without salary; a factual timeline, no proto-verdicts, counts or velocity; points to probe handed to the Guía; shareable as PDF; an alphabetical comparison table with no totals.
- [Unified Guía de entrevista](issues/07-interview-guide.md): one-hour Entrevistas with fixed blocks and an owner per block, more than one when the Dimensiones don't fit; numbered questions mapped to every Dimensión, technical ones included, drawn from a per-platform/track question bank in the suite; Puntos a indagar become neutral questions; self-contained for a delegated Entrevistador; no notes and no blank Scorecards, the transcript is the evidence; English assessed separately.
- [Unified Debrief](issues/08-debrief.md): one Debrief per Candidato across all their Entrevistas, next to the Evaluación de match; `Proposed:` Calificaciones per Entrevistador per Entrevista, cited by question id, confirmed by the hiring lead; Discrepancias (Tensions with one Entrevistador) with a blank Resolution; what each Punto a indagar showed; the hiring lead's dated Decision first (Advance / with conditions / Another interview / Do not advance, calibrated level); no averages, velocity or risk level.
- [Oportunidad status summary](issues/10-opportunity-status-summary.md): one dated Markdown file per Oportunidad for management (+ PDF), always the current state with no diff or free section; per Posición, every Candidato with Shortlist position, an Etapa derived from the files, availability and the hiring lead's latest Outcome; pending items as facts; no evidence, Calificaciones, comparison table or Claude judgment; names the client.
- [Acceptance cases](issues/09-acceptance-cases.md): 11 real cases (2 JD, 3 match, 3 Guía, 3 Debrief) plus one mutated case per stop-and-ask rule, shaped as skill-creator evals (inputs, request, rule and variant checks, no golden output); the real past decision is never a check; inputs and converted fixtures live in `tests/acceptance/<handle>/` and runs go to a sandbox; an Oportunidad's client may be internal.
- [Debrief inputs outside the suite's shape](issues/12-debrief-inputs-outside-the-suite-shape.md): off-guide evidence is cited by Qn follow-up or timestamp with the question as asked, and no Guía is ever written after the fact; a brought Scorecard is copied only on the suite's scale with a one-to-one mapping, anything else is quoted and never converted, and its recommendation is left out; with no Evaluación de match the skill offers to run it; Candidatos in progress at cutover enter the suite at their next step, rebuilt from the transcript, with no import action and no carried-over Decision; two new acceptance cases.
- [Handbook gaps for JDs](issues/11-handbook-gaps-for-jds.md): no official level equivalence exists, so the suite's table grows (Sr 3 split by whether the person leads people, SME/Manager/Director rows, no Globant `Lead`); each part of the base comes from the handbook, then a Descripción de cargo (HR versions copied into the suite), then Claude's `Proposed:` intake proposals the hiring lead confirms; a supplied JD sits above the base and contradictions go to the intake; new origins `hiring lead`, `presales`, `supplied JD`; off-handbook Posiciones flagged in `opportunity.md` and `jd.md`, not in the PDF; any Oportunidad may come without a Propuesta or P&L; Sitecore acceptance cases added.
- [Skill boundaries](issues/03-skill-boundaries.md): five model-invoked `staffing-*` skills, one per artifact, in this project's `.claude/` only (match also owns batches, re-evaluation, the comparison table and dictated Shortlist edits); shared reference in `.claude/shared/` read through `${CLAUDE_SKILL_DIR}`; inputs required (stop and offer) or offered (offer and go on), an accepted offer runs the other skill in the same session; inputs kept next to what they feed; the tree root is found upward; trigger drafts with negatives in evals; `human-resources@synced` disabled in the project settings; sandbox `tests/runs/<handle>/` without git.

## Not yet specified

<!-- nothing in the fog right now -->

## Out of scope

- Packaging as a shareable plugin for other leads: this is a personal suite.
- External publishing of the JD or a client-facing version: the JD is for recruiting.
- Integrations: ATS, HRIS, meeting recorders.
- Interviews run by the client.
- Redesigning `candidate-takehome-review`.
- Spanish versions of the templates.
- A portfolio status across Oportunidades, and purging a person's data (status snapshots are never scrubbed) ([Oportunidad status summary](issues/10-opportunity-status-summary.md)): not wanted for now.
- Building the skills, seeding the question bank from the per-stack workspaces, archiving those workspaces, and writing the handbook's `evaluation-criteria/` rubric pages ([Scorecards: dimensions and scale](issues/06-scorecards.md)): execution that follows the spec.
