# Templates

Two artifacts, both in English. Angle brackets are placeholders; drop any optional section that does not apply, along with its heading.

## `opportunity.md`

The intake analysis plus the hiring lead's answers. With the Status summary, it is the only artifact that names the real client.

````markdown
---
opportunity: <client>-<project>
updated: <YYYY-MM-DD>
---

# <Client>: <project>

## Context

- **Client:** <name; how it is sold, e.g. through a partner; internal or external>
- **Project:** <one line>
- **Workstreams:** <one bullet each: scope, dates, who staffs it>
- **Dates:** <start → end; the P&L's month mapping, e.g. Month 1 = Nov 2026>
- **Stack signals:** <by layer, as the Proposal states them>
- **Locations:** <from the P&L or the material>

## Sources read

- <file name>: <what it is; the parts read and the parts skipped>
- Supplied JD <file name>: supplied by <the hiring lead | the client | Presales>
- Handbook: <the pages read>
- HR job descriptions: <the files read>

## P&L lines → Positions

| # | P&L line (role · seniority · location) | Position (handbook role · level · platform) | Headcount | Start | JD | Flags |
|---|---|---|---|---|---|---|
| <n> | <Globant role · seniority · location, or "none (no P&L)"> | <role · level · platform, or "n/a"> | <n, or "open"> | <Mon YY, or "open"> | <`<position-slug>/jd.md` or "no: <reason>"> | <flags, or "none"> |

## Inconsistencies found

1. <what disagrees with what, citing both sources>

## Intake answers

1. <the question, in English> **Answer:** <the hiring lead's answer>
2. <the question> **Open:** no answer yet. Waiting on it: <the Requirements or rows that wait>
````

## `jd.md`

The recruiting brief. Its PDF export strips the origin tags and the off-handbook note, so both must keep exactly this form: tags in backticks closing the line, and a blockquote opening with `> **Off-handbook:**`.

````markdown
---
opportunity: <client>-<project>
position: <position-slug>
updated: <YYYY-MM-DD>
---

> **Off-handbook:** <which part of the base the handbook lacks: the platform, the role>. <Where those Requirements came from: the Proposal, the hiring lead's confirmed answers, an HR job description>.

# <Handbook role> · <Level> · <Platform>

**Location:** <country or region; remote or on site, or "To be confirmed">

<One line: who this person is and what they will build, with the client described, not named, e.g. "a US-based global travel company".>

## Must have

- [ ] <Requirement> `[<origin>]` `[<origin>]`

## Nice to have

- <Requirement> `[<origin>]`

## What the person will do

- <Responsibility> `[<origin>]`

## Search keywords

`<keyword>` `<keyword>` `<keyword>`

## Screening

1. "<Question for recruiting to ask>" A good answer mentions <what>.
2. Check in the CV or profile: <what, and what it should show>.

## Not a fit if

- <A profile recruiting can spot that lacks a Must have, at the Must have's strength>

## Logistics

- **Location:** <country or region | To be confirmed>
- **Remote:** <remote | hybrid | on site | To be confirmed>
- **Start:** <Mon YYYY | To be confirmed>
- **Full-time:** <the employment, not the project allocation>
````

Notes on the JD:

- The off-handbook note appears only when the base is incomplete.
- The title uses the handbook's names: `Frontend Developer · Senior Level 1 (L6) · Contentful`, `Tech Leader · Senior Level 3 (L8) · Sitecore`.
- The slug comes from the title: `frontend-developer-l6-contentful`.
- Every screening question and every "Not a fit if" line traces back to a Must have or Nice to have above it.
