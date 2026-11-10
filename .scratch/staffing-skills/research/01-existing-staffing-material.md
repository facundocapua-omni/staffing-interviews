# 01: Existing staffing material

Read-only survey, done 2026-10-21. Candidate data is cited by path only.

Path shorthands:
- `aem/`, `td/`, `react/`, `tl/` = `~/Workspace/leadership/{aem,td,react,tl}-interviews/`
- `hb/` = `~/Workspace/martech/structure/src/content/docs/`
- `mem-aem`, `mem-tl` = `~/.claude/projects/-Users-facundocapua-Workspace-leadership-{aem,tl}-interviews/memory/`

There is no project memory for react or td.

**Workspaces**
- **aem** (ES/EN, ~36 cases): the most mature, but its templates lag behind its prompts `Guias/Prompts/01–04`.
- **td** (ES): a fork of aem with leadership dimensions.
- **react** (ES): a separate design built around `guia-entrevista.md`.
- **tl** (EN): one guide. It is the newest and closest to the suite: it reads the handbook and gives no scores or verdict.

## JD

**Exists**
- **HR job descriptions.** `~/Workspace/leadership/ARCHITECT 30102024.docx` and `td/DXP TECHNOLOGY DIRECTOR - JOB DESCRIPTION (2).docx` share one Spanish corporate HR format:
  - Identificación, Misión
  - Responsabilidades as *qué / para qué* pairs
  - Indicadores (KPI + target)
  - Informes, Herramientas
  - Conocimientos (years, English level, tech)
  - Autoridad, Interacciones, Organización
  - A signature block

  Both describe an employee's job, not a client-project Posición.
- **td skill.** `td/.claude/skills/technology-director-interviewer/SKILL.md` §"Perfil de Referencia del Rol" condenses that JD.
- **Briefs inside guides.**
  - `react/guia-entrevista.md`: a "5–8 años" profile and client-domain blocks.
  - `tl/brandon-gallagher/interview-guide.md` §1 Context: the engagement, "What DXP expects from a Tech Leader (from the DXP structure…)", and the interview focus.

**Common core:** mission, responsibilities, must/nice requirements, seniority, reporting and decides-vs-escalates, tech per platform, Posición context.

**Conflicts**
- **Skeleton:** the HR format (ES, KPIs, signatures), the handbook role outline (EN), or an inline brief?
- **Years of experience and English level:** stated in the JDs and in react, absent from the handbook. Are they Posición-only additions?
- **KPIs:** in the JDs; the handbook keeps them in `hb/delivery-metrics/`, "never used to evaluate developers".
- **Missing from the handbook:** a Software Architect role, and the Sitecore platform (used in the tl case). Where does their baseline come from?
- **Seniority vocabulary:** "Semi Senior o Senior" vs. the 8 handbook levels vs. aem's Junior/Mid/Senior/Lead.

## Evaluación de match (CV screening / profile)

No existing artifact gives evidence per requirement against a JD. This artifact is new.

**Exists**
- **aem profile template** (`aem/Templates/EN - Template - Candidate Profile.md`):
  - Basic Info: Level, Location, Availability, Salary expectation, Source
  - Experience Summary
  - Screening Notes: motivation, first impression, role alignment
  - A Pipeline table and a Final Decision
- **aem prompt 01** (`aem/Guias/Prompts/01 - Interview Guide from CV.md`) holds the real analysis:
  - Executive Summary with "Seniority (your assessment)"
  - Growth velocity (years per level jump)
  - **CV Credibility Check:** title vs. evidence, skills vs. projects, inflated wording, transition gaps, certifications vs. depth. Each finding is claim → evidence → a question to verify it.
  - Open questions
- **Later aem profiles** add more (e.g. `aem/Evaluaciones/Completed/Yash Wadhwani/Candidate Profile - Yash Wadhwani.md`): Role Fit, a status per credibility item, a Working Hypothesis, and "Comparable precedents in this vault".
- **td profile** (`td/Templates/ES - Template - Perfil Candidato.md`): compares against the JD ("JD requiere ~13" years, B2), checks people actually managed, and lists areas to probe.
- **react prep skill** (`react/.claude/skills/preparar-entrevista/SKILL.md` step 4): checks the CV and take-home report against the guide's weighted areas, and separates strong evidence from High-weight areas with none.
- **tl guide** §2: "Points to explore (observations from the CV, not conclusions)".

**Common core:** credibility check (claim, evidence, question to verify); gaps become areas to probe; growth velocity; an internal vs. external flag.

**Conflicts**
- **Standalone or embedded:** a separate profile (aem/td templates) or part of the guide (aem prompt, react, tl).
- **Recruiting data:** keep or drop pipeline status, salary and availability?
- **Proto-verdicts:** "Seniority (your assessment)" and "Working Hypothesis" vs. tl's "observations, not conclusions".
- **Relative comparison:** "Comparable precedents" breaks prompt 04's rule against relative comparisons.

## Guía de entrevista

**Exists**
- **aem template** (`aem/Templates/EN - Template - Interview Guide.md`):
  - Opening of 5 min
  - 5 areas (Communication, Growth Mindset, Problem Solving, Collaboration, AEM-specific), each with Main question, Follow-up and What to look for
  - Closing of 5 min, where the situational question goes
- **aem 60-min model** (`aem/Guias/EN - interview-model-60min.md`): Opening 5 / Soft 25 (3 STAR questions) / AEM Technical 25 / Closing 5. A tech specialist writes the technical questions.
- **aem prompt 01**, which real guides follow (e.g. `aem/Evaluaciones/Completed/Everton Silva/EN - Everton Silva - Interview Guide.md`):
  - The technical block lists 4–6 areas but **no questions**.
  - It forces one follow-up that gets evidence of collaboration.
  - It ends with Signals to Watch: Verify / Red / Green.
- **Later aem guides** add an English phrasebook for a delegated interviewer and a "Post-Interview Verdict Sheet" (`.../Yash Wadhwani/Interview Guide - Yash Wadhwani.md`).
- **aem question bank:** `aem/Guias/EN - interview-evaluation-guide.md`. Its Top 20 is duplicated in the skill.
- **td 90-min model** (`td/Guias/ES - modelo-entrevista-90min.md`):
  - Blocks: Liderazgo Estratégico 15, Arquitectura 25, Equipos 15, Stakeholders 15, Ejecución/KPIs 10, plus opening and closing.
  - The template gives the last block ~15 min instead.
  - Questions come from the skill's Top 21.
- **react guide** (`react/guia-entrevista.md`, 60–75 min):
  - A rapid-fire "detector de bluff" opener
  - Blocks 1–8 mandatory, then 3–4 picked from blocks 9–17
  - Each question has a model answer, 🚩 warning signs and a follow-up
- **tl guide:**
  - An agenda with an **owner per block** (hiring lead, Expert, Managing Director)
  - Numbered questions mapped to an "Evaluation dimensions" table
  - Tips, e.g. no personal topics and don't name the client
  - A live-notes template

**Common core:**
- Timed blocks with an opening and a closing
- For each question: a main question, follow-ups, and what to look for
- STAR, plus "what did *you* do?"
- Personalised from the CV
- The candidate's closing questions count as data

**Conflicts**
- **Who writes the technical questions:** the aem tech specialist, or the guide itself (react, td, tl).
- **Length:** 60 min (aem, tl), 60–75 (react), 90 (td).
- **Where the question bank lives:** in the skill (aem, td), in its own file (react), or ad hoc (tl). This feeds the open "Question bank" item.
- **Model answers:** react has them; the others don't.
- **Verdict sheet:** the aem "Verdict Sheet" contradicts "no verdict".
- **Template drift:** the aem template has 5 areas, but practice uses 4 blocks.

## Scorecards (soft + technical)

**Exists**
- **aem Soft:** Communication, Problem Solving, Collaboration, Growth Mindset, Ownership. Scored 1–5 with evidence; red/green flags; Strong Hire … Strong No Hire.
- **aem Technical:** AEM Knowledge, Architectural Thinking, Code Quality, Debugging, Stack Breadth. Scored 1 "no knowledge" to 5 "can teach"; 10 AEM sub-areas; "Level matches CV?".
- **aem prompts 02/03:** add growth velocity, a calibrated level and a bias checklist. Only interview evidence counts; mark "not evaluated" rather than guess; a confident wrong answer is worse than an honest gap.
- **td:** Liderazgo uses the base dimensions plus "¿Lidera o ejecuta?". Técnico covers Visión Arquitectónica, Liderazgo y Mentoría, Stakeholders y Delivery, Gobierno Cloud/Seguridad, and Resultados y KPIs. Outcomes are Avanzar / Con reservas / No avanzar. With no concrete example after a follow-up, the score is ≤2 (`td/Guias/ES - guia-evaluacion-td.md`).
- **react:** 13 areas weighted Alto/Medio/Bajo, scored 1–4 or "No evaluado". Threshold: Alto average ≥3 and no 1.
- **tl:** no numbers. The evidence scale is Strong / Some / Little / Concern / Not assessed: "Leave scoring to the interviewers."

**Common core:** dimension × rating × evidence; flags; score independently and immediately; state missing evidence explicitly; compare the CV with what the interview showed.

**Conflicts**
- **Scale:**
  - 1–5 (aem, td). aem has two different wordings, and its guide anchors only 1/3/5.
  - 1–4 weighted (react).
  - Categorical (tl).
  - Unused Below/Meets/Exceeds (`martech/structure/_templates/evaluation-criteria-template.md`).
- **Missing evidence:**
  - aem gives "3/5 por dato insuficiente" (`aem/Guias/Mejoras pendientes del proceso.md` #1).
  - td gives ≤2.
  - react and tl mark it "Not assessed".
- **Recommendation:** aem, td and react put one on each scorecard, which breaks the no-verdict rule.
- **Dimensions differ by stack:**
  - Real aem cases even rename the tech dimensions (`.../Yash Wadhwani/EN - Yash Wadhwani - Scorecard Technical.md`).
  - This needs a fixed core plus stack-specific dimensions.
- **Layout:** one file per interviewer and type (aem), a single combined file (react), or one rater filling both (`mem-aem`).
- **Weights and thresholds:** only react has them.

## Debrief

**Exists**
- **aem template:** marked `generated: ai-draft`. An Interviewer 1–3 table covering **soft dimensions only**. Strengths / Concerns / Discrepancies, each with an empty **Resolution**. For/against, risks, and a Decision with calibrated level.
- **aem prompt 04**, which real debriefs follow (e.g. `.../Everton Silva/EN - Everton Silva - Debrief.md`): adds tech averages, **Onboarding Risk** (time to productivity, support, gaps, risk level) and Growth Velocity. Never fabricate a recommendation; no relative comparisons.
- **td:** a per-interviewer table; discrepancies with a hypothesis; onboarding risk including the authority needed on day 1. Decisión: Oferta / Con condiciones / Rechazo / Otra ronda.
- **react:** `scorecard-debrief.md`, written for HR. Claude writes the **Recomendación final** (Avanza / No avanza / Dudoso).
- **tl** (`mem-tl`): built from the transcript. Claude asks about unclear points and adds context; the user decides.
- **Tracking:** `aem/pipeline-summary.csv` has 19 columns (per-dimension scores, averages, velocity, summary, recommendation); its recommendation values have drifted into free text. `td/pipeline-summary.csv` has 8 columns.

**Common core:** a draft for humans; consolidated evidence; discrepancies showing each side's evidence and an empty resolution; for and against; onboarding risk; humans decide.

**Conflicts**
- **Verdict:** keep an empty Decision section for the hiring lead, or drop it? Every template has a decision vocabulary, and react fills it in.
- **Input:** scorecards (aem, td) or the transcript directly (react, tl). Do scorecards stay as a separate step?
- **Variants:** a single-rater/internal debrief (`mem-aem`) and a "light" one when raters agree (Mejoras #4).
- **Audience:** HR (react), managers and recruiting (tl), or the team (aem).
- **Level vocabulary:** the calibrated-level vocabulary doesn't match the handbook's.
- **Tracking CSV:** keep one or not?

## What `martech/structure` offers

**Roles**
- `hb/roles/` holds:
  - Leadership: director, regional-director, expert, manager, leader.
  - Individual contributors: developer, frontend, backend, devops, qa.
  - Plus principles.
- Every role file has the same sections: `Mission`, `Responsibilities`, `Objectives by level`, `Reporting & management`, `Decides vs. escalates`, `Requirements` (Must have / Nice to have / By platform), `Related documents`.
- **Nice to have is a pending placeholder in every role.**
- "Objectives by level" means the org layer, not seniority.
- No role file splits by seniority.

**By platform**
- Only the frontend, backend, devops and qa roles have it.
- It always lists all 6 platforms: AEM Traditional, AEM EDS, Optimizely Cloud, Contentful, Adobe Commerce PaaS and SaaS.
- Each entry is `[Platform](../technologies/<slug>.md): <tech>`.

**Levels and tracks**
- `hb/reference/career-levels.md`:
  - 8 levels: Trainee, Junior, Junior Advanced, Semi Senior, Semi Senior Advanced, Senior Level 1–3.
  - L8 is Tech Leader; above it the path forks to Manager or Expert, then Director.
  - Each transition has Autonomy, Impact and Mentorship criteria.
  - **No years of experience.**
- `hb/reference/tracks.md`: the four individual-contributor tracks (frontend, backend, devops, qa).
- `hb/career-paths/<track>.md`: scope per level and `X → Y` complexity criteria. This is the only content that varies by level.

**Other content**
- `hb/technologies/<platform>.md`: a "Stack by layer" table.
- `hb/roadmaps/<track>.md`: Essential / Recommended / Optional.

**Gaps**
- `hb/evaluation-criteria/` is "Pending" and empty.
- There is no interview material anywhere.

**How a skill would read it**
1. Read `roles/<slug>.md`.
2. Follow its By-platform bullet to `technologies/<platform>.md` and `shared-stack.md`.
3. Read the level row in `career-paths/<track>.md` and the matching career-levels transition. For L8, read `roles/leader.md`.
4. Treat all-italic lines and `badge: Pending` as undefined.

## Complete real cases (acceptance candidates)

**Complete** (CV + guide + transcript or notes + debrief):
- `td/Evaluaciones/Completed/Jose_David_Restrepo/`: Gemini notes, 2 scorecards.
- `td/Evaluaciones/In Progress/Gustavo_Hurtado/`: same set; the decision is pending another round.
- `react/candidatos/jhon-garces/`: `transcript.md` and a take-home report.

**Near-complete:**
- `aem/Evaluaciones/Completed/Swaroop Kumar Reddy/`: Gemini notes, but no CV file.

**Partial:**
- **Most aem completed cases:** CV, guide, scorecards and debrief, but no stored transcript. The evidence lives in the scorecards. Examples: `aem/Evaluaciones/Completed/Everton Silva/` (EN), `.../Daniel Carrasco Herrera/` (ES).
- **`aem/Evaluaciones/Completed/Amol Pandit/`:** internal, single-rater edge case.
- **`tl/brandon-gallagher/`:** CV and guide only.

## Workflow rules found in project memories

**`mem-tl/interview-workflow.md`**
- Flow: CV + Posición → guide (EN, ~1 h) → transcript → debrief.
- Questions are based on `martech/structure`.
- The debrief goes to managers and recruiting.
- **Never decide or recommend a verdict; ask when in doubt.**
- Chat in Spanish, deliverables in English.

**`mem-aem/project_internal_single_rater_debrief.md`**
- When one rater covers both scorecards, drop the multi-interviewer table.
- Reframe discrepancies as tensions inside that rater's evidence.
- Flag the single-rater limit as a risk.
- For internal candidates, "Hire" means a placement decision.
- The calibrated level goes through the user.

**Rules from the workspace docs** (`aem/Guias/ES - proceso-de-entrevistas.md`, `react/README.md`)
- Score before talking to other raters.
- Score immediately.
- AI output is a draft.
- Ask before overwriting.
- Identify input files by content.
