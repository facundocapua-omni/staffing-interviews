---
candidato: "Daniel Carrasco Herrera"
fecha: "2026-05-14"
entrevistador: "Facundo Capua - Galvis Herrera"
tags: [scorecard, evaluacion, tecnico]
---

# Scorecard Técnico — Daniel Carrasco Herrera

**Fecha:** 2026-05-14
**Entrevistador:** Facundo Capua - Galvis Herrera
**Duración:** ~54 min
**Nivel evaluado:** Senior AEM Backend Developer (12 años en AEM)

---

## Evaluación por Dimensión Técnica

| Dimensión                            | Puntuación (1-5) | Evidencia                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------ | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Conocimiento AEM                     | 3/5              | Base real en `AEM backend`: `Sling Models`, servicios `OSGi`, `Servlets`, `Resource Resolver`, `workflows` con `process steps`, `event listeners` sobre `DAM`, configuración de `Dispatcher` desde cero, pipelines de `Cloud Manager`, manejo de secretos vía `Secret Kit` y secret keys en cloud, `Content Fragments` + `GraphQL persistent queries` (Seven en Quidilla). Hay 12 años de experiencia real sin inflar. No sube porque la conversación expuso gaps relevantes para el rol declarado: `EDS` y `App Builder` confesados como desconocidos ("no lo he visto"), `JCR indexes` con miedo explícito ("le tengo miedo... no me atrevería"), y aclaró que la migración On-Prem → Cloud que aparece como claim del CV solo se hizo en papel ("quedó en papel, nunca hice una migración de On-Prem hacia cloud"). El claim de AEMaaCS de Clase Azul es real pero fue greenfield, no migración. |
| Pensamiento Arquitectónico           | 3/5              | Dio un caso concreto y bien narrado: la propuesta de `Dynamic Media` para el cliente Firestone/Bridgestone, partiendo de datos de `Analytics` que mostraban consumo mayoritariamente móvil con imágenes de 30-40 MB. Hizo `POC`, comparó performance contra el estado actual, y el cliente validó el resultado (no se compró por costos de licencia, no por la propuesta técnica). También mostró autocrítica madura sobre Clase Azul: "primero levantaría la mano y diría que es imposible", identificando que la falla nació en preventa, no en ejecución. No sube a 4 porque las decisiones descritas son operativas más que arquitectónicas profundas (no aparecieron decisiones de modelado de contenido de cero, ni trade-offs de migración, ni patrones AEM articulados con peso de arquitecto).                                                                                             |
| Calidad de Código & Buenas Prácticas | 2/5              | Esta es la zona más débil. Confesó explícitamente: "mi dolor de cabeza siempre ha sido los unit testing", y usó la IA principalmente para generar tests que admite "no me los hacía bien". En Qydiya constató que "el coverage está muy mal" pero no apareció como dueño de la mejora — fue observación, no acción. La señal positiva es que sí configuró los pipelines de dev/preprod/prod en Clase Azul con sus quality gates, y entiende que `coverage` y otras métricas vienen forzadas por defecto en `Cloud Manager` en stage/prod. Pero para un perfil con 12 años de experiencia el rol declarado, no hubo evidencia de disciplina propia de testing (`JUnit`, `Mockito`, integration tests), code review sostenido, ni de criterio sobre cobertura mínima o calidad del código del equipo.                                                                                                 |
| Debugging & Resolución Técnica       | 3/5              | El mejor caso técnico fue la conversión automática de imágenes `JPG`/`PNG` → `WebP` en Seven/Quidilla: implementó un `event listener` sobre `upload` al `DAM`, intercepta el binario, usa una librería de conversión, modifica metadata y vuelve a subir el asset transformado, todo transparente para el autor. Cuando Galvis le sugirió que la solución más "AEM-nativa" sería un `process step` dentro del workflow `DAM Update Asset` (Duplo), aterrizó bien: explicó que ya había modificado ese mismo workflow y que conoce el patrón de `process step` con clase Java propia para insertar lógica al pipeline. Buena señal de que conoce las dos rutas técnicamente, aunque la solución que él implementó no fue la más limpia. No subo más porque otras zonas tuvieron menos profundidad de debugging real (índices, performance, replicación) y porque no hubo casos de alta complejidad.  |
| Amplitud del Stack                   | 3/5              | La amplitud declarada en CV (`AEMaaCS`, `GraphQL`, `Adobe Campaign Standard`, `AWS Cognito SSO`, `Google BigQuery`, `Dynamic Media`, `Cloud Manager`) es razonable y diversa. Lo que se validó en esta sesión es principalmente el núcleo backend AEM, `GraphQL` + `Content Fragments` (Seven), `Dispatcher` (Clase Azul), `Cloud Manager pipelines`, y `Dynamic Media` (propuesta concreta para Bridgestone). `BigQuery` no se exploró, `Adobe Campaign Standard` no se exploró, `AWS Cognito` no se exploró — por tiempo, no por bloqueo. Frontend es declarado como no-foco explícitamente ("no soy nada creativo, no se me da"). Gaps confirmados: `EDS` ("no lo he visto"), `App Builder` ("no"), `índices JCR` ("le tengo miedo"). La amplitud real validada está alineada con backend AMS / Cloud, pero claramente no con la dirección EDS + App Builder.                                    |

**Promedio técnico:** 2,8/5

### Escala de referencia

| Puntuación | Significado |
|---|---|
| 1 | No demuestra conocimiento; respuestas incorrectas o vacías |
| 2 | Conocimiento superficial; sabe qué es pero no cómo usarlo |
| 3 | Competente; resuelve con guía, conoce las prácticas estándar |
| 4 | Sólido; resuelve sin guía, entiende trade-offs, propone alternativas |
| 5 | Experto; enseña, anticipa problemas, decisiones arquitectónicas maduras |

---

## Detalle por Área AEM

### Conocimiento AEM (1-5): 3/5

| Área | Nivel observado | Notas |
|---|---|---|
| HTL/Sightly | Competente | Mencionó el flujo backend → `Sling Model` → exposición de propiedades al `HTL` → consumo desde frontend. No se profundizó en patrones HTL avanzados. |
| Sling Models | Sólido | Narró bien la evolución personal desde la inyección directa (`@Property` tipo "punto, propiedad") en sus primeros proyectos hacia `Sling Models` con mapeo de nodos completo. Cuando Galvis le preguntó cómo obtendría metadata de una página desde un modelo, llegó por sí mismo a "el `resource`, después lo mapeas al objeto que necesites" — respuesta correcta para `ResourceResolver` + `adaptTo()`. |
| OSGi | Competente | Trabaja con servicios `OSGi`, configuraciones por `runmode`, manejo de secrets vía `Secret Kit` para encriptar y pegar el valor por ambiente en el `.config`. Para cloud usa la solución de `secret keys` nativa. |
| Componentes & Diálogos | Competente | 12 años creando componentes custom. Mencionó que sus primeros proyectos fueron "todos custom" porque no sabía que existían los `core components` para extender. Hoy sí los usa. |
| Templates & Políticas | n/e | No se evaluó en esta sesión. |
| Content Fragments / Experience Fragments | Competente | Trabajó con `Content Fragments` en Seven (Quidilla) y los conectó con `GraphQL persistent queries`. La descripción es operativa más que arquitectónica ("creabas el `Content Fragment` y creabas el `persistent query` hacia ese contenido"). |
| AEM as a Cloud Service | Limitado / Competente | El caso real es Clase Azul: proyecto greenfield en Cloud (no migración), donde configuró pipelines de dev/preprod/prod, dispatcher desde cero, y `secret keys`. Aclaró honestamente que la migración On-Prem → Cloud que aparece en su CV "quedó en papel" — hizo planning con `BPA`-style análisis (cantidad de contenido, componentes desfasados, librerías deprecadas, dispatcher) pero el cliente no compró la migración por costos de licencia. |
| Dispatcher / CDN | Competente | Configuró desde cero el dispatcher en Clase Azul. Conoce conceptos de `TTL`, qué cachear, filtros, redirección. Lo describe como "otro lenguaje" — buena humildad pero deja la lectura en competente, no en sólido. |
| Workflows | Sólido | El caso de la conversión WebP es la mejor evidencia: modificó el workflow `DAM Update Asset` (lo llama "Duplo"), conoce los `process steps`, entiende cómo insertar una clase Java propia en el pipeline. La conversación demostró que tiene exposición real al motor de workflows. |
| Permisos / ACLs | n/e | No se evaluó. |
| JCR Indexes | Limitado | Confesó miedo explícito: "Le tengo miedo, es como hacer un delete sin el where... yo no me atrevería". Solo ha hecho reindex con la sintaxis de documentación. Para 12 años Senior es un gap notable. |
| EDS / App Builder | n/e (gap declarado) | "No lo he visto" para EDS; "no" para App Builder. Galvis le recomendó leer documentación al cierre. |

### Pensamiento Arquitectónico (1-5): 3/5
- Caso `Dynamic Media` para Firestone/Bridgestone: propuesta basada en datos de Analytics (consumo móvil mayoritario, imágenes 30-40 MB), `POC` comparativo, validación de performance. El cliente aprobó técnicamente pero no compró por costos. Hay narrativa completa: problema → propuesta → POC → resultado.
- Caso `Clase Azul` como Tech Lead: 3 meses para migrar sitio completo desde Drupal/PHP. Identificó con autocrítica madura los puntos de fricción (preventa que no involucró delivery, PM ausente, cliente sin conocimiento de AEM) y articuló qué haría diferente: "primero levantaría la mano y diría que es imposible".
- En la mayoría de las respuestas técnicas estuvo más en modo descriptivo ("así lo hicimos") que comparativo ("estas eran las opciones, elegí esta porque...").
- No se exploraron decisiones de modelado de contenido de cero ni trade-offs de migración 6.x → AEMaaCS (porque admitió que no tiene esa experiencia).

**Observaciones:** El caso Dynamic Media y el de Clase Azul son las dos señales claras de pensamiento arquitectónico en la sesión. Hay madurez para autoidentificar errores del proceso (preventa, falta de capacitación al cliente) y para proponer mejoras concretas con datos. Lo que mantiene esta dimensión en 3 y no en 4 es que el rol de Tech Lead que ejerció fue acotado (3 meses, proyecto chico, equipo pequeño de 2 personas: un junior y un semi-senior frontend), y que el resto de las decisiones que mencionó son operativas más que arquitectónicas.

### Calidad de Código & Buenas Prácticas (1-5): 2/5
- Confesión explícita: "mi dolor de cabeza siempre ha sido los unit testing". Usa la IA para que se los genere, y admite que "al ejecutarlos no los hacía bien".
- En Quidilla observó que "el coverage está muy mal" pero no apareció como dueño de mejorar esa métrica.
- Sí configuró pipelines de Cloud Manager con quality gates en Clase Azul, pero la postura fue de "viene por defecto" más que de configuración deliberada.
- No mencionó `JUnit`, `Mockito`, `SonarQube`, ni un proceso de `code review` sostenido.

**Observaciones:** Es la dimensión más débil del perfil, y la confesión sobre testing es la señal más preocupante para 12 años de Senior. La honestidad cuenta a favor — no infla, no inventa — pero para un rol de Architect AEM en 2026, no tener testing sólidamente integrado al flujo de trabajo es un gap que se carga al perfil, no se descuenta. Si Daniel entra a un equipo donde la disciplina de testing es parte del estándar, tendría que apoyarse en compañeros o subir su nivel deliberadamente.

### Debugging & Resolución Técnica (1-5): 3/5
- Caso WebP conversion (Seven/Quidilla): identificación del trigger (`upload` al DAM), implementación de `event listener`, manipulación del binario con librería de conversión, modificación de metadata + nueva subida al DAM. Solución técnicamente válida.
- Cuando Galvis le sugirió que la ruta más limpia hubiera sido un `process step` dentro del workflow `DAM Update Asset`, Daniel mostró que ya había modificado ese workflow ("Duplo") para detectar formatos específicos, y aterrizó bien la mecánica de `process steps` con clase Java propia. Conoce las dos rutas, aunque eligió la menos ortodoxa.
- En `JCR indexes` declaró miedo, no debugging.
- No se exploró un caso de debugging complejo en producción (replicación, dispatcher cache misses, NPEs intermitentes).

**Observaciones:** Hay método y al menos un caso técnico concreto con suficiente detalle para ser creíble. El gap es que casi todas las respuestas técnicas fueron descriptivas y no aparecieron procesos de debugging frente a problemas no vistos antes. Para un Senior, lo razonable hubiera sido subir más naturalmente a "esto es lo que haría si nunca lo hubiera visto" — eso no apareció.

### Amplitud del Stack (1-5): 3/5
- Backend AEM (`Sling Models`, `OSGi`, `Servlets`, `JCR API`, `Workflows`, `Listeners`): sólido y consistente con 12 años.
- `Dispatcher`: configurado desde cero al menos una vez.
- `Cloud Manager`: configuró pipelines en Clase Azul.
- `Content Fragments` + `GraphQL` + `persistent queries`: trabajado en Seven.
- `Dynamic Media`: propuesto y POC realizado en Bridgestone.
- `BigQuery`, `Adobe Campaign Standard`, `AWS Cognito` del CV: no se exploraron por tiempo.
- Frontend: declarado como no-foco. Hace lo necesario pero no lo prefiere.
- `EDS`, `App Builder`: gap confesado.
- IA / agentic: principalmente para generar boilerplate de componentes (XML, HTML, content.xml, tabs, fields) y para tests (con resultado mixto). No usa agentes para tareas complejas.

**Observaciones:** La amplitud real es coherente con un Senior backend AEM con 12 años de exposición a múltiples proyectos. No es un perfil de Architect cross-stack en el sentido moderno (EDS + App Builder + Universal Editor) — es un Senior AMS/Cloud clásico. Para roles en proyectos AEM tradicionales encaja sin problema; para los proyectos donde Adobe Studio está apostando hoy (EDS + App Builder), hay un gap real que requeriría plan de upskilling con tiempo dedicado.

---

## Notas por Pregunta Técnica

### Pregunta 1:
**Pregunta:** ¿Has hecho migraciones de AEM On-Premise hacia AEMaaCS?
**Respuesta:** Aclaró honestamente que la planeación sí ("toda la cuestión de planificación y estimaciones, usé la herramienta que Adobe proporciona para ver qué tiene tu proyecto, qué actualizar, librerías a refactorizar, etc."), pero la ejecución "quedó en papel" porque el cliente no compró por costos de licencia. "Nunca he hecho así como una migración de On-Prem hacia cloud, no, nunca."
**Evaluación:** 2/5
**Observaciones:** Honestidad valorada. Pero el ítem aparecía como uno de los claims fuertes del CV y se desinfla aquí. Lo que sí validó es que conoce qué actividades entran en la estimación de una migración (contenido en/no productivo, componentes obsoletos, librerías deprecadas, dispatcher rules, integraciones frontend) — eso es nivel competente teórico.

### Pregunta 2:
**Pregunta:** En Clase Azul, ¿qué fue lo más diferente respecto a trabajar en AEM 6.5? ¿Cuál fue la decisión de arquitectura más difícil?
**Respuesta:** Clase Azul fue greenfield (cliente venía de Drupal/PHP), no migración On-Prem → Cloud. Como Tech Lead durante 3 meses, tuvo que configurar pipelines de Cloud Manager (dev/preprod/prod), dispatcher desde cero, manejo de `secret keys`. La decisión más difícil fue de proceso, no de arquitectura: "primero levantaría la mano y diría que la planeación de 3 meses para migrar todo un sitio era imposible".
**Evaluación:** 3/5
**Observaciones:** Hay experiencia real en AEMaaCS, pero acotada a un proyecto chico en 3 meses con un equipo de 2 personas. La autocrítica sobre el proceso es madura y muestra aprendizaje. Lo que no apareció fue una decisión arquitectónica concreta dentro de Clase Azul que justifique el título de "led the website redesign" del CV.

### Pregunta 3:
**Pregunta:** ¿Cómo configurarías los pipelines de Cloud Manager y los quality gates?
**Respuesta:** En Clase Azul configuró los pipelines por branch para tres ambientes. Mencionó que el coverage y quality gates "ya vienen por default cuando estás haciendo deploys en versiones stage y producción, son obligatorios". También mencionó los archivos de configuración para calcular coverage y métricas internas.
**Evaluación:** 3/5
**Observaciones:** Conoce el flujo. La postura es más de "uso lo que viene" que de "configuro deliberadamente para mi proyecto". Para un Senior se esperaría más ownership del pipeline.

### Pregunta 4:
**Pregunta:** ¿Cómo obtendrías información de una página (metadata) desde un Sling Model?
**Respuesta:** "Primeramente sería el resource, el recurso. De ahí ya lo puedes mapear al objeto que necesites — ya sea una clase en particular o un objeto en sí y regresarlo al frontend."
**Evaluación:** 4/5
**Observaciones:** Respuesta correcta y directa. Es la pregunta donde mejor se vio el músculo backend natural.

### Pregunta 5:
**Pregunta:** ¿Te ha tocado consumir APIs internas como la de Assets para procesamiento automático?
**Respuesta:** Caso concreto en Seven (Quidilla): el cliente quería que todas las imágenes se subieran en formato WebP, no en JPG/PNG (por tamaño y performance en móvil). Daniel implementó un `event listener` sobre el `upload` del DAM que detecta la imagen, la copia al servidor, usa una librería de conversión (mencionó "CPMGP" — probablemente confundido con ImageMagick o similar), convierte a WebP, modifica metadata (`título`, `formato`, `tipo`, `ubicación`) y vuelve a subir el asset. "Solo funciona para ciertos sitios, no para todos."
**Evaluación:** 4/5
**Observaciones:** Solución técnicamente válida con suficiente detalle para ser creíble. Hay método. Cuando Galvis sugirió que una ruta más "AEM-nativa" sería un `process step` dentro del workflow `DAM Update Asset` ("Duplo"), Daniel reconoció haber modificado ese workflow para detectar formatos específicos, y aterrizó bien el patrón de `process step` con clase Java propia. Conoce las dos rutas; eligió la menos ortodoxa pero defendible.

### Pregunta 6:
**Pregunta:** ¿Cómo manejas configuraciones por ambiente y secrets?
**Respuesta:** Para configuraciones: carpetas `config.author.dev`, etc., con configs `OSGi` por `runmode`. Para secrets en on-prem/AMS: encriptado vía `AEM Secret Kit` — encriptas el valor, pegas el resultado en el `.config` por ambiente. Para Cloud: secret keys nativos. Cuando Galvis mencionó integraciones con Azure Key Vault como alternativa, Daniel no lo conocía y reconoció que esas son "las dos únicas formas que conozco y las dos únicas que he usado".
**Evaluación:** 3/5
**Observaciones:** Patrón estándar y correcto. Falta amplitud (no conoce integraciones externas tipo Vault/KMS).

### Pregunta 7:
**Pregunta:** ¿Te ha tocado modificar índices JCR?
**Respuesta:** "La verdad muy poco. Le tengo miedo porque sí es un caos. Modificas un índice y te sale mal, ya perdiste todo tu contenido de DAM. He usado la sintaxis que ofrece la documentación de reindexar nada más, pero ni agregar ni quitar índices. Es como hacer un delete sin el where. Si tengo que hacerlo, lo hago, pero prefería no hacerlo."
**Evaluación:** 2/5
**Observaciones:** Honestidad clara, pero gap relevante para 12 años Senior. Reindex no es modificar índices — es ejecutar un comando documentado. Para un Architect AEM se esperaría haber definido al menos un Lucene index custom para resolver un problema de query.
.

### Pregunta 8:
**Pregunta:** ¿Has trabajado con GraphQL y persistent queries?
**Respuesta:** "Sí, precisamente en Seven. Creabas el Content Fragment y creabas el persistent query hacia ese contenido directamente, lo exponías y ya quedaba ahí." Confirmó que trabajó modelado de entidades, identificación de dominio y esquemas de GraphQL.
**Evaluación:** 3/5
**Observaciones:** Hay experiencia real, pero la descripción es operativa más que arquitectónica. No mencionó estrategia de caché, invalidación al cambiar contenido, ni trade-offs entre persisted queries vs queries ad-hoc.

### Pregunta 9:
**Pregunta:** ¿Conoces Edge Delivery Services?
**Respuesta:** Lo confundió inicialmente con headless. Galvis aclaró que es "la nueva forma que tiene Adobe ahora, más cliente, donde cambia la forma en cómo se desarrollan, la estructura es completamente diferente". Daniel: "No lo he visto."
**Evaluación:** 1/5
**Observaciones:** Cero exposición. Galvis le indicó al cierre que es justamente donde Adobe Studio está orientando los proyectos nuevos.

### Pregunta 10:
**Pregunta:** ¿Conoces App Builder?
**Respuesta:** "No."
**Evaluación:** 1/5
**Observaciones:** Cero exposición. Es la pieza complementaria a EDS para la capa de integraciones — Galvis le explicó la relevancia al cierre.

### Pregunta 11 (caso arquitectónico):
**Pregunta:** ¿Algún ejemplo de decisión de arquitectura propia con impacto medible?
**Respuesta:** Para el cliente Firestone/Bridgestone propuso migrar todo el contenido del DAM a `Dynamic Media`. La justificación nació de datos de Analytics: consumo mayoritariamente móvil con imágenes de 30-40 MB. Hizo POC, comparó performance vs estado actual, el cliente validó que efectivamente había mejora. La compra final no se cerró por costo de licencia (tenían infraestructura on-prem propia y subir a cloud era costoso), pero la propuesta técnica fue aprobada.
**Evaluación:** 4/5
**Observaciones:** Es la respuesta más sólida de la sesión en términos de pensamiento arquitectónico. Hay datos, POC, comparativa y narrativa de stakeholders. Para 12 años Senior se esperaría una decisión que sí se hubiera implementado en producción, pero el ejemplo es válido.

### Pregunta 12 (Tech Lead):
**Pregunta:** Si hoy te tocara el mismo reto de Clase Azul, ¿qué harías diferente?
**Respuesta:** "Primero levantaría la mano y diría que es imposible una migración en 3 meses dependiendo del contenido y sitio. Ver qué tienes en tu equipo, ver qué PM tienes — el que me tocó fue cero ayuda — plantear una solución a mediano plazo, programar 10 componentes a la semana. Capacitar al cliente que no sabía nada de AEM, y eso no lo gestionaba el PM, lo gestioné yo con el Tech Director negociando 2-3 semanas de capacitación a cambio de margen extra. Todo el problema pudo haberse solucionado desde la preventa."
**Evaluación:** 4/5
**Observaciones:** Autocrítica madura, claridad sobre dónde estuvo la falla, y diferenciación entre "problema técnico" y "problema de proceso/negocio". Para un Senior es la actitud correcta. El detalle de que negoció directamente con el Tech Director margen extra a cambio de capacitación es señal positiva de liderazgo real, no solo nominal.

### Pregunta 13 (uso de IA):
**Pregunta:** ¿Cómo está usando IA en tu día a día?
**Respuesta:** "Muy poco." Uso principal: generar unit tests para Sling Models (admite que "no los hace bien al ejecutarlos"). Creó un agente propio para generar boilerplate de componentes (estructura XML, HTML, `.content.xml`, carpetas) y le agregó lógica para crear tabs y fields. "Ya no pierdo 10 minutos de mi vida copiando uno y pegándolo."
**Evaluación:** 2/5
**Observaciones:** Uso real pero superficial. Está en el primer estadio (asistente para tareas repetitivas), no en copiloto interactivo ni en programación agéntica. Para un Senior en 2026 esto está retrasado respecto a la curva del equipo de Adobe Studio.

---

## Impresión Técnica General

**Fortalezas técnicas principales:**
- 12 años de AEM con núcleo backend (`Sling Models`, `OSGi`, `Servlets`, `Resource Resolver`, `Workflows`, `event listeners`) sostenido con naturalidad en conversación.
- Buen caso de listener + workflow para conversión WebP: muestra que conoce el motor de workflow (`process steps`) y la API de DAM.
- Experiencia real en AEMaaCS greenfield (Clase Azul): configuración de dispatcher desde cero, pipelines de Cloud Manager por ambiente, manejo de `secret keys`.
- Caso arquitectónico sólido en Firestone/Bridgestone con `Dynamic Media`: datos, POC, comparativa y narrativa de stakeholders.
- Autocrítica madura sobre Clase Azul como Tech Lead: separa "problema técnico" de "problema de preventa/proceso" y articula concretamente qué haría diferente.
- Postura honesta y consistente: no infla el CV, reconoce gaps (testing, índices, EDS, App Builder), admite cuando una respuesta es por preparación de examen vs experiencia real.
- Experiencia con `Content Fragments` + `GraphQL persistent queries` en Seven (Quidilla).

**Gaps técnicos identificados:**
- **Testing es la zona más débil del perfil:** "mi dolor de cabeza siempre ha sido los unit testing", uso de IA para generarlos con resultado mixto, observación pasiva del bajo coverage en Quidilla. Para 12 años Senior esto pesa.
- **Migración On-Prem → AEMaaCS:** el claim del CV se aclaró como "quedó en papel" — solo planning con la herramienta de Adobe, no ejecución. La experiencia real en cloud es greenfield (Clase Azul, proyecto chico, 3 meses).
- **`EDS` y `App Builder`: gap total.** Justo donde Adobe Studio está concentrando los proyectos nuevos según mencionó Facundo al cierre.
- **`JCR indexes`: gap declarado.** Solo reindex con sintaxis de documentación, nunca definió un índice custom. "Le tengo miedo... no me atrevería."
- Frontend declarado como no-foco — coherente con perfil backend, pero limita amplitud.
- Sin certificaciones en 10+ años (no se exploró el por qué en esta sesión).
- Tenure plana sin ascensos sostenidos en 12 años — solo VMLY&R como Tech Lead duró 4 meses (no se exploró el por qué). El rol de Tech Lead en Clase Azul también duró ~3 meses.
- Uso de IA en estadio 1 (asistente repetitivo) — retrasado respecto al equipo de Adobe Studio que ya está en copiloto/agéntico.

**¿Nivel real coincide con lo declarado en CV?** [ ] Sí | [x] Parcialmente | [ ] No

**Recomendación técnica:** [ ] Strong Hire | [x] Hire | [ ] No Hire | [ ] Strong No Hire

**Justificación:** Daniel tiene una base técnica real y consistente en AEM backend, sostenida por 12 años con un historial de proyectos diversos (Royal Caribbean, Okta, Clase Azul, Seven/Quidilla, Firestone) y al menos dos casos técnicos sólidos en la sesión (conversión WebP en DAM y propuesta de Dynamic Media). La postura honesta — no infla el CV, reconoce gaps cuando los hay, separa lo que sabe por estudio de lo que sabe por hacer — cuenta a favor.

El problema es la combinación de varios gaps moderados que, sumados, atenúan la calibración de Senior AEM en 2026: testing como debilidad declarada, índices JCR con miedo explícito, `EDS` y `App Builder` desconocidos, el claim de migración On-Prem → Cloud que se aclaró como "quedó en papel", uso de IA en estadio 1, y un patrón de tenure plana sin ascensos sostenidos.

Lo marco como **Hire**, no Strong Hire, por dos razones: (1) la base técnica AEM se sostiene pero los gaps en la dirección hacia donde se mueve Adobe Studio (EDS + App Builder + disciplina de testing) son reales y van a requerir upskilling deliberado; (2) el patrón profesional de Daniel sugiere un Senior backend competente y honesto, pero no un Architect con ambición de empujar la práctica — lo cual no es un problema para roles AMS/Cloud existentes en cuentas en curso (Qydiya, Royal Caribbean), pero sí lo sería para liderar un proyecto greenfield Cloud + EDS desde cero.

Encaje natural: Senior backend AEM en cuentas existentes (AMS o AEMaaCS estable), con espacio para crecer hacia EDS si hay plan de capacitación con tiempo dedicado. No encaja hoy como Tech Lead/Architect en proyectos nuevos donde la práctica de Adobe Studio está concentrando esfuerzo.
