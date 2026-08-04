# Laborbuch — demo-project

> Example lab book. Three entries, newest on top: one result, one correction, one dead end. This is the shape the real thing takes.

## 2026-02-21 — noise sweep complete, numbers frozen

Ran the full grid (5 seeds × 3 noise levels) after the atomic-write fix. Slope and offset recover the ground truth at every level; the effect of noise is entirely in the spread (slope std 0.0000 → 0.0012 → 0.0029). Test R² 1.0000 / 0.9992 / 0.9951.

Numbers copied into `CLAUDE.md` as the canonical table. `Output.txt` now labels each value with where it goes in the note, so the pre-submission check is a text comparison rather than a rerun.

Proposed one knowledge export (the `Output.txt` labelling trick, as a writing lesson rather than a fitting one). User approved with a comment, both are now in the export section.

## 2026-02-20 — correction: yesterday's "bias at high noise" was an artefact

Yesterday I recorded an apparent slope bias at noise 0.05. Wrong: the run had used four of the five seeds, because the fifth unit had failed to write and the loader silently skipped the missing file. With all five units present the bias disappears (2.5009 ± 0.0029, truth 2.5).

Two changes came out of this. The loader now **raises** on a missing intermediate instead of skipping it, and `generate.py` writes atomically via a temporary file, so a crash mid-write cannot leave a half-file that looks present. The atomic-write helper had a second bug on top: numpy appends `.npz` to a temporary name that does not end in it, so the rename missed the file entirely and no unit was ever written. Both fixed in `helpers.atomic_savez`.

Lesson for the workspace, not just this project: a silently skipped input is worse than a crash, because it produces a plausible number. Noted for the error catalogue.

## 2026-02-19 — bootstrap intervals tried and dropped

Wanted per-parameter confidence intervals and implemented a bootstrap over the training split. Dropped it again: with a deterministic generator the seed-to-seed spread already measures the same quantity, the two agreed to within 3 % on a test case, and the bootstrap pulled a resampling dependency into `evaluate.py`, which is supposed to run anywhere in seconds.

Not deleted, parked: as soon as the data are real and seeds stop being repeatable, the bootstrap is the right tool. Recorded in `CLAUDE.md` under "Parked" with the reason, so it is not rediscovered from scratch.
