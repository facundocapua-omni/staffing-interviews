Leí la Propuesta (deck de 54 slides) y el P&L (hojas Labor Estimate y SOW), más el handbook y las Descripciones de cargo. **No pude copiar los inputs** a `opportunities/expedia-contentful-migration/`. Los nombres de archivo tienen corchetes y el control de permisos los toma como un patrón glob, así que bloqueó el `cp`. La carpeta todavía no existe y los originales siguen intactos en `inbox/`. Cuando contestes, apruebo el `cp` (o copialos vos) y los guardo junto con los artefactos.

## Análisis de intake: Expedia · migración de AEM a Contentful

**Contexto**
- **Cliente:** Expedia Group, externo. Se vende desde Globant Salesforce Studio.
- **Workstreams:**
  - **Partner Web** (12 meses, T&M): migrar 4 sitios (unos 102.600 assets) de AEM a Contentful, con front nuevo en Next.js.
  - **Content Resolution API** (8 semanas): una app de Contentful que resuelve variantes por locale, tono y canal, con integración a SFMC y NBA.
- **Fechas:** Mes 1 = nov 2026 y fin en oct 2027, según la facturación de la SOW. El timeline del deck termina en sep 2027.
- **Stack que define la Propuesta:**
  - Contentful: content model, environments, workflows, Live Preview y App Framework para las editor apps y el workflow por locale.
  - Front: Next.js App Router + Tailwind sobre OpenNext en AWS (Lambda, S3, DynamoDB, SQS, CloudFront), con componentes EGDS (design system de EG).
  - Edge y CI/CD: Akamai + CGP; IaC con SST, Terraform o CDK; GitHub Actions; Datadog y CloudWatch; Lighthouse en el pipeline.
  - Migración: pipeline scriptado extract → transform → load idempotente.
- **Ubicaciones:** Colombia en casi todas las líneas, México en la del Architect.

**Líneas del P&L → Posiciones** (seniority sale del Labor Estimate; plataforma, de la Propuesta)

| # | Línea del P&L | Posición propuesta | HC | Inicio | JD |
|---|---|---|---|---|---|
| 1 | Tech Project Manager · Manager · Perú | — | 1 | nov 26 | no: ya asignada a Anthony Ramirez |
| 2 | Tech Director · Director · España | — | 1 | nov 26 | no: governance |
| 3 | Client Engagement Director · USA | — | 1 | nov 26 | no: structure, no billable |
| 4 | AEM Backend Dev · **Sr 3** · "Architect" · México | **espera preguntas 2–3** · Contentful | 1 | ene 27 | pendiente |
| 5 | AEM Backend Dev · Mid Level · Colombia | Backend Developer · L5 · Contentful | 1 | feb 27 | sí |
| 6 | Web UI Dev · Sr · Colombia | Frontend Developer · L6 · Contentful | 1 | ene 27 | sí |
| 7 | Web UI Dev · Mid Level · Colombia | Frontend Developer · L5 · Contentful | 1 | feb 27 | sí |
| 8 | AEM QC Analyst · Sr · Colombia | QA Engineer · L6 · Contentful | 1 | abr 27 | sí |
| 9 | DevOps Engineer · Sr · Colombia | DevOps Engineer · L6 · Contentful (AWS) | 1 | ene 27 | sí |
| 10–11 | Martech Content Specialist · Sr · Colombia (2 líneas) | Off-handbook role: Content Specialist | 2 | nov 26 / abr 27 | espera pregunta 5 |
| 12 | Cultural Hacking Lead · Lead · México | — | 1 | ene 27 | no: rol de práctica (`Lead`) |

En todos los JDs, la familiaridad con AEM entra como Nice to have, por ser la plataforma de origen.

**Inconsistencias encontradas**
1. **La SOW y el Labor Estimate no coinciden en seniority:**
   - Architect: Sr Level 2 en la SOW, Sr 3 en el LE.
   - "AEM Backend Developer": Sr en la SOW, Mid Level en el LE.
   - Web UI: "Sr Level 2" y "Sr" en la SOW, contra Sr y Mid Level en el LE.

   Uso el LE; las diferencias quedan como flag en `opportunity.md`.
2. **La Content Resolution API no está en el Labor Estimate.** Solo aparece en la SOW: TPM, AEM Backend Sr Level 2, AEM Backend Sr y AEM QC. Además, la SOW la factura en ago–sep 2027, mientras el deck dice "8 semanas desde el kick-off" con integración el 1 de noviembre.
3. **Los nombres de rol del P&L no coinciden con la plataforma.** "AEM Backend Developer" y "AEM QC Analyst" chocan con la Propuesta, que es Contentful + Next.js. Tomo la plataforma de la Propuesta.
4. **La fila 20 de la SOW está corrida:** pone "Cultural Hacking Lead" a la izquierda y "Content Specialist" a la derecha. Además, el Tech Director figura como LATAM* en una columna y Europe* en la otra.

## Preguntas

1. **Content Resolution API:** ¿la staffea la misma gente de Partner Web? Si es así, sumo sus necesidades (Contentful App Framework, integración con SFMC y NBA, trazabilidad) a los JDs de Backend y QA. Si no, ¿son Posiciones aparte, con qué seniority (la del LE no existe) y desde cuándo?
2. **Línea 4 (Sr 3, Client's Role Name "Architect"):** ¿es una Posición de **Expert** o de **Tech Leader**?
   - **Expert:** Software Architect, 11 años; lleva el flag "Expert is a regional role in the handbook".
   - **Tech Leader:** L8.
3. **Línea 4:** ¿esta persona lidera gente?
   - Si es Tech Leader: ¿los años salen de **Tech Lead I (7+)** o de **Tech Lead II (10+)**?
   - Si no lidera ni es Expert, queda como L7 IC con el flag "priced as Sr 3, IC Position mapped to L7". En ese caso: ¿**Experience Senior I (7)** o **II (8)**?
4. **Ubicación:** el P&L dice Colombia y México. ¿Busco solo en ese país o en LATAM, y en remoto?
5. **Content Specialist (off-handbook):** ¿lleva JD? Es más autoría y migración de contenido que desarrollo. Si sí, el handbook no lo cubre, así que propongo estos Requisitos para que confirmes la redacción y el tier:
   - `Proposed:` Hands-on content authoring and publishing in a headless CMS (Contentful preferred) — **Must have**
   - `Proposed:` Content migration QA: validating migrated entries, links, locales and assets against the source — **Must have**
   - `Proposed:` Multilingual content operations (locales, fallback, translation workflows) — **Must have**
   - `Proposed:` Working knowledge of AEM authoring (Sites, Assets, Content Fragments) — **Nice to have**
   - `Proposed:` SEO basics for content (metadata, redirects, hreflang) — **Nice to have**
6. **Inglés:** queda B2 para todas las Posiciones. ¿Alguna no tiene contacto con el cliente y querés bajarla a B1?

Los JDs y `opportunity.md` los escribo apenas me contestes. Lo que quede sin respuesta va a `opportunity.md` como pregunta abierta.