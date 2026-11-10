Leí el brief, el handbook (rol Tech Leader, niveles) y las descripciones de cargo de Technical Lead I y II. Todavía no escribí ningún archivo: necesito tus respuestas antes de armar el JD.

## Lo que entendí del brief

- **Contexto:** un proyecto Sitecore que ya está en curso. El cliente es muy exigente, conoce bien la plataforma y tiene un equipo técnico propio fuerte. La persona entra con el proyecto andando, no arranca uno desde cero.
- **Qué querés priorizar:** (1) capacidad de liderazgo, (2) adaptabilidad para sumarse a mitad de camino, (3) resiliencia con clientes difíciles.
- **Material disponible:** solo el brief. No hay Propuesta ni P&L.

**Posición propuesta**

| # | Línea de P&L | Posición | Cantidad | Inicio | JD | Observaciones |
|---|---|---|---|---|---|---|
| 1 | no hay P&L | Tech Leader · Senior Level 3 (L8) · Sitecore | ? | ? | `tech-leader-l8-sitecore/jd.md` | Sitecore no está en el handbook |

**Qué cubre el handbook y qué no**

- **Rol y nivel:** sí están, en `roles/leader.md` y `career-levels.md`.
- **Plataforma:** el handbook no tiene una página de Sitecore y ninguna descripción de cargo habla de Sitecore (las de Technical Lead piden Magento y Adobe Commerce). Como tampoco hay Propuesta, los requisitos de plataforma salen solo de lo que confirmes en la pregunta 7. No voy a suponer qué stack usa el proyecto.

**Inconsistencias:** no encontré ninguna; hay una sola fuente.

## Preguntas

1. **Cliente y proyecto.** ¿Cómo se llaman? Los necesito para nombrar la carpeta de la Oportunidad (`<cliente>-<proyecto>`).
2. **¿El cliente es interno?** Si es externo, el nombre del cliente no aparece en el JD.
3. **Dónde guardar los archivos.** No hay carpetas de staffing (`opportunities/`, `people/`) ni en este directorio ni más arriba. ¿Las creo en `/Users/facundocapua/Workspace/leadership/staffing/tests/runs/staffing-jd/iteration-1/jd-off-handbook/sandbox/`? Ahí copio el brief (sin moverlo de `inbox/`) y escribo el JD.
4. **Nivel.** Como no hay P&L, te lo confirmo: ¿es un Tech Leader L8 que lidera personas? Si en realidad no tiene gente a cargo, sería un perfil individual de nivel L7.
5. **Experiencia mínima.** La descripción de cargo Technical Lead I pide 7+ años y la Technical Lead II pide 10+. ¿Cuál usamos?
6. **Datos de la búsqueda.** ¿Cuántas personas, desde cuándo, en qué país o región, y si es remoto, híbrido o presencial?
7. **Requisitos de plataforma.** Te dejo la redacción exacta con la que entrarían al JD. Para cada uno, decime si lo confirmás o lo cambiás, y si va como Must have (excluyente) o Nice to have (suma):
   - a. `Proposed: 7+ years of hands-on Sitecore development, including technical leadership on at least one Sitecore implementation`. Sugiero Must have, porque el cliente domina la plataforma. El número de años se ajusta a lo que respondas en la 5.
   - b. `Proposed: Strong C# / .NET and ASP.NET MVC experience on Sitecore`. Sugiero Must have.
   - c. `Proposed: Experience with Sitecore Headless (JSS / Headless SXA) and Next.js`. Must have o Nice to have según el proyecto.
   - d. `Proposed: Experience with Sitecore XM Cloud`. Must have o Nice to have según el proyecto.
   - e. `Proposed: Sitecore Developer certification`. Sugiero Nice to have.
   - f. **Clave para las tres anteriores:** ¿qué producto y arquitectura usa el proyecto? Las opciones son XP o XM tradicional (MVC), headless con JSS, o XM Cloud. Con eso defino c y d.
8. **Tus tres prioridades del brief.** Te propongo esta redacción, todas como Must have:
   - `Proposed: Has led a development team (people leadership, not only technical direction) on a client project`
   - `Proposed: Has joined a project already in flight and taken over technical leadership mid-delivery (onboarding to an existing codebase, decisions and team)`
   - `Proposed: Has worked with a demanding client that has its own strong technical team, holding technical positions and managing pushback constructively`

   ¿Las confirmás así, las cambiás, o alguna pasa a Nice to have?

Cuando respondas, armo `opportunity.md` y el JD. Lo que quede sin respuesta lo registro como pendiente en `opportunity.md` y no entra al JD.