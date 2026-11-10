---
opportunity: expedia-contentful-migration
updated: 2026-10-28
---

# Expedia Group: AEM to Contentful migration

## Context

- **Client:** Expedia Group (EG); external. Sold by Globant's Salesforce Studio, Time & Materials.
- **Project:** migrate EG's partner web from AEM to Contentful, with a new Next.js front end on EG's AWS account, and build a Content Resolution API that serves the same content to Salesforce Marketing Cloud and CRM/VMC.
- **Workstreams:**
  - Partner Web: Contentful setup and custom development (live preview, custom workflow and editor apps), Next.js front end on OpenNext, Akamai edge routing, AWS environments and pipelines, scripted content migration of four sites (partner.expediagroup.com, host.vrbo.com, escapia.com, expediagroup.com; ~102,600 items), training and hypercare. 12 months. Staffed by the Labor Estimate lines.
  - Content Resolution API: a Contentful app that resolves variants by locale, tone and channel with fallback, pushes a Marketing Object to SFMC, takes NBA's decision payload and logs every resolution. 8 weeks; the SOW bills it Aug–Sep 2027. Staffed by the same backend people as Partner Web (intake answer 6).
- **Dates:** Nov 2026 → Oct 2027; Month 1 = Nov 2026 (the SOW's first billing date is 2026-11-30). The deck's timeline runs Nov 2026 → Sep 2027.
- **Stack signals:**
  - Content platform: Contentful (spaces, locales and fallback, environments, workflows, Contentful Personalization depending on the tier), Contentful App Framework for the Content Resolution API and the editor apps.
  - Front end: Next.js (App Router), Tailwind, EG's design system (EGDS) React components, ISR and SSR, live preview on a preview domain, hreflang and SEO parity, analytics data layer, Lighthouse in the pipeline.
  - Hosting and edge: EG's AWS account, OpenNext (server, image and revalidation Lambdas), S3 page cache, DynamoDB tag cache, SQS revalidation queue, infrastructure as code (SST, Terraform or CDK), Akamai and Cloud Gate Proxy, Datadog and CloudWatch, GitHub Actions or equivalent.
  - Migration: scripted, idempotent pipeline from AEM (extract, transform, load, validate with counts, required fields, broken links and visual diff); disposition log and redirect map.
  - Integrations: Salesforce Marketing Cloud, NBA, EG's log system, translation route to be chosen (Babel Prime or a connector).
- **Locations:** P&L lines in LATAM (Mexico, Colombia, Peru), Spain and USA. The six JD Positions are remote, open to all of LATAM (intake answer 11).

## Sources read

- `[Globant - Expedia_TPA] SF Contentful Migration - October 2026 (1).pptx`: the Proposal. Read whole: executive summary, Partner Web scope, deliverables, target architecture, front-end options, timeline, EG involvement, commercials, Content Resolution API scope and timeline. The appendix case studies and methodology slides were read for context only.
- `[TPA Expedia] Contentful Migration Proposal - Pricing Sheet V4 _AI PODs_.xlsx`: the P&L. Read `2.1 Labor Estimate`, `SOW`, `1. Settings & Acc. Info`, `Summary`; `2.2.1` and `2.2.2` AI POD sheets are empty. Rate, cost and margin sheets skipped.
- Handbook: `roles/leader.md`, `roles/backend.md`, `roles/frontend.md`, `roles/qa.md`, `roles/devops.md`, `roles/developer.md`, `roles/index.md`, `reference/career-levels.md`, `career-paths/backend.md`, `career-paths/frontend.md`, `career-paths/qa.md`, `career-paths/devops.md`, `technologies/contentful.md`.
- HR job descriptions: `technical-lead-i.md`, `backend-semi-senior-ii.md`, `frontend-senior-i.md`, `frontend-semi-senior-ii.md` (years only; the handbook covers every other part of the base). No HR job description exists for QA or DevOps; their years come from `level-equivalence.md`.

## P&L lines → Positions

| # | P&L line (role · seniority · location) | Position (handbook role · level · platform) | Headcount | Start | JD | Flags |
|---|---|---|---|---|---|---|
| 1 | Tech Project Manager · Manager · LATAM - Peru | n/a | n/a | Nov 26 | no: already assigned to a named person | SOW lists it as Sr |
| 2 | Tech Director · Director · EU - Spain | n/a | n/a | Nov 26 | no: governance line | SOW lists it as LATAM* |
| 3 | Client Engagement Director · Director · NA - USA Primary | n/a | n/a | Nov 26 | no: structure line, non-billable | none |
| 4 | AEM Backend Developer · Sr 3 · LATAM - Mexico | Tech Leader · Senior Level 3 (L8) · Contentful | 1 | Jan 27 | `tech-leader-l8-contentful/jd.md` | SOW lists it as Sr Level 2; P&L label is AEM, Proposal platform is Contentful |
| 5 | AEM Backend Developer · Mid Level · LATAM - Colombia | Backend Developer · Semi Senior Advanced (L5) · Contentful | 1 | Feb 27 | `backend-developer-l5-contentful/jd.md` | SOW lists it as Sr; P&L label is AEM, Proposal platform is Contentful |
| 6 | Web UI Developer · Sr · LATAM - Colombia | Frontend Developer · Senior Level 1 (L6) · Contentful | 1 | Jan 27 | `frontend-developer-l6-contentful/jd.md` | SOW lists it as Sr Level 2 |
| 7 | Web UI Developer · Mid Level · LATAM - Colombia | Frontend Developer · Semi Senior Advanced (L5) · Contentful | 1 | Feb 27 | `frontend-developer-l5-contentful/jd.md` | SOW lists it as Sr |
| 8 | AEM QC Analyst · Sr · LATAM - Colombia | QA Engineer · Senior Level 1 (L6) · Contentful | 1 | Apr 27 | `qa-engineer-l6-contentful/jd.md` | P&L label is AEM, Proposal platform is Contentful |
| 9 | DevOps Engineer · Sr · LATAM - Colombia | DevOps Engineer · Senior Level 1 (L6) · Contentful (AWS) | 1 | Jan 27 | `devops-engineer-l6-contentful/jd.md` | none |
| 10 | Martech Content Specialist · Sr · LATAM - Colombia | n/a | n/a | Nov 26 | no: not a DXP technical role (intake answer 2) | Off-handbook role: Martech Content Specialist |
| 11 | Martech Content Specialist · Sr · LATAM - Colombia | n/a | n/a | Apr 27 | no: not a DXP technical role (intake answer 2) | Off-handbook role: Martech Content Specialist |
| 12 | Cultural Hacking Lead · Lead · LATAM - Mexico | n/a | n/a | Jan 27 | no: practice role (Globant `Lead`) | none |

## Inconsistencies found

1. The SOW sheet lists lower seniorities than the Labor Estimate: AEM Backend Developer Sr 3 → "Sr Level 2", Mid Level → "Sr"; Web UI Developer Sr → "Sr Level 2", Mid Level → "Sr"; Tech Project Manager Manager → "Sr". Levels follow the Labor Estimate (intake answer 3).
2. The SOW's Partner Web rows for Content Specialist and Cultural Hacking Lead are shifted: "1.0 Cultural Hacking Lead" sits against "Content Specialist 0.5", and the Cultural Hacking row has no left-hand label.
3. The Content Resolution API workstream has SOW lines (Tech Project Manager, AEM Backend Developer "Sr Level 2" and "Sr", AEM QC Analyst) but no Labor Estimate lines. Intake answer 6 assigns it to the backend people; the SOW's QC line on the API has no answer and no JD of its own.
4. The Tech Director is "LATAM*" in the SOW and "EU - Spain" in the Labor Estimate.
5. The P&L runs 12 months (Nov 2026 → Oct 2027); the deck's timeline ends in Sep 2027.
6. Role labels in the P&L name AEM (AEM Backend Developer, AEM QC Analyst) while the Proposal's target platform is Contentful with a Next.js front end; AEM is the migration's source.

## Intake answers

1. Which P&L lines get a JD? **Answer:** only the six technical lines, 4–9. Lines 1–3 are already assigned or are structure.
2. Do the Martech Content Specialist lines (10, 11) get a JD? **Answer:** no. A P&L lists the whole team, and intake keeps only DXP technical roles. The proposed content-specialist Requirements were not confirmed and reach no file.
3. Which sheet sets the seniority when the SOW and the Labor Estimate disagree? **Answer:** the Labor Estimate.
4. Which level equivalence applies? **Answer:** Mid Level → L5 (4 years), Sr → L6 (5), Sr Level 2 → L7 (6), Sr 3 → L8 (Tech Lead I / II, 7+ / 10+). "Lead" and the old Experience Senior I / II stay unmapped.
5. Where do the platform Requirements come from? **Answer:** from the technology the Proposal defines, Contentful; "AEM Backend Developer" is only today's catalog name.
6. Does the Content Resolution API need its own Positions? **Answer:** no. The same backend people staff it, so its needs (SFMC, Contentful App) become requirements of the backend JDs.
7. Does allocation enter the JD? **Answer:** no; a JD sources a profile.
8. Which English level applies? **Answer:** B2 minimum for everyone; B1 possible as an exception for roles that do not face the client. No exception was granted for these six Positions.
9. Line 4 (AEM Backend Developer, Sr 3): does the person lead people, and which HR job description sets the years? **Answer:** yes, Tech Leader (L8); years from Tech Lead I (7+).
10. The handbook's Contentful backend platform includes a search integration (Algolia or Elasticsearch), which the Proposal does not use: keep it? **Answer:** Nice to have.
11. Where and how do the Positions work? **Answer:** remote, open to all of LATAM. Starts follow the Labor Estimate.
12. Is SFMC integration experience a Must have or a Nice to have in the backend JDs (Tech Leader L8 and Backend Developer L5)? **Open:** no tier given yet. Waiting on it: the SFMC Requirement, its screening point and its responsibility line in `tech-leader-l8-contentful/jd.md` and `backend-developer-l5-contentful/jd.md`. Neither JD mentions SFMC until the answer.
