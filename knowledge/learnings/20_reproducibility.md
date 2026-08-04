# Reproducible numbers, analysis in exactly three files

**Rule:** every number reported in a manuscript is produced by a script from a stored data file. Not from a notebook cell, not from a console session, not from memory.

## The three files

1. **Generation script** — everything expensive: simulations, training, sweeps. Writes intermediate results to disk (see [10_longrunners.md](10_longrunners.md)) and is resumable. It is run rarely and may need special hardware.
2. **Evaluation script** — produces **every figure and every reported number** from the stored intermediates. Runs in seconds, needs no GPU and no simulation dependency. It writes `Output.txt`, in which each number is labelled with **where it appears in the manuscript** (table, section, figure caption).
3. **Shared helpers** — configuration, paths, the functions both scripts use. Expensive dependencies are imported lazily so the evaluation script keeps running without them.

## Why this shape

The split is what makes a manuscript number checkable months later: a reviewer question, a rerun after a bug fix, or a co-author asking where a value came from is answered by running file 2, not by reconstructing a session. `Output.txt` with manuscript locations turns the check from "which of these numbers is table 2?" into a text comparison.

## Practical points

- Include a **self-check** in the evaluation script: recompute something the generation script already stored and assert that both agree. It catches silent format drift.
- Keep the analysis in the publication language, so the three files can ship as supplementary material.
- If the folder ships as supplementary material, reset any partial-run switches before packaging, otherwise you distribute a configuration that only reproduces the step you last worked on.
- A number that appears in the manuscript but not in `Output.txt` is an open item, not a rounding difference.
