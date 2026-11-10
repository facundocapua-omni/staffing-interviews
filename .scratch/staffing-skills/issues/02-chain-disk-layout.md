# Disk layout of the chain

Type: grilling
Status: resolved
Blocked by: none
Map: [Staffing skills suite](../map.md)

## Question

How are Oportunidades, Posiciones, Candidatos and their artifacts laid out under `~/Workspace/leadership/staffing/` so each skill finds the output of the previous step?

The layout must handle:

- One Candidato evaluated against several Posiciones, possibly in different Oportunidades.
- Internal and external Candidatos.
- An optional `candidate-takehome-review` report (today it writes to `<repo>/reviews/<candidate-or-branch>-<YYYY-MM-DD>.md`).
- Notes or scorecards from several Entrevistadores for one interview.
- Whether a per-Candidato profile file (like the existing "Candidate Profile" template) exists separately from the Evaluación de match.
- Whether a pipeline tracking file (today each workspace keeps a `pipeline-summary.csv`) exists, and what it holds. See the Debrief "Tracking" conflict in the [inventory findings](../research/01-existing-staffing-material.md).

Also decide naming conventions (slugs, dates) and the metadata each artifact carries to link back to its Posición and Candidato.

## Answer

Grilled 2026-10-21. Terms resolved in [GLOSSARY.md](../../../GLOSSARY.md): Candidato, Colaborador, Candidato interno/externo, Shortlist, Posición headcount.

> **Amended by [Unified Debrief](08-debrief.md)** (2026-10-22). There is one Debrief per Candidato, consolidating every Entrevista: `people/<p>/<op>--<pos>/debrief.md` (+ `debrief.pdf`), next to `match-evaluation.md`. `interviews/<YYYY-MM-DD>/` keeps the Guía and the transcript, notes or Scorecards of that Entrevista, but no Debrief. The Debrief's frontmatter adds `interviews`, the list of Entrevista dates it covers.

> **Amended by [Oportunidad status summary](10-opportunity-status-summary.md)** (2026-10-22). The status summary is `opportunities/<op>/status-<YYYY-MM-DD>.md` (+ `.pdf` on request); earlier dated files are kept. Its frontmatter is `opportunity` and `date` only. It names the real client, like `opportunity.md`. Purging a person is out of scope for now, so status files are never scrubbed.

> **Amended by [Skill boundaries](03-skill-boundaries.md)** (2026-10-27). Every input is kept next to what it feeds and identified by content: files under their original names, pasted text as `pasted-<YYYY-MM-DD>.md`. The Propuesta, the P&L and any brief or supplied JD go to `opportunities/<op>/`, so the P&L, with its rates, lives in `opportunities/`. The tree root is the first folder, from the working directory upward, that holds `opportunities/` or `people/`; when there is none, a skill that writes asks before creating them. Claude edits `shortlist.md` only as dictated, through `staffing-match`.

**Domain**

- A **Candidato** is one person considered for one Posición: the same person in two Posiciones is two Candidatos. A **Colaborador** is an employee; a Candidato is internal when the person is a Colaborador, fixed per Candidato because it changes over time. The person has no domain term; on disk they are a `people/` folder.
- A Posición may have several seats (headcount) and still has one JD.
- An Evaluación de match is always against one Posición. Fitting one person to several Posiciones means one evaluation per Posición.
- The **Shortlist** is the hiring lead's ordered list of Candidatos for a Posición. Claude never orders it; it offers an unordered comparison table, generated on request and not stored.

**Layout** (root `~/Workspace/leadership/staffing/`)

```
opportunities/<client>-<project>/
  opportunity.md                    # Oportunidad context
  status-<YYYY-MM-DD>.<ext>         # status summary, generated on request
  <position-slug>/
    jd.md (+ jd.pdf)                # frontmatter `updated:`
    shortlist.md                    # hiring lead's order + one note per Candidato
people/<first>-<last>/
  <CV, public profile, internal history>   # any name, identified by content
  <opportunity>--<position>/               # one Candidato
    match-evaluation.md                    # records `jd_updated`
    <take-home report copy>                # optional; candidate-takehome-review unchanged
    interviews/<YYYY-MM-DD>/
      interview-guide.md
      <transcript, notes, scorecards>      # one file per Entrevistador, any name
      debrief.md (+ debrief.pdf)
```

- Person-first: everything about a person, including an internal Candidato's previous Debriefs, sits in one folder, and purging a person is deleting `people/<p>/` and removing them from Shortlists. `opportunities/` holds no personal data except Shortlist names and status summaries.
- One subfolder per interview; a second round is another subfolder with its own Guía and Debrief.
- No status folders, no pipeline CSV, no separate candidate profile file. Stage is derived from which artifacts exist; the CV analysis lives only in the Evaluación de match.

**Naming and metadata**

- Folders and files in English. Generated artifacts have fixed names; inputs you bring keep any name and are identified by content.
- Slugs are kebab-case ASCII: Oportunidad `<client>-<project>`, Posición from its title, person `<first>-<last>`. Numeric suffix only on collision. ISO dates.
- Every generated artifact carries frontmatter `opportunity`, `position`, `person`, `candidate_kind: internal | external`, `date`; the Guía and the Debrief add `interviewers`. The path is the link skills follow; the frontmatter makes a forwarded or exported file self-describing.
- When `jd_updated` in a match evaluation differs from the JD's `updated`, the skill flags the evaluation as stale and never re-evaluates on its own.

**Format**

- Markdown is the source of every artifact, since the chain reads it back.
- Whatever goes to other people is exported next to its source on request, same name, other extension: the JD and the Debrief as PDF, the status summary in the format its own ticket picks.

**Handed to other tickets**

- The Oportunidad status summary is a new output; the destination was widened for it: [Oportunidad status summary](10-opportunity-status-summary.md).
- Who writes `opportunity.md`: [JD structure](04-jd-structure.md).
- Whether recruiting data (salary, availability) is kept: [Evaluación de match rubric](05-match-evaluation-rubric.md).
- Scorecard file names if the suite generates them: [Scorecards: dimensions and scale](06-scorecards.md).

