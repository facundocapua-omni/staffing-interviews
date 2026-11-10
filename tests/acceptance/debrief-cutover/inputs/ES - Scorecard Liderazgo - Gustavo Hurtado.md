# Scorecard de Liderazgo — Gustavo Hurtado Sarasti

**Entrevistador(a)**: Facundo Capua · **Fecha**: 2026-07-03

## Puntuaciones — Rúbrica Base

| Dimensión                   | Score (1-5) | Evidencia concreta observada |
| ---------------------------- | :---------: | ----------------------------- |
| Comunicación                 |      4      | Discurso extenso y con digresiones (estilo conversacional, propio de alguien acostumbrado a hablar más que a resumir), pero el contenido es claro y estructurado una vez desarrollado. Usa analogías efectivas para audiencias no técnicas: "Excel vs. tecnología" para describir su frustración con la carga comercial, "la gente de tecnología es binaria — te dicen si se puede o no se puede, pero no te dan la alternativa" para explicar un problema de equipo. Explicó con orden y sin jerga el flujo técnico de AdScan (Cannes) a un entrevistador no experto en ese proyecto puntual. |
| Resolución de Problemas      |      4      | Caso WhatsApp/Día de la Madre (México): detectó un error de cálculo de costos propio ("yo hice mal el cálculo"), abortó una solución con 2 semanas de trabajo ya invertido apenas vio que iba a costar 3x lo cotizado, evaluó una segunda alternativa (Twilio, aún cara) y llegó a una tercera (BSP regional a $6.000) que resolvió el problema. Decisión de migrar una arquitectura completa de AWS a Google cuando detectaron que necesitaban un servicio de Google, priorizando velocidad de procesamiento sobre el costo marginal. |
| Colaboración                 |      4      | Describe su método como "me siento con los equipos, escucho, escucho, escucho y hasta que no tengo un punto de vista no lo manifiesto". En el caso del director de tecnología con evitación al conflicto, buscó primero el contexto personal (separación familiar) y contrastó con el feedback de los pares de esa persona antes de intervenir. Trabajó junto a arquitectos en la propuesta de AdScan y en la definición de infraestructura cloud. |
| Growth Mindset               |      5      | Motivo explícito del cambio de rol es volver a enfocarse en tecnología ("me estoy perdiendo de la capa técnica, que es la parte que a mí me interesa más"), y ya viene negociando con su empleador actual diluir su carga comercial desde hace tiempo — no es una narrativa improvisada para la entrevista. Se preparó la noche previa revisando el roadmap de Adobe pese a no ser su plataforma principal. Empuja activamente a su equipo a salir de su zona de confort ("no que se maten en horas, sino que piensen qué herramienta usar para hacer lo mismo en menos tiempo"). |
| Ownership                    |      4      | Asume personalmente el error de estimación de costos en la campaña de WhatsApp ("es mi responsabilidad"). Gestiona proactivamente señales de riesgo comercial para evitar despidos ("no he tenido que despedir a nadie en 4-5 años porque en cuanto veo que un tema no va a funcionar, hago algo antes de tener que buscar cabezas"). Cumple y supera su propio target de revenue ($2M de $2.5M a la fecha, tras haber superado la meta del año anterior). |

**Score Liderazgo Promedio**: 4.2 / 5

## Distinción Clave: ¿Lidera o Ejecuta?

Evidencia sólida de "yo decidí" en primera persona, no solo narrativa de equipo: la decisión de consumir modelos vía Vertex AI en lugar de servicios externos ("yo les dije: vamos a usar los modelos de Google para no tener que salir de la infraestructura"), la decisión de migrar una arquitectura completa de AWS a GCP, y la decisión de abortar el desarrollo de la integración de WhatsApp cuando detectó el sobrecosto ("yo decidí, ya acordé, les dije a los chicos del equipo"). Esto contrasta con la preocupación señalada en el CV credibility check sobre el patrón "with my engineering team" — en la entrevista distingue con claridad sus decisiones personales de las del equipo. Team size y ownership de revenue confirmados de forma consistente con el CV (40-50 personas, $1.5M-2.5M USD).

## Red Flags Observados

- Ninguno relevante en lo cubierto por la entrevista.
- (Nota de proceso, no del candidato): la entrevista no llegó a cubrir el Bloque 5 de la guía (KPIs operativos, gobierno de seguridad/PCI/OWASP, incidentes de producción) ni la pregunta de reserva sobre discrepancias con decisiones comerciales que tuvo que ejecutar igual — esto debe cerrarse en la siguiente instancia antes de decidir.

## Green Flags Observados

- Motivación de cambio genuina y sostenida en el tiempo (ya venía negociando reducir su carga comercial con su empleador actual), no una racionalización ad-hoc frente al "downgrade" de autoridad que señalaba el CV credibility check.
- Ejemplo concreto y específico de mentoría/feedback difícil (el director de tecnología evitador de conflicto) — resuelve directamente la sección más débil del CV, que solo tenía lenguaje aspiracional sin casos.
- Reconoce con naturalidad un error propio de estimación/costeo sin desviar responsabilidad — resuelve la ausencia total de fracasos en el CV.
- Respuesta honesta y con plan concreto ante una brecha declarada (Adobe): "no me gusta vender humo", estima 8-12 semanas con criterios claros de qué necesita aprender primero (modelo de contenidos, arquitectura, orquestación).

## Preguntas del Candidato al Cierre

Preguntó por el día a día real del rol (una semana típica). Es una pregunta legítima y de due diligence práctica, pero está más orientada a validar su propio fit ("¿esto es lo que yo me imagino?") que a explorar el equipo, la arquitectura actual o el negocio del cliente — sería el patrón ideal según la guía. Señal moderada: interés genuino y aterrizado, no señal de máxima curiosidad hacia el negocio/equipo que hereda.

## Recomendación

- [x] Avanzar con reservas (detallar)
- [ ] Avanzar
- [ ] No avanzar

**Justificación**: El candidato muestra evidencia consistente y verificable de liderazgo real (decisiones propias, mentoría concreta, ownership de errores), lo que reduce significativamente el riesgo de "título sin sustancia" señalado en el CV credibility check. La principal reserva no es de liderazgo sino de alineación: viene de un rol con mayor autoridad formal (C-level, revenue propio) y su narrativa de "quiero volver a lo técnico" es creíble y sostenida, pero debe confirmarse explícitamente en la siguiente instancia (con el DXP Director) su tolerancia real a recomendar sin decidir en el ámbito comercial, dado que en esta entrevista esa pregunta puntual de la guía (Bloque 4, discrepancia con decisión comercial que tuvo que ejecutar) no llegó a formularse.

## Bias Check Reminder

Completa este scorecard usando solo la rúbrica ANTES de leer los scorecards de otros entrevistadores o discutir el candidato con el equipo. Un título de "Director" en el CV no reemplaza evidencia concreta de liderazgo.
