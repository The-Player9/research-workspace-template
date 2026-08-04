# Creating a sub-project

Followed by `/new-subproject`, and by hand if the skill is not used. Every sub-project is part of this workspace and shares its knowledge base.

## Steps

1. **Symlink to the knowledge base**, relative so it survives a move between machines: `ln -s ../knowledge knowledge` from the new project root.
2. **`Laborbuch.md`** created from `templates/subproject_Laborbuch.md`, empty apart from the header.
3. **`CLAUDE.md`** created from `templates/subproject_CLAUDE.md`, with the header block filled in:

````
## Knowledge base (read-only)

Shared base via symlink `knowledge/ → ../knowledge` (read-only). Own project file: `knowledge/projects/<NAME>.md`. Rules (reading, writing, knowledge export) → parent `CLAUDE.md`, "Rules in sub-projects".

## Lab book
Dated entries, experiment logs and running notes → `Laborbuch.md`, not in this file, which stays lean.
````

4. **If raw data lives outside the workspace** (multi-GB on a NAS or acquisition machine), add `data/raw_manifest.md`: per dataset its location, acquisition date, size and the script that produced it. Without it the workspace cannot be traced back to its source after a transfer.
5. **Leave the sections you cannot fill yet empty.** "Reproduction" stays empty until a real analysis exists; describing an intended one turns the file into a plan instead of a record.

## Variants

- **Not a research project** (a meta-project, an archive, a grant application): it still gets a `CLAUDE.md`, but no file under `knowledge/projects/`, and it belongs on the "excluded from knowledge sync" list in `knowledge/INDEX.md`. Otherwise the next sync creates a knowledge entry for something that has no findings to share.
- **Standalone project outside a workspace**: put a note at the top of its `CLAUDE.md` saying it is the project's memory file and that no memory files are kept outside the repository; add a `Laborbuch.md` as usual. No symlink, no shared base.

## Afterwards

Add the project to the sub-project table in `knowledge/INDEX.md` on the next `/sync-knowledge` run rather than by hand, so the status column stays consistent with what the sync actually found.
