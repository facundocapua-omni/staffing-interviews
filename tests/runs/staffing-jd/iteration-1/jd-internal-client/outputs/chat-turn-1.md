No pude escribir nada todavía: no existe un árbol de staffing (no encontré `opportunities/` ni `people/` en esta carpeta ni en `leadership/staffing/`) y faltan definiciones que no puedo resolver solo. Te paso el análisis y una ronda de preguntas. Con tus respuestas escribo `opportunity.md` y el `jd.md`.

## Análisis

**Contexto**
- **Cliente:** Omni.pro, interno: es la propia unidad Digital Experience Platforms. Por ser interno, el JD no se anonimiza.
- **Material:** solo la descripción de cargo que me pasaste, sin Propuesta ni P&L. La tomo como JD provisto por vos. Tiene el mismo contenido que la copia de HR (`hr-job-descriptions/dxp-technology-director.md`).
- **Qué tomo del JD provisto:** conocimientos, años y responsabilidades. Quedan afuera los KPIs, la autoridad, la línea de reporte, los informes y las herramientas.
- **Ubicación:** remoto, con presencia en la sucursal de la ciudad que corresponda cuando haga falta. No dice país.

**Posiciones**

| # | Línea | Posición | Headcount | Inicio | JD | Flags |
|---|---|---|---|---|---|---|
| 1 | sin P&L | Tech Director · Director · ¿plataforma? | ¿1? | ? | pendiente | pendiente según pregunta 3 |

**Inconsistencias**
1. **El alcance del rol no coincide con el handbook.** En el handbook, el Tech Director (`roles/regional-director.md`) es un rol estratégico: gestiona a Tech Managers y al Expert y define estrategia y gobernanza. El JD provisto, en cambio, describe un rol muy hands-on: escribir y enseñar código, manejar Pull Requests, seguir las horas del equipo, estimar y supervisar integraciones de pagos.
2. **La plataforma no coincide con la unidad.** El JD provisto asume Adobe Commerce (buenas prácticas, flujos core, PCI). La unidad DXP del handbook también cubre AEM (tradicional y EDS), Contentful y Optimizely.
3. **La línea de reporte no coincide.** El JD provisto reporta al DPX Business Unit Director. El Tech Director del handbook reporta al Global Tech Director. Esto no entra en el JD, pero pesa en la pregunta 3.

Los años (13) y el inglés (B2) no chocan con la base.

## Preguntas

1. **Carpeta de trabajo.** ¿Creo `opportunities/` y `people/` en `…/tests/runs/staffing-jd/iteration-1/jd-internal-client/sandbox`, que es esta carpeta?
2. **Nombre de la Oportunidad.** Propongo `omnipro-dxp-unit`, con cliente Omni.pro (interno). ¿Te sirve, o preferís otro nombre de proyecto?
3. **Rol del handbook.** ¿Es **Tech Director** (regional, gestiona Tech Managers y Expert) o **Global Tech Director** (`roles/director.md`)? Mi recomendación es Tech Director. En `level-equivalence.md` el nivel es "Director", con 13 años: ¿lo confirmás?
4. **Alcance (inconsistencia 1).** ¿Qué perfil querés?
   - (a) El del JD provisto completo, hands-on incluido: Must haves del handbook más las responsabilidades del JD.
   - (b) Solo la parte estratégica y de gestión: dejo afuera escribir código, Pull Requests y seguimiento de horas.
   - (c) Una mezcla: decime qué queda.
5. **Plataforma (inconsistencia 2).** ¿Adobe Commerce es Must have, o el rol cubre toda la unidad? Si cubre toda la unidad, ¿qué plataformas van como Must have y cuáles como Nice to have (Adobe Commerce PaaS/SaaS, AEM tradicional, AEM EDS, Contentful, Optimizely)?
6. **Lista técnica del JD provisto.** El JD marca como requeridos Java, Python, Node.js, .NET, React y Angular; AWS, GCP y Azure con Kubernetes y Terraform; ISO 27001, OWASP y Zero Trust; SQL, NoSQL y Big Data; Scrum, SAFe y Kanban; New Relic, Prometheus y Grafana. ¿Cómo lo escribo?
   - (a) Todo como Must have, al pie de la letra.
   - (b) Cada grupo como Must have, con las tecnologías como ejemplos ("experiencia en al menos un cloud: AWS, GCP o Azure").
   - (c) Algunos grupos pasan a Nice to have: decime cuáles.
7. **Certificación.** El JD pide "al menos una certificación del plan de formación de la unidad DXP". ¿Es Must have para contratar, o es una obligación una vez que la persona entra (y entonces queda fuera del JD)?
8. **Logística.** ¿Headcount 1? ¿Fecha de inicio? ¿País o región donde se busca, y qué sucursal o ciudad para la presencia ocasional?

Después de escribir, te pregunto si querés exportar el JD a PDF.