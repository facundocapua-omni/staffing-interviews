# JD structure

Type: prototype
Status: resolved
Blocked by: 01
Map: [Staffing skills suite](../map.md)

## Question

What does a JD look like, and what does the skill need from you to write one?

Decide:

- Its sections, written for the recruiting team.
- How it composes the handbook base (role, career level, and the platform's `### By platform` requirements in `martech/structure`) with the Posición's own additional requirements and the Oportunidad's context (client, project, dates, allocation).
- What is told to recruiting and what stays internal.
- The minimum input you give the skill, and who writes `opportunities/<op>/opportunity.md` (see [Disk layout of the chain](02-chain-disk-layout.md)).

Prototype a rough JD for a realistic Posición to react to. Build on the findings of [Inventory existing staffing material](01-inventory-existing-staffing-material.md), especially any existing JDs it found. Start from the JD conflicts listed in the [findings](../research/01-existing-staffing-material.md#jd): skeleton, years of experience and English level, KPIs, roles and platforms the handbook lacks (Software Architect, Sitecore), and seniority vocabulary (ranges vs the handbook's numbered levels).

## Answer

Prototyped 2026-10-21 on a real Oportunidad (Expedia Group, AEM → Contentful): [intake analysis](../prototypes/04-jd/PROTOTYPE-01-intake-analysis.md) and [three JD variants](../prototypes/04-jd/PROTOTYPE-02-jd-variants.md). Terms resolved in [GLOSSARY.md](../../../GLOSSARY.md): Propuesta, P&L, Requisito excluyente, Plus.

> **Amended by [Acceptance cases](09-acceptance-cases.md)** (2026-10-22). An Oportunidad's client may be internal (e.g. the company's own Technology Director role). Then the input is the hiring lead's material, as files or pasted text: an existing JD or a brief, in place of the Propuesta and P&L. The level is asked in the intake round, nothing is anonymised, and `opportunity.md` is still written.

> **Amended by [Handbook gaps for JDs](11-handbook-gaps-for-jds.md)** (2026-10-23). That ticket holds the replacements:
> - The level equivalence table: Sr 3 splits on whether the person leads people; SME, Manager and Director rows are added; Globant `Lead` has no row. The column "Old Omni JD" is now "HR job description" (a Descripción de cargo).
> - The origins list: `old JD (years)` becomes `HR job description`, and `presales`, `supplied JD` and `hiring lead` are added. Claude is never an origin.
> - Any Oportunidad, not only one with an internal client, may come with only the hiring lead's material. A JD the hiring lead supplies for a Posición sits above the handbook base.
> - Where the base comes from when the handbook lacks a role or platform, and how `opportunity.md` and `jd.md` flag it.

**Flow and input**

- The skill works per Oportunidad, not per Posición. Its input is the Propuesta (usually a deck) and the P&L.
- It reads both, writes an intake analysis, asks the hiring lead one round of questions, then writes `opportunity.md` and every `jd.md` of the Oportunidad in the same run.
- `opportunity.md` is that intake analysis: context (client, workstreams, dates, stack signals), a table of P&L lines → Posiciones (handbook role · level · platform) with flags, the inconsistencies found, and the answers to the question round. It is the only artifact that names the real client.

**Intake rules**

- Keep only DXP technical lines: a P&L lists the whole priced team. Lines already assigned to a person, and structure or governance lines, get no JD.
- Seniority comes from the P&L's Labor Estimate, never from its client-facing SOW sheet.
- Platform and technical Requisitos come from the technology the Propuesta defines. A P&L role label (e.g. "AEM Backend Developer") is only the catalog name homologated today.
- Workstreams staffed by the same people fold their needs into the same JD (e.g. the API workstream's SFMC needs go into the backend JDs).
- Allocation (FTE curves, gaps between months) is not part of a JD: the JD is for sourcing a profile.
- English: B2 minimum for every Posición; B1 only as an exception for roles that do not face the client.

**Level equivalence** (a reference table of the suite)

| Globant P&L | Handbook | Old Omni JD | Years |
|---|---|---|---|
| Mid Level | L5 Semi Senior Advanced | Semi Senior II | 4 |
| Sr | L6 Senior Level 1 | Senior I | 5 |
| Sr Level 2 | L7 Senior Level 2 | Senior II | 6 |
| Sr 3 | L8 Senior Level 3 | Tech Lead I / II | 7+ / 10+ |

Years of experience come from the old Omni JDs (`~/Downloads/ENGINEERING`), since the handbook has none. Missing rows: [Handbook gaps for JDs](11-handbook-gaps-for-jds.md).

**JD shape** (`jd.md` in English; recruiting reads its PDF export)

- The skeleton is the recruiting brief (variant B):
  - Title (role · level · platform) and location.
  - A one-line summary.
  - Requisitos excluyentes as a checklist, then Plus.
  - What the person will do.
  - Search keywords.
  - Screening: questions with what a good answer mentions, and/or points to check in the CV or profile.
  - "Not a fit if".
  - Logistics: location, remote, start, full-time.
- Two Requisito tiers only, Requisito excluyente and Plus, with no numeric weights.
- Every Requisito carries its origin in the Markdown source: handbook role, handbook level, handbook platform, Propuesta, old JD (years), or suite rule. The PDF export strips the tags.
- Requisitos compose from: the handbook role's Must have, the level's scope (career path), By platform, the Propuesta's own needs, years (old JDs) and the English rule.
- The client is anonymised in the JD (e.g. "a US-based global travel company").
- The handbook-mirror (A) and HR-format (C) variants are discarded.

**Calls made without an explicit answer (correct them if wrong)**

- The seniority gap between the SOW and the Labor Estimate is recorded as a flag in `opportunity.md`, not in the JD.
- Familiarity with a migration's source platform (e.g. AEM for extraction) enters as Plus, not as Requisito excluyente.
- English labels in a JD follow the handbook: "Must have" / "Nice to have".

**Handed to other tickets**

- Requisito tiers and origin tags are fixed: [Evaluación de match rubric](05-match-evaluation-rubric.md).
- The Expedia Oportunidad is an acceptance case for the JD skill: [Acceptance cases](09-acceptance-cases.md).
- The JD skill also owns the intake and `opportunity.md`: [Skill boundaries](03-skill-boundaries.md).
- Missing levels, roles and platforms: [Handbook gaps for JDs](11-handbook-gaps-for-jds.md).
