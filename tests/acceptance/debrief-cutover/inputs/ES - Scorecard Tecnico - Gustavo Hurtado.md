# Scorecard Técnico — Gustavo Hurtado Sarasti

**Entrevistador(a)**: Facundo Capua · **Fecha**: 2026-07-03

## Puntuaciones — Rúbrica de Liderazgo Técnico y Arquitectura

| Dimensión                             | Score (1-5) | Evidencia concreta observada |
| -------------------------------------- | :---------: | ----------------------------- |
| Visión Arquitectónica                  |      4      | Describe con detalle técnico real (no solo de negocio) el diseño de AdScan/Coca-Cola: modelos Gemini livianos corriendo client-side entrenados con data sintética (stable diffusion) para evitar latencia de ida y vuelta al backend, fallback a Google Vision + contexto vía LLM cuando el catálogo no reconoce productos locales, y split de responsabilidades cliente/servidor en la lectura de códigos de barra por motivos de seguridad. Articula trade-offs concretos de costo/latencia (ej. mover una arquitectura completa de AWS a GCP por velocidad de procesamiento; usar Vertex AI en vez de llamadas directas a OpenAI por costo de tokens). **Consideración**: toda esta experiencia es en Salesforce/Pycore/GenAI propietario, no en el ecosistema Adobe (AEM/Adobe Commerce), que es donde está el mayor volumen de proyectos de la organización — ver sección dedicada abajo sobre su plan de ramp-up. |
| Liderazgo y Mentoría de Equipo         |      5      | Caso concreto y detallado de coaching a un director de tecnología técnicamente fuerte pero evitador de conflicto: investigó el contexto personal, diagnosticó el patrón (siempre "arreglaba" el código ajeno en vez de dar feedback), diseñó una conversación que generó una confrontación real, y sostuvo el proceso hasta un cambio de comportamiento validado por terceros ("la gente me decía que el man cambió un montón"). Resuelve directamente la brecha de evidencia de mentoría señalada en el CV credibility check. |
| Gestión de Stakeholders y Delivery     |      4      | Explica con claridad el balance negocio/técnica en la propuesta a Grupo UMA (Guatemala): migrar de CMS sin perder redirecciones ni posicionamiento SEO mientras los sitios actuales siguen operando. Gestiona de forma transparente la tensión entre su interés técnico y su responsabilidad comercial (meta de $2.5M, ya en $2M). No se llegó a probar directamente cómo maneja una discrepancia fuerte con una decisión comercial que debió ejecutar igual (pregunta planificada en Bloque 4 no se formuló) — queda pendiente de validar. |
| Gobierno Cloud/DevOps/Seguridad        |   No evaluado (gap de la entrevista, no del candidato)   | La entrevista no cubrió PCI, OWASP, ISO 27001, Zero Trust, Kubernetes ni Terraform — las preguntas planificadas del Bloque 2 (PCI/Zero Trust sobre AdScan) y Bloque 5 (estándares de seguridad) no se llegaron a formular. Única señal tangencial: decisión de mantener todo el procesamiento dentro de la infraestructura de un mismo proveedor cloud (Google) por eficiencia, y separación cliente/servidor de datos sensibles (código de barra) "por temas de seguridad" — insuficiente para puntuar esta dimensión con la rúbrica. **Debe cerrarse en la siguiente instancia antes de una decisión final**, dado que es un requisito explícito del JD y una brecha ya identificada en el CV. |
| Orientación a Resultados y KPIs        |      3      | Fuerte evidencia de gestión proactiva de KPIs comerciales (estimados semanales por ~$1M, seguimiento activo de su meta de revenue, ajuste de forecast). Cero evidencia sobre KPIs operativos de plataforma (disponibilidad, tasa de defectos, éxito de despliegues) — el Bloque 5 de la guía, diseñado específicamente para sondear esto dado que el CV tampoco los menciona, no se llegó a preguntar. Score refleja gestión de KPIs real pero unidimensional (solo negocio), consistente con el gap ya señalado en el CV. |

**Score Técnico Promedio**: 4.0 / 5 (calculado sobre las 4 dimensiones evaluadas; "Gobierno Cloud/DevOps/Seguridad" queda sin puntuar por falta de cobertura en la entrevista, no computa en el promedio)

## CV Credibility Check vs. Entrevista

Consistente, y en algunos puntos supera lo esperado por el CV. La preocupación principal del credibility check — que el trabajo técnico profundo llevara siempre la coletilla "with my engineering team" sin evidencia de rol personal — queda en gran medida resuelta: en la entrevista distingue con precisión decisiones que tomó él mismo (Vertex AI, migración AWS→GCP, aborto de la integración de WhatsApp) de las de su equipo, y explica el "por qué" técnico de cada una. La sección más débil del CV (mentoría, solo lenguaje aspiracional) también queda resuelta con un caso real y específico. Lo que sigue sin verificar, porque no se preguntó, son exactamente las brechas que el CV ya dejaba abiertas: seguridad/compliance, multi-cloud más allá de AWS/GCP puntual, Kubernetes/Terraform, y KPIs operativos de plataforma (disponibilidad, defectos, despliegues, incidentes).

## Consideración de Onboarding: Brecha de Experiencia en el Ecosistema Adobe

**Tema a considerar** (no es un red flag, pero sí un riesgo real a planificar): el candidato tiene experiencia sólida liderando personas y arquitectura en general, pero su experiencia hands-on es en Salesforce y Pycore, y "un poco menos" en Adobe (AEM/Adobe Commerce) — nunca fue developer en esa plataforma, solo la conoce "más hacia la parte de arquitectura y estructura de proyectos" (ver CV Credibility Check). Dado que la mayoría de los proyectos de la organización giran alrededor del ecosistema Adobe, este es un ramp-up real y no menor para el día a día del rol (orientar al equipo, participar en soluciones, hablar con autoridad técnica en el partnership con Adobe).

**Pregunta formulada** (~00:55:37): Facundo le planteó directamente esta brecha — que si bien Martech Studio busca ser agnóstico de plataforma, el mayor porcentaje de proyectos hoy es sobre Adobe, y le preguntó qué tan rápido se ve haciendo el ramp-up (no a conocimiento profundo, pero sí al nivel necesario para orientar al equipo).

**Respuesta del candidato** (~00:56:46–00:59:38):
- Se apoya en un precedente concreto de aprendizaje acelerado: lo subieron a un avión con un jueves de aviso para vender Salesforce al lunes siguiente ("me dijeron: usted es el director"), y aprendió lo necesario en una semana.
- Ya empezó el ramp-up de forma proactiva antes de la entrevista: la noche anterior revisó el roadmap de Adobe (parte agéntica, CMS, DAM) para "reconectar" con por qué alguien elegiría AEM sobre otra plataforma.
- Da un número concreto y acotado: estima **8-12 semanas** para entender lo general lo suficiente como para sentarse con el equipo a tomar decisiones — no para dominio profundo.
- Explica su método de ramp-up con criterio propio, no genérico: prioriza entender primero los principios de arquitectura de contenidos (multi-idioma, multi-país, cómo se actualizan los contenidos, si el cliente puede costear un DAM o no) y desde ahí bajar a cómo se orquesta la solución y qué componentes ya están construidos en la plataforma — es decir, plantea que la arquitectura es transferible entre plataformas y que lo que cambia es la implementación puntual.
- Nota que en la práctica muchos clientes ya llegan con la plataforma decidida (Adobe, Pycore, Drupal, WordPress), lo que en su lectura reduce parte de la necesidad de dominar Adobe end-to-end desde el día uno.
- Declara explícitamente su filosofía de aproximarse a una brecha de conocimiento: "no me gusta vender humo" — prefiere escuchar al equipo primero y no dar opinión hasta tener un punto de vista formado.
- Cuando se le preguntó si vive esto como desafío o como presión, respondió sin ambigüedad que lo ve "más como un desafío", y lo conectó con una reflexión propia sobre la estrategia de largo plazo de Adobe vs. Salesforce en el mercado — muestra curiosidad genuina por la plataforma, no solo tolerancia resignada a aprenderla.

**Evaluación**: la respuesta sigue el patrón green-flag ("no conozco eso, pero así lo abordaría", con plan concreto y honestidad sobre el nivel real de profundidad) más que un red flag de inflar experiencia que no tiene. Aun así, la brecha en sí es real y no debe minimizarse solo porque la respuesta fue buena: 8-12 semanas es su propia estimación para un entendimiento general, no para dominio de arquitectura Adobe a nivel de decisión de alto impacto — algo a monitorear activamente en el plan de onboarding (ej. mentoría cruzada con un arquitecto Adobe senior del equipo, o acotar su autonomía de decisión técnica en proyectos Adobe complejos durante ese período inicial).

## Growth Velocity

Consistente con la lectura del perfil: progresión sólida pero no meteórica, con un mix híbrido de tecnología y negocio que calza con el rol. La entrevista aporta una lectura nueva sobre el riesgo de "dirección" señalado en el perfil (viene de un rol con más autoridad/alcance): el candidato no está buscando este rol a pesar de tener menos autoridad comercial, sino en parte *por eso* — ya viene reduciendo activamente su propia carga comercial en su rol actual. Esto reduce el riesgo de fuga temprana por frustración de autoridad, aunque no lo elimina del todo (falta confirmar tolerancia real a "recomendar, no decidir" bajo presión).

## Red Flags Observados

- Ninguno en lo efectivamente cubierto por la entrevista.
- Brecha de cobertura de la entrevista (no atribuible al candidato): gobierno de seguridad/compliance/multi-cloud y KPIs operativos de plataforma quedaron sin sondear. Esto es un requisito central del JD (PCI compliance, ISO 27001, OWASP, Zero Trust, disponibilidad ≥99.5%, defectos ≤5%, despliegues ≥95%) y debe evaluarse explícitamente antes de una recomendación final.
- **Impresión general del entrevistador (a validar en la próxima ronda)**: pese al score alto en Visión Arquitectónica, la sensación global es la de un perfil más orientado a gestión/orquestación (management) que a liderazgo técnico hands-on de bajo nivel. Los ejemplos de arquitectura que da son sólidos a nivel de decisión y trade-off (qué usar, por qué, con qué costo), pero no hay evidencia de profundidad en implementación/código o discusión técnica de detalle fino. Riesgo a probar en la siguiente instancia: si el equipo necesita un director que también pueda bajar a discutir decisiones técnicas de bajo nivel con ingenieros senior, esto podría ser una limitación.

## Green Flags Observados

- Explica arquitectura con trade-offs técnicos reales y concretos (costo de tokens, latencia cross-cloud, seguridad en split cliente/servidor), no solo relato de resultado de negocio.
- Reconoce y resuelve con naturalidad un error propio de cálculo/costeo en una decisión técnica (integración WhatsApp), con cifras y proceso de corrección específicos — contrasta con un CV sin ningún fracaso mencionado.
- Plan de ramp-up realista y honesto ante una brecha reconocida (Adobe): estimación de 8-12 semanas, con criterio claro de qué priorizar (arquitectura de contenidos antes que herramientas puntuales) y una filosofía explícita de "no vender humo".
- Caso de mentoría específico, verificable en su narrativa (contexto personal + diagnóstico de patrón + intervención + resultado validado por terceros).

## Preguntas del Candidato al Cierre

Ver detalle en Scorecard de Liderazgo — pregunta centrada en el día a día real del rol, señal de due diligence práctica pero orientada a su propio fit más que a explorar el equipo o la arquitectura que heredaría.

## Recomendación

- [x] Avanzar con reservas (detallar)
- [ ] Avanzar
- [ ] No avanzar

**Justificación**: Fuerte evidencia técnica y de liderazgo en las dimensiones que sí se cubrieron (arquitectura, mentoría, gestión de stakeholders comercial/técnica). Las reservas son dos, de naturaleza distinta: (1) gobierno de seguridad/compliance/multi-cloud y KPIs operativos de plataforma son requisitos explícitos del JD que no se sondearon en esta entrevista y ya eran una brecha declarada en el CV — no es un problema del candidato sino de cobertura, a cerrar en la siguiente instancia; (2) la falta de experiencia hands-on en el ecosistema Adobe es una brecha real y conocida (declarada por el propio candidato), con un plan de ramp-up razonable (8-12 semanas) pero que va a requerir soporte activo del equipo Adobe senior durante el onboarding — no descalificante, pero sí a planificar explícitamente y no asumir como resuelto solo porque la respuesta en la entrevista fue honesta y estructurada. Recomendación concreta: antes de una decisión final, incluir las preguntas pendientes (Bloque 5 de la guía, más la pregunta de reserva sobre PCI/Zero Trust del Bloque 2) en la próxima instancia con el DXP Director, y si se avanza con la oferta, definir explícitamente el soporte de ramp-up en Adobe para los primeros 2-3 meses.

## Bias Check Reminder

Completa este scorecard usando solo la rúbrica ANTES de leer los scorecards de otros entrevistadores o discutir el candidato con el equipo.
