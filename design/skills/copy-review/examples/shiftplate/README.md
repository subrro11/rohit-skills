# Showcase: Shiftplate copy review

A full copy review of a fictional product's first prototype. Shiftplate is the meal-planning app for nurses on rotating 12-hour shifts from the [PRD Generator showcase](../../../../../product/skills/prd-generator/examples/shiftplate/). A coding agent built v0.1 from the PRD; this review writes the copy for v0.2.

- [Read the review](REVIEW.md)
- [v0.1 prototype](prototype/index.html), the before
- [v0.2 with the copy applied](prototype/index-v0.2-copy.html), the after

Both open in a browser with no build step.

Moments worth looking at:

- **The worst finding isn't about wording.** The banner asks "Regenerate plan?" when the plan has already changed, and there's no button to answer it. Copy that isn't true ranks above copy that's unclear.
- **The silence is a Blocker.** A dish past its use-by date drops out of the plan without a word, while the fridge count still includes it. The review writes the message that should have been there.
- **A placeholder hides a default.** Leaving the date blank saves it as today, which quietly adds days to food prepped earlier. The fix is a four-word hint.
- **Seven words for one thing.** Servings, meals, items, inventory, prep, qty and portion all mean the same here. The glossary picks "portion" and retires the rest, which settles a whole group of strings in one move.
- **Most rewrites are deletions.** All three screen descriptions, all six eyebrow labels and the welcome line go. The v0.2 screens say more with less.
- **It stays on copy.** A date picker, an undo for Remove and the contrast of the grey text are real problems, but they're one line each under *Out of scope, for ux-review*.

In v0.2 only strings changed, plus the smallest logic that generates them: date formats, plurals, one error per field and the past use-by message. With the welcome and intro gone, the main button moved below the shift chips so the screen still starts with its heading. Everything listed under Out of scope is left as it was.
