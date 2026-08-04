# Review Adversarial — reviewer-2 pass over a manuscript

Read a manuscript (paper, proceeding, grant proposal) as a well-meaning but incorruptible referee and list everything that could lead to rejection or major revision.

## When to invoke

`/review-adversarial <path to manuscript>`, on explicit request, as step 4 of the writing pipeline (`knowledge/learnings/30_paper_kickoff.md`): after the citation check, before the author's final pass.

**A fresh context is part of the method.** Whoever wrote the text reads over its gaps. If the same session drafted the manuscript, run the review in a **subagent** that sees only the manuscript, the data basis and this instruction, not the drafting history.

## Steps

### 1. Read the text, not the history

Read the manuscript plus the number basis (`Output.txt`, derived data). **Not** the lab book and not the draft history: the referee does not have them either. Anything that exists only in the author's head is a finding.

### 2. Work through seven axes

Be concrete on each (section, line, number), never generic:

1. **Core claim** — is it in one sentence in the abstract, and do the shown data carry it? Where is the gap between claim and evidence?
2. **Numbers** — does every reported number have a data basis? Do text, table and figure agree? Are spread, n and units given? Is a precision claimed that the method cannot deliver?
3. **Methods** — is the procedure described well enough to reproduce? Are calibrations, reference measurements or parameter values missing? Which assumption is left unstated?
4. **Alternative explanations** — which other cause explains the finding equally well, and is it excluded? This is the most common reason for rejection; be sharpest here.
5. **Statistics and generalisation** — is a broad conclusion drawn from few samples? Are train and test cleanly separated? Is the overfitting risk named?
6. **Positioning** — is the relevant prior work cited, and is the advance over it quantified? Is there a work that already showed this?
7. **Form** — the writing conventions from the workspace `CLAUDE.md`, figure quality, labelling, page limit.

### 3. Structure the result

- **Blockers** — cause rejection or major revision if unfixed. Per point: location, why a referee stumbles there, and the smallest possible fix.
- **Weaknesses** — cost goodwill, but are curable.
- **Cosmetics** — form, language, consistency. Keep short.
- **What carries** — the two or three places that genuinely make the text strong, so they are not diluted during revision.

Blockers first, sorted by severity. No politeness formulas, no summary of the manuscript.

### 4. Do not revise

The review delivers the list, not the correction. Changes happen after the author decides which points to address.

## Notes

- For **proposals**, additionally check: does every work package open with its objective, is every objective backed by a checkable number, is there a risk section for the high-risk packages, and is anything repeated (which eats the page limit)?
- A point that cannot be evidenced from the text does not belong in the list. Mark suspected weaknesses as suspected.
