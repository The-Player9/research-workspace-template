# Ask Literature — cited answers from your own PDF collection

Queries a local **PaperQA2** collection and returns an answer **with citations and DOIs** from the published literature. Second mode: **cite-check**, verifying that the claims in a manuscript are actually supported by what they cite.

> **Boundary:** this is the **external literature** layer, separate from the internal `knowledge/` base (your own findings) and from general model knowledge. Always label answers from here as coming from the literature collection, and never mix them silently with the other two.

> **Not a code library.** The word "library" appears twice in this template and means two different things. The **literature collection** is other people's PDFs, queried here for cited answers. The **house code library** is the group's own importable functions, covered by a section in `CLAUDE.md` and never queried by this skill.

## When to invoke

**Only on explicit request.** Unlike `/ask-knowledge`, never call this on your own initiative: every query costs real money at an LLM provider, whereas reading `knowledge/` is free. The user starts it deliberately.

- `/ask-literature <question>`
- `/ask-literature cite-check <path to .tex or claim list>`

## First run: create the literature project

If the literature project does not exist yet, create it before answering, and tell the user what still needs their hand (API key, PDFs). It is a **sub-project of its own**, with its own environment, index and cost:

```
literature/
├── CLAUDE.md            what this is, model configuration, known traps
├── requirements.txt     pinned versions (pip freeze), the only synced artefact
├── setup_venv.sh        rebuilds the environment on a new machine
├── ask                  wrapper: resolves venv + key + paths, works from any cwd
├── build_index.py       incremental index build
├── papers/              the PDFs
└── key.txt              API key, git-ignored, never committed
```

Two setup rules that are worth stating because both are learned the hard way:

- **Keep the virtual environment outside the synced workspace folder** (for example `~/.venvs/<name>`), and reconstruct it from `requirements.txt` on each machine. File-sync tools do not handle symlinks and will destroy a synced venv; a `.gitignore` does not help when the sync is not git.
- **Give the index a fixed name.** If the name is derived from the settings, a relative and an absolute path to the same PDF folder produce two different indices and one silent full rebuild.

PaperQA2 (`paper-qa`, FutureHouse) is **Apache-2.0** licensed and is installed by the user via pip, not shipped with this template. Its dependencies and the LLM provider are the user's choice; the PDFs are copyrighted and never redistributed.

## Mode A — literature question

1. Call the wrapper: `bash literature/ask "<question>"`. From a sub-project the relative path `../literature/ask` works and stays portable.
2. **Return the answer with its citations and DOIs verbatim.** Do not trim the citations; they are the point.
3. **State the cost** reported by the run.
4. **Label the source** as coming from the literature collection. If the collection does not cover the question, say so explicitly rather than filling the gap from general knowledge without marking it.

## Mode B — cite-check

Checks whether the citations in a manuscript carry the claims they are attached to. This fans out over claims and **each claim costs a query**, so tell the user up front roughly how many queries are coming.

1. Read the manuscript locally (free) and extract claim-citation pairs: each `\cite{}` together with the assertion in its sentence.
2. Ask one targeted literature question per claim.
3. Compare: does the literature answer support the assertion, and does the cited work match it?
4. Report a compact list, per claim *supported / questionable / miscited*, with the evidence and a one-line reason, and the summed cost at the end.

## Known traps

Worth knowing before the first build, all of them cheap to avoid and expensive to diagnose:

- **Deduplication is by filename**, not by content hash. Changing a file's content without renaming it does not trigger a re-index.
- **A file that fails to parse can poison itself**: the failure is recorded in the index manifest, after which the file counts as done and is skipped on every later build, without ever being retrievable as evidence. The usual cause is not a broken PDF but a transient rate limit in the metadata lookup. Check after each build whether new failure entries appeared.
- **Metadata lookups get rate-limited** when run with high concurrency; build with concurrency 1 if lookups start failing.
- **Auxiliary models default to a different provider.** Any model role you do not set explicitly (parsing, enrichment, summarisation) may fall back to a default that needs a different API key.
- **Multimodal parsing** sends page images and fails on text-only models; turn it off unless the model accepts images.

## Notes

- This skill **never writes** to `knowledge/`. A literature finding enters the internal base only on explicit request, curated and marked as an external source.
- Source order for mixed questions: `knowledge/` (internal) → project `CLAUDE.md` → literature collection (external, costs money) → general knowledge, clearly marked.
- Adding new PDFs and rebuilding the index is the literature project's own business, not this skill's.
