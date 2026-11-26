# Copy Review

Review every word in an interface and get back severity-ranked findings, each with a rewrite ready to paste and a reason. It fixes term chaos with a glossary, checks tone against the moment the user is in, and can apply the rewrites to the code.

It works on a running prototype, a codebase, a design file export or screenshots, and it catches the strings people miss: errors that only appear on a bad input, text written by script, screen reader names, and the messages that should exist but don't.

**Who it's for:** designers, PMs, content designers and engineers who want the words fixed before a test or a launch, and teams whose prototype was written by a coding agent and reads like it.

## Try it

```
Review the copy in <file or screen>. It's <product> for <who>, who are usually <their state> when they use it.
```

Other prompts:

- *"What should this button say?"* gives one rewrite, one alternative and the reason, in chat
- *"Rewrite these error messages"*
- *"Fix the empty states on the dashboard"*
- *"We call this three different things. Make a glossary"*
- *"Is the tone right for someone who's just been told their payment failed?"*
- *"Apply the Blocker and Major fixes"* after a review

You can also call it directly: `/design:copy-review` in Claude Code, `$copy-review` in Codex.

## How it works

```
Context ─▶ Inventory ─▶ Glossary ─▶ Findings ─▶ Rewrites ─▶ Apply
```

| Step | What it does | What makes it trustworthy |
|---|---|---|
| **Context** | Names the product, the user and the state they're in | Sets the tone for every rewrite |
| **Inventory** | Lists every string, including generated, error-only, hidden and missing ones | Each string is quoted exactly and marked OK or linked to a finding |
| **Glossary** | Picks one term per concept and retires the rest | Rewrites can't drift back to the old words |
| **Findings** | Checks each string by element type: headings, buttons, labels, errors, empty states, confirmations, toasts, tooltips, dates | Ranked Blocker, Major, Minor, Polish by what the words cost the user |
| **Rewrites** | Writes the actual words, usually fewer of them | Each one is true to what the product does, or marked as a guess |
| **Apply** | Changes strings in the code, Blockers first | Strings only, no logic or layout; the changed screens are checked again |

The house rules: no eyebrow labels, no explaining the interface, nouns for headings and verbs for buttons, one term per concept, errors that say what happened and what to do next, empty states that say how to fill them, sentence case, and dates the way people say them.

## What you get

A `COPY-REVIEW.md` with:

- **A three-line summary.** The biggest problem, counts by severity, and what to fix first.
- **A glossary.** One term per concept and the words to stop using.
- **Findings by severity.** Before → after, a reason in terms of the user's cost, and the rule.
- **The full inventory.** Every string, so you can see nothing was skipped.
- **Out of scope.** UX and accessibility problems spotted along the way, one line each, for a UX review.
- **An apply list.** One row per string change, ready for you or an agent to work through.

## See it work

[Shiftplate copy review](examples/shiftplate/) is a full review of a fictional product's first prototype, built by a coding agent from a PRD. It finds a banner that describes something that didn't happen, a food-safety message that doesn't exist, and six words for one portion of curry.

## Install just this skill

**Any agent:** `npx skills add subrro11/rohit-skills`, then choose `copy-review`.

**Claude Code:** `/plugin marketplace add subrro11/rohit-skills`, then `/plugin install design@rohit-skills` (installs every design skill).

**Codex, Cursor, Grok Build:** clone the repo and link this folder into `~/.agents/skills/copy-review` (or `~/.grok/skills/` for Grok Build).

**Claude.ai:** zip this folder, keeping the name `copy-review`, and upload it under Customize → Skills.

It reads files and screenshots. Applying fixes needs an agent that can edit files.

## Files

| File | Purpose |
|---|---|
| [`SKILL.md`](SKILL.md) | The skill itself |
| [`references/copy-rules.md`](references/copy-rules.md) | Rules by element, numbers and dates, glossary format, and the tone ladder |
| [`references/finding-format.md`](references/finding-format.md) | Severity scale, inventory, finding and apply list formats |
| [`references/quality-checklist.md`](references/quality-checklist.md) | 30 checks to run before handover |
| [`references/sources.md`](references/sources.md) | Further reading |
| [`examples/shiftplate/`](examples/shiftplate/) | A full review of a fictional prototype, with the fixed version |
