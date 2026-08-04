# Knowledge Base — Index

Shared base for **domain** knowledge across sub-projects. Read for cross-project work; single-project tasks do not need it. Read/write rules → parent `CLAUDE.md`, "Rules in sub-projects".

## What goes where

| File | Content | Level of abstraction |
|---|---|---|
| `insights.md` | scientific findings and mechanisms, across projects | the generalised statement plus its mechanism (the *what* and *why*), **no** raw measurement tables |
| `methods.md` | reusable technical lessons: what works, what does not, and at which settings | the *how*, including the numbers that back it |
| `projects/<name>.md` | one file per sub-project: current state, scientific results, method lessons | mirror of the project's `## Knowledge Export`, condensed |
| `learnings/` | **process** knowledge: how work is done in this workspace | see `learnings/00_INDEX.md` |

Rule of thumb: an insight about *the field* → `insights.md` / `methods.md`; an insight about *how we work* → `learnings/`.

## Structure

```
knowledge/
├── INDEX.md          — this file
├── insights.md       — cross-project scientific findings
├── methods.md        — reusable technical lessons
├── learnings/        — process knowledge
└── projects/         — one file per sub-project
```

## Sub-projects

| Directory | Topic | Status | In knowledge sync |
|---|---|---|---|
| _(filled by `/sync-knowledge`)_ | | | |

## Excluded from knowledge sync

Directories that are not research projects and must be skipped entirely (no knowledge file, no index entry):

- _(add as needed, e.g. archives, meta-projects, grant applications)_
