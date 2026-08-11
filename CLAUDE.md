<!-- TEMPLATE SKELETON — these are NOT active rules for the surrounding workspace. Placeholders are filled by /init-workspace when this repo is used as a workspace of its own. -->
<!-- workspace-framework: 0.1.4 | profile: {{PRESET}} | lang-notes: {{LANG_NOTES}} | lang-pub: {{LANG_PUB}} | modules: {{MODULES}} | source: https://github.com/The-Player9/research-workspace-template -->

# Research Workspace — Parent CLAUDE.md

Main memory file of this workspace: several research sub-projects in {{FIELD}}, each with its own `CLAUDE.md`.

## Portability: everything inside the workspace

**All data, notes and configuration live inside this folder**, so it can move between machines without loss of information. Nothing persistent outside it (no global memory files, no auto-memory store). Links to the shared `knowledge/` base use **relative** symlinks (`knowledge/ → ../knowledge`).

{{#IF RAW_DATA_EXTERNAL}}
**Raw-data exception:** very large raw datasets (multi-GB) stay on the acquisition machine or NAS; the workspace then holds only derived data (`data/derived/`) plus a **`data/raw_manifest.md`** in the sub-project, listing per dataset its location, acquisition date, size and the script that produced it (otherwise the workspace cannot be traced back to its source after a transfer).
{{/IF}}

## Memory: four stores

Persistent information lives in exactly four places.

- **`CLAUDE.md`** (parent + one per sub-project) — stable project context, structure, design decisions, rules, current status. Loaded every session, so **keep it lean**.
- **`Laborbuch.md`** (one per sub-project) — chronological: dated entries (`## YYYY-MM-DD`), experiment logs, intermediate results, failed attempts, running TODOs. Read only on demand.
- **`knowledge/`** — cross-cutting **domain** knowledge (insight about *the field*): mechanisms, results, method recipes.
- **`knowledge/learnings/`** — **process** knowledge (insight about *how we work*): entry point `knowledge/learnings/00_INDEX.md`; not loaded automatically, the triggers sit as one-liners in this file. Reachable from every sub-project through the `knowledge/` symlink.

How these files relate, what is loaded when, and where a given piece of information belongs → `knowledge/learnings/05_layout.md`, **read once at setup**.

### Rules

- **Writing:** day-to-day notes go into `Laborbuch.md`, **not** into `CLAUDE.md`; newest entry on top. The lab book is **updated without asking on every piece of news**: a new analysis, a new finding, a correction of an older one, a methodological pitfall, a discarded approach and why. Once something becomes a stable conclusion or decision, condense it **briefly** into `CLAUDE.md`; the detail stays in the lab book. What an entry contains, why a correction is a new entry rather than an edit, and how this file stands next to a paper lab book → `knowledge/learnings/06_labbook.md`, **read once at setup**.
- **Reading:** before substantive work on a sub-project, read its `CLAUDE.md` first; pull `Laborbuch.md` only when the history is needed.
- **New sub-projects:** run `/new-subproject` → `knowledge/learnings/50_new_subproject.md`, **read and follow it every time**.
- **Precedence on conflict:** the closest `CLAUDE.md` decides local working details; no sub-project file may weaken the workspace-wide rules (portability, knowledge-first, edit-don't-append, citation rules). Deliberate deviations must be marked as exceptions there and justified.
- **Guard-rail `CLAUDE.md` in subfolders:** only where a folder carries a rule whose forgetting causes damage (write ban, frozen paper state, non-final numbers, legacy code) — not because a folder has its own purpose. Three to five lines: the rule plus a pointer to the project `CLAUDE.md`, no index. It also applies when the project `CLAUDE.md` is not in context (long session, subagent given a direct path).

## Critical Rule: Knowledge-First Answering

Answer **first** from documented sources: `knowledge/`, sub-project `CLAUDE.md`, code, manuscripts. If the information is not there, **say so explicitly** ("this is not in the project documentation") and mark your own knowledge as such ("from my general knowledge"). Never silently mix project facts and your own assumptions.

## Critical Rule: Edit, Don't Append

Make changes by replacing or shortening existing text first, not by appending; keep the edit as small as possible. New text only where the content is genuinely new (lab-book entries, new citations, new work packages).

## Rules in sub-projects

Apply to **every** sub-project; stated only here, not duplicated in the project files.

- **Reading `knowledge/`:** read-only, consult before substantive tasks (knowledge-first). Entry point `knowledge/INDEX.md`; own project file `knowledge/projects/<name>.md`.
- **Writing `knowledge/`:** only when explicitly asked, entries short (2–3 sentences per insight), timestamp in `INDEX.md` updated. **Single exception:** `knowledge/learnings/40_error_catalog.md` may be extended without asking whenever a repeatable process error shows up. Otherwise: project-specific notes, decisions and TODOs into the project `CLAUDE.md`, dated entries into `Laborbuch.md`. Sub-project `CLAUDE.md` files are **never** overwritten from the parent level.
- **Knowledge export (ask first):** do **not** enter export-worthy findings yourself; propose them (1–2 sentences plus the intended sink: `insights.md` scientific / `methods.md` technical). The user decides and comments; only then does the finding go, **together with that comment**, into the `## Knowledge Export` section at the end of the project `CLAUDE.md`, from where `/sync-knowledge` picks it up.
- **Closeout pass:** at the end of every substantive task check — (i) lab-book entry written, (ii) do the results change numbers, status or TODOs in the project `CLAUDE.md`, (iii) export-worthy finding → export proposal (see above). State in one sentence which of these stores you deliberately did **not** touch, and why.
- **Cross-project lookup:** call `/ask-knowledge` (also on your own initiative) as soon as a question reaches beyond the current sub-project. For published third-party literature use `/ask-literature` instead (explicit request only, incurs cost).
{{#IF LONGRUNNERS}}
- **Long runs checkpoint themselves**: every long-running job (training, data generation, sweeps) writes intermediate state to disk continuously and can resume after a crash → `knowledge/learnings/10_longrunners.md`, **read before starting such a run**.
{{/IF}}
{{#IF PUBLISHING}}
- **Papers: reproducible numbers, analysis in exactly three files**: every reported number producible by script from a stored data file; the analysis split into a generation script, an evaluation script (writes `Output.txt` with the manuscript location of each number) and shared helpers → `knowledge/learnings/20_reproducibility.md`, **read when setting up a paper analysis**.
{{/IF}}

{{#IF PUBLISHING}}
## Writing conventions (workspace-wide)

Conventions for **every** scientific text. Fill these in for your own venue; the shipped example instance shows one filled-in variant.

- Spelling: {{SPELLING}}. Citation style: {{CITATION_STYLE}}. Format: {{DOC_FORMAT}}.
- **One main thought per sentence**, in every text type, papers as much as proposals. No multiply subordinated constructions; two sentences beat one sentence with two subordinate clauses. A longer sentence carries no more information, it spreads the same information over more words. Set a concrete target length in words and record it here, because a rule without a number does not survive a long drafting session.
- **No filler sentences.** Cut anything that only announces, transitions, or asserts that something is important, and keep the substance as a statement of its own. Test: delete the sentence; if the text does not lose a claim about the subject matter, it stays deleted. A frame sentence that does carry a finding is rewritten to state the finding, not kept as a frame.
- **Grade interpretations honestly.** Measured things as findings, inferred things with hedging ("it is assumed", "likely", "consistent with", "cannot be conclusively explained").
- **Citations are content-bound**, never by author name and never as a bare bundled citation: attach each `\cite{}` to a specific claim named in the sentence.
- **Cite only published or preprinted work.** Unpublished own manuscripts are mentioned in the text and shown as a figure, without a citation.
- **Pipeline:** numbers final → storyline (decided by the user) → draft section by section → citation check → `/review-adversarial` in a fresh context → final pass by the user. Details → `knowledge/learnings/30_paper_kickoff.md`, **read before the first draft**.
{{#IF GRANTS}}
- **Funding proposals:** additional rules (work-package objectives state what will be known, with the number on the validation criterion; no repetition across sections; justification duty; risk section) → `knowledge/learnings/60_grant_proposal.md`, **read before the first line of a proposal**. The conventions above apply there as well.
{{/IF}}
{{/IF}}

{{#IF HOUSE_LIB}}
## House code library `{{LIB_NAME}}`

Own **code** library (`import {{LIB_IMPORT}}`), meaning functions written in this group. Not to be confused with the literature collection, which holds papers written by other people and is queried with `/ask-literature`. For matching code tasks, **check first whether a `{{LIB_NAME}}` function already exists** instead of writing something new. Keep its API reference in `knowledge/{{LIB_NAME}}.md` up to date when the library changes.
{{/IF}}

## Knowledge system

Shared base in `knowledge/`, entry point `knowledge/INDEX.md`: structure tree, `insights.md` (scientific) vs. `methods.md` (technical), sub-project table, excluded-from-sync list. **Read only for cross-project work.** Read/write rules → "Rules in sub-projects".

## Custom skills

Defined in `.claude/commands/<name>.md`.

| Skill | Purpose |
|-------|---------|
| `/init-workspace` | Sets this workspace up. Runs once; refuses to run again. |
| `/update-workspace` | Brings this workspace to a newer framework version: untouched rule files updated and reported, edited ones asked about, follow-up decisions written down as TODOs. |
| `/new-subproject` | Creates a sub-project: symlink, empty `Laborbuch.md`, `CLAUDE.md` header block. |
| `/sync-knowledge` | Scans project directories, updates `knowledge/projects/` and `INDEX.md`. |
| `/ask-knowledge` | Cross-project lookup in `knowledge/`; may be called autonomously. |
| `/review-adversarial` | Reviewer-2 pass over a manuscript, in a fresh context. |
{{#IF LITERATURE_RAG}}
| `/ask-literature` | Question answered from the literature collection, meaning other people's papers (external service, incurs cost, explicit request only). |
{{/IF}}
