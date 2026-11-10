# Scorecard Técnico — José David Restrepo

**Entrevistador(a)**: Facundo Capua · **Fecha**: 2026-07-06

## Puntuaciones — Rúbrica de Liderazgo Técnico y Arquitectura

| Dimensión                             | Score (1-5) | Evidencia concreta observada |
| -------------------------------------- | :---------: | ----------------------------- |
| Visión Arquitectónica                  |      3      | Caso fuerte: frenó una propuesta de un consultor externo (reescribir en Python/microservicios) para un cuello de botella de sincronización de ~120k registros, y en su lugar diseñó una solución con cola de mensajes (RabbitMQ) manteniendo todo dentro del ecosistema Adobe/PHP — buen juicio para evitar sobre-ingeniería innecesaria. Pero al preguntarle por qué RabbitMQ y no un servicio cloud-native de colas, respondió *"porque era el que ya usaba"* — no hubo un análisis de trade-offs, solo familiaridad. Buen entendimiento conceptual de AEM (lo describe correctamente como plataforma de contenido headless-agnóstica, no un "CMS" tradicional), pero **gaps duros**: no supo nombrar AEMaaCS ("se me olvidó"), sin experiencia en migraciones a cloud, desconoce EDS. Sin ninguna mención de Kubernetes, Terraform, multi-cloud u observabilidad (New Relic/Prometheus/Grafana) pese a ser requisitos explícitos del JD. En ningún momento de la entrevista propuso una solución fuera del ecosistema Adobe. |
| Liderazgo y Mentoría de Equipo         |      3      | Dos ejemplos concretos y creíbles de coaching: (1) escaló formalmente a una desarrolladora técnicamente fuerte pero con fricción en trato con cliente/equipo, dándole feedback directo antes de escalar — la empresa ofreció apoyo psicológico, no se resolvió y la persona sigue en la empresa; (2) coacheó a un desarrollador introvertido con tácticas concretas (git hooks/linters, code reviews informales, tagging de reviewers, onboarding a IA) con resultado positivo (la persona mejoró y fue promovida a otro equipo). Ambos casos usan "yo" en primera persona con acciones específicas. Sin embargo, admite explícitamente que la evaluación de desempeño formal la manejaba un área de RRHH separada ("no era tanto como un par de carrera") y no ha tenido título de gestión formal (Manager/Director) en 13 años. El único episodio de autoridad real de gestión (Talos, decidir dar de baja a un contractor, negociar capacidad con PM) es de ~2017-2019, ad hoc por una licencia de un colega, no un rol asignado. |
| Gestión de Stakeholders y Delivery     |      3      | Manejo directo y sostenido de un cliente de alta exigencia (Coca-Cola vía CI&T): reuniones semanales de arquitectura con el arquitecto de Adobe, respuesta a incidentes fuera de horario, traducción de urgencia de negocio en respuesta técnica. En Talos, gestionó escalamiento de clientes en fin de semana y negociación de capacidad de horas con PM. Sin embargo, no hay evidencia de negociación a nivel ejecutivo/C-level, ni de traducir riesgo técnico a términos de impacto de negocio ($/riesgo) en ninguna respuesta — se queda en el nivel operativo cliente/PM, un escalón por debajo de lo que exige interactuar con un BU Director. |
| Gobierno Cloud/DevOps/Seguridad        |      3      | Seguridad aplicada sólida y concreta: manejo de idempotencia para evitar duplicados en reintentos de App Builder, conciencia de PCI compliance, protección ante fuerza bruta/DoS por rate-limiting, hardening de URLs y endpoints con tokens/OAuth. Buena profundidad real, no genérica. En infraestructura, la migración de Adobe Commerce Cloud a on-prem fue una decisión válida pero **reactiva** (motivada por quejas de facturación y soporte, no por una estrategia de gobierno de infraestructura), y no mencionó definición de estándares de IaC, contenedores u observabilidad. Confirma el patrón: fuerte en seguridad de aplicación, débil en gobierno cloud/DevOps moderno. |
| Orientación a Resultados y KPIs        |      2      | Al preguntarle explícitamente por KPIs de la **solución/producto** (no de personas), su primera respuesta mezcló métricas de desempeño individual (tiempo en columnas de Jira, cantidad de "request changes" por ticket, asistencia a reuniones) — tuvo que ser redirigido explícitamente ("no tanto de las personas, sino de la solución") antes de dar respuestas más pertinentes (vigencia de versión de Commerce, librerías deprecadas, cobertura de pruebas unitarias, monitoreo de integraciones). Nunca mencionó ningún KPI de negocio/SLA (% despliegues exitosos, disponibilidad, defectos por HU, cumplimiento de plazos) — exactamente los KPIs que el JD define como el corazón del rol. Confirma la nota del entrevistador: falta de mentalidad orientada a resultados medibles a nivel de negocio. |

**Score Técnico Promedio**: 2.8 / 5

## CV Credibility Check vs. Entrevista

- **No resuelto en esta entrevista.** El `Perfil-Candidato.md` identificó como prioridad #1 aclarar los solapamientos de fechas del CV (consultoría independiente activa en paralelo a roles full-time; Univar vs. CI&T coincidiendo en fechas de inicio). Estas preguntas **no se hicieron** durante la entrevista — quedan pendientes antes de tomar una decisión final, independientemente del resultado técnico.
- Lo que sí es consistente: la especialización profunda y verificable en Adobe Commerce/AEM (12 años, desde Magento 1.6), y el patrón de progresión siempre en roles de tipo "Lead/Architect" sin título de gestión formal — confirmado en vivo cuando él mismo admite que nunca tuvo autoridad formal de evaluación de desempeño o contratación en un rol asignado.
- El salto de título a "Solutions Architect" (hace ~2 meses en ANTA) se sostiene parcialmente: sus respuestas muestran razonamiento de arquitecto (evaluar propuestas de terceros, decisiones de integración), aunque acotado siempre al ecosistema Adobe.

## Growth Velocity

Consistente en el eje técnico (de developer a lead técnico/arquitecto dentro del ecosistema Adobe Commerce/AEM), pero **plana en el eje organizacional**: 13 años sin un título de gestión formal en un empleador directo, y su propio testimonio confirma que la autoridad de gestión real (presupuesto, contratación, evaluación de desempeño) fue siempre delegada a otra área o asumida de forma ad hoc y temporal (caso Talos, 2017-2019). La progresión hacia el nivel de decisión y autoridad que exige un Technology Director es más lenta que lo que sugiere el resumen ejecutivo del CV.

## Red Flags Observados

- [x] Sesgo de ecosistema: en ningún momento de la entrevista propuso o consideró una solución fuera de Adobe Commerce/AEM, incluso cuando se le preguntó directamente por qué eligió una tecnología específica (RabbitMQ) — la respuesta fue familiaridad, no un análisis de alternativas.
- [x] Gaps técnicos duros en el stack DXP moderno que exige el rol: no conoce AEMaaCS (ni el nombre), no conoce EDS, sin experiencia en migraciones a cloud, sin mención de Kubernetes/Terraform/observabilidad.
- [x] Débil mentalidad orientada a resultados de negocio: necesitó ser redirigido para distinguir KPIs de producto de KPIs de personas, y nunca mencionó KPIs de negocio/SLA pese a ser el corazón del rol según el JD.
- [x] CV credibility check (solapamiento de fechas) sigue sin resolver — riesgo pendiente independiente del resultado técnico.

## Green Flags Observados

- [x] Cuando no domina algo, lo reconoce sin ponerse a la defensiva ("en teoría debería ser capaz de hacerlo, pero nunca lo he hecho" sobre migraciones a AEM Cloud) — honestidad intelectual clara.
- [x] Buen ejemplo de resolución de problemas complejos con trade-offs explícitos (caso de sincronización de pagos), evitando una solución sobredimensionada propuesta por un tercero.
- [x] Seguridad aplicada con profundidad real y ejemplos concretos (idempotencia, PCI, rate-limiting).
- [x] Interés activo y verificable en IA aplicada al desarrollo (certificación Anthropic, impulsó adopción de Claude Code/MCP con su equipo).

## Preguntas del Candidato al Cierre

Preguntó sobre el día a día del rol de TD en Omnipro, el mayor reto para quien ingrese, qué cambiaría el entrevistador con presupuesto ilimitado, cuánto debería involucrarse un TD con el código, y cómo está integrando la empresa la IA como "miembro del equipo" (no solo como agente de codificación). Son preguntas razonables y reflexivas que muestran interés genuino en el alcance real del rol y en la práctica de IA de la empresa — un green flag de madurez —, aunque ninguna aborda arquitectura actual, negocio o el equipo que heredaría, que hubiera sido una señal aún más fuerte para un rol de Director.

## Recomendación

- [ ] Avanzar
- [ ] Avanzar con reservas (detallar)
- [x] No avanzar

**Justificación**: El candidato tiene una base técnica sólida y verificable en Adobe Commerce, con buenos instintos de resolución de problemas y seguridad aplicada. Pero el perfil técnico presenta tres gaps grandes y consistentes con lo requerido para Technology Director: (1) sesgo de ecosistema — nunca busca ni evalúa alternativas fuera de Adobe, lo que limita su capacidad de definir arquitectura de forma independiente del stack que ya conoce; (2) gaps duros en el AEM moderno (AEMaaCS, EDS, migraciones cloud) y en gobierno cloud/DevOps en general, ambos núcleo del JD; (3) débil orientación a resultados medibles de negocio — no pudo articular KPIs de producto sin ser redirigido, y nunca mencionó los KPIs que el rol posee explícitamente (disponibilidad, % despliegues exitosos, defectos por HU). El promedio de 2.8/5 refleja un perfil más cercano a Technical Lead/Solutions Architect senior dentro de un dominio acotado que a un Technology Director con la amplitud y autoridad que exige el JD.

## Bias Check Reminder

Completa este scorecard usando solo la rúbrica ANTES de leer los scorecards de otros entrevistadores o discutir el candidato con el equipo.
