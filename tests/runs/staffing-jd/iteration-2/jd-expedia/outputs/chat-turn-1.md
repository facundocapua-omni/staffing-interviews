Copié la Propuesta y el P&L a `opportunities/expedia-contentful-migration/` (los originales siguen en `inbox/`). Te paso el análisis de intake y una ronda de preguntas. No escribo nada más hasta tener tus respuestas.

## Análisis de intake: Expedia · Migración de AEM a Contentful

**Contexto**
- **Cliente:** Expedia Group, externo. La venta es de Globant Salesforce Studio.
- **Workstreams:**
  - **Partner Web:** migrar 4 sitios de AEM a Contentful (unos 102.600 ítems), con front Next.js sobre OpenNext en AWS, Akamai, live preview, workflows custom y pipeline de migración. Son 12 meses, T&M.
  - **Content Resolution API:** una app de Contentful con variantes por locale, tono y canal, fallback, integración con SFMC y trazabilidad. Son 8 semanas.
- **Fechas:** el Mes 1 del P&L es nov 2026 y el Mes 12 es oct 2027. El timeline del deck termina en sep 2027.
- **Ubicaciones:** México y Colombia para los perfiles técnicos.

**Líneas del P&L → Posiciones**

| # | Línea del P&L (Labor Estimate) | Posición | HC | Inicio | JD |
|---|---|---|---|---|---|
| 1 | Tech Project Manager · Manager · Perú | — | — | — | No: ya está asignada a una persona |
| 2 | Tech Director · Director · España | — | — | — | No: es governance |
| 3 | Client Engagement Director · Director · USA | — | — | — | No: es estructura, no facturable |
| 4 | AEM Backend Developer · Sr 3 · México | Backend L8 Tech Leader, o L7 · Contentful | 1 | ene 2027 | Depende de la pregunta 3 |
| 5 | AEM Backend Developer · Mid Level · Colombia | Backend Developer · L5 · Contentful | 1 | feb 2027 | Sí |
| 6 | Web UI Developer · Sr · Colombia | Frontend Developer · L6 · Contentful | 1 | ene 2027 | Sí |
| 7 | Web UI Developer · Mid Level · Colombia | Frontend Developer · L5 · Contentful | 1 | feb 2027 | Sí |
| 8 | AEM QC Analyst · Sr · Colombia | QA Engineer · L6 · Contentful | 1 | abr 2027 | Sí |
| 9 | DevOps Engineer · Sr · Colombia | DevOps Engineer · L6 · Contentful (AWS) | 1 | ene 2027 | Sí |
| 10–11 | Martech Content Specialist · Sr · Colombia (×2) | Rol fuera del handbook | 2 | nov 2026 / abr 2027 | Depende de la pregunta 6 |
| 12 | Cultural Hacking Lead · Lead · México | — | — | — | No: es un rol de práctica |

En las líneas 4 a 8, la etiqueta "AEM" es solo el nombre de catálogo. La plataforma que define la Propuesta es Contentful + Next.js, así que los Requirements salen de ahí y AEM entra como Nice to have, por ser la plataforma de origen de la migración.

**Inconsistencias encontradas**

1. La hoja SOW baja la seniority de casi todas las líneas respecto del Labor Estimate:
   - Backend: Sr 3 → "Sr Level 2" y Mid → "Sr".
   - Web UI: Sr → "Sr Level 2" y Mid → "Sr".
   - TPM: Manager → "Sr".
   
   Para los niveles uso el Labor Estimate y la diferencia queda como flag.
2. En la SOW, las filas de Content Specialist y Cultural Hacking Lead están corridas: "1.0 Cultural Hacking Lead" aparece contra "Content Specialist 0.5".
3. El workstream **Content Resolution API** tiene líneas en la SOW pero ninguna en el Labor Estimate: Backend "Sr Level 2" y "Sr", QC y TPM, facturado entre ago y sep 2027.
4. El Tech Director figura en "LATAM*" en la SOW y en "EU - Spain" en el Labor Estimate.

## Preguntas

1. **Content Resolution API:** ¿la staffean las mismas personas de Partner Web (Backend y QA)? Si es así, sumo sus necesidades a esos JDs. ¿O la API necesita Posiciones propias?
2. **SFMC:** si se suma la API, ¿la experiencia integrando Salesforce Marketing Cloud va como Must have o como Nice to have en los Backend? ¿En cuáles: L5, Sr 3 o los dos?
3. **Línea 4 (Backend Sr 3):** ¿esta persona lidera al equipo? En el P&L no hay otro Tech Leader.
   - Si lidera: queda Tech Leader L8. ¿Los años salen de Tech Lead I (7+) o de Tech Lead II (10+)?
   - Si no lidera: queda Backend Developer L7, con el flag "priced as Sr 3, IC Position mapped to L7". ¿Los años salen de Experience Senior I (7) o de Experience Senior II (8)?
4. **Búsqueda:** el handbook incluye Algolia/Elasticsearch en la parte de plataforma del Backend Contentful, pero la Propuesta no tiene búsqueda. ¿Lo dejo afuera o va como Nice to have?
5. **Logística:** el P&L dice México y Colombia. ¿Las Posiciones son remotas dentro de cada país, híbridas o abiertas a LATAM? ¿Las fechas de inicio del P&L valen tal cual?
6. **Martech Content Specialist (×2):** es un rol que no está en el handbook (flag `Off-handbook role`). En el proyecto hace autoría y migración de contenido, disposition log y publicación. ¿Lleva JD?
   - Si lleva JD, son 1 Posición con 2 seats. Te propongo estos Requirements, con la redacción exacta con la que irían. Indicá Must o Nice en cada uno:
     - a. `Proposed: Hands-on content authoring and publishing in Contentful (entries, references, locales)`, Must have.
     - b. `Proposed: Content migration between CMSs: content inventory, migrate/rebuild/retire decisions and validation of migrated pages`, Must have.
     - c. `Proposed: Multilingual content publishing across several locales, with translation workflows`, Must have.
     - d. `Proposed: Familiarity with AEM authoring (Sites, Content Fragments)`, Nice to have.
     - e. `Proposed: SEO basics for content: metadata, redirects, canonical URLs`, Nice to have.
   - Si no lleva JD, decime el motivo para dejarlo registrado.

Con tus respuestas escribo `opportunity.md` y los JDs.