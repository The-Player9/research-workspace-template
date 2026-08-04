# Sync Knowledge — project findings into the shared base

Transfers approved findings from the sub-projects into `knowledge/`, and keeps the index current. Run from the workspace root.

The transfer is a **handover between two stores**: without a note written back, the project session cannot know what has already been taken over, and the same points get offered again or tracked by hand.

## First run

If `knowledge/` is missing or incomplete, create what is missing before scanning, then say so in the report:

```
knowledge/
├── INDEX.md      — entry point, structure tree, sub-project table, excluded list
├── insights.md   — cross-project scientific findings (with a keyword index at the top)
├── methods.md    — reusable technical lessons (keyword index at the top)
└── projects/     — one file per sub-project
```

Each file gets its header line stating what belongs in it and at which level of abstraction. An empty base without those lines becomes a dumping ground.

## 1. Scan for projects

- List the directories in the workspace root, excluding `knowledge/` and hidden directories.
- **Exclude** everything on the "excluded from knowledge sync" list in `knowledge/INDEX.md`: archives, meta-projects, grant applications. These get no knowledge file and no index entry.
- For each remaining directory, check whether `knowledge/projects/<name>.md` exists. Report which projects are new and which are known.

## 2. Read project context

For each project: read its `CLAUDE.md`, glance at the directory structure, and compare the current state against the stored summary.

**Specifically check the `## Knowledge Export` section.** Its content is already user-approved (nothing enters that section without the user having decided and commented), so anything there that is not yet reflected in `knowledge/projects/` counts as a **pending transfer**, and the project is marked as changed. **Carry the user's comment along**: it is their framing of the finding and must not be lost at the handover.

Classify each candidate as **scientific** (a result, finding or mechanism you would cite in a paper) → `insights.md` plus the project file's results section, or **technical** (how something is done, what works and what does not) → `methods.md` plus the project file's methods section.

## 3. Check each candidate before writing

Mandatory on every run; this is the core job.

1. **Find existing coverage.** Grep the candidate's keywords and obvious synonyms across `insights.md`, `methods.md`, **all** `projects/*.md` and the project's own `CLAUDE.md`.
2. **Classify:** *new* (add), *duplicate* (skip), *refinement* (edit in place, do not append a second entry).
3. **Handle contradictions explicitly, never silently.** Collect each into a **conflicts** list with the topic, both statements verbatim, their locations (`file:section`) and, where derivable, which is newer (a project `CLAUDE.md` usually beats an older central entry, but confirm). Do **not** write a contradicting candidate; leave both sinks untouched and let the user decide.
4. **Base-wide consistency pass — occasionally, not every run.** A full scan for drift that crept in earlier: the same claim stated differently in two project files, a central entry disagreeing with the project file that links to it. It is expensive, so run it only when the user asks, or when roughly five syncs have passed since the last one (track this in `knowledge/sync_log.md`). Otherwise skip it and say so in the report, naming the date of the last full pass.

## 4. Write

- **New project:** create `knowledge/projects/<name>.md` in the same shape as the existing ones: what it is, current status, scientific results (generalised statement plus mechanism, **no** detail numbers), methods and lessons (the how, including the numbers that back it), key files, connections, deadlines.
- **Changed project:** update in place, preserving what is still accurate.
- **Level of abstraction, the rule that keeps the base readable:** scientific entries carry the generalised conclusion and its mechanism, not measurement tables. Concrete values belong in the methods section or in the project's own files. When in doubt, shorten an existing entry rather than append detail.
- **Keyword index:** extend the alphabetical index at the top of the file with genuinely new keywords; reuse existing ones instead of inventing near-synonyms.

## 5. Update the index

Update `knowledge/INDEX.md`: new rows in the sub-project table, the structure tree if files were added, the excluded list if it changed, and the "last updated" date of every file you touched.

## 6. Leave the parent `CLAUDE.md` alone

The workspace inventory lives in `INDEX.md`, not in the parent file. Change the parent `CLAUDE.md` only when a rule itself changed.

## 7. Write the sync note back

After every run **with transfers**, note in the sub-project's `## Knowledge Export` section what was taken over and when, so the next session in that project can see it.

This is not a violation of "sub-project files are never overwritten from the parent level": that rule protects the **substantive** project context. Permitted here is only the status note plus the correction of references that this run itself made stale. Overview, status and results sections stay untouched.

## 8. Log and report

Append one row to `knowledge/sync_log.md`: number, date, the added/refined/skipped balance, whether a full scan ran, and a one-line note on any conflict. If a full scan ran and verified the whole base, reset the log to a single baseline row.

Report: projects scanned, new and changed ones, transfers per sink, **conflicts** (these first, if any), whether the full consistency pass ran or was skipped, and which sub-project files received a sync note.
