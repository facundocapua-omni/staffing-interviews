Leí la descripción de cargo, la copia congelada `hr-job-descriptions/dxp-technology-director.md` (tiene el mismo contenido que tu archivo), `level-equivalence.md` y estas páginas del handbook: `roles/director.md`, `roles/regional-director.md`, `roles/principles.md`, `reference/career-levels.md`, `orgchart/global.md` y `technologies/index.md`.

Todavía no escribí nada en el árbol. Tu archivo no nombra a la empresa (dice "LA EMPRESA"), así que copio el input a `opportunities/` cuando confirmes el slug (pregunta 1).

## Análisis de intake

**Contexto**
- **Cliente:** interno, nuestra propia unidad DXP (Digital Experience Platforms Business Unit). Como es interno, el JD no se anonimiza.
- **Proyecto:** cubrir la Posición de DXP Technology Director. No hay Propuesta ni P&L: la única fuente es la descripción de cargo.
- **Stack:** la descripción de cargo está escrita para Adobe Commerce (misión de e-commerce, "prácticas recomendadas por Adobe Commerce", pasarelas de pago, PCI). El handbook de la unidad cubre más plataformas: AEM Traditional, AEM EDS, Contentful, Adobe Commerce PaaS y Adobe Commerce SaaS.
- **Ubicación:** la descripción de cargo dice "asistencia remota a las sucursales" y "presencia en la sucursal de la ciudad correspondiente si es necesario". No nombra país.

**Posiciones**

| # | Línea | Posición (rol handbook · nivel · plataforma) | Headcount | Inicio | JD | Flags |
|---|---|---|---|---|---|---|
| 1 | ninguna (sin P&L) | Director · ? (ver pregunta 2) · plataformas DXP (ver pregunta 4) | abierto | abierto | depende de las preguntas 2–8 | ninguno |

**Base que aporta cada fuente**
- **Años:** 13 y **inglés:** B2. Coinciden la descripción de cargo y `level-equivalence.md`, así que no hay contradicción.
- **Must have del rol en el handbook:** depende de la pregunta 2. Ninguno de los dos roles de director trae Nice to have ni career path definido.

**Inconsistencias encontradas**
1. **Capa del rol.** El handbook pone a los directores en la capa estratégica (horizonte de trimestres; "un Director que aprueba decisiones técnicas de un proyecto" figura como señal de alerta). La descripción de cargo, en cambio, incluye trabajo operativo:
   - "Escribir y enseñar código"
   - "Participar activamente en la creación de módulos"
   - "Implementar desarrollos según las prácticas de Adobe Commerce"
   - "Dar seguimiento a las horas estimadas", "manejo de Pull Requests"
2. **A quién gestiona.** Según la descripción de cargo, lidera directamente "al equipo de desarrollo". Según el handbook, el Global Tech Director gestiona Tech Directors y el Tech Director gestiona Tech Managers y al Expert.
3. **Plataforma.** La descripción de cargo es solo Adobe Commerce; la unidad DXP abarca también CMS (AEM y Contentful).

## Preguntas

1. **Slug de la Oportunidad.** Propongo `omnipro-dxp-technology-director` (cliente Omni.Pro, interno). ¿Lo confirmás o preferís otro?
2. **Rol del handbook.**
   - **Global Tech Director** (`director.md`): tope de la jerarquía técnica, gestiona Tech Directors. Must have: Technical strategy, Org design, Leadership, Cross-functional influence, Technology vision, Executive communication.
   - **Tech Director** (`regional-director.md`): alcance regional, gestiona Tech Managers + Expert. Must have: Regional technical leadership, Org design at regional scale, Coaching senior managers, Cross-functional influence, Technology strategy execution, Stakeholder communication.

   El reporte al "DPX Business Unit Director" y el alcance "nuestra unidad DXP" me hacen pensar en el primero, pero la decisión es tuya. ¿Cuál es?
3. **Quién supplied la descripción de cargo.** ¿La aportás vos como hiring lead para esta Posición? De eso depende la etiqueta de origen: `supplied JD` si la elegiste vos para la Posición, `HR job description` si se usa solo como base.
4. **Plataformas.** Elegí una de estas opciones:
   - (a) solo Adobe Commerce, como dice la descripción de cargo;
   - (b) toda la unidad DXP (AEM Traditional/EDS, Contentful, Adobe Commerce PaaS/SaaS), exigiendo **cada una** o **al menos una**;
   - (c) otra combinación.

   ¿Cuáles van a Must have y cuáles a Nice to have?
5. **Contradicción de capa (inconsistencias 1 y 2).** Compará los dos lados:
   - **Handbook:** rol estratégico, que gestiona líderes y no codea en proyectos.
   - **Descripción de cargo:** rol hands-on: escribe y enseña código, crea módulos, sigue horas y PRs, lidera devs directamente.

   ¿Qué entra al JD? ¿Las responsabilidades operativas quedan, se reformulan como "supervisa" o se sacan? ¿A quién gestiona la persona?
6. **Stack genérico de la descripción de cargo** (Java/Python/Node.js/.NET/React/Angular; AWS/GCP/Azure, Kubernetes, Terraform; ISO 27001/OWASP/Zero Trust; SQL/NoSQL/Big Data; Scrum/SAFe/Kanban; New Relic/Prometheus/Grafana). ¿Cada grupo es Must have con **al menos una** tecnología del grupo, hay que tenerlas **todas**, o algún grupo pasa a Nice to have?
7. **Certificación.** La descripción de cargo pide "al menos una certificación del plan de formación de la unidad DXP". ¿Es Must have al contratar (¿cuáles cuentan?) o una obligación después del ingreso, que entonces queda fuera del filtro?
8. **Logística.**
   - **Headcount:** ¿1?
   - **Inicio:** ¿cuándo?
   - **Ubicación:** ¿país o región?
   - **Modalidad:** ¿remoto, híbrido o presencial?

Cuando respondas, copio el input y escribo `opportunity.md` y el `jd.md`. Lo que quede sin respuesta se registra como pregunta abierta y no entra al JD.