> **PROTOTYPE, throwaway.** Step 1 of a hypothetical JD skill: the intake analysis it would write after reading a proposal deck and a P&L, before asking questions and writing JDs. Ticket: [JD structure](../../issues/04-jd-structure.md). Costs, rates and margins are deliberately ignored.

# Opportunity intake: Expedia Group, AEM → Contentful migration

**Sources read**
- Proposal deck: 55 slides. Read the scope, solution, timeline and team slides; skipped the commercials and appendix.
- P&L: sheets `2.1 Labor Estimate` (the internal staff plan) and `SOW` (the client-facing team).
- Handbook: `martech/structure`, the roles and career levels.
- Old JD base: `Downloads/ENGINEERING`, which provides years of experience and English level per old level.

## Opportunity context (draft for `opportunity.md`)

- **Client**: Expedia Group, sold through Globant.
- **Project**: migrate partner web from AEM to Contentful.
- **Workstreams**
  - **Partner Web.** Migrate 4 sites (partner.expediagroup.com, host.vrbo.com, escapia.com, expediagroup.com): ~102.6k items, 9/19/3/1 locales. The new front end is Next.js on OpenNext in EG's AWS account, with Akamai routing traffic during the migration. Runs **Nov 2026 → Sep 2027**, through milestones M1 Platform ready … M7 AEM off.
  - **Content Resolution API.** A Contentful App that resolves content variants by locale, tone and channel for SFMC email sends, from an NBA payload. It takes **8 weeks**; the SOW bills it in **Aug–Sep 2027**.
- **Stack signals**
  - **Contentful**: content model, environments, locales and fallback, workflows, editor apps, live preview, Personalization.
  - **Front end**: Next.js App Router, Tailwind, EGDS React components, ISR/SSR.
  - **AWS**: Lambda, S3, DynamoDB, SQS, CloudFront, with IaC in SST, Terraform or CDK.
  - **Edge**: Akamai + Cloud Gate Proxy.
  - **Delivery and observability**: GitHub Actions, Datadog, CloudWatch.
  - **AEM, as the source**: extraction and the component disposition.
  - **Other**: SFMC, Figma.
- **Locations in the P&L**: LATAM (Colombia, Mexico, Peru), EU-Spain, USA.
- **P&L month mapping**: Month 1 = Nov 2026, Month 12 = Oct 2027.

## Lines in the P&L → proposed Posiciones

| # | P&L line (Globant role · seniority · location) | Proposed Posición (handbook role · level · platform) | Allocation by month (M1–M12) | Starts | JD? | Flags |
|---|---|---|---|---|---|---|
| 1 | Tech Project Manager · Manager · Peru | n/a (PM, not in the handbook) | 0.3 → 1.0 → 0.5 | Nov 26 | ✗ | A person is already named in the P&L |
| 2 | Tech Director · Director · Spain | Tech Director (`regional-director`) | 1.0 → 0.1 | Nov 26 | ✗ | Governance; probably already assigned |
| 3 | Client Engagement Director · Director · USA | n/a | 0.05–0.1, non-billable | Nov 26 | ✗ | Structure |
| 4 | AEM Backend Developer · **Sr 3** · Mexico | Backend Developer · Senior Level 3 (L8)? · Contentful | 1.0 in M3, then 0.5 | Jan 27 | ✓ | SOW says "Sr Level 2"; labelled AEM but the work is Contentful + AEM extraction; L8 is Tech Leader territory |
| 5 | AEM Backend Developer · **Mid Level** · Colombia | Backend Developer · Semi Senior Adv. (L5)? · Contentful | 1.0 M4–M9, 0.5 M10–M11 | Feb 27 | ✓ | SOW says "Sr" |
| 6 | Web UI Developer · **Sr** · Colombia | Frontend Developer · Senior Level 1 (L6)? · Contentful | 0.5 M3–M12 | Jan 27 | ✓ | SOW says "Sr Level 2"; half allocation for the whole project |
| 7 | Web UI Developer · **Mid Level** · Colombia | Frontend Developer · Semi Senior Adv. (L5)? · Contentful | 1.0 M4–M8 | Feb 27 | ✓ | SOW says "Sr"; 5 months only |
| 8 | AEM QC Analyst · Sr · Colombia | QA · Senior Level 1 (L6)? · Contentful | 1.0 M6–M12 | Apr 27 | ✓ | Labelled AEM; the work is migration QA + Next.js front end |
| 9 | DevOps Engineer · Sr · Colombia | DevOps Engineer · Senior Level 1 (L6)? · Contentful/AWS | 0.5 M3–M4 and M10–M12 | Jan 27 | ✓ | Gap in M5–M9 |
| 10 | Martech Content Specialist · Sr · Colombia (two lines) | n/a (no content/migration track in the handbook) | 1.0 M1–M10 + 0.5 M6–M9 | Nov 26 | ? | Off-handbook; one seat ramping up or two seats? |
| 11 | Cultural Hacking Lead · Lead · Mexico | n/a | 1.0 M3–M12 | Jan 27 | ? | Off-handbook; probably a Globant practice |
| API | SOW only: TPM 0.3, AEM Backend Sr Level 2 0.5, AEM Backend Sr 1.0, QC Sr 0.5 | Same seats as 4/5/8, or extra ones? | Aug–Sep 27 | Aug 27 | ? | Not in the Labor Estimate; needs SFMC + Contentful App skills |

## Inconsistencies the hiring lead must resolve

1. **Seniority**: the SOW (client-facing) labels lines 4–7 one step higher than the Labor Estimate (internal).
2. **Role names**: the Globant catalog says "AEM …" for lines whose target platform is Contentful.
3. **API team**: it appears only in the SOW, so it is unclear whether it means more seats or the same people extended.
4. **Level vocabulary**: the Globant scale (Mid Level, Sr, Sr Level 2, Sr 3, Lead), the old Omni scale (Junior I/II, Semi Senior I/II, Senior I/II, Experience Senior I/II) and the handbook's 8 levels need one mapping.

## Questions before writing the JDs: round 1 answers

1. **JDs**: only the 6 technical lines (4–9). Lines 1–3 are already assigned or are structure.
2. **Off-handbook lines** (10, 11) are out. A P&L lists the whole team, not only DXP, so intake keeps only DXP technical roles.
3. **Seniority source**: the Labor Estimate.
4. **Level equivalence** (only "Sr 3" was corrected):

   | Globant P&L | Handbook | Old Omni JD | Years (old JDs) |
   |---|---|---|---|
   | Mid Level | L5 Semi Senior Advanced | Semi Senior II | 4 |
   | Sr | L6 Senior Level 1 | Senior I | 5 |
   | Sr Level 2 | L7 Senior Level 2 | Senior II | 6 |
   | Sr 3 | L8 Senior Level 3 | Tech Lead I / II | 7+ / 10+ |

   Still unmapped: "Lead" and the old Experience Senior I/II (7/8 years).
5. **Platform**: the technology the proposal defines (Contentful). A Globant role label such as "AEM Backend Developer" is only the catalog name that is homologated today.
6. **API workstream**: the same backend people, so its needs (SFMC, Contentful App) become requirements of the backend JDs.
7. **Allocation** is irrelevant to the JD, which is about sourcing a profile.
8. **English**: B2 minimum for everyone; a B1 exception is possible for roles that do not face the client.

Next: [JD variants for line 6, Frontend Developer · Senior Level 1](PROTOTYPE-02-jd-variants.md).
