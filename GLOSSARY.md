# Staffing

Personal skill suite that supports staffing work for client projects: from describing what a project needs to deciding on a candidate after the interview.

## Language

**Oportunidad**:
A staffing need coming from a client project (client, project, dates, allocation). The client may be internal: the company staffing a role of its own, such as a Technology Director, is an Oportunidad like any other. Holds one or more Posiciones.
_In English_: Opportunity
_Avoid_: Vacante, request, búsqueda

**Posición**:
A single role inside an Oportunidad (e.g. "Backend Magento Sr"). It is what a JD describes and what Candidatos are evaluated against. It may have several seats (headcount) and still has one JD.
_In English_: Position
_Avoid_: Rol (when referring to the slot to fill), puesto, perfil, one Posición per seat

**JD**:
The description of a Posición for the recruiting team, written to source Candidatos: its Requisitos, what the person will do, and how to screen. Its Requisitos come from the handbook role, level and platform (or a Descripción de cargo where the handbook has none), plus what the Posición itself needs, as stated in the Propuesta, by Presales or by the hiring lead, who may also supply a JD of their own.
_Avoid_: Job posting, perfil buscado

**Descripción de cargo**:
The HR document of a job at one role and level (mission, responsibilities, KPIs, reporting line, years, English), such as the old Omni ones. It describes an employee's job, not a Posición: a source of a JD's Requisitos where the handbook has none, never a JD itself.
_In English_: HR job description
_Avoid_: JD viejo, old JD

**Propuesta**:
The proposal sent to the client for an Oportunidad, usually a deck. It defines the scope and the technology, and is where a Posición's own Requisitos come from.
_In English_: Proposal
_Avoid_: Oferta, pitch

**P&L**:
The pricing sheet of an Oportunidad. Its staff plan (the Labor Estimate) lists the whole team that is priced, by role, seniority, location and month. It is the source of a Posición's seniority, never of its technology.
_In English_: P&L
_Avoid_: Pricing, cotización, SOW (the client-facing team sheet inside it)

**Presales**:
The team that builds an Oportunidad's Propuesta and P&L. Beyond those documents, it may state Requisitos of its own.
_In English_: Presales
_Avoid_: Preventa, ventas

**Requisito excluyente**:
A Requisito a Candidato must meet to be considered for the Posición.
_In English_: Must have
_Avoid_: Knock-out, mandatory, obligatorio

**Plus**:
A Requisito that adds to a Candidato's fit but whose absence does not rule them out.
_In English_: Nice to have
_Avoid_: Deseable, bonus, strong plus

**Candidato**:
A person considered for one Posición. The same person considered for two Posiciones is two Candidatos. Either internal or external; the pipeline is the same for both.
_In English_: Candidate
_Avoid_: Candidatura, postulante, aplicante, recurso

**Colaborador**:
Someone who already works at the company, whether on a project, on bench or being reassigned.
_In English_: Employee
_Avoid_: Recurso, bench (as a noun for the person)

**Candidato interno**:
A Candidato who is a Colaborador, whose project history and prior feedback can be used as evidence. Being internal is fixed per Candidato, not per person: someone external in one Posición can be internal in a later one.
_In English_: Internal candidate

**Candidato externo**:
A Candidato who is not a Colaborador, for whom the evidence is limited to CV, public profile and what the interview shows.
_In English_: External candidate

## Pipeline

**Evaluación de match**:
The assessment of one Candidato against their Posición, built from a Nivel de evidencia per Requisito in documents only, before any interview. It never carries a verdict. Fitting one person to several Posiciones means one Evaluación de match per Posición, never one against the whole Oportunidad.
_In English_: Match evaluation
_Avoid_: Screening, perfil, fit score

**Nivel de evidencia**:
How well the documents about a Candidato show one Requisito, before any interview: Evidenced, Claimed, Partial, No evidence, or Not met.
_In English_: Evidence level
_Avoid_: Calificación (that is the Scorecard's), match score, cumple / no cumple

**Punto a indagar**:
A doubt about one Requisito, or about the credibility of the CV, that the Evaluación de match hands to the Guía de entrevista to verify. It states what to verify, not the question to ask. After the Entrevista, the Debrief records whether it was Confirmed, Contradicted, Inconclusive or Not probed.
_In English_: Point to probe
_Avoid_: Gap, red flag (flags are what an interview shows)

**Entrevista**:
One one-hour session with a Candidato, run by one or more Entrevistadores from its own Guía de entrevista. Covering a Posición may take more than one Entrevista.
_In English_: Interview
_Avoid_: Sesión, ronda (as something other than an Entrevista)

**Guía de entrevista**:
The plan for one Entrevista of one Candidato, usable by whichever Entrevistador runs it, including one with none of the hiring lead's context.
_In English_: Interview guide
_Avoid_: Interview kit, cuestionario

**Debrief**:
The consolidated record of every Entrevista of one Candidato that structures their evidence and holds the hiring lead's decisions, which Claude never fills.
_Avoid_: Feedback, informe de entrevista

**Discrepancia**:
A difference between Entrevistadores, or between Entrevistas, about the same Dimensión or Punto a indagar, or with a single Entrevistador a tension inside their own evidence, that only the hiring lead resolves.
_In English_: Discrepancy (Tension, with a single Entrevistador)
_Avoid_: Conflicto, desacuerdo, inconsistencia

**Shortlist**:
The hiring lead's ordered list of the Candidatos they consider for a Posición. The order is always the hiring lead's decision, never Claude's.
_In English_: Shortlist
_Avoid_: Ranking, priorización

**Entrevistador**:
The person who runs an interview: the hiring lead, a pair, or a team member the interview was delegated to.
_In English_: Interviewer
_Avoid_: Panel, evaluador

**Etapa**:
Where a Candidato stands in the pipeline: Not evaluated, Evaluated, Interview planned, Interviewed, Debriefed, or Decided. It ends at the hiring lead's decision; offer, acceptance and assignment are outside it. Being on the Shortlist is not an Etapa.
_In English_: Stage
_Avoid_: Estado (of a Candidato), fase, seat covered

**Resumen de estado**:
The current Etapa of every Candidato of one Oportunidad, per Posición, with what is pending. It holds no evidence and no Claude judgment, and is a picture of the present, not a history.
_In English_: Status summary
_Avoid_: Reporte de pipeline, tracking, dashboard

## Scorecards

**Scorecard**:
One Entrevistador's own ratings for one Entrevista, soft and technical together, each with its evidence, in whatever shape they bring it. Only its ratings on the Calificación scale are Calificaciones. An optional input to the Debrief.
_Avoid_: Hoja de evaluación, rating sheet

**Dimensión**:
One aspect of a Candidato that a Scorecard rates. Every Posición shares the soft Dimensiones and the technical core, and leadership Posiciones add a leadership block; what changes is what meeting each one means at the Posición's level.
_In English_: Dimension
_Avoid_: Área, criterio, competencia

**Calificación**:
Where a Candidato stands on one Dimensión against the career level of the Posición: Below, Meets or Exceeds, or Not assessed when no evidence for it was collected: the Entrevista did not cover it, or a result provided separately (English) never arrived.
_In English_: Rating
_Avoid_: Score, puntaje, nota
