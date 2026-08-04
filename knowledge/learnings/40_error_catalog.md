# Error catalogue

Archive of **repeatable process errors** in this workspace: what happened, why, and where the countermeasure was written. Deliberately empty at setup. Foreign incidents help nobody; yours are the only ones worth recording.

**This is the one file that may be extended without asking**, as soon as an error appears that can recur. Everything else in `knowledge/` needs an explicit request.

## Entry format

```markdown
## YYYY-MM-DD — one-line title

**What happened:** the concrete incident, in two sentences.
**Why:** the mechanism, not the blame. Usually a rule that was absent, or present in a file that was not open at the time.
**Countermeasure:** the concrete change.
**Written to:** the file and section where the active rule now lives.
```

## The rule that makes this file work

**Every countermeasure is additionally written, compressed, at the place where it takes effect.** A lesson that lives only in this catalogue sits in a file that is not open at the moment it is needed, which is exactly the moment the error recurs.

- A permanently valid rule → one line in the appropriate `CLAUDE.md`, so it applies without anyone reading anything.
- A situational rule → a checklist item in the responsible learnings file.
- A rule bound to one folder → a guard-rail `CLAUDE.md` in that folder.

The catalogue keeps the incident and the reasoning; the active rule lives where it applies. If a countermeasure fits none of these places, say so explicitly in the entry, so it remains visible that it exists only in the archive.

## What does not belong here

Scientific mistakes (a wrong model, a bad assumption) go into the project's `Laborbuch.md` and, if they generalise, into `knowledge/`. This file is only about **how the work is organised**: things forgotten, files not read, steps skipped, tools misused.

---

_(no entries yet)_
