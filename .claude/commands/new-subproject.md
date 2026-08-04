# New Subproject

Creates a sub-project inside this workspace. Read `knowledge/learnings/50_new_subproject.md` and follow it; this file is the short form.

## Ask first

1. **Name** of the project directory.
2. **One sentence** on what it is and what comes out of it (one paper, a method, a dataset).
3. **Research project or not?** Meta-projects, archives and grant applications get no file under `knowledge/projects/` and belong on the excluded-from-sync list.
4. **Raw data outside the workspace?** If yes, a raw-data manifest is created.

## Then create

1. Directory.
2. Relative symlink: `ln -s ../knowledge knowledge` from inside it. Relative, so the workspace survives a move between machines.
3. `Laborbuch.md` from `templates/subproject_Laborbuch.md`, header only.
4. `CLAUDE.md` from `templates/subproject_CLAUDE.md`, header block filled with the project name and the one-sentence overview. **Leave every section you cannot fill empty** — especially "Reproduction" and "Current results". An empty section is a truthful record; a described intention is not.
5. If raw data is external: `data/raw_manifest.md` from the template.
6. If it is not a research project: add it to the excluded list in `knowledge/INDEX.md` and say so in the report.

## Do not

- Do not invent results, numbers or a structure the project does not have yet.
- Do not add the project to the sub-project table by hand; the next `/sync-knowledge` does that with a consistent status.
- Do not copy rules from the parent `CLAUDE.md` into the new file. They apply anyway, and a duplicate drifts.

## Report

Which files were created, which sections were deliberately left empty, and what the first lab-book entry should record once work begins.
