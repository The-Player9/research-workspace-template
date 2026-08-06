# Changelog

Versions of the **framework**, meaning the rule set and the skills, not of any workspace built from it.

This file is what makes an update deliverable. `/init-workspace` writes the version into the marker at the top of your `CLAUDE.md`; on a later run it compares that version against this file and proposes only what changed since. Without the marker and without this changelog, a template can be copied but never updated.

Each entry states what a user must **decide**, not only what moved. Format: `Added` / `Changed` / `Removed`, with the affected file in brackets.

## 0.1.2 — 2026-08-06

**Changed** [`CLAUDE.md`, `examples/filled-instance/README.md`, `knowledge/learnings/30_paper_kickoff.md`, `knowledge/learnings/60_grant_proposal.md`]

- The writing conventions gain two rules that hold for every text type: one main thought per sentence, and no filler sentences, with a deletion test for the second. Both sit in the core `CLAUDE.md`, so they apply without anyone opening a learnings file.
- The example instance no longer asks for "long, densely argued prose paragraphs". It asks for dense paragraphs, states that "prose" means "not a bullet list" and nothing more, and carries a concrete sentence-length target of 20 to 25 words.
- Grant proposals get a register section of their own: short main clauses, justifications in separate sentences, no sentence that announces the next one, and a word budget agreed per work package before drafting.

**Why:** the rule set described the paper register with the words "long" and "prose", and a drafting model reads that as permission to pad. The result was proposal text whose sentences ran past forty words and whose paragraphs opened with a sentence about the aim rather than a statement of it. Naming the failure mode is not enough, because "long, densely argued" contains its own contradiction: the fix is to ask for density and to state the sentence length as a number.

**Decide, if you are updating from 0.1.1:** set your own sentence-length target and write it into the writing conventions of your `CLAUDE.md`. The 20 to 25 words in the example instance are one group's choice, not a framework default. If your conventions currently use the word "prose" anywhere, decide which of the two meanings you intend and say so in the same line.

**Not done, deliberately:** the sentence target is not a `{{PLACEHOLDER}}` filled by `/init-workspace`. A style target is a decision a group makes after reading its own drafts, not at setup time, and a placeholder would force an answer at the one moment when nobody has evidence for it.

## 0.1.1 — 2026-08-04

**Changed** [`.claude/commands/sync-knowledge.md`, `knowledge/learnings/50_new_subproject.md`]

- The exclusion list in `knowledge/INDEX.md` is now stated as the **only** place where a postponed knowledge file survives. Step 1 of the sync says so explicitly, and the sub-project procedure names it as the place such a decision belongs.

**Why:** a project can reasonably want to exist without a `knowledge/projects/` file for a while, and the obvious place to record that is the project's own `CLAUDE.md`. The sync never read it there. It checks whether the file exists, and creates one for every directory that is not excluded, so the next run would quietly overturn the decision and produce a knowledge entry for a project with nothing to hand over.

**Decide, if you are updating from 0.1.0:** check whether any of your projects postponed their knowledge file with a note in their own `CLAUDE.md`. Move that decision onto the exclusion list, marked as temporary, before your next sync. Nothing else changes; no file moves, no rule is removed.

**Not done, deliberately:** the alternative was to have the sync read a marker such as `<!-- no-knowledge-file -->` in the project's `CLAUDE.md`. That would put the decision where it is made, but it creates a second place where a sync decision can live, which is the kind of duplicate store this framework argues against everywhere else.

## 0.1.0 — 2026-08-04

Initial release. Everything below is new; there is nothing to migrate.

**Core rules** [`CLAUDE.md`]
- Four stores: parent `CLAUDE.md`, per-project `CLAUDE.md`, per-project `Laborbuch.md`, shared `knowledge/` with a `learnings/` subtree.
- Lab book written without asking on every piece of news; stable conclusions condensed into `CLAUDE.md`.
- Knowledge-first answering with explicit source marking.
- Edit, don't append.
- Portability: everything inside the workspace folder, relative symlinks, raw-data manifest for what stays outside.
- Precedence: the closest document decides local details, no child may weaken the workspace-wide rules.
- Guard-rail `CLAUDE.md` in folders that carry a damage-causing rule.
- Closeout pass at the end of every substantive task, including a statement of what was deliberately left untouched.
- Knowledge export only after asking: findings are proposed, the user decides and comments, the comment travels with the finding.

**Process knowledge** [`knowledge/learnings/`]
- `05_layout.md`, `40_error_catalog.md`, `50_new_subproject.md` are core and cannot be switched off.
- `10_longrunners.md` (module `LONGRUNNERS`), `20_reproducibility.md` and `30_paper_kickoff.md` (module `PUBLISHING`), `60_grant_proposal.md` (module `GRANTS`, implies `PUBLISHING`).

**Skills** [`.claude/commands/`]
- `init-workspace` with four presets, eight questions, a module map and an update mode.
- `new-subproject`, `sync-knowledge`, `ask-knowledge`, `review-adversarial`, and the optional `ask-literature`.
- Every skill creates the scaffolding it needs if it is missing, rather than assuming init ran.

**Examples** [`examples/`]
- `demo-project/` with a runnable three-file analysis; the numbers in its `CLAUDE.md` are real output of the shipped scripts.
- `filled-instance/` showing profile-dependent conventions as one instance, not as rules.

**Known gaps in this release**
- The literature module documents its setup but ships no wrapper scripts; the skill creates them on first activation.
- `knowledge/projects/` has no worked example beyond what `/sync-knowledge` generates.
