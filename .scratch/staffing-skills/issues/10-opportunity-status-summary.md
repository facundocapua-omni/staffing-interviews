# Oportunidad status summary

Type: grilling
Status: resolved
Blocked by: none
Map: [Staffing skills suite](../map.md)

## Question

What does the status summary of an Oportunidad look like, so the hiring lead can see what is done and what is pending and pass a status on to management (dirección)?

It is generated on request and saved as `opportunities/<op>/status-<YYYY-MM-DD>.<ext>` (see [Disk layout of the chain](02-chain-disk-layout.md)). Decide:

- The share format: Excel or PDF, and whether a Markdown source sits next to it as for the other artifacts.
- Its content for management: per Posición and per Candidato, the stage derived from which artifacts exist, what is pending, and dates.
- How it shows the Shortlist (the hiring lead's order) and the unordered comparison table of Candidatos per requirement. If [Evaluación de match rubric](05-match-evaluation-rubric.md) is still open, agree the table's shape here and record it there.
- What it must never show, given the no-verdict rule and that management reads it.

From [Evaluación de match rubric](05-match-evaluation-rubric.md), the comparison table's shape is fixed:
- rows: Requisitos in the JD's order with their tier, plus Logistics;
- columns: Candidatos in alphabetical order, never by fit;
- cells: the Nivel de evidencia;
- no totals or counts;
- a stale column is marked in its header.

Still for this ticket: whether and how the status summary shows the table.

From [Unified Debrief](08-debrief.md), what a Debrief offers the summary:
- One `debrief.md` per Candidato at `people/<p>/<op>--<pos>/`; its frontmatter `interviews` lists the Entrevistas it covers.
- The Decision is a dated list, newest first. Its latest Outcome (Advance / Advance with conditions / Another interview / Do not advance) is the hiring lead's; an empty latest entry means pending.
- Calificaciones still marked `Proposed:` are unconfirmed; open Discrepancias have an empty Resolution.

## Answer

Grilled 2026-10-21/22. Terms resolved in [GLOSSARY.md](../../../GLOSSARY.md): Etapa (Stage), Resumen de estado (Status summary).

**Audience and format**

- One document, written for management (dirección). The hiring lead reads it too and may edit the `.md` before exporting. There is no separate working view.
- It is always a picture of the current state. It does not compare with a previous summary and has no free section for the hiring lead: the suite feeds management's process, not the other way round.
- Markdown source `opportunities/<op>/status-<YYYY-MM-DD>.md`, exported as `status-<YYYY-MM-DD>.pdf` on request, like the JD, the Guía and the Debrief. Not Excel: there is nothing to compute, and a spreadsheet invites sorting by columns, which is a ranking by another name.
- Each run writes a new dated file. Earlier ones are kept; a second run on the same day overwrites that day's file.
- One Oportunidad per summary. A portfolio view across Oportunidades is out of scope.
- In English, like every deliverable.

**Etapa** (derived from the files, never stored)

| Stage | When |
|---|---|
| Not evaluated | The Candidato folder `<op>--<pos>/` exists without `match-evaluation.md`. |
| Evaluated | `match-evaluation.md` exists, and no Entrevista is planned. |
| Interview planned | An `interviews/<YYYY-MM-DD>/` has its Guía and no transcript. |
| Interviewed | An Entrevista has a transcript whose date is not yet in the Debrief's `interviews`. |
| Debriefed | The Debrief covers every Entrevista with a transcript, and its latest Decision entry is empty. |
| Decided | The Debrief's latest Decision entry is filled in. |

- With several Entrevistas, the stage of the latest is shown with its number ("Interview 2 planned").
- A latest Outcome of *Another interview* stays Decided until the next Guía exists, with a pending item "Another interview decided, not planned"; then it is "Interview 2 planned".
- The Shortlist is not an Etapa: it is a separate column, since a Candidato may be interviewed before being shortlisted.
- The summary ends at the hiring lead's decision. Offer, acceptance, onboarding and an internal's assignment are outside the suite, so it never says a seat is covered.

**Document** (`status-<YYYY-MM-DD>.md`)

1. **Header:**
   - frontmatter `opportunity` and `date` only, since it covers a whole Oportunidad;
   - client (named), project and dates, from `opportunity.md`;
   - the fixed line *"Status derived from the files on <date>. Not a hiring recommendation."*
2. **Overview:** one line per Posición, in `opportunity.md`'s order:
   - role · level · platform;
   - headcount;
   - the start date needed, from the P&L;
   - Candidatos per Etapa;
   - the decisions recorded.
3. **Per Posición:**
   - the JD's `updated` date and whether it was exported;
   - a table of **every** Candidato of the Posición, including those off the Shortlist and those already Decided. Shortlisted ones come first in the hiring lead's order, then the rest alphabetically, never by fit;
   - its pending items.

Columns of the Candidato table:

- **Candidate:** name, internal or external. A person who is a Candidato in two Posiciones appears in both, with "also Candidate for <Posición>".
- **Shortlist:** the hiring lead's position (#1, #2…) or "—".
- **Stage.**
- **Last change:** a date.
- **Available from:** from the Evaluación de match's Logistics. It sits next to the Posición's start date with no judgment ("at risk") added.
- **Decision:** the hiring lead's latest entry, as Outcome · Calibrated level · date · Decided by. Justification, Conditions and Next steps stay in the Debrief.

**Pending items** (facts, never advice, each with "since <date>" and no computed waiting time)

- No JD, or a JD not exported.
- No Candidates.
- An Evaluación de match stale against the JD.
- An Entrevista whose date has passed with no transcript.
- A transcript the Debrief does not cover yet.
- Decision pending.
- English result missing.
- Evaluated Candidatos neither on the Shortlist nor decided.
- Another interview decided, not planned.

Discrepancias with an empty Resolution and Calificaciones still `Proposed:` stay inside the Debrief: they are the hiring lead's work, and in front of management they hint at how a Candidato did.

**Never shown**

- Calificaciones, `Proposed:` or confirmed.
- Niveles de evidencia, Puntos a indagar, credibility observations.
- Counts of Requisitos or Dimensiones ("8/11"). Process counts (Candidatos per Etapa, decisions recorded) are allowed: they count stages, not evidence.
- CV content beyond the name and internal/external; salary.
- The hiring lead's notes in `shortlist.md`.
- The comparison table per Requisito: it stays an on-request output for the hiring lead, not stored. A Requisito × Candidato matrix in front of management invites counting cells.
- Any Claude wording that judges a Candidato ("strong profile", "risky").

**Client name**

- The summary names the real client: it goes to internal management, and the folder slug already does. It is the second artifact that does, after `opportunity.md`; the JD and the Guía stay anonymised.

**Handed to other tickets**

- [Disk layout of the chain](02-chain-disk-layout.md): amended with the status file's name, export and frontmatter.
- [Skill boundaries](03-skill-boundaries.md): which skill writes the Resumen de estado and the comparison table.
- Purging a person is not done for now, so status snapshots are never scrubbed: out of scope on the [map](../map.md).
