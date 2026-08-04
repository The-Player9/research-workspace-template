# Ask Knowledge — cross-project lookup

Consult the shared knowledge base in `knowledge/` to answer a question that reaches beyond the current sub-project. Reachable from any sub-project through the `knowledge/` symlink, and directly from the workspace root.

## When to invoke

**Manually:** `/ask-knowledge <question>`, or when the user says "look at the other projects", "have we solved this before", "does this exist elsewhere".

**On your own initiative**, as soon as a question needs knowledge outside the current sub-project: methodological or architectural questions that could matter in several projects, comparisons between projects, mechanisms that are not specific to the project at hand, and any question that sounds methodological but is not answered by the loaded project `CLAUDE.md`. When in doubt, check the base rather than answer from general knowledge.

## First run

If `knowledge/INDEX.md` does not exist, the base has not been set up. Create the scaffolding (`INDEX.md`, `insights.md`, `methods.md`, `projects/`, each with its header line explaining what belongs in it), say that it was empty, and answer from the project documentation and general knowledge with both clearly marked. Do not silently proceed as if the base had been consulted.

## Steps

1. **Note the current sub-project.** It is the context the answer must be mirrored against.
2. **Read `knowledge/INDEX.md` first.** It decides which files are relevant: `insights.md` (scientific mechanisms and findings), `methods.md` (technical lessons and recipes), `projects/<name>.md` (per-project syntheses).
3. **Read only the relevant sections.** Grep for keywords when the material is large.
4. **Respect knowledge-first.** If the answer is in the base, cite it with its file path (ideally `file.md:line`). If it is **not**, say so explicitly. If you add your own knowledge, mark it as "from my general knowledge, not from the project documentation". Never mix the two silently.
5. **Synthesise**, typically 100–400 words: what the base says (with the citation), how it relates to the current sub-project, and what is missing or unclear. Do not repeat what the loaded project `CLAUDE.md` already states.

## Notes

- This skill does **not** write to `knowledge/`. Updates go through `/sync-knowledge` or an explicit user request.
- Source order: knowledge base → project `CLAUDE.md` → general knowledge, clearly marked.
