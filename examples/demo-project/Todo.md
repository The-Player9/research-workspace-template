# Todo — demo-project

Open work steps of this project. A done item is deleted here and recorded in `Laborbuch.md` with its date, not struck through, so this file stays short enough to read before every task. Open decisions belong in `CLAUDE.md`, not here.

## Open

- [ ] Extend to a misspecified model (quadratic truth, linear fit): the case where unbiasedness is expected to fail.

## Parked

> **Bootstrap confidence intervals instead of seed spread.** Tried and dropped: with a deterministic generator the seed spread already measures what the bootstrap would estimate, and the extra machinery made `evaluate.py` depend on a resampling library. Reason kept because it will come back the moment the data are real. Detail in the lab book, 2026-02-19.
