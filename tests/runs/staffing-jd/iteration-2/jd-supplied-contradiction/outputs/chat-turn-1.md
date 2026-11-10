Leí el JD que pasaste, la copia de RR. HH. del mismo cargo y los roles de liderazgo del handbook. Antes de escribir hay preguntas abiertas, así que todavía no creé ningún archivo: ni `opportunity.md`, ni `jd.md`, ni la copia del input en `opportunities/`.

## Análisis de intake

**Contexto**
- **Cliente:** interno, la propia unidad Digital Experience Platforms. El JD se anonimiza solo si el cliente es externo, así que acá no hace falta.
- **Proyecto:** cubrir el cargo DXP Technology Director. Según el documento reporta al DPX Business Unit Director e indirectamente al CEO.
- **Sin Propuesta ni P&L:** la fuente es solo el JD que pasaste. El nivel sale de la fila "Director" de `level-equivalence.md`.
- **Señales de stack:** casi todo es Adobe Commerce: buenas prácticas de Adobe Commerce, sus flujos core, pasarelas de pago y PCI. Además hay una lista amplia de lenguajes, nubes, seguridad y observabilidad.
- **Ubicación:** trabajo remoto para todas las sedes, con presencia en la sede de la ciudad cuando haga falta. No dice país.

**Posiciones**

| # | Línea | Posición | Headcount | Inicio | JD | Flags |
|---|---|---|---|---|---|---|
| 1 | ninguna (sin P&L) | Tech Director o Global Tech Director (pregunta 4) · Director · plataforma por definir (pregunta 5) | abierto | abierto | espera la ronda | Las competencias del nivel Director no están en el handbook; se toman de la descripción de cargo de RR. HH. `dxp-technology-director.md` |

**Base:**
- **Requisitos excluyentes del rol:** salen del `### Must have` del handbook. Son seis competencias de liderazgo: estrategia técnica, diseño de organización, influencia transversal, etc.
- **Años:** 13, según `level-equivalence.md`.
- **Inglés:** B2. Coinciden la regla de la suite y tu JD.

**Inconsistencias encontradas**
1. **Años de experiencia.** Tu JD pide 8 y la base pide 13. Fuera de eso, tu JD tiene el mismo contenido que la copia de RR. HH.
2. **Nivel operativo vs. estratégico.** Tu JD pide trabajo de nivel operativo: escribir código, gestionar Pull Requests, seguir las horas estimadas del equipo, implementar en Adobe Commerce. El handbook ubica a los dos roles Director en la capa estratégica.
3. **Plataforma.** Tu JD se centra en Adobe Commerce, pero la unidad DXP también cubre AEM (Traditional y EDS) y Contentful.
4. **Certificación requerida.** Tu JD pide una certificación del plan de formación interno de la unidad. Un candidato externo no puede tenerla antes de entrar.

## Preguntas

1. **Nombre de la Oportunidad.** El documento no nombra a la empresa. ¿Uso `omnipro-dxp-technology-director`? Copio el JD a esa carpeta cuando confirmes.
2. **Origen del JD.** ¿Quién aportó este JD: vos, la unidad (el cliente) o Presales? Cada requisito lleva una etiqueta de origen y tiene que reflejar tu respuesta.
3. **Contradicción en años:**

   | Fuente | Años |
   |---|---|
   | Tu JD | 8 |
   | Base (`level-equivalence.md` / descripción de RR. HH.) | 13 |

   ¿Cuál va como requisito excluyente?
4. **Rol del handbook:**
   - **Tech Director:** alcance regional; reporta al Global Tech Director; gestiona Tech Managers y al Expert.
   - **Global Tech Director:** tope de la jerarquía técnica; gestiona a los Tech Directors.

   ¿A cuál corresponde la Posición?
5. **Plataforma:**
   - ¿Es solo Adobe Commerce (PaaS, SaaS o ambas), o toda la unidad DXP (AEM Traditional, AEM EDS, Contentful, Adobe Commerce)?
   - Si son varias, ¿necesita cada una o al menos una?
   - ¿Cuáles pasan a Plus?
6. **Responsabilidades operativas.** ¿Dejo en "What the person will do" las responsabilidades de nivel operativo (escribir código, PRs, seguir horas, implementar en Adobe Commerce, supervisar pasarelas de pago), o las saco por ser propias de un Tech Leader?
7. **Listas de tecnologías.** En los requisitos técnicos, ¿cada lista entre paréntesis es un ejemplo (alcanza con una) o se exige toda? Las listas son:
   - Java/Python/Node.js/.NET/React/Angular
   - AWS/GCP/Azure/Kubernetes/Terraform
   - ISO 27001/OWASP/Zero Trust
   - SQL/NoSQL/Big Data
   - New Relic/Prometheus/Grafana
8. **Certificación del plan de formación.** ¿Queda como requisito excluyente, como Plus, o fuera del JD (se cumple después de entrar)?
9. **Logística:**
   - ¿Headcount 1?
   - ¿Fecha de inicio?
   - ¿País o región de la Posición?
   - ¿Remoto con presencia ocasional, como dice tu JD?

Con tus respuestas escribo `opportunity.md` y el `jd.md`. Lo que quede sin respuesta figura como pregunta abierta en `opportunity.md` y no entra al JD.