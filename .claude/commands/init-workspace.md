# Init Workspace

Sets up this research workspace, or updates an existing one to a newer framework version. Runs **once** at setup; every later run is an update.

## 0. Detect mode

Look for the marker comment at the top of `CLAUDE.md`:

```
<!-- workspace-framework: <version> | profile: <preset> | lang-notes: <xx> | lang-pub: <xx> | modules: <a,b,c> -->
```

- **No marker** → init mode, continue at step 1.
- **Marker present** → update mode, jump to step 5. Never re-run init over an existing instance.

## 1. Preset

Ask for one preset. It sets every default below; only what it leaves open is asked afterwards.

| Preset | Defaults |
|---|---|
| `wet-lab` | raw-data manifest **on**, long runs **off**, reproducibility **on**, measurement-protocol section in the sub-project template |
| `computational` | long runs **on**, reproducibility **on**, raw-data manifest optional |
| `theory` | long runs **off**, raw data **off**, reproducibility **on** (derivations rather than numbers) |
| `mixed` | everything **on**, the user removes what they do not need |

## 2. Questions

Ask only these, and only the ones the preset leaves open. Do not invent further questions; anything else is derived and reported in step 4 so the user can object.

1. **Field / subdiscipline** (free text) — shapes examples, section names and the `knowledge/` header lines.
2. **Language of notes** and **language of publications** (two separate values; internal notes may differ from manuscripts).
3. **Role**: PhD student / postdoc / PI — controls how much explanation the rule texts carry and whether the grant module is included.
4. **Publication conventions**: spelling (BE/AE), citation style, LaTeX or Word.
5. **Long-running jobs?** (training, sweeps, long simulations) — enables the checkpointing rule.
6. **Raw data outside the workspace?** — enables the raw-data manifest.
7. **Own helper library?** (name, import) — enables the "check the library first" rule.
8. **Set up the literature RAG?** — default **no**; if yes, state plainly that it calls an external service and incurs cost per query.

## 2b. Module map

What each answer switches on. `GRANTS` implies `PUBLISHING`; the grant bullet is nested inside the writing-conventions block.

| Module | Trigger | Files it brings |
|---|---|---|
| **core** (never optional) | — | `05_layout.md`, `40_error_catalog.md`, `50_new_subproject.md`, `00_INDEX.md`; skills `new-subproject`, `sync-knowledge`, `ask-knowledge`; `templates/subproject_*`, `templates/guardrail_CLAUDE.md` |
| `LONGRUNNERS` | Q5 yes | `10_longrunners.md` + the checkpointing rule in `CLAUDE.md` |
| `PUBLISHING` | default yes, off only if the user says they do not publish | `20_reproducibility.md`, `30_paper_kickoff.md`, skill `review-adversarial`, the writing-conventions block |
| `GRANTS` | Q4 role, or asked directly | `60_grant_proposal.md` + its bullet |
| `RAW_DATA_EXTERNAL` | Q6 yes | `templates/raw_manifest.md` + the portability exception |
| `HOUSE_LIB` | Q7 yes | the house-library section, filled with the given name and import |
| `LITERATURE_RAG` | Q8 yes | skill `ask-literature` + its row in the skills table |

`40_error_catalog.md` and `05_layout.md` ship even in the leanest profile: the first carries the mechanism that keeps every other lesson from being filed where nobody reads it, the second is what makes the three levels of `CLAUDE.md` comprehensible at all.

## 3. Write the instance

1. `CLAUDE.md` **in place**: fill every `{{PLACEHOLDER}}`, keep `{{#IF MODULE}}` blocks only for active modules, delete the block markers themselves, and write the version marker at the top. The shipped `CLAUDE.md` is the skeleton; after init it is the user's file and is never regenerated.
2. `knowledge/INDEX.md`, `insights.md`, `methods.md`, `projects/`, `sync_log.md` — empty, each with the header line explaining what belongs in it and at what level of abstraction. An empty base without those lines becomes a dumping ground.
3. `knowledge/learnings/` — only the files of active modules; trim `00_INDEX.md` to those rows.
4. `.claude/commands/` — remove the skills of inactive modules.
5. `.gitignore` — raw data, results, model checkpoints, large binaries.
6. `CHANGELOG.md` — one line recording the init date and version.

Do **not** create any sub-project. That is `/new-subproject`, so the procedure is identical for the first and the twentieth.

## 4. Report

Tell the user, briefly: which modules are active, which defaults came from the preset rather than from an answer, what each written file is for, and one concrete suggestion for the first sub-project. Invite correction of the derived defaults.

## 5. Update mode

1. Read the version from the marker and compare it with the template version in `CHANGELOG.md`.
2. Build the difference: which core rules were added, changed or removed since the user's version.
3. Present each change **as a proposal**: the rule text, the file it belongs in, and the insertion point. The user decides rule by rule and may comment.
4. Apply only what was accepted. **Never** overwrite `CLAUDE.md` wholesale, and never touch `Laborbuch.md`, `knowledge/` contents or any sub-project file.
5. If anything was accepted, raise the version in the marker; otherwise leave it and say so.

## Constraints

- **Every skill creates what it needs on first activation.** Init writes the scaffolding, but no skill may assume it is there: `/sync-knowledge` creates a missing `knowledge/` tree, `/ask-knowledge` creates it and says the base was empty, `/ask-literature` creates the literature project. A workspace that was set up by hand, or predates a module being switched on, must still work.
- Everything stays inside the workspace folder; write nothing outside it. The one documented exception is a Python environment for the literature module, which is deliberately kept outside a synced folder and rebuilt from `requirements.txt`.
- Never overwrite a file that already carries user content. On collision, show the difference and ask.
- Keep the written rule texts as short as the template's: this file's own output is loaded into every future session.
