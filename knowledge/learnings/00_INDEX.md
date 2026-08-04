# Learnings — process and collaboration

Entry point for **process** knowledge: how work is done in this workspace. Not to be confused with `knowledge/` itself, which holds **domain** knowledge (mechanisms, results, method recipes). Rule of thumb: an insight about *the field* → `knowledge/`; an insight about *how we work* (tooling, procedure, recurring mistake, prompting) → here.

These files are **not** loaded automatically, which keeps every session cheaper. The parent `CLAUDE.md` carries one trigger line each; the reasoning, examples and detail live here.

| File | Content | When to read |
|---|---|---|
| [05_layout.md](05_layout.md) | how the memory files relate: parent vs. project vs. guard-rail `CLAUDE.md`, what is loaded when, where each piece of information goes | once at setup, and whenever it is unclear where something belongs |
| [10_longrunners.md](10_longrunners.md) | checkpointing and resumability of long jobs | before every training run, sweep or generation job |
| [20_reproducibility.md](20_reproducibility.md) | every reported number reproducible; analysis in exactly three files | when setting up a paper analysis |
| [30_paper_kickoff.md](30_paper_kickoff.md) | writing pipeline and kickoff checklist | before the first draft |
| [40_error_catalog.md](40_error_catalog.md) | incident archive: repeated process errors, their cause, and where the countermeasure went | rarely; when a known pitfall is suspected, or when adding a new incident |
| [50_new_subproject.md](50_new_subproject.md) | procedure for creating a sub-project | on every `/new-subproject` |
| [60_grant_proposal.md](60_grant_proposal.md) | additional rules for funding proposals: quantified objectives, work-package shape, risk section | before the first line of a proposal |

**Writing:** like `knowledge/`, only when explicitly asked, with one exception — `40_error_catalog.md` may be extended without asking as soon as a repeatable process error appears. Keep entries dated, short, and tied to a concrete countermeasure.

**Every countermeasure is additionally written in compressed form where it takes effect.** Otherwise it sits in a file that is not open at the moment it is needed. Permanent rules become a line in the appropriate `CLAUDE.md`; situational rules become a checklist item in the responsible learnings file. The catalogue keeps the incident and the reasoning; the active rule lives at the place where it applies. If a countermeasure fits neither place, say so explicitly in the entry, so it stays visible that it exists only in the archive.
