# Writing pipeline and kickoff checklist

Applies to every scientific text: paper, proceeding, grant proposal, cover letter. The order is fixed, because each step invalidates the previous one if taken out of turn.

## The pipeline

**0. Numbers final.** No drafting before the reported values are stable and reproducible from stored data (see [20_reproducibility.md](20_reproducibility.md)). Text written around numbers that later move has to be rewritten, and the rewrite is where inconsistencies survive.

**1. Storyline, decided by the user.** A short `storyline.md`: the claim, the evidence for it in order, what is deliberately left out, and one line per section (per objective or work package in a proposal) naming its claim, its criterion and its deliverable. If one of the three cannot be said in a single sentence, the decision behind it is still open, and the draft will spread it over supporting quantities instead of stating it. This is a human decision, not a drafting step. Everything downstream inherits it.

**2. Draft, section by section.** One section at a time, each reviewed before the next begins. Drafting the whole text in one pass produces a document whose middle contradicts its own introduction.

**3. Citation check.** Every citation attached to a claim named in the sentence, no bare bundles, nothing cited that is not published or preprinted. Check the bibliography against what the text actually asserts, not against the reference list.

**4. Adversarial review in a fresh context.** Run `/review-adversarial`. It must not be the context that wrote the draft: that context knows what it meant and reads the gaps as filled.

**5. Final pass by the user.** Not delegable.

## Kickoff checklist

Answer before step 1, because each answer constrains the storyline:

- **Target venue** and its hard constraints: length, figure count, structure, citation style, whether supplementary material is allowed.
- **Which numbers are final**, and which are still moving. If any are still moving, the pipeline has not started.
- **Which figures exist**, which are placeholders, and who produces the missing ones.
- **Author list and contributions**, decided at the start rather than negotiated at submission.
- **Data and code availability**: what is released, where, under what licence, and whether a DOI is needed before submission.
- **AI-assistance declaration**: what the venue requires and what you will state.
- **Preprint policy** of the venue, and whether you intend to post one.
- **Style anchor and length budget**: which existing text defines the register, and how many words each section gets. A per-section budget disciplines sentence structure, a total page count does not. For a text type the anchor does not cover, a proposal when the anchor is a paper, get a sample paragraph from the user before the first line.
- **Known reviewer objections**: the two or three comparisons or controls a hostile reader will demand. Decide now whether to run them, and if not, why the paper stands without them.

## Recurring traps

- A style word that can name both a format and a register will be read as a register instruction. "Prose" meant "not a bullet list" and was read as "write in a flowing style", which is where transition and announcement sentences come from. Pin such a word to one reading when you write it into a `CLAUDE.md`.
- A sentence hedges because a decision is missing, not because the author lacks nerve. Where it is undecided which of two quantities carries the claim, both appear as interpretations and neither as a statement. Settling the question is what makes the sentence direct; a style pass on an undecided sentence only polishes the evasion.
- A style rule stated for one text type is applied to that type only. A rule against long sentences that sits under "proposals" leaves the papers untouched, even when the same sentences were the problem there. Rules about sentences belong in the section that covers every text type.
- A text block moved from an earlier manuscript brings its old framing; reread its first and last sentence in the new context.
- Conclusions written before the discussion tend to claim more than the results section supports.
- A limitation discovered late is easier to state plainly than to hide; reviewers find it either way, and a stated one costs less.
