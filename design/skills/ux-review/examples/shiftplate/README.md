# Showcase: Shiftplate UX review

A real review of a fictional product's prototype. Shiftplate is the meal-planning app for nurses on rotating 12-hour shifts from the [PRD Generator showcase](../../../../../product/skills/prd-generator/examples/shiftplate/). The [prototype](prototype/index.html) is the first pass a coding agent built from its prototype prompt, with real problems left in. This review decides what changes for v0.2, before five nurses test it.

[Read the review](REVIEW.md)

Moments worth looking at:

- **The top finding came from tapping, not reading.** The browser back gesture changes the address but not the screen, so Log Prep is a dead end. That only showed up by actually pressing back.
- **A silent drop outranks a loud error.** The expired stew is counted on Home and listed in the fridge, then left out of the plan with no word. It's ranked a blocker, above the generic error message.
- **Measurements, not adjectives.** Day chips are 48 × 28 px with 4 px gaps, and the muted grey is 2.22:1. Both were measured, not eyeballed.
- **It says what it only read.** The use-by bug for big fridges (F16) comes from the code, not the screen, and the review says so and adds a test fridge to trigger it.
- **Copy is handed off, not rewritten.** "Rota mutation detected" gets one line under *Copy, handed off* for the copy-review skill.
- **It keeps what works.** The day, night and off colours and the two-tap loop are listed so v0.2 doesn't lose them.

## Screens

| File | What it shows |
|---|---|
| [`screens/1-home.png`](screens/1-home.png) | Home at 390 px: Optimise at the top, unlabelled day chips |
| [`screens/2-rota-changed.png`](screens/2-rota-changed.png) | After one chip tap: the banner, and Upcoming meals already changed |
| [`screens/3-plan.png`](screens/3-plan.png) | The plan: faint tags, no summary, the same dish all day |
| [`screens/4-log-error.png`](screens/4-log-error.png) | Log Prep after an empty Submit: one error for every field, no way back |
