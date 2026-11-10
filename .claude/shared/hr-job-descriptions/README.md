# HR job descriptions

Frozen Markdown copies of the HR job descriptions (Descripciones de cargo) the suite uses, converted on 2026-10-27 from the `.docx` named in each file's `source`. Read these copies, never the originals. A JD takes from one only what the handbook does not cover (the source order is in `staffing-jd`).

## Files

Individual contributors are `<track>-<level>.md`:

| Track prefix | Platform the document assumes |
|---|---|
| `backend-` | Adobe Commerce (Magento) |
| `frontend-` | Adobe Commerce (Magento) |
| `aem-backend-` | AEM |
| `aem-frontend-` | AEM |

Levels: `semi-senior-ii`, `senior-i`, `senior-ii`, `experience-senior-i`, `experience-senior-ii`.

Leadership roles: `technical-lead-i.md`, `technical-lead-ii.md`, `software-architect.md`, `technical-manager.md`, `dxp-technology-director.md`. Most of them also assume Adobe Commerce.

Map a P&L seniority or handbook level to its HR job description through `level-equivalence.md`.

## What to take

The documents are in Spanish; whatever a JD takes from them is written in English. Take exactly these:

- Knowledge and requirements: `CONOCIMIENTOS ESPECÍFICOS DE LA POSICIÓN` (required and desirable technical knowledge, specific skills, certifications).
- Years: `Años de experiencia requeridos`, which matches `level-equivalence.md`.
- Responsibilities: `RESPONSABILIDADES CLAVES` (the "Qué debe hacer" column), which feeds the JD's "What the person will do".

Everything else stays out, notably KPIs (`INDICADORES DE GESTIÓN`), the reporting line (`ORGANIZACIÓN`, `Cargo jefe inmediato`), authority (`AUTORIDAD`) and the English level, which follows the suite's B2 rule.

Adobe Commerce and Magento items (Magento years, KnockoutJS, UI Components, Fastly) are the platform part of a document: take them only for a Position on Adobe Commerce.
