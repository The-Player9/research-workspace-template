# Research Workspace Template

A Claude Code workspace for **long-running scientific work**: several parallel research projects, one shared knowledge base, and a set of rules that keep the context files small enough to load every session.

This is a **template repository**, not a library and not a framework with a support promise. Copy it, run the init skill once, and it becomes your workspace.

## Quickstart

1. Use this template on GitHub (or copy the folder), open it with Claude Code.
2. Run `/init-workspace`. It asks for a preset and up to eight questions, then writes your `CLAUDE.md`, the `knowledge/` scaffolding and the skills your profile needs.
3. Run `/new-subproject` for your first project.
4. Work. Write findings into the project's `Laborbuch.md` as they happen; condense stable conclusions into its `CLAUDE.md`.

## The five ideas this encodes

1. **Two memory files per project, not one.** `CLAUDE.md` holds the stable context and is loaded every session, so it must stay lean. `Laborbuch.md` holds the dated log: experiments, intermediate numbers, dead ends and why they failed. It is read only when the history is actually needed. Without this split the context file grows into a diary and becomes both expensive and unreadable.
2. **Domain knowledge and process knowledge are different things.** `knowledge/` collects cross-project scientific findings; `knowledge/learnings/` collects how you work: recurring pitfalls, checklists, tool lessons. Every countermeasure is additionally written **where it takes effect**, otherwise the lesson sits in a file nobody opens at the moment it is needed.
3. **Reported numbers must be reproducible.** Every number in a manuscript comes from a script run against a stored data file. The analysis lives in exactly three files: one that generates the expensive intermediates, one that produces every figure and writes `Output.txt` with the manuscript location of each number, and one with shared helpers.
4. **Writing follows a fixed pipeline.** Numbers final, then a storyline decided by you, then section-by-section drafting, then a citation check, then an adversarial review in a fresh context, then your own final pass. The adversarial review is a separate step on purpose: the context that wrote the draft cannot see its own gaps.
5. **Answer from documented sources first.** Project docs, code and manuscripts before model knowledge. If something is not documented, that gets said out loud, and general knowledge is marked as such. You must always be able to tell where a statement came from.

## What you get

```
CLAUDE.md                  your workspace rules, written by the init skill
knowledge/                 shared base: findings, methods, process learnings
.claude/commands/          init-workspace, new-subproject, sync-knowledge,
                           ask-knowledge, review-adversarial, ask-literature
templates/                 copy-in shapes for sub-projects, guard rails, manifests
examples/                  a runnable demo project and one filled-in instance
CHANGELOG.md               framework versions; what an update would change
```

Modules are switched on by your answers at init: long-running jobs, publishing,
grant proposals, external raw data, a house library, a literature RAG. What you
do not switch on is not written, so the rules you carry are the ones you use.

## See it work in one minute

```
cd examples/demo-project/analysis
python generate.py     # 15 intermediates, written atomically
python generate.py     # writes nothing: "15 already present" — that is resumability
python evaluate.py     # Output.txt, every number labelled with where it appears
```

The numbers in `examples/demo-project/CLAUDE.md` are the real output of those
scripts, and its `Laborbuch.md` shows the shape of a working log: a result, a
correction, and a dead end kept with its reason.

## Design constraints worth knowing

- **Everything lives inside the workspace folder.** Nothing persistent outside it, so the whole thing can move between machines without loss. Links into the shared knowledge base are relative symlinks. Multi-GB raw data is the documented exception and is recorded in a manifest instead.
- **The closest doc wins on local details**, but no sub-project file may weaken the workspace-wide rules.
- **Guard rails, not a doc hierarchy.** A folder gets its own small `CLAUDE.md` only when it carries a rule whose forgetting causes damage: frozen paper code, non-final numbers, legacy code. Not because the folder has its own purpose.

## Licence and third-party software

Copyright (c) 2026 Martin Hohmann. Skills and example code: **MIT** (`LICENSE-MIT`). Documentation and rule texts: **CC BY 4.0** (`LICENSE-CC-BY-4.0`, full legal code included).

If you build on the rule texts, the attribution line is:

    Based on "Research Workspace Template" by Martin Hohmann, licensed CC BY 4.0.

This repository contains no third-party code. The optional literature module expects **PaperQA2** (`paper-qa`, FutureHouse, Apache-2.0) to be installed by you via pip; it is never redistributed here, and neither are your PDFs or your index.

## Scope

This is a template, not a product. There is no support promise, no versioned API and no upgrade automation beyond `/init-workspace` proposing what changed. Fork it, cut what you do not need, and keep the version marker so a later update is still deliverable.
