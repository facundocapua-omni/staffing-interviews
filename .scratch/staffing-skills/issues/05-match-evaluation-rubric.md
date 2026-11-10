# Evaluación de match rubric

Type: grilling
Status: resolved
Blocked by: 04
Map: [Staffing skills suite](../map.md)

## Question

How does an Evaluación de match assess one Candidato against one Posición?

Decide:

- Already fixed by [JD structure](04-jd-structure.md): the requirements are the JD's Requisitos, in two tiers (Requisito excluyente, Plus) with no weights, each tagged with its origin. Still open: how an unmet Requisito excluyente shows up without becoming a verdict.
- Evidence levels (e.g. meets / partial / not met / no evidence) and what counts as evidence from a CV or profile.
- How the extra evidence for a Candidato interno (project history, prior feedback, previous Debriefs) is used.
- The output: per-requirement assessment, gaps, and the "points to probe" handed to the Guía de entrevista, with no global verdict.

No existing artifact does this; start from its nearest ancestors and the conflicts listed in the [inventory findings](../research/01-existing-staffing-material.md#evaluación-de-match-cv-screening--profile): the CV credibility check, recruiting data (salary, availability), proto-verdicts ("Seniority (your assessment)", "Working Hypothesis") and relative comparisons.

## Answer

Grilled 2026-10-21. Terms resolved in [GLOSSARY.md](../../../GLOSSARY.md): Nivel de evidencia, Punto a indagar. Requisito tiers come from [JD structure](04-jd-structure.md): Requisito excluyente and Plus, with no numeric weights.

**What is assessed**

- Every Requisito excluyente and every Plus in the JD gets one row, in the JD's order, with its tier.
- A line with several parts ("5+ years in frontend, 2+ with React in production") is split into atomic rows (1a, 1b) that point back to the JD line.
- "What they'll do" is not assessed: those are not Requisitos.
- "Not a fit if" is not assessed separately, since it is recruiting's version of the excluyentes. When the CV hits one, it is recorded as a credibility observation.

**Nivel de evidencia** (a different vocabulary from the Scorecard's Calificación, on purpose)

| Level | When |
|---|---|
| Evidenced | A concrete project or role shows it: what, where, how long. |
| Claimed | Stated (skills list, summary) but no project backs it. |
| Partial | Evidence of something adjacent (Sanity instead of Contentful, Pages Router only), or of one part of a compound Requisito. |
| No evidence | Not mentioned. Absence from a CV is not proof the Candidato lacks it. |
| Not met | The documents show the Candidato falls short: 3 years against 5+, a whole career in Angular. |

**Sources and citation**

- Sources: CV, public profile, the optional take-home report, and recruiting's screening notes when they exist.
- Every level cites its evidence (quote and file). Only No evidence may go without a citation.
- Evidence carries its period ("React, 2016–2018"). Its age is shown, never weighted.
- Interview evidence never enters here: it belongs to the Scorecard and the Debrief.

**Candidato interno**

- Extra sources from `people/<p>/`: project history, prior feedback, and previous Debriefs and Scorecards, each cited with its date and Posición.
- They carry no more weight than the CV; they can reach Evidenced through observed work rather than claims.
- A Calificación from an earlier interview is cited as a dated fact. It is never carried over as a Calificación.
- When internal evidence contradicts the CV, the contradiction is flagged.
- Prior feedback is not treated as sensitive: the Evaluación de match can be shared.

**Recruiting data**

- A Logistics block holds facts: location, work mode, availability or start date, notice period. It is checked against the JD's Logistics.
- Salary is not recorded.
- The aem profile's Pipeline and Final Decision are dropped: stage is derived from which artifacts exist ([Disk layout of the chain](02-chain-disk-layout.md)).

**Left out** (proto-verdicts)

- "Seniority (your assessment)" and "Working Hypothesis".
- "Comparable precedents", or any comparison between Candidatos.
- Counts or percentages ("8/11 met").
- Any summary that concludes.
- A computed growth velocity (years per level jump): titles do not compare across companies, and the number becomes a judgment about potential.

**Points to probe** (the hand-off to the Guía de entrevista)

- What becomes a point:
  - every Requisito excluyente that is not Evidenced (Claimed, Partial, No evidence, and Not met in case the hiring lead interviews anyway);
  - every Plus that is Claimed or Partial;
  - every credibility observation.
- Each point carries:
  - the Requisito row and its tier;
  - the Nivel de evidencia;
  - the quote it rests on;
  - what to verify, worded as a doubt, not a question;
  - the Dimensión or Dimensiones it lands on ([Scorecards: dimensions and scale](06-scorecards.md)).
- Order: excluyentes first, then Plus; within each, Claimed → Partial → No evidence. This orders the interview plan; it is not a judgment.
- No questions are written here: the Guía owns timing and coverage.

**Document** (`match-evaluation.md`)

1. **Header:**
   - the Disk layout frontmatter plus `jd_updated`;
   - the fixed line *"Evidence from documents only, before any interview. Not a hiring recommendation."*;
   - a statement that the Niveles de evidencia are Claude's reading of the sources;
   - the list of sources read.
2. **Requisitos:** a table with id, Requisito, tier, Nivel de evidencia, and evidence (quote · file · period).
3. **Logistics,** checked against the JD.
4. **Career timeline:** facts only (roles, companies, dates, duration).
5. **Credibility observations:** those not tied to a Requisito, e.g. timeline gaps, inflated titles, certifications without projects, a "Not a fit if" hit.
6. **Points to probe.**

There is no separate Gaps section (the points to probe open with the excluyentes), and no summary or conclusion.

- The Niveles de evidencia carry no `Proposed:` prefix. The document is entirely Claude's and says so once in its header. The hiring lead corrects a level by editing it in place. The suite-wide rule was refined in [Scorecards: dimensions and scale](06-scorecards.md).
- It can be shared, and is exported as PDF on request next to its source, the same as the JD and the Debrief.

**Comparison table per Posición** (generated on request, not stored)

- One row per Requisito, in the JD's order and with its tier, plus the Logistics rows.
- One column per Candidato, in alphabetical order, never ordered by fit.
- Each cell holds the Nivel de evidencia.
- No totals or counts.
- A column whose evaluation is stale against the JD is marked in its header.

**Handed to other tickets**

- The shape of the points to probe: [Unified Guía de entrevista](07-interview-guide.md).
- The shape of the comparison table: [Oportunidad status summary](10-opportunity-status-summary.md).
