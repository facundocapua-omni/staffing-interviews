# Guía de Entrevista — Gustavo Hurtado Sarasti

**Rol**: Technology Director (DXP) · **Entrevistador(a)**: [nombre] · **Fecha**: [fecha] · **Duración sugerida**: 90 min
(Candidato con 20+ años de experiencia y trayectoria C-level → considerar extender Bloque 1 a 20 min
y ajustar Bloque 2 a 20 min, según nota del modelo de entrevista para candidatos muy senior)

## Contexto del Candidato (de CV Credibility Check)

Actual CTIO de VML Colombia (WPP), lidera 40+ personas, ownership directo de revenue ($1.5M-2.1M
USD/año), Cannes Lions Bronze 2024. Credibilidad de liderazgo ALTA (números concretos de equipo y
revenue). Señal principal a confirmar: **viene de un rol con más autoridad y alcance que el que ofrece
esta posición** (C-level con revenue target propio → Technology Director que "recomienda" pero no
decide en solitario sobre propuestas comerciales). Brechas a sondear: seguridad/compliance (PCI, OWASP,
ISO 27001, Zero Trust — ausentes en CV), multi-cloud más allá de AWS, Kubernetes/Terraform, KPIs
operativos de plataforma (disponibilidad, defectos, despliegues). Sección más débil del CV: evidencia
concreta de mentoría (solo lenguaje aspiracional, sin ejemplo). Ver perfil completo en
`ES - Perfil Candidato - Gustavo Hurtado.md`.

## Bloque 1 — Liderazgo Estratégico y Visión Técnica (~20 min)

- Pregunta base: "Hoy sos CTIO de VML Colombia, con un target de revenue propio y 40+ personas a cargo. Este rol de Technology Director tiene un alcance distinto: reportás a un Business Unit Director, y en decisiones comerciales (complejidad de propuestas de terceros, horas estimadas vs. propuesta) **recomendás pero no decidís en solitario**. ¿Qué te llevó a considerar este cambio y cómo te imaginás operando con ese nivel de autoridad?"
  - Follow-up: "¿Qué necesitarías ver en los primeros 90 días para confirmar que la decisión fue correcta?"
  - Qué buscar: honestidad sobre la motivación (relocation, industria, estabilidad, etapa de vida) vs. respuesta evasiva o genérica. Red flag si minimiza la diferencia de autoridad sin reflexión real.
- Pregunta base 2: "Contame cómo llegaste a diseñar la arquitectura de IA empresarial para Ecopetrol.
  ¿Qué alternativas de enfoque (build vs. buy, proveedor de LLM, nivel de automatización) descartaste y
  por qué?"
  - Follow-up: "¿Qué decisión de esa arquitectura tomaste vos personalmente, a diferencia de lo que
    definió tu equipo de ingeniería?"
  - Qué buscar: profundidad técnica personal real (no solo orquestación/sponsorship del proyecto).
- Qué buscar en general: decisiones propias ("yo decidí"), no solo de equipo; visión de mediano plazo.

## Bloque 2 — Arquitectura y Decisiones Técnicas (~20 min)

- Pregunta base / ejercicio de diseño: "AdScan combinó Google Cloud Vision y OpenAI para un caso de
  e-commerce con Makro. Diseñame de alto nivel cómo estructurarías una integración similar hoy para un
  DXP de e-commerce, considerando performance, seguridad de datos de pago (PCI) y escalabilidad."
  - Follow-up: "¿Cómo asegurarías compliance PCI en un flujo que combina visión por computadora y un
    LLM de terceros? ¿Qué harías distinto si el cliente exige Zero Trust?"
  - Qué buscar: esta pregunta empalma su experiencia real (AdScan) con una brecha declarada en el CV
    (seguridad/PCI). Es la pregunta más importante del bloque — mide si puede razonar sobre gobierno de
    seguridad aunque no lo haya ejecutado hands-on él mismo.
- Pregunta base 2: "Tu stack declarado es fuerte en AWS pero no mencionás GCP, Azure, Kubernetes o
  Terraform. ¿Qué tanta profundidad tenés en gobierno multi-cloud e infraestructura como código, y cómo
  lo compensarías si el equipo actual tiene esas brechas también?"
  - Qué buscar: honestidad tipo "no conozco eso, pero así lo abordaría" (green flag) vs. minimizar la
    brecha o inflar experiencia que no sostiene con ejemplos.
- Pregunta base 3 (error de arquitectura): "Contame sobre una decisión de arquitectura o de tecnología
  de la que fuiste responsable y que no salió como esperabas. ¿Qué cambiaste después?"
  - Qué buscar: el CV no tiene ningún fracaso mencionado — esta pregunta es clave para ver si reconoce
    errores con naturalidad (green flag) o los evade/atribuye a otros (red flag).
- Qué buscar en general: trade-offs explícitos, consideración de escalabilidad/seguridad/performance.

## Bloque 3 — Gestión y Desarrollo de Equipos (~15 min)

- Pregunta base: "Tu CV describe una filosofía de liderazgo sólida, pero no menciona un caso concreto.
  Contame sobre una persona específica de tu equipo (en VML o antes) a la que ayudaste a crecer:
  ¿cuál era su situación al inicio, qué hiciste concretamente, y dónde está hoy?"
  - Follow-up: "¿Cómo diste feedback difícil a alguien senior de tu equipo que no lo esperaba bien?"
  - Qué buscar: esta es la brecha de evidencia más grande del CV — necesita un ejemplo real y específico,
    no una repetición de la filosofía general. Red flag si no puede nombrar a nadie o si se mantiene en
    abstracciones.
- Pregunta base 2: "Escalaste la capacidad operativa de tu equipo con herramientas de Agentic AI sin
  aumentar headcount. ¿Cómo decidiste qué tareas automatizar y qué mantener humano? ¿Hubo resistencia
  del equipo y cómo la manejaste?"
  - Qué buscar: delegación según nivel de conocimiento, manejo de cambio organizacional, no solo la
    métrica de eficiencia.
- Qué buscar en general: evidencia concreta de mentoría, delegación, feedback difícil dado.

## Bloque 4 — Gestión de Stakeholders y Comunicación (~15 min)

- Pregunta base: "Ganaste el RFP de Coca-Cola (OneXP/XTND) compitiendo contra consultoras. Explicame
  cómo le comunicarías a un cliente no técnico por qué tu propuesta técnica era mejor que la de una
  consultora tradicional, sin usar jerga técnica."
  - Follow-up: "¿Hubo algún punto donde el cliente pedía algo técnicamente inviable en el timeline
    propuesto? ¿Cómo lo negociaste?"
  - Qué buscar: capacidad de traducir riesgo/valor técnico a impacto de negocio, sin subestimar al cliente.
- Pregunta base 2: "En este rol, la autoridad sobre estimaciones de horas y complejidad de propuestas de
  terceros es de recomendación, no de decisión final — la decisión la toma el Business Unit Director o
  el comercial. Contame de una vez que discrepaste fuertemente con una decisión comercial o de negocio
  y tuviste que ejecutarla igual. ¿Cómo lo manejaste?"
  - Qué buscar: esta pregunta prueba directamente el punto de fricción identificado en el CV credibility
    check (viene de un rol donde él decidía, no solo recomendaba). Red flag si nunca ha estado en esa
    posición o si muestra rigidez ante decisiones que no controla.

## Bloque 5 — Ejecución, KPIs y Gobierno Cloud/Seguridad (~10 min)

- Pregunta base: "Tu CV documenta muy bien KPIs de negocio (revenue, cobertura de entrega). Este rol
  también pide ownership de KPIs operativos de plataforma: disponibilidad (≥99.5%), tasa de defectos por
  historia de usuario (≤5%), éxito de despliegues (≥95%). ¿Tenés experiencia gobernando este tipo de
  indicadores? Dame un ejemplo concreto de cómo actuaste sobre uno de ellos."
  - Qué buscar: si la respuesta es genérica o se apoya solo en KPIs de negocio, es una brecha real a
    documentar (no descalificante, pero sí a considerar en el plan de onboarding).
- Pregunta base 2: "Contame sobre un incidente de producción o un despliegue fallido del que hayas sido
  responsable. ¿Cuál fue tu rol en la respuesta y qué cambió después en el proceso de despliegue?"
  - Qué buscar: el CV no menciona ningún incidente — ver si tiene una respuesta real de gobierno de
    despliegues o si el contexto de agencia (proyectos por entrega, no plataformas 24/7) lo deja sin
    experiencia directa en esto.
- Pregunta base 3: "¿Cómo definirías y harías cumplir estándares de seguridad tipo PCI u OWASP en un
  equipo que hoy no los tiene formalizados?"
  - Qué buscar: plan concreto vs. respuesta vaga; conexión con la brecha de seguridad del CV.

## Cierre (~5 min)

- Preguntas del candidato: [registrar y analizar qué revelan — ideal: pregunta sobre el equipo actual, la
  arquitectura existente, el nivel real de autonomía en decisiones técnicas y comerciales, o la relación
  con el Business Unit Director]
- Confirmar expectativa de compensación y de autoridad de decisión (tema abierto desde el CV credibility check)
- Próximos pasos comunicados: [sí/no]

## Notas Libres Durante la Entrevista

[Espacio para notas en vivo — no interpretar todavía, solo registrar hechos observados]

## Preguntas Adicionales de Reserva (si sobra tiempo o hay que profundizar)

- "El período dic 2020–dic 2024 en Equitel Ventures fue part-time y se solapa con tu rol full-time en VML
  desde mayo 2021. ¿Cómo manejaste eso con tu empleador?" (transparencia / manejo de conflicto de interés)
- "Entre 2012 (cierre de 3Metas) y 2014 (Aranda Software) — contame qué pasó en ese período." (cerrar
  el expediente, no acusatorio)
- "Fuiste fundador y luego volviste a un rol de Technical Lead en 2015. ¿Qué te hizo tomar esa decisión?"
  (entender el pivote, ownership del cierre del emprendimiento)
