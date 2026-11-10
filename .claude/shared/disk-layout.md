# Disk layout

Where every artifact and kept input lives. `<root>` is the tree root (`conventions.md`, Tree root).

```
<root>/
  opportunities/<client>-<project>/
    opportunity.md                        # staffing-jd
    <Proposal, P&L, brief, supplied JD>   # kept inputs, any name
    status-<YYYY-MM-DD>.md (+ .pdf)       # staffing-status; earlier dates kept
    <position-slug>/
      jd.md (+ jd.pdf)                    # staffing-jd
      shortlist.md                        # the hiring lead's; Claude edits it only as dictated
  people/<first>-<last>/
    <CV, public profile, internal history>                    # kept inputs, any name
    <op>--<position>/                                         # one Candidate
      match-evaluation.md (+ .pdf)                            # staffing-match
      debrief.md (+ .pdf)                                     # staffing-debrief, one per Candidate
      <take-home report copy, screening notes, English result># kept inputs, any name
      interviews/<YYYY-MM-DD>/                                # one per Interview
        interview-guide.md (+ .pdf)                           # staffing-interview-guide
        <transcript, notes, brought Scorecards>               # one file per Interviewer, any name
```

- Person-first: everything about a person sits in `people/<p>/`, including an internal Candidate's earlier Debriefs in their other Candidate folders. `opportunities/` holds no personal data beyond Shortlist names and Status summaries.
- One person considered for two Positions is two Candidate folders under one person folder.
- A second Interview gets its own `interviews/<YYYY-MM-DD>/` with its own Interview guide. The Debrief stays one per Candidate.
- The tree is the whole state: no status folders, no pipeline CSV, no separate candidate profile. The CV analysis lives only in the Match evaluation, and `staffing-status` derives each Candidate's Stage from which files exist.

## Naming

- Folders and files are in English. Generated artifacts have the fixed names above; inputs keep any name.
- Slugs are kebab-case ASCII: an Opportunity is `<client>-<project>`, a Position comes from its title, a person is `<first>-<last>`. A numeric suffix only on collision. Dates are ISO (`YYYY-MM-DD`).
- A Candidate folder is `<op>--<position>`: the Opportunity slug, a double dash, the Position slug.

## Frontmatter

Skills follow the path; the frontmatter makes a forwarded or exported file describe itself.

| Artifact | Fields |
|---|---|
| `opportunity.md` | `opportunity`, `updated` |
| `jd.md` | `opportunity`, `position`, `updated` |
| `match-evaluation.md` | `opportunity`, `position`, `person`, `candidate_kind` (`internal` or `external`), `date`, `jd_updated` |
| `interview-guide.md` | the five fields of `match-evaluation.md`, plus `interviewers` |
| `debrief.md` | the five fields of `match-evaluation.md`, with `date` as the last update, plus `interviewers` (every Interviewer across the Interviews) and `interviews` (the Interview dates, which are their folder names) |
| `status-<YYYY-MM-DD>.md` | `opportunity`, `date` |

## `shortlist.md`

An ordered list, one Candidate per line, in the hiring lead's order:

```
1. <person-slug>: <note>
2. <person-slug>: <note>
```
