---
opportunity: expedia-contentful-migration
updated: 2026-10-28
---

# Expedia: AEM to Contentful migration

## Context

- **Client:** Expedia Group (EG), sold through Globant's Salesforce Studio; external.
- **Project:** migrate EG's four partner websites and about 102,600 content items and assets from AEM to Contentful, with a new Next.js front end on EG's AWS account behind Akamai.
- **Workstreams:**
  - Partner Web Content: Contentful setup and custom development (live preview, custom workflow app, editor apps), the Next.js front end, CDN/environments/pipelines, the scripted content migration, training and hypercare. 12 months, staffed by the Labor Estimate team.
  - Content Resolution API: a Contentful app that resolves content variants by locale, tone and channel with fallback, pushes a Marketing Object to Salesforce Marketing Cloud, takes the NBA decision payload and logs one record per resolution. 8 weeks. Staffed by the same backend people (intake answer 6).
- **Dates:** Nov 2026 → Oct 2027; Month 1 = Nov 2026. Contract signing expected Oct 31, team integration Nov 1. Proposal timeline: platform setup Nov–Dec 2026, model frozen and scope sign-off in discovery, rollout host.vrbo.com → escapia.com → expediagroup.com → partner.expediagroup.com, AEM off after the last site at 100%.
- **Stack signals:**
  - Content platform: Contentful (content model of pages, sections and blocks; locales and fallback for 9, 19, 3 and 1 locales; environments; workflows and tasks; Contentful Personalization if the tier includes it; translation route still to decide: Babel Prime or a supported connector).
  - Contentful extensibility: App Framework apps for per-locale approval workflows and cross-entry checks; the Content Resolution API as a Contentful app.
  - Front end: Next.js (App Router) and Tailwind, deployed with OpenNext; ISR with on-demand revalidation from the publish webhook, SSR for private sections, Draft Mode preview on a separate domain with click-to-edit; component library on EGDS (generation 1 or 2 to confirm); SEO and analytics/consent parity; Lighthouse gate in the pipeline.
  - Infrastructure: EG's AWS account (Lambda, S3 page cache, DynamoDB tag cache, SQS revalidation queue, CloudFront or ALB or function URL as origin), IAM, networking, WAF; IaC with SST, Terraform or CDK; GitHub Actions or equivalent; Datadog and CloudWatch.
  - Edge: Akamai and Cloud Gate Proxy, routing by path and cohort, redirect map from the disposition log.
  - Migration: scripted, idempotent extract → transform → load → validate pipeline from AEM (counts, required fields, broken links, visual diff); waves at 20%, 50% and 100%.
  - Integrations: Salesforce Marketing Cloud, CRM/VMC, NBA, EG's log system.
- **Locations:** P&L lines in LATAM (Mexico, Colombia, Peru), Spain and USA. Every Position is remote, open to all of LATAM (intake answer 11).

## Sources read

- `[Globant - Expedia_TPA] SF Contentful Migration - October 2026 (1).pptx`: the Proposal. Read whole: scope, deliverables, target architecture, front-end options, timeline, Content Resolution API scope and timeline, POD slide. Case studies and methodology slides read for context only.
- `[TPA Expedia] Contentful Migration Proposal - Pricing Sheet V4 _AI PODs_.xlsx`: the P&L. Read `2.1 Labor Estimate` and `SOW`; the AI POD sheets are empty; rates, costs and margins skipped.
- Handbook: `roles/backend.md`, `roles/frontend.md`, `roles/devops.md`, `roles/qa.md`, `roles/developer.md`, `roles/leader.md`, `roles/index.md`, `career-paths/backend.md`, `career-paths/frontend.md`, `career-paths/devops.md`, `career-paths/qa.md`, `reference/career-levels.md`, `technologies/contentful.md`, `technologies/aem-traditional.md`.
- HR job descriptions: `technical-lead-i.md` (years only), `aem-backend-senior-i.md` and `backend-experience-senior-i.md` (checked; nothing taken: their technical content is AEM or Adobe Commerce). Years for the other levels from `level-equivalence.md`.

## P&L lines → Positions

| # | P&L line (role · seniority · location) | Position (handbook role · level · platform) | Headcount | Start | JD | Flags |
|---|---|---|---|---|---|---|
| 1 | Tech Project Manager · Manager · LATAM - Peru | n/a | 1 | Nov 26 | no: already assigned (Anthony Ramirez) | none |
| 2 | Tech Director · Director · EU - Spain | n/a | 1 | Nov 26 | no: governance line | none |
| 3 | Client Engagement Director · Director · NA - USA | n/a | 1 | Nov 26 | no: structure line (non-billable) | none |
| 4 | AEM Backend Developer · Sr 3 · LATAM - Mexico | Tech Leader · Senior Level 3 (L8) · Contentful | 1 | Jan 27 | `tech-leader-l8-contentful/jd.md` | SOW says "AEM Developer, Sr Level 2" |
| 5 | AEM Backend Developer · Mid Level · LATAM - Colombia | Backend Developer · Semi Senior Advanced (L5) · Contentful | 1 | Feb 27 | `backend-developer-l5-contentful/jd.md` | SOW says "AEM Backend Developer, Sr" |
| 6 | Web UI Developer · Sr · LATAM - Colombia | Frontend Developer · Senior Level 1 (L6) · Contentful | 1 | Jan 27 | `frontend-developer-l6-contentful/jd.md` | SOW says "Web UI Developer, Sr Level 2" |
| 7 | Web UI Developer · Mid Level · LATAM - Colombia | Frontend Developer · Semi Senior Advanced (L5) · Contentful | 1 | Feb 27 | `frontend-developer-l5-contentful/jd.md` | SOW says "Web UI Developer, Sr" |
| 8 | AEM QC Analyst · Sr · LATAM - Colombia | QA Engineer · Senior Level 1 (L6) · Contentful | 1 | Apr 27 | `qa-engineer-l6-contentful/jd.md` | none |
| 9 | DevOps Engineer · Sr · LATAM - Colombia | DevOps Engineer · Senior Level 1 (L6) · Contentful | 1 | Jan 27 | `devops-engineer-l6-contentful/jd.md` | none |
| 10 | Martech Content Specialist · Sr · LATAM - Colombia | n/a | 1 | Nov 26 | no: not a DXP technical role (intake answer 2) | Off-handbook role: Martech Content Specialist |
| 11 | Martech Content Specialist · Sr · LATAM - Colombia | n/a | 1 | Apr 27 | no: not a DXP technical role (intake answer 2) | Off-handbook role: Martech Content Specialist |
| 12 | Cultural Hacking Lead · Lead · LATAM - Mexico | n/a | 1 | Jan 27 | no: practice role | none |

## Inconsistencies found

1. Seniority differs between the Labor Estimate and the client-facing SOW sheet: line 4 is Sr 3 in the Labor Estimate and "AEM Developer, Sr Level 2" in the SOW; line 5 is Mid Level vs "Sr"; line 6 is Sr vs "Sr Level 2"; line 7 is Mid Level vs "Sr". The Labor Estimate rules (intake answer 3).
2. The Content Resolution API workstream is in the Proposal and the SOW (Tech Project Manager, AEM Backend Developer Sr Level 2, AEM Backend Developer Sr, AEM QC Analyst Sr) but has no lines in the Labor Estimate. The Proposal's POD slide also names a Marketing Cloud Architect and a Marketing Cloud Developer that no sheet prices. Resolved: the same backend people staff it (intake answer 6).
3. P&L role labels name AEM ("AEM Backend Developer", "AEM QC Analyst") while the Proposal's target platform is Contentful with a Next.js front end on AWS. The JDs follow the Proposal; AEM enters as a Nice to have, as the migration's source (intake answer 5).
4. The Proposal's timeline puts platform setup (Contentful, AWS, edge) in Nov–Dec 2026, but no technical line in the Labor Estimate starts before Month 3 (Jan 2027). Open: see intake answer 12.
5. On the SOW sheet, the Cultural Hacking Lead line maps to "Content Specialist" in the client-facing columns. No effect: line 12 gets no JD.

## Intake answers

1. Which P&L lines get a JD? **Answer:** only the six technical lines (4–9); lines 1–3 are already assigned or are structure.
2. Do the Martech Content Specialist lines (10, 11), off-handbook, get a JD? **Answer:** no. A P&L lists the whole team; intake keeps only DXP technical roles.
3. Which sheet sets seniority when the SOW and the Labor Estimate disagree? **Answer:** the Labor Estimate.
4. Which level equivalence applies? **Answer:** Mid Level → L5 Semi Senior Advanced, Semi Senior II, 4 years; Sr → L6 Senior Level 1, Senior I, 5 years; Sr Level 2 → L7 Senior Level 2, Senior II, 6 years; Sr 3 → L8 Senior Level 3, Tech Lead I / II, 7+ / 10+ years. "Lead" and Experience Senior I / II (7 / 8 years) stay unmapped.
5. Do the AEM role labels set the platform? **Answer:** no. The platform is the technology the Proposal defines (Contentful); the Globant label is only today's catalog name.
6. Who staffs the Content Resolution API workstream? **Answer:** the same backend people; its needs (SFMC, Contentful App) become Requirements of the backend JDs (lines 4 and 5).
7. Does allocation enter the JD? **Answer:** no; a JD sources a profile.
8. Which English level applies? **Answer:** B2 minimum for every Position; B1 possible as an exception for a role that does not face the client. No exception was granted for these six Positions.
9. Does line 4 (AEM Backend Developer, Sr 3) lead people, and which HR job description sets its years? **Answer:** yes, it leads people: Tech Leader (L8). Years from Tech Lead I (7+).
10. The handbook's Contentful backend lists a search integration (Algolia or Elasticsearch), and the Proposal has no search in scope: which tier? **Answer:** Nice to have.
11. Where is each Position located? **Answer:** remote, open to all of LATAM.
12. Are the Labor Estimate's starts right (lines 4, 6 and 9 in Jan 2027), or do they move earlier for the platform setup in Nov–Dec 2026? **Open:** no answer yet. Waiting on it: the Start in the Logistics of `tech-leader-l8-contentful`, `frontend-developer-l6-contentful` and `devops-engineer-l6-contentful`, which follow the Labor Estimate until it is answered.
