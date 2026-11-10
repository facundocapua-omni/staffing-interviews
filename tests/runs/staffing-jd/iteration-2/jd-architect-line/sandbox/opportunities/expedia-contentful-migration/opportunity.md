---
opportunity: expedia-contentful-migration
updated: 2026-10-28
---

# Expedia: Contentful migration

## Context

- **Client:** Expedia Group; external client of Globant's Salesforce Studio (account already active).
- **Project:** Migrate Expedia Group's partner websites from Adobe Experience Manager to Contentful, and build a Content Resolution API that serves the same content to Salesforce Marketing Cloud, CRM/VMC and partner web.
- **Workstreams:**
  - Partner Web Content: four sites (partner.expediagroup.com, host.vrbo.com, escapia.com, expediagroup.com), ~102,600 items. Contentful setup and custom development, Next.js front end, Akamai edge, content migration pipeline, training, hypercare. 12 months, Time & Materials. Staffed by the Labor Estimate lines below.
  - Content Resolution API: a Contentful app that resolves variants by locale, tone and channel, integrates with SFMC and NBA, and logs every resolution. 8 weeks. Not in the Labor Estimate; staffed by the same backend people (answer 6), so its needs fold into the backend JDs.
- **Dates:** Nov 2026 → Oct 2027. P&L Month 1 = Nov 2026 (Proposal: "Team Integration (Nov-1)"; SOW billing from 2026-11-30). Contract signing "Oct-31?" in the Proposal.
- **Stack signals:**
  - Content platform: Contentful (content model, environments, locales and fallback, workflows and tasks, App Framework apps, live preview, Contentful Personalization by tier).
  - Front end: Next.js (App Router), Tailwind, the client's EGDS React components, ISR/SSR, Draft Mode preview, deployed with OpenNext.
  - Infrastructure: client's AWS account (Lambda, S3, DynamoDB, SQS, optionally CloudFront/ALB), IaC with SST, Terraform or CDK, GitHub Actions or equivalent, Datadog and CloudWatch, Lighthouse in the pipeline.
  - Edge: Akamai and Cloud Gate Proxy, routing by path and cohort, redirects.
  - Migration: scripted, idempotent extract-transform-load-validate pipeline from AEM.
  - API: Content Resolution API as a Contentful app; SFMC Marketing Object; NBA decision payload.
- **Locations:** Labor Estimate: Mexico (Architect line), Colombia (the rest). Sourcing: remote, open to all of LATAM (answer 11).

## Sources read

- `[Globant - Expedia_TPA] SF Contentful Migration - October 2026 (1).pptx`: the Proposal. Read in full; the appendix case studies and Salesforce Studio credentials skimmed.
- `[TPA Expedia] Contentful Migration Proposal - Pricing Sheet V4 _AI PODs_.xlsx`: the P&L. Read `2.1 Labor Estimate` and `SOW`; `Summary`, `1. Settings & Acc. Info` and the AI POD sheets (empty) checked; rates and costs not carried over.
- Handbook: `roles/` (index, developer, backend, frontend, qa, devops, expert), `career-paths/backend.md` (and the Semi Senior Advanced / Senior Level 1 rows of frontend, qa, devops), `reference/career-levels.md`, `technologies/contentful.md`.
- HR job descriptions: `software-architect.md`; years for the other levels from `level-equivalence.md`.

## P&L lines → Positions

| # | P&L line (role · seniority · location) | Position (handbook role · level · platform) | Headcount | Start | JD | Flags |
|---|---|---|---|---|---|---|
| 1 | Tech Project Manager · Manager · Peru | n/a | n/a | n/a | no: already assigned to a named person | none |
| 2 | Tech Director · Director · Spain | n/a | n/a | n/a | no: governance line | none |
| 3 | Client Engagement Director · Director · USA | n/a | n/a | n/a | no: non-billable structure line | none |
| 4 | AEM Backend Developer · Sr 3 · Mexico (Client's Role Name: "Architect") | Expert · Senior Level 3 (L8) · Contentful | 1 | open | `expert-l8-contentful/jd.md` | Expert is a regional role in the handbook; project scope from the Propuesta. SOW: "Sr Level 2" |
| 5 | AEM Backend Developer · Mid Level · Colombia | Backend Developer · Semi Senior Advanced (L5) · Contentful | 1 | open | `backend-developer-l5-contentful/jd.md` | SOW: "Sr" |
| 6 | Web UI Developer · Sr · Colombia | Frontend Developer · Senior Level 1 (L6) · Contentful | 1 | open | `frontend-developer-l6-contentful/jd.md` | SOW: "Sr Level 2" |
| 7 | Web UI Developer · Mid Level · Colombia | Frontend Developer · Semi Senior Advanced (L5) · Contentful | 1 | open | `frontend-developer-l5-contentful/jd.md` | SOW: "Sr" |
| 8 | AEM QC Analyst · Sr · Colombia | QA Engineer · Senior Level 1 (L6) · Contentful | 1 | open | `qa-engineer-l6-contentful/jd.md` | none |
| 9 | DevOps Engineer · Sr · Colombia | DevOps Engineer · Senior Level 1 (L6) · Contentful | 1 | open | `devops-engineer-l6-contentful/jd.md` | none |
| 10 | Martech Content Specialist · Sr · Colombia | n/a | n/a | n/a | no: not a DXP technical role (answer 2) | Off-handbook role: Content Specialist |
| 11 | Martech Content Specialist · Sr · Colombia | n/a | n/a | n/a | no: not a DXP technical role (answer 2) | Off-handbook role: Content Specialist |
| 12 | Cultural Hacking Lead · Lead · Mexico | n/a | n/a | n/a | no: practice role (Globant `Lead`) | none |

Start is open on every Position (question 8). For reference, the first P&L month with allocation is Month 3 (Jan 2027) for lines 4, 6 and 9, Month 4 (Feb 2027) for lines 5 and 7, and Month 6 (Apr 2027) for line 8.

## Inconsistencies found

1. Seniority differs between the SOW sheet and the Labor Estimate: line 4 is Sr 3 in the Labor Estimate and "AEM Developer Sr Level 2" in the SOW; line 5 is Mid Level vs "Sr"; line 6 is Sr vs "Sr Level 2"; line 7 is Mid Level vs "Sr". The Labor Estimate rules (answer 3).
2. The Content Resolution API workstream appears in the SOW sheet (TPM, AEM Backend Developer Sr Level 2, AEM Backend Developer Sr, AEM QC Analyst Sr) and in the Proposal (8 weeks, priced separately), but has no Labor Estimate lines; the Labor Estimate total matches the Partner Web price only. Resolved: staffed by the same backend people (answer 6).
3. P&L role labels name AEM ("AEM Backend Developer", "AEM QC Analyst") while the Proposal's target platform is Contentful; AEM is the migration's source. Resolved: Contentful is the platform (answer 5); AEM familiarity is Nice to have.
4. The SOW sheet's client-facing column lists the Cultural Hacking Lead as "Content Specialist Sr", while its internal column lists it separately as "Cultural Hacking · Lead".
5. The Proposal's "Project POD" slide names a Marketing Cloud Architect and a Marketing Cloud Developer, which the P&L does not price. Resolved by answer 6: the API needs go to the backend JDs, with no separate Positions.

## Intake answers

1. Which lines get a JD? **Answer:** only the six DXP technical lines (4–9); lines 1–3 are already assigned or are structure.
2. Do the Martech Content Specialist lines (10, 11; off-handbook role) get a JD? **Answer:** no. A P&L lists the whole team; intake keeps only DXP technical roles. The proposed Content Specialist Requirements were discarded.
3. Is the Labor Estimate the current source for seniority, given the SOW gaps? **Answer:** yes, the Labor Estimate.
4. Level equivalence. **Answer:** the hiring lead restated the table (Mid Level → L5 / Semi Senior II / 4 years; Sr → L6 / Senior I / 5; Sr Level 2 → L7 / Senior II / 6; Sr 3 → L8 / Tech Lead I / II / 7+ / 10+). "Lead" and Experience Senior I / II (7 / 8 years) remain unmapped.
5. Is Contentful the platform for every JD, despite the "AEM" labels? **Answer:** yes; the platform is the technology the Proposal defines, and a Globant role label is only today's catalog name.
6. Is the Content Resolution API staffed by the same people, or by separate Positions? Do the Marketing Cloud roles on the POD slide apply? **Answer:** the same backend people; its needs (SFMC, Contentful app) become Requirements of the backend JDs.
7. Allocation. **Answer:** irrelevant to the JD, which sources a profile.
8. English. **Answer:** B2 minimum for everyone; B1 possible only for roles that do not face the client. No exception granted for these six Positions.
9. Line 4 (Sr 3, Client's Role Name "Architect"): Expert or Tech Leader, and does it lead people? **Answer:** an Expert Position (no reports). Years follow the Software Architect HR job description (11).
10. Search integration (Algolia / Elasticsearch, from the handbook's Contentful backend entry). **Answer:** Nice to have.
11. Location and remote. **Answer:** remote, open to all of LATAM.
12. Start dates: keep the P&L's first month with allocation (Month 1 = Nov 2026), or shift them with the contract signing ("Oct-31?")? **Open:** no answer yet. Waiting on it: the Start in the Logistics of all six JDs, which read "To be confirmed".
