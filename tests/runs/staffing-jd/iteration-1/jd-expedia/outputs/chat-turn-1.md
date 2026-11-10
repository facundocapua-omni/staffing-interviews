Inputs leídos (Propuesta de 53 slides, P&L con Labor Estimate y SOW), más el handbook (roles, career paths, Contentful) y `level-equivalence.md`. Todavía no escribí nada: no hay árbol de staffing en el sandbox, así que necesito tu OK antes de crearlo (pregunta 0).

## Análisis de intake: Expedia · Migración de AEM a Contentful

**Contexto**
- **Cliente:** Expedia Group. Es un cliente externo y lo vende el Salesforce Studio.
- **Proyecto:** migrar 4 sitios partner (partner.expediagroup.com, host.vrbo.com, escapia.com, expediagroup.com) y ~102.600 ítems de AEM a Contentful. Se hace con un front nuevo en Next.js sobre OpenNext en el AWS de Expedia, con Akamai como edge.
- **Workstreams:**
  - **Web:** 12 meses, T&M.
  - **Content Resolution API:** 2 meses. Es una app de Contentful con integración a SFMC y a NBA.
- **Fechas:** Month 1 = Nov 2026 hasta Oct 2027. Firma prevista el 31 de octubre y equipo integrado el 1 de noviembre.
- **Stack por capa:**
  - **Contentful:** content model, live preview, App Framework (workflow custom, editor apps).
  - **Front:** Next.js App Router, Tailwind, ISR/SSR, el design system de Expedia, paridad de SEO y analytics, Lighthouse en el CI.
  - **Infra:** AWS (Lambda, S3, DynamoDB, SQS, CloudFront), IaC (SST, Terraform o CDK), Akamai, GitHub Actions, Datadog y CloudWatch.
  - **Migración:** pipeline scripted e idempotente desde AEM, con validación y visual diff.

**Líneas del P&L → Posiciones**

| # | Línea del Labor Estimate | Posición | HC | Inicio | JD |
|---|---|---|---|---|---|
| 1 | Tech Project Manager · Manager · Perú | — | — | — | No: ya asignado (Anthony Ramirez) |
| 2 | Tech Director · Director · España | — | — | — | No: línea de governance |
| 3 | Client Engagement Director · USA | — | — | — | No: línea de estructura, non-billable |
| 4 | AEM Backend Developer · **Sr 3** · México | Backend Developer · L7 o Tech Leader L8 · Contentful | 1 | Ene 27 | Espera la pregunta 1 |
| 5 | AEM Backend Developer · Mid Level · Colombia | Backend Developer · L5 · Contentful | 1 | Feb 27 | Sí |
| 6 | Web UI Developer · Sr · Colombia | Frontend Developer · L6 · Contentful | 1 | Ene 27 | Sí |
| 7 | Web UI Developer · Mid Level · Colombia | Frontend Developer · L5 · Contentful | 1 | Feb 27 | Sí |
| 8 | AEM QC Analyst · Sr · Colombia | QA Engineer · L6 · Contentful | 1 | Abr 27 | Sí |
| 9 | DevOps Engineer · Sr · Colombia | DevOps Engineer · L6 · Contentful sobre AWS | 1 | Ene 27 | Sí |
| 10–11 | Martech Content Specialist · Sr · Colombia (×2) | Rol fuera del handbook | 2 | Nov 26 / Abr 27 | Espera la pregunta 2 |
| 12 | Cultural Hacking Lead · Lead · México | — | — | — | No: rol de práctica |

**Inconsistencias**
1. **El SOW y el Labor Estimate no coinciden en seniority:**
   - Backend: Sr 3 en el Labor Estimate, "Sr Level 2" en el SOW.
   - Backend: Mid en el Labor Estimate, "Sr" en el SOW.
   - Web UI: Sr en el Labor Estimate, "Sr Level 2" en el SOW.
   - Web UI: Mid en el Labor Estimate, "Sr" en el SOW.
2. **El workstream Content Resolution API está en el SOW y en la Propuesta, pero no tiene líneas en el Labor Estimate.** El SOW pone TPM, Backend Sr L2, Backend Sr y QC Sr. La Propuesta además nombra "Marketing Cloud Architect / Developer" en el slide del POD.
3. **Las etiquetas del P&L no coinciden con la plataforma de la Propuesta.** "AEM Backend Developer" y "AEM QC Analyst" quedan en Contentful / Next.js / AWS según la Propuesta, y AEM entra como Nice to have porque es la plataforma de origen.
4. **El timeline pone el platform setup (Contentful, AWS, edge) en Nov–Dic 2026, pero ninguna línea técnica arranca antes de Month 3 (Ene 2027).**
5. **En el SOW, la línea Cultural Hacking Lead aparece del lado cliente como "Content Specialist".** No cambia nada porque igual no lleva JD.

## Preguntas

0. No encontré `opportunities/` ni `people/`. ¿Creo el árbol en `…/jd-expedia/sandbox/`, con la Oportunidad como `opportunities/expedia-contentful-migration/`?
1. **Backend Sr 3 (México):**
   - ¿Lidera personas?
   - Si lidera, queda Tech Leader L8. ¿Los años salen de Tech Lead I (7+) o de Tech Lead II (10+)?
   - Si no lidera, queda Backend L7 y la marco "priced as Sr 3, IC Position mapped to L7". ¿Los años salen de Experience Senior I (7) o de Experience Senior II (8)?
2. **Martech Content Specialist (×2):** el rol no está en el handbook.
   - ¿Lleva JD?
   - Si lleva, ¿confirmás estos Requisitos tal cual, o los cambiás?
     - a. `Proposed: Hands-on authoring and publishing in Contentful: entries, references, locales and scheduled publishing.` → Must have
     - b. `Proposed: Content migration between CMSs: inventory, migrate / rebuild / retire decisions, page rebuilds and link clean-up.` → Must have
     - c. `Proposed: Multilingual content operations: locales, fallback and hand-offs to a translation workflow.` → Must have
     - d. `Proposed: Content QA against a source site: counts, required fields, broken links and visual comparison.` → Must have
     - e. `Proposed: Writing authoring guides and training content authors.` → Nice to have
3. **Content Resolution API:** ¿lo cubren las mismas personas del Web, y entonces sumo sus necesidades a los JDs de Backend y QA (Contentful App Framework, SFMC)? ¿O son Posiciones aparte? Si son aparte, ¿con qué nivel y desde qué fecha?
4. ¿Confirmás que la seniority sale del Labor Estimate y no del SOW (inconsistencia 1)? La diferencia queda marcada solo en `opportunity.md`.
5. ¿Los inicios del Labor Estimate están bien (Backend, Frontend y DevOps en Ene 2027), o se adelantan para el platform setup de Nov–Dic?
6. El handbook pide integración de búsqueda (Algolia o Elasticsearch) como Requisito de plataforma del Backend en Contentful, pero la Propuesta no tiene búsqueda en el alcance. ¿La dejo como Must have, la paso a Nice to have o la saco?
7. **Ubicación:** ¿cada Posición es remota desde el país del P&L (México o Colombia) o está abierta a LATAM?

Quedo esperando las respuestas para escribir `opportunity.md` y los JDs.