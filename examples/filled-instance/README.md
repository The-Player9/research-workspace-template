# A filled-in instance (excerpt)

What the profile-dependent sections look like after a group has decided them. This is **one** instance, shown to make the shape concrete. The core rules of the template are deliberately not repeated here.

---

## Writing conventions (workspace-wide)

Conventions for **every** scientific text (paper, proceeding, funding proposal, cover letter). The reference style is the group's most recent accepted paper. Where a venue's style guide contradicts these, the local project `CLAUDE.md` wins, marked as an exception.

### Always

- **No em or en dashes in running text** as a punctuation mark; use a comma, colon, semicolon, brackets, or split the sentence. Compound hyphens (`ground-truth`) and source-code comment separators are exempt.
- **One paragraph = one source line** in `.tex`; paragraphs separated by a blank line. This keeps diffs readable.
- **British spelling** (normalise, colour, centre).
- **Acronyms introduced on first use**: `hyperspectral image~(HSI)`.
- **Grade interpretations honestly.** Measured things as findings, inferred things hedged ("it is assumed", "likely", "consistent with", "cannot be conclusively explained"). In proposals too: objectives as what will be achieved, not as what already holds.
- **No meta filler.** A sentence that only asserts a concept is "central" or "the key" to something gets cut down to its substance. Self-commentary without content ("we consider this a core contribution") is deleted outright.

### Citations

- **Content-bound, never by name and never as a bare bundle.** Each citation attaches to a claim named in the sentence, so only the number sits behind the assertion. No author names in running text, no merged `[4,5]`: introduce several sources individually, each with its own keyword.
- **Only published or preprinted work.** Unpublished own manuscripts are named in the text and shown as a figure, without a citation; the bibliography entry waits for publication.

### Papers

- **Long, densely argued prose paragraphs**, one complete thought each: topic sentence → mechanism → consequence.
- **No bullet lists in running text**; enumerate inline as (i)/(ii)/(iii).
- **Mechanistic and quantitative**: write out the why and how, with the values inline.

---

## Defaults for new models

When building a **new** network (not when modifying an existing one): a cosine-decay learning-rate schedule rather than a fixed rate, and residual blocks rather than plain dense layers in the body.

---

## Funder specifics

Emphasis conventions, section numbering and mandatory annexes differ per funder and per call. They are recorded in the proposal project's own `CLAUDE.md` and checked against the current call document, never carried over from the previous proposal.
