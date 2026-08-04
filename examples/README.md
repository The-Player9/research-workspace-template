# Examples

Two things that are easier to show than to describe. Neither is loaded as context by the workspace; both are here to be read once and then deleted or adapted.

## `demo-project/`

A sub-project as it looks after a few weeks of work: a filled `CLAUDE.md` with a canonical results table, a `Laborbuch.md` with a result, a correction and a dead end, and a runnable three-file analysis.

The data are synthetic, but **the numbers in `CLAUDE.md` are real output of the shipped scripts**. Reproduce them in about a second:

```
cd demo-project/analysis
python generate.py     # writes 15 intermediates, atomically, skipping what exists
python evaluate.py     # writes Output.txt and results/figure_1.png
```

Worth looking at specifically:

- `generate.py` run twice: the second run writes nothing and says so. That is what "resumable" means in practice.
- `Output.txt`: every number carries the place it appears in the manuscript.
- The self-check in `evaluate.py`: it recomputes a stored metric from stored raw arrays. If the two scripts drift apart in format, this is what catches it.
- The lab book entry of 2026-02-20: a silently skipped input produced a plausible wrong number. The countermeasure went into the code, and the lesson into the error catalogue. That is the loop the whole system is built around.

## `filled-instance/`

An excerpt of one filled-in workspace, showing what the profile-dependent parts look like once a real group has decided them: writing conventions, defaults for new models, funder specifics.

**Read it as an example, not as a rule.** Those conventions grew out of one group's venues and one group's mistakes. Yours will differ, and copying them wholesale is how a template turns into an opinion about someone else's field.
