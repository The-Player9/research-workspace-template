# A filled-in instance (excerpt)

What the profile-dependent sections look like after a group has decided them. This is **one** instance, shown to make the shape concrete. The core rules of the template are deliberately not repeated here.

---

## Writing conventions (workspace-wide)

Conventions for **every** scientific text (paper, proceeding, funding proposal, cover letter). The reference style is the group's most recent accepted paper. Where a venue's style guide contradicts these, the local project `CLAUDE.md` wins, marked as an exception.

### Always

- **Sentence length 20 to 25 words, one main thought per sentence.** Papers and proposals alike. No multiply subordinated constructions; two sentences beat one with two subordinate clauses. A longer sentence carries no more information, it spreads the same information over more words.
- **No em or en dashes in running text** as a punctuation mark; use a comma, colon, semicolon, brackets, or split the sentence. Compound hyphens (`ground-truth`) and source-code comment separators are exempt.
- **One paragraph = one source line** in `.tex`; paragraphs separated by a blank line. This keeps diffs readable.
- **British spelling** (normalise, colour, centre).
- **Acronyms introduced on first use**: `hyperspectral image~(HSI)`.
- **Grade interpretations honestly.** Measured things as findings, inferred things hedged ("it is assumed", "likely", "consistent with", "cannot be conclusively explained"). In proposals too: objectives as what will be achieved, not as what already holds.
- **No meta filler.** A sentence that only asserts a concept is "central" or "the key" to something gets cut down to its substance. Self-commentary without content ("we consider this a core contribution") is deleted outright. The same goes for sentences that talk about the text instead of about the subject ("what the aim buys is", "this is the first point at which", "where that boundary runs is the result of"). Test: delete the sentence; if the text does not lose a claim about the subject matter, it stays deleted. A frame sentence that does carry a finding, a target value or a negative outcome is rewritten to state that finding.

### Citations

- **Content-bound, never by name and never as a bare bundle.** Each citation attaches to a claim named in the sentence, so only the number sits behind the assertion. No author names in running text, no merged `[4,5]`: introduce several sources individually, each with its own keyword.
- **Only published or preprinted work.** Unpublished own manuscripts are named in the text and shown as a figure, without a citation; the bibliography entry waits for publication.

### Papers

- **Dense paragraphs, one complete thought each**: claim → mechanism → consequence. The first sentence states the claim itself; it does not announce what the paragraph is about to do. A paragraph runs as long as the thought needs, and no longer. Density is the target, length never is.
- **"Prose" here means "not a bullet list", nothing more.** It is not an instruction to write in a flowing, ornamented register. No transition, announcement or summary sentences between the substantive ones. Density comes from dropping the connective padding, not from longer sentences.
- **No bullet lists in running text**; enumerate inline as (i)/(ii)/(iii).
- **Mechanistic and quantitative**: write out the why and how, with the values inline.

### Funding proposals

- **Short main clauses, not the paper register.** The sentence rule above is enforced strictly. Justifications go into their own short sentences rather than into subordinate clauses.
- **No sentence that announces what the next one says.** The paper habit of opening a paragraph with a topic sentence produces exactly the frame sentences banned under "Always".
- **A word budget per objective or work package** is agreed before the first line, not just a total page count. A total budget does not discipline sentence structure; a per-paragraph budget does.

---

## Defaults for new models

When building a **new** network (not when modifying an existing one): a cosine-decay learning-rate schedule rather than a fixed rate, and residual blocks rather than plain dense layers in the body.

---

## Funder specifics

Emphasis conventions, section numbering and mandatory annexes differ per funder and per call. They are recorded in the proposal project's own `CLAUDE.md` and checked against the current call document, never carried over from the previous proposal.
