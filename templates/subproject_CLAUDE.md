# CLAUDE.md — {{PROJECT_NAME}}

## Knowledge base (read-only)

Shared base via symlink `knowledge/ → ../knowledge` (read-only). Own project file: `knowledge/projects/{{PROJECT_NAME}}.md`. Rules (reading, writing, knowledge export, `/ask-knowledge`) → parent `CLAUDE.md`, "Rules in sub-projects".

## Lab book
Dated entries, experiment logs and running notes → `Laborbuch.md`, not in this file, which stays lean.

## Overview

_One paragraph: what this project is, what question it answers, and what comes out of it (one paper, a method, a dataset). Name the boundary to neighbouring projects._

## Data and code

_Where the input data lives and what format it has. Which script does what. If raw data sits outside the workspace, point at `data/raw_manifest.md`._

## Reproduction

_Which script regenerates the numbers reported below, and from which stored data file. Leave empty until a real analysis exists; do not describe an intended one._

```
# e.g. python analysis/evaluate.py   → figures/ + Output.txt
```

## Current results

_The canonical numbers. This section, not the lab book, is the source of truth for what is currently true. Every value here must be reproducible via the command above._

## Open work

- [ ] _active items_

### Parked

> _Items deliberately not being worked on, with the reason. Parked is not deleted: the reason is often the finding._

## Knowledge Export

_(Findings proposed for the shared base. Nothing is entered here without the user having decided and commented — see parent `CLAUDE.md`. Sync from here via `/sync-knowledge`.)_
