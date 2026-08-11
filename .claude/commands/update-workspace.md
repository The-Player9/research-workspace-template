# Update Workspace

Brings an existing workspace to a newer framework version. It **never re-runs the setup**: no question is asked again, no module is re-chosen, nothing you wrote is regenerated.

Changes are sorted by **conflict, not by importance**. A rule file you never touched is brought up to date and reported. Only a file you edited yourself produces a question, which in practice is a handful of places rather than twenty. The judgement calls a changelog demands about your own material are not asked in the chat at all; they are written into your workspace as dated obligations, because a decision that scrolls past in a session is a decision nobody made.

If `CLAUDE.md` carries no version marker, this workspace was never initialised. Say so and stop; `/init-workspace` is the right command then.

## Modes

| Call | Behaviour |
|---|---|
| `/update-workspace` | Default. Applies every conflict-free change, asks only on files you edited, writes the obligations down. |
| `/update-workspace --review` | Asks about every change individually, including the conflict-free ones. Worth it across a large version jump. |
| `/update-workspace --dry-run` | Changes nothing. Reports what would be applied, what would be asked, and what obligations would follow. |

A path may be passed in any mode: `/update-workspace --review ~/rwt-upstream`.

## 1. Get the reference copy

The comparison needs a **current copy of the template, from outside this workspace**. The `CHANGELOG.md` inside an instance is that instance's own log; it froze at setup and can never report a newer version. Comparing against it was the defect that made update runs report "nothing changed" before 0.1.4.

Take the first of these that works, and say which one you took:

1. A path passed with the call.
2. A clone that already sits next to the workspace.
3. A fresh clone from the `source:` URL in the marker: `git clone https://… /tmp/rwt-upstream`. Clone with full history and tags, because step 4 needs both.
4. No network available: ask the user to download the repository as a zip and give the path. Step 4 then falls back to its weaker test.

If the marker carries no `source:` field, it predates this skill. Use `https://github.com/The-Player9/research-workspace-template`, ask whether this workspace came from a fork instead, and write the answer into the marker so the next run needs no question. Delete a clone you created yourself when the run finishes; leave one the user provided.

## 2. Read the marker

```
<!-- workspace-framework: <version> | profile: <preset> | lang-notes: <xx> | lang-pub: <xx> | modules: <a,b,c> | source: <url> -->
```

The version says which changelog entries apply. The module list says which of them can apply at all: a change to a file of an inactive module is reported in one line and otherwise ignored.

## 3. Build the difference

Read `CHANGELOG.md` in the **reference copy** and take every entry above the marker version. Each entry names its affected files in brackets, so only those files need inspecting. An unlisted difference between the two folders is the user's own doing and is never touched.

## 4. Establish the baseline, then classify

The question per file is not "does it differ from the current template", which every filled-in file does. It is "has the user edited it since their own version". That needs the file **as it was shipped at the marker version**.

**With tags**, the normal case: every release is tagged `v<version>`, so the baseline is `git show v<version>:<path>`. Check with `git tag` that the tag exists before relying on it.

**With history but without the tag**, a fork that does not tag, or a version predating tagging: find the release commit by walking the commits that modified `CHANGELOG.md` and reading its top heading at each, then take the file from that commit.

**Without history**, a zip download or a shallow clone: no baseline exists. Fall back to the per-rule test described below for every file, and say in the report that the weaker test was used.

Then sort each affected file:

| Case | What happens |
|---|---|
| File absent, module inactive | Reported in one line, nothing proposed |
| File identical to its baseline | **Conflict-free.** Updated without asking, listed in the report |
| File already identical to the reference | Nothing to do, not mentioned unless `--dry-run` |
| File differs from its baseline | **Conflicted.** Goes to step 6 as a question |

**`CLAUDE.md` is always conflicted at file level** and is never treated wholesale. Init filled its placeholders and dropped the blocks of inactive modules, so it has differed from the skeleton since the day it was written. Descend to rule level instead: for each change the entry describes, look for the **old rule text** in the user's file. Found unchanged, so the user never touched that rule, and the replacement is conflict-free. Altered or absent, so it becomes a question with the surrounding text shown. The same per-rule test applies to any file the user extends by design, `knowledge/learnings/40_error_catalog.md` above all.

## 5. Apply the conflict-free set

Apply it, then report it as a plain list of file and rule. Do not ask for confirmation, and do not present these one at a time; that is the whole point of the classification. In `--review` they are presented individually anyway, and in `--dry-run` only listed.

## 6. Ask about the conflicted set

Per conflicted change show the new rule text, the user's current text at that place, and the insertion point. The user accepts, rejects, or edits. Nothing here is decided by default, because these are the places where the user has already expressed an intention.

## 7. Write the obligations down

Every changelog entry carries a paragraph headed **"Decide, if you are updating from …"**. That paragraph concerns material the framework cannot see: existing proposals, drafts, project files, records. It is **not** a gate on applying the rule, and it is never resolved in this conversation. Write it into the workspace instead, as a dated TODO line, so it outlives the session:

- Concerns one sub-project → a TODO line in that project's `CLAUDE.md`, dated, quoting the obligation in one sentence.
- Concerns records or measurements → a dated entry in that project's `Laborbuch.md`.
- Workspace-wide, or the project is not identifiable → a TODO line in the parent `CLAUDE.md`, and say so in the report.

**A rejected change becomes an obligation too**, phrased as the decision it is: either "not yet, revisit" or "deliberately not adopted, because …". Write the user's reason down verbatim if they gave one. Without this line the rejection is invisible on the next run and the same offer arrives again with no memory of why it was declined.

## 8. Close out

- Raise the version in the marker only if something was applied. Otherwise leave it and say so, so the same offer arrives next time.
- Add one dated line to the workspace `CHANGELOG.md`: version applied, how many changes were conflict-free, which were rejected. That file is this workspace's log; the framework's own history stays in the reference copy.
- Report, in this order: applied without asking, decided by the user, skipped for inactive modules, obligations written and where. Name the baseline method, because a run that fell back to the weaker test is less certain about what counted as untouched.

## Constraints

- **Never** touch `Laborbuch.md` other than to add an obligation entry, never touch the contents of `knowledge/`, and never touch a sub-project's own files beyond the TODO lines of step 7. A framework update changes rules, never records or results.
- **Never** overwrite `CLAUDE.md` wholesale, in any mode. It holds decisions no changelog knows about.
- Never re-ask the init questions. A module the user now wants is a separate request, and it adds files rather than rewriting existing ones.
- `--dry-run` writes nothing at all, including the obligations of step 7.
