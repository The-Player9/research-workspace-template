# Long-running jobs save intermediate state

Applies to every job that runs longer than a coffee break: training, sweeps, data generation, long simulations.

**Rule:** the job writes its intermediate state to disk continuously and can resume from it after a crash. A run that has to start from zero after an interruption is a run you will not repeat, and its numbers will quietly stay unverified.

**Minimum implementation:**

- Write results incrementally, not once at the end. One file per completed unit (seed, sweep point, epoch block) beats one large file at the finish.
- Write **atomically**: to a temporary file, then rename. A crash during the write must not corrupt the previous state.
- On start, check what already exists and skip those units. Resumability is a property of the entry point, not of a flag nobody sets.
- Store the configuration alongside the results, in the same file or next to it. Results whose settings cannot be recovered are not results.
- Log which unit finished when, so an interrupted run can be reported honestly.

**Trap:** a resumable script whose resume path is never tested is not resumable. Kill the job once on purpose, restart it, and confirm it continues rather than restarts.
