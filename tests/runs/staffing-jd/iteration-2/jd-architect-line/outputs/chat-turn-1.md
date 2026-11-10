Te dejo el análisis de la Oportunidad y las preguntas de intake. No escribo ningún JD hasta tener tus respuestas.

**Pendiente de tu permiso:** el permiso me bloqueó el `cp`, así que la Propuesta y el P&L todavía no están en `opportunities/expedia-contentful-migration/`. Siguen solo en `inbox/` y no se movió nada. Cuando respondas, aprobá la copia o copialos vos.

## Análisis de intake: Expedia · Migración de AEM a Contentful

**Contexto**
- **Cliente:** Expedia Group, externo. Lo vende el Salesforce Studio de Globant.
- **Workstreams:**
  - **Partner Web:** 12 meses, USD 883k. Se migran 4 sitios (unos 102.600 assets) a Contentful, con un front nuevo en Next.js + OpenNext sobre el AWS de Expedia y Akamai como edge.
  - **Content Resolution API:** 8 semanas, USD 54,5k. Es una app de Contentful que integra con SFMC y NBA.
- **Fechas:** el Mes 1 del P&L es nov 2026 ("Team Integration Nov-1") y el proyecto termina en oct 2027.
- **Stack:**
  - Contentful: modelo, workflows, App Framework, Personalization.
  - Next.js (App Router), Tailwind y EGDS, desplegado con OpenNext en AWS (Lambda, S3, DynamoDB, SQS), con IaC en SST, Terraform o CDK.
  - Akamai, GitHub Actions, Datadog y CloudWatch.
  - Un pipeline de migración scripteado que lee de AEM.

**Líneas del Labor Estimate → Posiciones**

| # | Línea del P&L | Posición propuesta | Seats | Inicio | JD | Flags |
|---|---|---|---|---|---|---|
| 1 | Tech Project Manager · Manager · Perú | n/a | – | – | no: ya asignado a una persona | – |
| 2 | Tech Director · Director · España | n/a | – | – | no: gobierno | – |
| 3 | Client Engagement Director · USA | n/a | – | – | no: estructura | – |
| 4 | AEM Backend Developer · **Sr 3** · México, *Client's Role Name: "Architect"* | Expert o Tech Leader (o IC L7) · Contentful | 1 | ene 2027 | espera P1–P2 | SOW: "Sr Level 2" |
| 5 | AEM Backend Developer · Mid Level · Colombia | Backend Developer · L5 · Contentful | 1 | feb 2027 | sí | SOW: "Sr" |
| 6 | Web UI Developer · Sr · Colombia | Frontend Developer · L6 · Contentful | 1 | ene 2027 | sí | SOW: "Sr Level 2" |
| 7 | Web UI Developer · Mid Level · Colombia | Frontend Developer · L5 · Contentful | 1 | feb 2027 | sí | SOW: "Sr" |
| 8 | AEM QC Analyst · Sr · Colombia | QA Engineer · L6 · Contentful | 1 | abr 2027 | sí | – |
| 9 | DevOps Engineer · Sr · Colombia | DevOps Engineer · L6 · Contentful | 1 | ene 2027 | sí | – |
| 10–11 | Martech Content Specialist · Sr · Colombia (2 líneas) | Content Specialist · Sr | 2 | nov 2026 / abr 2027 | espera P6 | Off-handbook role |
| 12 | Cultural Hacking Lead · Lead · México | n/a | – | – | no: rol de práctica | – |

**Inconsistencias**
1. **Seniority distinta entre SOW y Labor Estimate** en las líneas 4, 5, 6 y 7. Tomo la del Labor Estimate y la diferencia queda como flag en `opportunity.md`, no en el JD.
2. **El workstream Content Resolution API no está en el Labor Estimate.** Sí aparece en el SOW (Backend Sr Level 2, Backend Sr, QC Sr y TPM) y en el deck, que lo cotiza por separado. El total del Labor Estimate coincide exactamente con el de Partner Web.
3. **Las etiquetas del P&L dicen "AEM"** ("AEM Backend Developer", "AEM QC Analyst"), pero la plataforma de la Propuesta es Contentful. AEM es la plataforma de origen de la migración.
4. **El SOW etiqueta mal al Cultural Hacking Lead:** a la izquierda lo pone como "Content Specialist Sr" y a la derecha aparece separado.
5. **La slide "Project POD" nombra roles que el P&L no tiene:** Marketing Cloud Architect y Marketing Cloud Developer.

## Preguntas

1. **Línea 4** (Sr 3, "Architect"): ¿la Posición es **Expert** (Software Architect, 11 años, sin reportes) o **Tech Leader**? El P&L no tiene otra línea de liderazgo técnico.
2. **Línea 4:** ¿la persona **lidera personas**?
   - Si es Tech Leader: ¿los años salen de **Tech Lead I (7+)** o de **Tech Lead II (10+)**?
   - Si no es Expert ni lidera personas, queda como IC L7: ¿**Experience Senior I (7)** o **II (8)**?
3. **Brechas SOW vs Labor Estimate** (inconsistencia 1): ¿confirmás que el Labor Estimate es la versión vigente?
4. **Content Resolution API:**
   - ¿Lo staffean las mismas personas de Partner Web? En ese caso sumo sus necesidades (app de Contentful, integración con SFMC y NBA, fallback y variantes) a los JDs de Backend y QA.
   - ¿O son Posiciones aparte? Si son aparte, necesito sus líneas en el Labor Estimate.
   - ¿Los roles de Marketing Cloud de la slide de POD aplican?
5. **Plataforma:** confirmo **Contentful** como plataforma de todos los JDs. La familiaridad con AEM entraría como Nice to have, por ser la plataforma de origen. ¿Ok?
6. **Content Specialists** (líneas 10–11, dos seats, rol que no está en el handbook): ¿llevan JD? Si llevan, confirmá o cambiá cada uno de estos Requirements:
   - **Must have:**
     - `Proposed: Hands-on content authoring and publishing in Contentful (entries, references, locales, scheduled publishing)`
     - `Proposed: Has migrated or rebuilt web pages from one CMS to another, including content inventory and migrate/rebuild/retire decisions`
     - `Proposed: Multilingual content operations: locales, fallback, and coordination with translators or native reviewers`
     - `Proposed: Content QA before publishing: required fields, broken links, and visual checks across breakpoints`
   - **Nice to have:**
     - `Proposed: Writing authoring guides or training authors`
     - `Proposed: SEO basics for content: titles, metadata, and redirects`
   - **Años:** no hay una HR job description para este rol. ¿Uso los 5 años que corresponden a "Sr"?
7. **Ubicación:** el Labor Estimate pone un país por línea (México o Colombia) y el SOW dice "LATAM*".
   - ¿La búsqueda se limita a ese país o se abre a LATAM?
   - ¿Es remoto?
8. **Inicios:** los saqué del primer mes con asignación en el P&L, tomando Mes 1 = nov 2026. ¿Te sirven así, o hay que correrlos según la firma del contrato (que el deck pone el 31 de octubre, con signo de pregunta)?