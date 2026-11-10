Escribí `opportunity.md` y los 6 JDs en `opportunities/expedia-contentful-migration/`, con las tus respuestas aplicadas. Los dos inputs están copiados en esa carpeta y los originales siguen en `inbox/`.

| P&L | JD |
|---|---|
| 4 · AEM Backend Sr 3 | `tech-leader-l8-contentful/jd.md` (7+ años, Tech Lead I) |
| 5 · AEM Backend Mid | `backend-developer-l5-contentful/jd.md` |
| 6 · Web UI Sr | `frontend-developer-l6-contentful/jd.md` |
| 7 · Web UI Mid | `frontend-developer-l5-contentful/jd.md` |
| 8 · AEM QC Sr | `qa-engineer-l6-contentful/jd.md` |
| 9 · DevOps Sr | `devops-engineer-l6-contentful/jd.md` |

Revisé los 6 archivos:
- **Tiers:** solo Must have y Nice to have, sin pesos.
- **Tags de origen:** cada Requisito y cada línea de "What the person will do" cierra con el suyo.
- **Inglés:** B2 en todos. No apliqué la excepción B1 a ninguna Posición.
- **Datos excluidos:** no hay allocation, tarifas ni costos.
- **Anonimización:** el cliente aparece como "a US-based global travel company". Busqué Expedia, EG, Vrbo, Escapia, EGDS, NBA, Cloud Gate Proxy, Babel Prime y Bernie, y no aparecen. El slug en el frontmatter sí nombra al cliente, pero el export no lo incluye en el PDF.

**Para que revises:**
1. **Workstream de la API:** sumé sus necesidades a los dos JDs de Backend, con este tier:
   - **Must have:** Contentful App Framework y la resolución de variantes por locale, tono y canal con fallback.
   - **Nice to have:** la integración con SFMC. Lo decidí así porque la API dura 8 semanas de un proyecto de 12 meses y Contentful con SFMC es un perfil escaso.

   Si SFMC tiene que ser Must have, lo cambio.
2. **Búsqueda (Algolia / Elasticsearch):** quedó como Nice to have en el Tech Leader y en Backend L5, como pediste.
3. **AEM:** entra como Nice to have en todos los JDs, por ser la plataforma de origen de la migración.
4. **Inicios:** no respondiste la pregunta 5. Quedó abierta en `opportunity.md` y los JDs usan los meses del Labor Estimate (Ene 2027 para Tech Leader, Frontend L6 y DevOps). Si se adelantan por el platform setup de Nov–Dic, lo actualizo.

¿Exporto los JDs a PDF?