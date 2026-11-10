# Export to PDF

Export only when the hiring lead asks. Each skill exports its own artifact: `jd.md`, `match-evaluation.md`, `interview-guide.md`, `debrief.md`, `status-<YYYY-MM-DD>.md`.

Run the script next to this file:

```
node <folder of this file>/export-pdf.mjs <path/to/artifact.md>
```

It writes the PDF next to its source, with the same name and the `.pdf` extension, and prints the PDF's path. It renders through `npx md-to-pdf`, which downloads on first use.

- The PDF carries the same content as the source, `Proposed:` prefixes included. Its frontmatter opens the PDF as a table, except in `jd.md` and `interview-guide.md`: their `opportunity` slug names the client they anonymise.
- `jd.md` is the one exception: recruiting sees only confirmed Requirements, so the script strips every origin tag and the off-handbook note. For the script to find them, write them exactly so in `jd.md`:
  - origin tags close the Requirement's line, one backticked tag per source: `` `[handbook platform]` `[Propuesta]` ``;
  - the off-handbook note is a blockquote whose first line opens with `> **Off-handbook:**`.
- `debrief.md`: before running the script, read the latest Decision. When it is empty, warn the hiring lead and ask before exporting.
