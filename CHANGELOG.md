# Changelog

Versions of the **framework**, meaning the rule set and the skills, not of any workspace built from it.

This file is what makes an update deliverable. `/init-workspace` writes the version into the marker at the top of your `CLAUDE.md`, and `/update-workspace` compares that version against **this file in a fresh copy of the template**, then proposes only what changed since. The copy inside your own workspace is your instance's log and froze at setup; comparing against it finds nothing, which is the defect fixed in 0.1.4.

Each entry states what a user must **decide**, not only what moved. Format: `Added` / `Changed` / `Removed`, with the affected file in brackets.

Every release carries the git tag `v<version>`, which is how `/update-workspace` reconstructs the state your workspace started from. A fork that drops the tags still updates, on a weaker test; keep them if you can.

## 0.1.4 — 2026-08-11

**Added** [`.claude/commands/update-workspace.md`, `knowledge/learnings/06_labbook.md`, `README.md`]

- Updating is now its own skill, `/update-workspace`. It reads the version marker, obtains a current copy of the template, and repeats no setup question.
- Changes are sorted by **conflict, not by importance**. A file still identical to the state shipped at the user's own version is updated without asking and listed in the report; only a file the user edited becomes a question. `CLAUDE.md` and `40_error_catalog.md` are compared rule by rule instead of as a whole, because init and daily use guarantee they differ.
- The `Decide` paragraph of each entry is no longer a gate. It is written into the workspace as a dated TODO, in the project it concerns, and so are rejected changes together with the user's reason. A decision that only appeared in the chat was a decision nobody made.
- Three modes: the default above, `--review` for the older behaviour of asking about everything, and `--dry-run` for a report that changes nothing.
- The marker gains a `source:` field naming the repository the workspace came from, so a fork updates from its own origin. A marker without the field is completed on the first update run.
- Releases are tagged `v<version>`, retroactively back to `v0.1.0`. The tag is what makes "has the user edited this file since their own version" an exact question rather than an inferred one.
- `06_labbook.md` documents the store people write into daily: what an entry contains, why a correction is a new entry rather than an edit, what belongs in `CLAUDE.md` instead, and how the file stands next to a paper lab book kept at the bench.
- The README gains three sections users asked for: how to update, directly below the quickstart; how the lab book is used and divided against a paper one; and a table separating the house **code** library from the literature collection.

**Changed** [`CLAUDE.md`, `.claude/commands/init-workspace.md`, `.claude/commands/ask-literature.md`, `knowledge/learnings/00_INDEX.md`, `templates/subproject_Laborbuch.md`]

- `/init-workspace` refuses to run on an initialised workspace and points to the update skill. Its old step 5 is gone, so one skill no longer holds two state machines.
- Init question 7 asks about an "own code library" and question 8 about a search over other people's papers. Both now state what they are not.

**Why:** the update path could not work as shipped. Step 5 of `init-workspace` compared the marker against `CHANGELOG.md`, meaning the copy inside the user's own workspace, which freezes at setup and additionally receives an init line. The comparison ran against the very file the marker came from and could never report a difference, and no document said where a newer version should come from. The naming did the rest: users who had finished setting up did not want to run a command called `init` on their workspace, and there was nothing else to run. The library wording failed the same way, by using one word for a code package and for a PDF collection, so the second init question read as a repeat of the first.

The rule-by-rule design was itself a second obstacle. It treated every change as a decision, although two different approvals were hiding in one prompt: permission to change a rule file, which is mechanical and safe wherever the file is untouched, and the follow-up work on the user's own material, which no tool can do and which the skill only ever displayed. Gating the first on the second made a routine update expensive, and an expensive update is skipped, after which the workspace drifts from the framework it claims to follow. Splitting the two makes bulk updating safe: the mechanical half runs, and the human half is recorded as an obligation instead of scrolling past in a chat.

**Decide, if you are updating from 0.1.3:** decide where your reference copy lives, a permanent clone next to the workspace or a throwaway one per update, and whether the `source:` URL points at this repository or at your own fork. If you keep a paper lab book, read `06_labbook.md` and settle the boundary explicitly, then write one line into each project `CLAUDE.md` saying which half of the record is on paper. That decision cannot be derived from your files, and getting it wrong produces two divergent accounts of the same experiment.

**Not done, deliberately:** the module identifiers `HOUSE_LIB` and `LITERATURE_RAG` keep their names, although `CODE_LIB` and `LITERATURE_COLLECTION` would read better. They stand in the marker of every existing workspace, and renaming them would invalidate those markers to fix wording that only ever appears in prose. The clarification therefore sits in the visible text, not in the identifiers.

**Still open, and known:** the marker has no list of declined changes, so a rejection survives only as the TODO line written in step 7. A later run cannot yet tell "not yet" from "deliberately never", and it raises the version marker even when something was declined.

## 0.1.3 — 2026-08-07

**Changed** [`CLAUDE.md`, `knowledge/learnings/00_INDEX.md`, `knowledge/learnings/60_grant_proposal.md`, `.claude/commands/review-adversarial.md`]

- The section "Quantify the objectives" is replaced by "Objectives, criteria and means are three different things". A work-package objective states what will be known at the end; the checkable number moves onto the validation criterion, and the method moves to the approach.
- The same file gains three checks: an objective whose result may also be a negative answer is an objective, a package that only enables the variation states its deliverable instead, and objectives are derived downwards from the project's research question with one varied factor per package.
- `review-adversarial` no longer asks whether every objective carries a checkable number. It asks whether the objective states what will be known, and whether the number sits on the validation criterion. The trigger line in the core `CLAUDE.md` and the table row in the learnings index say the same.

**Why:** the previous rule demanded a checkable number in every work-package objective. The most checkable sentence available is the validation criterion, so the criterion kept taking the objective's place, and the shipped example ("determine the response of X over the range A to B with an uncertainty below C") demonstrated exactly that substitution. The failure survives a style pass, because polishing a sentence does not change what type of statement it is. Reviewers do want something checkable, which is why the number stays mandatory; it just belongs one line further down.

**Decide, if you are updating from 0.1.2:** read your last proposal's work-package objectives and sort each one into question, criterion or method. Only the first is an objective. Decide for the packages that state a criterion whether the underlying question is the one you actually want to answer, because that question is usually broader than the threshold that replaced it. Packages that generate data or build instrumentation keep their deliverable as the objective; do not rewrite those into questions.

**Not done, deliberately:** no rule was added about how to phrase the objective sentence. The verb pattern is not the problem, and prescribing one ("establish whether …") would let a means sentence pass review as long as it starts correctly.

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
