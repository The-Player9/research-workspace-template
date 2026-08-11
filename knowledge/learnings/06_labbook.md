# The lab book

Read this once at setup. `Laborbuch.md` is the store you write into most often, and the one whose value depends entirely on when it is written.

The name is German for "lab book" and is kept as a filename so that it looks the same in every workspace built from this template. Rename it if you prefer, but rename it everywhere: the rule lines in `CLAUDE.md` and the sub-project template refer to it by name.

## What it is

One `Laborbuch.md` per sub-project, chronological, newest entry on top, dated headings `## YYYY-MM-DD`. It is written **without asking**, at the moment something happens, not at the end of the week.

The split from `CLAUDE.md` is a cost decision, explained in `05_layout.md`: the project `CLAUDE.md` is loaded in every session and therefore holds the **current state**, while the lab book holds **how that state came about** and is read only when the history is needed. The two answer different questions. "What is the R² of the current model" is a `CLAUDE.md` question. "Why did we stop using the other loss function" is a lab book question.

## What an entry contains

- **The result together with the settings that produced it.** A number without its parameters, seed and input file cannot be reproduced, and an entry that cannot be reproduced is a rumour.
- **Corrections as new entries.** When an older result turns out to be wrong, write a new dated entry that says so and why. Do **not** edit the old one. This is the one place where the workspace-wide rule "edit, don't append" does not apply: the record of what you believed on a given date is itself data, and a paper defence needs it.
- **Dead ends with the reason they were dropped.** This is the most valuable and most often omitted category. Without it the same approach is tried twice, once by you in a year and once by the next person.
- **Methodological pitfalls** the moment they cost you time.
- **Running TODOs**, which move out again as soon as they are done.

## What does not belong in it

| It is… | It goes to |
|---|---|
| a stable conclusion drawn from several entries | condensed into the project `CLAUDE.md`; the detail stays here |
| the current canonical number a manuscript will report | the project `CLAUDE.md`, reproducible by the documented script |
| a finding other projects would benefit from | proposed as a knowledge export, decided by the user |
| a lesson about how we work rather than about the science | `knowledge/learnings/`, and `40_error_catalog.md` if it is a repeatable process error |

The failure this table prevents is the project `CLAUDE.md` slowly turning into a diary, which makes every future session more expensive and the current state harder to find.

## Next to a paper lab book

Same function, different medium, and in most groups both exist. The digital lab book covers everything that happens on the computer: analyses, fits, simulations, model runs, data processing. The paper book covers what happens at the bench, where a keyboard is not at hand and a signature may be required.

Four rules keep them from contradicting each other:

- **Each observation lives in exactly one of the two.** Duplicated entries drift apart, and then neither can be trusted. This is the same argument that gives this framework four stores rather than five.
- **Cross-reference at the boundary.** Where a measurement is taken on paper and evaluated on the computer, the digital entry names the paper book and page, and the paper entry names the project folder and the date. A number whose trail breaks at the boundary is not reproducible, no matter how carefully each half was kept.
- **A digital lab book does not replace a legally required one.** Where your institute, good laboratory practice, or patent evidence requires a bound, paginated and countersigned book, keep it. This file is a working log, not a legal record. Treat the digital book as the analysis half and say so in the project `CLAUDE.md`, so nobody assumes the paper trail is complete.
- **Purely computational projects have no split.** Then the digital book is the whole lab book, and the rules above collapse to the first section of this file.

## The four ways it goes wrong

- **Written later.** By the end of the week the settings are gone and the entry becomes "trained a model, looked fine".
- **Only successes recorded.** The dead ends are the expensive knowledge, because they are what stops a repetition.
- **Conclusion without evidence.** An entry that states an interpretation but not the number behind it cannot be re-examined when the interpretation is later challenged.
- **Old entries edited into correctness.** That destroys exactly the record that makes the book worth keeping.
