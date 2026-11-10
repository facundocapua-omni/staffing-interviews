# Inventory existing staffing material

Type: research
Status: resolved
Blocked by: none
Map: [Staffing skills suite](../map.md)

## Question

What staffing material already exists outside this workspace that the suite should reuse or unify, and where does it agree or conflict?

Cover:

- `~/Workspace/leadership/{aem,tl,react,td}-interviews/`: templates (EN and ES), guides, scorecards, evaluations, debriefs, `pipeline-summary.csv`, plus each workspace's project memory under `~/.claude/projects/-Users-facundocapua-Workspace-leadership-*-interviews/memory/`. For each artifact type: its sections, scales, dimensions, and the workflow rules around it.
- `~/Workspace/martech/structure/src/content/docs/`: what `roles/`, `reference/career-levels.md`, `reference/tracks.md`, `technologies/`, `roadmaps/`, `career-paths/` and `evaluation-criteria/` offer as JD requirements, seniority levels, and interview or scorecard material, including the per-platform `### By platform` subsections.
- Any existing JDs or role briefs (e.g. `~/Workspace/leadership/ARCHITECT 30102024.docx`).
- Complete real cases (CV + guide + transcript or notes + debrief) usable later as acceptance examples, listed by path only. Copy no personal data into the findings.

Expected output, per artifact type (JD, Evaluación de match, Guía de entrevista, scorecards, Debrief): what exists, the common core, and the conflicts that will need a decision.

## Answer

Findings: [Existing staffing material: inventory, common core, conflicts](../research/01-existing-staffing-material.md).

- Four workspaces with diverging lineages: `td` forks `aem`, `react` is a separate design, `tl` is closest to the suite (reads the handbook, no scores, no verdict).
- No existing artifact assesses evidence per requirement against a JD: the Evaluación de match is new. Its nearest ancestors are the aem CV-credibility check and the td/aem candidate profiles.
- Every artifact type has a common core plus listed conflicts; the conflicts are the starting point for the JD, match, scorecard, guide and debrief tickets.
- `martech/structure` gives role, track, platform and per-level career-path content, but no years of experience, no Nice-to-have (pending everywhere), no evaluation criteria, and no interview material. Software Architect and Sitecore are absent.
- Acceptance candidates: two td cases and one react case are complete (CV, guide, transcript or notes, debrief); several aem cases are near-complete or partial, mostly lacking a stored transcript; one internal single-rater edge case.
- aem is the most mature (EN+ES templates, prompts 01–04 that real cases follow more closely than the templates, skill `aem-interviewer`, pipeline CSV, ~36 cases); react has its own 1–4 weighted scorecard and two skills.
- The JDs on disk are Spanish HR "descripción de cargo" docs (Architect, TD), not Posición JDs.
- Common core everywhere:
  - The CV credibility check (claim → evidence → a question to verify it).
  - Timed guide blocks with follow-ups and "what to look for".
  - Rating by dimension with evidence, scored independently.
  - A debrief draft with discrepancies and an empty resolution, plus onboarding risk. Humans decide.
- Main conflicts:
  - **Verdict:** Strong Hire… / Avanzar… / Avanza… are filled in by Claude in react and aem, against the suite's no-verdict rule.
  - **Rating scale:** 1–5, 1–4 weighted, or categorical evidence.
  - **Missing evidence:** 3, ≤2, or "Not assessed".
  - **Level vocabulary:** Junior/Mid/Senior/Lead vs. the 8 handbook levels.
  - **Who writes technical questions.**
  - **Profile:** a standalone profile or part of the guide.
  - **Debrief input:** scorecards or the transcript.
  - **Off-handbook roles/platforms:** Architect, Sitecore.
