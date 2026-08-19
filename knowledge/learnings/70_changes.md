# Rule changes

Chronology of the rule changes in this workspace: what changed, where it now stands, and why. Newest on top. Deliberately empty at setup, like the error catalogue; only your own rule history is worth keeping here.

Two boundaries. Against [40_error_catalog.md](40_error_catalog.md): the catalogue is sorted by **incident** and keeps its mechanism, this file is sorted by **rule and date** and also records changes that came from a decision rather than from a mistake. Against the framework's `CHANGELOG.md`: that file logs the versions of the template you started from, this one logs what you changed afterwards.

Without this file the occasion for a rule is lost. A condensed rule sits where it applies and says only what to do. If its occasion is written nowhere, someone deletes it as bureaucracy a year later. Putting `(incident YYYY-MM-DD → 40_error_catalog.md)` into the rule text is the cheaper first move, but it costs space in files that are read on every application.

**When the reference in the rule text can go.** Two conditions, both required: (i) the rule carries its own why in its own sentence, rather than only prescribing; (ii) the rule is settled, meaning confirmed by the user and applied at least once. A fresh rule keeps the reference until both hold. Once it goes, the entry here takes its place, and the entry still points at the catalogue.

**Writing:** on every change to a `CLAUDE.md`, to a file in `learnings/`, or to a skill in `.claude/commands/`. At the same time as the change, not collected afterwards. Like the error catalogue, this file may be written without asking.

## Entry format

```markdown
## YYYY-MM-DD — title of the change

**Added / Changed / Removed** [`file.md`, section] — what now stands there, in one sentence.
**Reason:** decision, incident or observation; for an incident `(incident YYYY-MM-DD → 40_error_catalog.md)`.
**Reference in the rule text:** removed / kept, with the reason from the two conditions above.
```

A reference that points at the catalogue as a whole is not resolvable once the catalogue has more than a handful of entries. Give the date, and where a date carries two entries, the keyword as well.

---

_(no entries yet)_
