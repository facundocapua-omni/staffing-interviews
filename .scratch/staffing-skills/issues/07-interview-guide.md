# Unified Guía de entrevista

Type: grilling
Status: resolved
Blocked by: 06
Map: [Staffing skills suite](../map.md)

## Question

What single Guía de entrevista replaces the per-stack guides?

Decide:

- Sections and timing (the current format is about one hour).
- How questions map to the dimensions fixed in [Scorecards: dimensions and scale](06-scorecards.md).
- How the "points to probe" from the [Evaluación de match rubric](05-match-evaluation-rubric.md) and an optional take-home report become questions. If that ticket is still open, agree the hand-off shape here and record it there.
- What makes the guide usable by a delegated Entrevistador with none of your context, as well as by you alone or by a pair.

Start from the Guía conflicts listed in the [inventory findings](../research/01-existing-staffing-material.md#guía-de-entrevista): who writes the technical questions, duration, model answers, the "verdict sheet", and template drift.

From [Scorecards: dimensions and scale](06-scorecards.md): map questions to its 14 Dimensiones (6 soft, 5 technical, 3 leadership for leadership roles). The blank `scorecard-<interviewer-slug>.md` files, one per Entrevistador in `interviewers`, are written together with the Guía.

From [Evaluación de match rubric](05-match-evaluation-rubric.md): the points to probe arrive ordered (excluyentes first, then Plus; within each, Claimed → Partial → No evidence). Each carries the Requisito and its tier, the Nivel de evidencia, the quote, what to verify (worded as a doubt) and the Dimensiones it lands on. The Guía turns them into questions.

## Answer

Grilled 2026-10-21. Terms resolved in [GLOSSARY.md](../../../GLOSSARY.md): Entrevista; Calificación refined (Not assessed also covers a result provided separately that never arrived).

**Format**

- Every Entrevista lasts one hour, for every Posición, leadership roles included.
- Blocks in a fixed order: Opening → Background & motivation → Soft → Technical → Leadership (leadership roles only) → Candidate questions → Closing.
- The agenda names an owner per block, from `interviewers`. Minutes and owners are a starting split for the Entrevistadores to adjust, and the agenda says so in one line.
- **More than one Entrevista:** the skill first tries to fit the hour with at least one main question per Dimensión and every Punto a indagar on a Requisito excluyente. When that does not fit, it says so and proposes what moves to another Entrevista. The hiring lead chooses between another Entrevista and listing those Dimensiones as not covered. Each Entrevista has its own `interviews/<YYYY-MM-DD>/` folder and its own Guía ([Disk layout of the chain](02-chain-disk-layout.md)).
- A later Entrevista of the same Candidato reads the previous Debrief and Scorecards. It targets the Dimensiones left Not assessed and the open discrepancies, and does not repeat questions already asked.

**Questions**

- Numbered across the whole Guía (Q1…Qn). The ids are stable, and everything written after the Entrevista cites them.
- Each question has:
  - the main question;
  - follow-ups;
  - **Listen for:** what a strong answer mentions at the Posición's level;
  - **Watch for** (optional): signals specific to that question;
  - the Dimensiones it gives evidence for;
  - its origin: handbook, JD Requisito, Punto a indagar, take-home, or question bank.
- No model answers in prose (react) and no per-question Below/Meets/Exceeds anchors (aem): the anchors belong to the rubric, per Dimensión.
- **Technical questions:** the Guía writes them too, as suggested prompts the technical Entrevistador adapts. They come from three sources:
  - Platform knowledge's sub-areas (`technologies/<platform>.md`);
  - the JD's Requisitos;
  - the level's scope in `career-paths`.
  When the handbook lacks the platform, they come only from the JD's Requisitos, and the Guía says so.
- **Question bank:** pluggable content inside the suite, per platform and per track. It is seeded from the existing banks: aem's Top 20, td's Top 21, react's guide and tl's ad hoc questions. Bank questions have the same shape as above. When no bank covers the platform or track, the Guía generates the questions and says the bank is missing. The bank is not in the handbook, because Candidatos internos can read the handbook.

**Coverage**

- Every Dimensión of the Posición has at least one main question. Otherwise it is listed as "Not covered in this interview", so its Not assessed is planned, not accidental.
- A coverage table maps each Dimensión to its question numbers.
- English is not assessed in the Entrevista. Its row reads "Assessed separately" (see "No notes, no blank Scorecards").

**Inputs and Puntos a indagar**

- **Required:** the JD and the Evaluación de match.
  - The Guía never reads the CV itself: the CV analysis lives only in the Evaluación de match. The minimum source behind it may be only a public profile (LinkedIn).
  - When the evaluation is missing, the skill stops and offers to run it.
  - When it is stale against the JD (`jd_updated`), the skill says so.
- **Optional:** a copy of the take-home report in the Candidato folder. Its follow-up interview questions enter the Technical block, adapted, with origin `take-home`. A "walk me through your submission" question is added.
- **Order:** the Puntos a indagar arrive in the shape and order fixed by [Evaluación de match rubric](05-match-evaluation-rubric.md). Credibility observations not tied to a Requisito come after the Plus. Each is asked in the block where it fits: the timeline in Background & motivation, an unexplained career gap at the Closing, once and neutrally.
- **Conversion:** each Punto a indagar becomes a question or a follow-up, worded neutrally so the Candidato does not feel targeted. A table at the top maps each Punto a indagar to where it is asked. A list gives what the Entrevista tests, in priority order.
- **Requisito excluyente not Evidenced:**
  - It is probed early in its block.
  - The briefing states it neutrally: "The Evaluación de match found no evidence for Must have X; this interview should collect it."
  - Whether to hold the Entrevista is the hiring lead's call before asking for the Guía. The Guía never suggests declining, so aem's "Before you schedule this" section is dropped.

**Usable without the hiring lead's context**

- **Briefing:**
  - the Posición (role · level · platform);
  - the project, with the client anonymised (only `opportunity.md` names it);
  - what is being tested, in priority order;
  - what the Calificaciones are measured against: the rubric link, or "rubric pending: using career-paths".
- **Fixed interviewer tips:**
  - Ask for STAR examples.
  - Ask "what did *you* do?".
  - Let the Candidato talk 70–80% of the time.
  - Give an honest exit on technical questions: "I'd rather know the edges than hear a guess."
  - No personal topics.
  - Don't name the client.
  - Confirm Claude's proposed Calificaciones before discussing with other Entrevistadores.
- **What you can tell the candidate:** the logistics from the JD.
- **English phrasebook:** only on request.
- **Recording:** the Opening script tells the Candidato the call is recorded and transcribed, and asks for consent. Without consent, the Entrevistador takes minimal notes per block. That is the only case where anyone takes notes.

**No notes, no blank Scorecards**

- The Entrevistador writes nothing during the Entrevista: the transcript is the evidence. The Guía has no notes template.
- The Guía no longer writes blank `scorecard-<interviewer-slug>.md` files. This amends [Scorecards: dimensions and scale](06-scorecards.md).
- After the Entrevista, Claude builds the evidence per Dimensión from the transcript:
  - its Calificaciones are marked `Proposed:` and cite question ids;
  - each block is attributed to its owner in the agenda.
- A Scorecard or notes an Entrevistador brings are still accepted, identified by content.
- **English:** its result is provided to the hiring lead separately; the Entrevista does not produce it. When the Scorecard is put together without it, the skill asks for it. If it never arrives, English is Not assessed.

**Hand-off with a delegated Entrevistador**

- Only the Guía goes out, exported as PDF on request next to its source, like the JD.
- Only the transcript comes back. It is dropped in the Entrevista's folder under any name and identified by content.

**Marking and metadata**

- `Proposed:` is not used in the Guía. The Guía is a plan written entirely by Claude, so its header says so once (the rule as refined in [Scorecards: dimensions and scale](06-scorecards.md)).
- Frontmatter: the Disk layout fields plus `interviewers`.

**Calls made without an explicit answer (correct them if wrong)**

- The Guía is in English whatever language the Entrevista is held in.
- The skill asks for missing inputs in one round before writing: the `interviewers` with the blocks each owns, and the date.
- The question bank does not grow on its own: adding a question is a deliberate edit.

**Handed to other tickets**

- [Unified Debrief](08-debrief.md): the transcript as the main evidence, the transcript-based Calificaciones, one Debrief per Entrevista or consolidated, English as a separate input, and what a later Entrevista needs from the Debrief.
- [Skill boundaries](03-skill-boundaries.md): which skill builds the evidence from the transcript (no blank Scorecards any more), and where the question bank lives in the suite.
- [Scorecards: dimensions and scale](06-scorecards.md): amended, with no blank Scorecards and English provided separately.
- Fog cleared from the map: "Question bank by platform and track" and "Hand-off with a delegated Entrevistador".
