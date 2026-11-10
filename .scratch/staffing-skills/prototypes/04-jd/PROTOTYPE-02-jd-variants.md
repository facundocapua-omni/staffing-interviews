> **PROTOTYPE, throwaway.** Three radically different JDs for the same Posición, to react to. Source line: P&L line 6 in the [intake analysis](PROTOTYPE-01-intake-analysis.md), "Web UI Developer, Sr, Colombia" → **Frontend Developer · Senior Level 1 · Contentful**.
>
> Each requirement carries its origin tag:
> - `[HB]`: handbook role (`roles/frontend.md`).
> - `[HB-L6]`: handbook level (`career-paths/frontend.md`, `career-levels.md`).
> - `[HB-CF]`: handbook platform (`roles/frontend.md` By platform + `technologies/contentful.md`).
> - `[PROP]`: the proposal.
> - `[OLD]`: old Omni JD (years).
> - `[RULE]`: suite rule (English).

---

# Variant A: Handbook mirror

```yaml
opportunity: expedia-partner-web-contentful
position: frontend-developer-senior
updated: 2026-10-21
level: L6 Senior Level 1
platform: Contentful
```

## Frontend Developer · Senior Level 1 · Contentful

**Mission** `[HB]`: Build and maintain the user-facing experience (functional, performant and accessible interfaces) for a headless Contentful platform.

**Posición context** `[PROP]`
- A US-based global travel company is migrating four partner-facing websites from AEM to Contentful.
- A new Next.js front end serves all four sites from one reusable component library on the client's AWS account.
- Multi-locale: up to 19 locales per site.

**Responsibilities**
- Implement page, section and block components from Figma designs on the client's React design system. `[HB]` `[PROP]`
- Own the project's frontend architecture decisions: component structure, rendering strategy (ISR/SSR), performance budget. `[HB-L6]`
- Make performance and accessibility trade-off calls (bundle size, WCAG conformance) without escalating. `[HB-L6]`
- Integrate with the Contentful Delivery and Preview APIs, including live preview and on-demand revalidation on publish. `[HB]` `[PROP]`
- Implement locale routing, hreflang and analytics/consent parity with the current sites. `[PROP]`
- Write component, unit and end-to-end tests for the UI layer. `[HB]`

**Requirements**

| Requirement | Kind | Origin |
|---|---|---|
| HTML/CSS/JS fundamentals | Must | `[HB]` |
| React in production | Must | `[HB]` `[HB-CF]` |
| Next.js (App Router), fully decoupled from the CMS | Must | `[HB-CF]` `[PROP]` |
| Responsive, accessible UI (WCAG) | Must | `[HB]` |
| REST/GraphQL API integration | Must | `[HB]` |
| Frontend testing (Playwright or equivalent) | Must | `[HB]` |
| Headless CMS integration, Contentful preferred | Must | `[HB-CF]` |
| ISR/SSR and cache revalidation strategies | Must | `[PROP]` |
| Internationalisation: locale routing, hreflang | Must | `[PROP]` |
| 5+ years of experience | Must | `[OLD]` |
| English B2+ (client-facing) | Must | `[RULE]` |
| Tailwind CSS | Nice | `[PROP]` |
| Building on a corporate design system's React components | Nice | `[PROP]` |
| Contentful App Framework / live preview | Nice | `[HB-CF]` `[PROP]` |
| Next.js on AWS (OpenNext, Lambda, S3, CloudFront) | Nice | `[PROP]` |

**Reports to** `[HB]`: Tech Leader. **Decides**: implementation within the agreed design and architecture. **Escalates**: design ambiguities, blockers, scope or estimate risks.

---

# Variant B: Recruiting brief (one page, for sourcing)

## Senior Frontend Developer: Next.js + headless CMS · LATAM (Colombia), remote

**In one line**: a senior React/Next.js engineer who will build a multi-site, multi-language front end on a headless CMS (Contentful) for a US travel company.

**Knock-out criteria** (all required)
- [ ] 5+ years in frontend, 2+ with React in production `[OLD]` `[HB]`
- [ ] Next.js in production, App Router preferred `[HB-CF]` `[PROP]`
- [ ] Has consumed a headless CMS (Contentful, Sanity, Strapi, Storyblok…) `[HB-CF]`
- [ ] English B2+: will talk to the client daily `[RULE]`
- [ ] Accessibility and web performance are part of their work, not an afterthought `[HB]` `[HB-L6]`

**Strong plus**: Contentful specifically · Tailwind · i18n / multi-locale sites · Playwright · Next.js on AWS (OpenNext, Lambda) · working on a corporate design system.

**What they'll do**: build the component library for four sites from Figma; decide rendering and caching per page; connect the editors' live preview; ship with tests.

**Search keywords**: `Next.js` `App Router` `React` `Contentful` `headless CMS` `ISR` `SSR` `Tailwind` `i18n` `hreflang` `Playwright` `design system` `OpenNext` `AWS Lambda`

**Screening questions for recruiting**
1. "Tell me about a Next.js site you shipped: how were pages rendered and refreshed when content changed?" A good answer names ISR or SSR and revalidation, or webhooks.
2. "Which headless CMS have you used, and what did you build against it?" A good answer names a content model, the APIs used and preview.
3. "How do you check accessibility before release?" A good answer names WCAG, tooling and manual checks.

**Not a fit if**: only Angular/Vue · only monolithic CMS theming (WordPress/AEM templates) with no decoupled front end · no production Next.js.

**Logistics**: LATAM (Colombia), remote · full-time · start Jan 2027.

---

# Variant C: Company HR format, adapted (EN, no KPIs, no signatures)

## JOB DESCRIPTION: FRONTEND DEVELOPER SENIOR I (CONTENTFUL)

**Position identification**
- Name: Frontend Developer Senior I
- Area: Digital Experience Platforms Business Unit
- Reports to: Technical Lead
- Opportunity: AEM → Contentful migration, partner web

**Mission**: Drive the development and evolution of decoupled, performant and accessible front ends on Contentful, aligned with the client's design system and business goals.

**Key responsibilities**

| What | What for |
|---|---|
| Develop the Next.js component library from Figma with minimal supervision | One library serves four sites consistently |
| Decide the rendering and caching strategy per page (ISR/SSR) | Fast pages that refresh within seconds of a publish |
| Integrate the Contentful Delivery and Preview APIs, including live preview | Editors see exactly what visitors will get |
| Implement locale routing and hreflang | Correct experience and SEO in every locale |
| Write unit and E2E tests; take part in code reviews | Quality and maintainability |
| Estimate tasks and advise on technical decisions | Realistic planning, fewer delivery risks |

**Specific knowledge**
- Years of experience: **5** · English: **B2**
- Required: HTML5, CSS3, JavaScript/TypeScript; React and Next.js (App Router); headless CMS integration (Contentful); REST/GraphQL; responsive and accessible UI (WCAG); Playwright or equivalent; Git.
- Desirable: Tailwind; design-system-based development; Contentful App Framework; Next.js hosting on AWS (OpenNext).
- Skills: effective communication with an English-speaking client; problem analysis; estimation; critical thinking.

**Authority**: decides implementation details within the agreed design and architecture; escalates design ambiguities, blockers and scope risks.

**Interactions**: Tech Leader, backend developers, QA, client design and Web Ops teams.
