# How the memory files relate

Read this once when setting up, and again whenever it is unclear where something belongs. Everything here is mechanism, not preference.

## The three levels of `CLAUDE.md`

**1. Parent `CLAUDE.md`** (workspace root) — the rail. Workspace-wide rules, conventions, the memory model. Loaded in **every** session, in every sub-project. That is why it must stay lean: everything written here is paid for in every future conversation. Rules that only apply sometimes live in `knowledge/learnings/` and are referenced here by a single trigger line ("read this file before X").

**2. Sub-project `CLAUDE.md`** (one per project folder) — the project's stable context: what the project is, where its data and code are, how to reproduce its numbers, what the current results are, what is open. Loaded when work happens in that folder. It is the **canonical source of the current numbers**; the lab book holds how they came about.

**3. Guard-rail `CLAUDE.md`** (inside a specific subfolder) — three to five lines carrying one rule for that folder: frozen paper code, an archive that must not be modified, results that are not paper-valid, legacy code that is not on the active path. Created **only** where forgetting the rule causes damage, never merely because a folder has its own purpose.

The reason the third level exists: a rule that sits on line 200 of a long project file is loaded, but it competes with everything else in that file, and it is not loaded at all when a subagent is sent straight to a path. A guard rail is read exactly when someone touches that folder.

## What is loaded when

| File | When it enters context |
|---|---|
| Parent `CLAUDE.md` | every session |
| Sub-project `CLAUDE.md` | when working in that project |
| Guard-rail `CLAUDE.md` | when touching files in that folder |
| `Laborbuch.md` | only when explicitly read |
| `knowledge/`, `knowledge/learnings/` | only when explicitly read |

This table is the whole cost model. Anything you want always available goes into the parent file and must earn its place; anything else goes into a file with a documented trigger.

## Precedence

The closest document decides local working details. No sub-project file may weaken the workspace-wide rules (portability, knowledge-first, edit-don't-append, citation rules). A deliberate local deviation must be marked as an exception and justified where it stands, for example a venue whose style guide contradicts the house style.

## Where does this piece of information go?

| It is… | It goes to |
|---|---|
| a dated observation, an experiment log, a failed attempt and why | the project's `Laborbuch.md`, **without asking** |
| a stable conclusion or decision derived from the above | condensed into the project's `CLAUDE.md`; the detail stays in the lab book |
| a current number that a manuscript will report | the project's `CLAUDE.md`, "Current results", reproducible by the documented script |
| a finding that other projects would benefit from | proposed as a knowledge export; the user decides and comments, only then does it enter the export section |
| a lesson about how we work (a pitfall, a procedure, a tool trap) | `knowledge/learnings/`; if it is a repeatable process error, `40_error_catalog.md` may be extended without asking |
| a rule that must hold from now on | the appropriate `CLAUDE.md`, as one line, at the level where it applies; the change itself is logged in `70_changes.md` |

Two failure modes this table prevents: the project file slowly turning into a diary, and a lesson being filed somewhere that is not open at the moment it would be needed. The first row is the one used daily; how to fill it, and how it divides against a paper lab book, is in `06_labbook.md`.

## Working in subfolders

When a task touches files deep inside a project, the applicable chain is: parent `CLAUDE.md` → project `CLAUDE.md` → any guard rail on the path. Do not rely on memory of what those files said in an earlier session; the ones that are not auto-loaded must be read again.

When you delegate to a subagent with a bare path, only what lies **on** that path reaches it. That is the case guard rails are built for: if a folder carries a rule that must survive delegation, the rule belongs in that folder.

## The closeout pass

At the end of every substantive task: was the lab book written, do the results change numbers or status or TODOs in the project file, is there an export-worthy finding to propose. Then say in one sentence which of these you deliberately left untouched and why. The reporting half is the point: it makes a skipped step visible instead of silent.
