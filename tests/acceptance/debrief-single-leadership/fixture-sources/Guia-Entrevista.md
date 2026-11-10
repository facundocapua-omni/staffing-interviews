# Guía de Entrevista — José David Restrepo Balbin

**Rol**: Technology Director · **Entrevistador(a)**: [nombre] · **Fecha**: [fecha] · **Duración sugerida**: 90 min

## Contexto del Candidato (de CV Credibility Check)

13 años de experiencia (CV declara "15+", inflación leve a validar). Especialista muy sólido en Adobe
Commerce/AEM/PHP con certificaciones vigentes y clientes reconocidos (Disney, Coca-Cola LATAM, Acer,
telco de 300k+ clientes). Progresión consistente en el eje técnico (developer → lead técnico → arquitecto),
pero **plana en el eje organizacional**: nunca tuvo título de gestión formal (Manager/Director) en 13 años,
y el título de "Solutions Architect" es de hace solo 2 meses (rol actual en ANTA).

**Dos alertas de credibilidad a resolver ANTES de profundizar en competencias**: (1) su consultoría
independiente (oct-2017 → hoy) se superpone con todos los roles full-time posteriores (Globant, CI&T,
ANTA) sin explicación; (2) Univar Solutions (ago-2023 a mar-2024) coincide exactamente en fecha de
inicio con CI&T/Coca-Cola (ago-2023 a may-2025), con un retroceso de título ("Magento developer" vs.
"Adobe Commerce Lead Developer"). Ver `Perfil-Candidato.md` para el detalle completo.

El gap más importante a sondear en esta entrevista es la **brecha entre liderazgo técnico de
proyecto/cuenta (que tiene bien evidenciado) y liderazgo organizacional con autoridad de negocio,
presupuesto y KPIs** (que el CV no evidencia en absoluto).

## Apertura (~5 min)

- Romper el hielo, explicar formato (90 min, bloques de liderazgo/arquitectura/equipo/stakeholders/KPIs) y que se tomarán notas.
- **Aclarar timeline antes de continuar** (no dejar para el cierre — condiciona la interpretación de todo lo demás):
  - "Veo que tu consultoría independiente en Adobe Commerce empieza en octubre de 2017 y sigue activa hoy, en paralelo con tus roles en Globant, CI&T y ANTA. ¿Cómo compaginabas ambos? ¿Era part-time, fines de semana, entre contratos?"
  - "También veo que Univar Solutions (ago-2023 a mar-2024) y CI&T/Coca-Cola (ago-2023 a may-2025) arrancan exactamente el mismo mes. ¿Fueron simultáneos? ¿Cuál era tu dedicación real a cada uno?"
  - Qué buscar: respuesta clara, específica y verificable (nombres de proyectos, % de dedicación, por qué el cambio de título hacia abajo en Univar) vs. respuesta vaga o evasiva → red flag de inconsistencia CV.

## Bloque 1 — Liderazgo Estratégico y Visión Técnica (~15 min)

- Pregunta base: "Tu título de 'Solutions Architect' en ANTA es de hace apenas dos meses. Cuéntame una decisión de arquitectura que hayas tomado ahí con autoridad total — ¿qué alternativas descartaste y por qué?"
- Follow-up: "Antes de ANTA, en CI&T eras 'Lead Developer', no arquitecto. ¿Qué cambió realmente en tu nivel de autoridad de decisión entre un rol y otro, más allá del título?"
- Follow-up: "¿Cómo te mantienes actualizado en tecnología, y qué decidiste NO adoptar en tu equipo por no estar maduro o no ser prioritario?"
- Qué buscar: decisiones propias ("yo decidí", "yo definí"), no solo descripciones de lo que "se hizo"; distinguir autoridad real de título nuevo/aspiracional.

## Bloque 2 — Arquitectura y Decisiones Técnicas (~25 min)

- Pregunta base / ejercicio de diseño: "En CI&T mencionas una arquitectura Headless con Adobe Commerce, GraphQL y microservicios en Azure, sosteniendo hasta 700 transacciones por minuto para Coca-Cola LATAM. Dibújame ese diseño de alto nivel — ¿qué componentes había, dónde estaban los cuellos de botella, y qué decisión tomaste vos específicamente para sostener esa carga?"
- Follow-up: "En ANTA integraste Adobe Commerce/AEM con Microsoft Dynamics 365 vía Adobe App Builder para una plataforma con 300,000+ clientes. ¿Qué riesgos de seguridad o performance identificaste en esa integración y cómo los mitigaste?"
- Follow-up (para sondear breadth fuera de Adobe): "Tu CV lista Java, Node.js y React como skills. ¿En qué proyecto reciente los usaste en profundidad, más allá de Adobe Commerce/PHP?"
- Follow-up (error de arquitectura): "Cuéntame de una decisión de arquitectura tuya que en retrospectiva no fue la correcta. ¿Cómo te diste cuenta y qué cambiaste?"
- Qué buscar: trade-offs explícitos y verificables (no solo buzzwords repetidos del CV como "scalable, secure, reliable"); honestidad ante el error; evidencia real de profundidad fuera del stack Adobe si el rol lo requiere.

## Bloque 3 — Gestión y Desarrollo de Equipos (~15 min)

**Bloque crítico dado el gap identificado — no comprimir tiempo aquí.**

- Pregunta base: "Mencionas haber liderado equipos distribuidos de hasta 10 ingenieros en tres zonas horarias. Contame de alguien específico de esos equipos a quien ayudaste a crecer — ¿qué hiciste concretamente?"
- Follow-up: "Describe una conversación de feedback difícil que tuviste que dar a alguien de tu equipo. ¿Cómo la abordaste y qué resultado tuvo?"
- Follow-up: "En ninguno de tus roles el título fue 'Manager' o 'Director'. ¿Tuviste alguna vez responsabilidad formal sobre contratación, evaluaciones de desempeño o presupuesto de tu equipo? Si no, ¿cómo te preparaste para asumir eso en un rol de Technology Director?"
- Qué buscar: ejemplos concretos y verificables de mentoría/feedback (no generalidades); honestidad sobre la falta de experiencia formal de gestión de personas si es el caso, y un plan concreto de cómo la abordaría ("no tengo esa experiencia formal, pero así es como la construiría...").

## Bloque 4 — Gestión de Stakeholders y Comunicación (~15 min)

- Pregunta base: "El JD de este rol reporta a un Business Unit Director e interactúa indirectamente con el CEO. En tu carrera, ¿cuál fue el nivel más alto de stakeholder de negocio con el que interactuaste directamente, y en qué contexto?"
- Follow-up: "Explícame la arquitectura Headless de Coca-Cola LATAM como si yo fuera un cliente no técnico que está preocupado por el costo del proyecto."
- Follow-up: "Cuéntame de una negociación con un cliente o PM donde el alcance o tiempo pedido no era técnicamente viable. ¿Cómo lo resolviste?"
- Qué buscar: capacidad real de traducir riesgo técnico a impacto de negocio; evidencia de trato con roles ejecutivos (no solo PMs/POs técnicos), dado que el CV no muestra esto explícitamente.

## Bloque 5 — Ejecución, KPIs y Gobierno Cloud/Seguridad (~15 min)

- Pregunta base: "Tu CV no menciona métricas de calidad o entrega — ¿qué KPIs usabas para medir la salud de tus proyectos en CI&T o ANTA (defectos por HU, % de despliegues exitosos, disponibilidad)? Dame un ejemplo de cómo actuaste sobre uno de ellos."
- Follow-up: "Mencionas 'PCI compliance' y 'disaster recovery strategy design' en roles anteriores (IDlink, Talos Digital). Contame un caso concreto: ¿qué estándar definiste vos, y cómo lo hiciste cumplir en el equipo?"
- Follow-up: "Más allá de 'cloud-based initiatives' y microservicios en Azure, ¿qué rol jugaste vos, a diferencia de un DevOps engineer, en decisiones de infraestructura (Kubernetes, Terraform, observabilidad)?"
- Follow-up (innovación/IA): "Veo que hiciste el Anthropic Developer Program / sos Anthropic Certified Developer. ¿Qué hiciste concretamente con eso y cómo lo aplicaste (o pensás aplicarlo) en tu forma de liderar un equipo de desarrollo?"
- Qué buscar: ownership proactivo de KPIs (no reactivo post-incidente); definición real de estándares (no solo ejecución de estándares de otros); profundidad real en gobierno cloud más allá de lo declarado en el CV; la respuesta sobre IA es una buena señal de green flag si es concreta y no genérica.

## Cierre (~5 min)

- Validar nivel de inglés: intercalar 2-3 minutos de conversación en inglés en algún bloque técnico (no anunciarlo como "examen", que fluya natural).
- Preguntas del candidato: [registrar y analizar qué revelan — ¿pregunta sobre el equipo actual, la arquitectura existente, o solo sobre condiciones laborales?]
- Próximos pasos comunicados: [sí/no]

## Notas Libres Durante la Entrevista

[Espacio para notas en vivo — no interpretar todavía, solo registrar hechos observados]
