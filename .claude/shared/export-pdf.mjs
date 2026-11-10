#!/usr/bin/env node
// Export one staffing artifact to PDF, next to its source: node export-pdf.mjs <artifact.md>
// Rules in export.md. Rendering goes through `npx md-to-pdf`.
import { copyFileSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { basename, dirname, join, resolve } from 'node:path';
import { spawnSync } from 'node:child_process';

// The origins a JD Requirement may carry (staffing-jd). Only these are stripped,
// so other inline code in a JD survives the export.
const ORIGINS = [
  'handbook role', 'handbook level', 'handbook platform', 'HR job description',
  'Propuesta', 'presales', 'supplied JD', 'hiring lead', 'suite rule',
];

// [[key, value], ...] from a YAML frontmatter block. Indented or `- ` lines
// continue the previous key, so a block list becomes one comma-separated value.
function splitFrontmatter(md) {
  const m = md.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n?/);
  if (!m) return { fields: [], body: md };
  const fields = [];
  for (const line of m[1].split(/\r?\n/)) {
    const kv = line.match(/^([A-Za-z_][\w-]*):\s*(.*)$/);
    if (kv) fields.push([kv[1], kv[2].trim().replace(/^\[(.*)\]$/, (_, items) => items.split(/\s*,\s*/).join(', '))]);
    else if (line.trim() && fields.length) {
      const last = fields[fields.length - 1];
      const item = line.trim().replace(/^-\s*/, '');
      last[1] = last[1] ? `${last[1]}, ${item}` : item;
    }
  }
  return { fields, body: md.slice(m[0].length) };
}

// Artifacts whose PDF shows no frontmatter: their `opportunity` slug is
// `<client>-<project>`, and these two anonymise the client.
const ANONYMISED = new Set(['jd.md', 'interview-guide.md']);

// The Markdown that opens the PDF in place of the frontmatter, which md-to-pdf
// would otherwise swallow as its own config: every field, so the PDF describes itself.
function pdfHeader(file, fields) {
  if (ANONYMISED.has(file) || !fields.length) return '';
  const cell = (s) => s.replace(/\|/g, '\\|');
  return ['| Field | Value |', '|---|---|', ...fields.map(([k, v]) => `| ${cell(k)} | ${cell(v)} |`)].join('\n');
}

function stripForRecruiting(body) {
  const tag = `\`\\[(?:${ORIGINS.map((o) => o.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('|')})\\]\``;
  return body
    .replace(new RegExp(`(?:[ \\t]*${tag})+[ \\t]*$`, 'gm'), '')
    .replace(/^> \*\*Off-handbook:\*\*.*(?:\r?\n>.*)*(?:\r?\n)*/m, '');
}

const arg = process.argv[2];
if (!arg || !arg.endsWith('.md')) {
  console.error('usage: node export-pdf.mjs <artifact.md>');
  process.exit(2);
}
const src = resolve(arg);
const file = basename(src);
const name = basename(src, '.md');

let { fields, body } = splitFrontmatter(readFileSync(src, 'utf8'));
if (file === 'jd.md') body = stripForRecruiting(body);
const header = pdfHeader(file, fields);

const work = mkdtempSync(join(tmpdir(), 'staffing-export-'));
try {
  const tmp = join(work, file);
  writeFileSync(tmp, header ? `${header}\n\n${body}` : body);
  const run = spawnSync('npx', ['--yes', 'md-to-pdf', tmp], { stdio: 'inherit' });
  if (run.status !== 0) process.exit(run.status ?? 1);
  const pdf = join(dirname(src), `${name}.pdf`);
  copyFileSync(join(work, `${name}.pdf`), pdf);
  console.log(pdf);
} finally {
  rmSync(work, { recursive: true, force: true });
}
