# Changelog

## 0.4.0 · 2026-11-13
- Added **Deep Research** (`product/skills/deep-research`): decision-led research on a company or an idea, run in order: company (or problem), competitors, news, trends, then frameworks. It cites only sources it read, logs every claim in an evidence ledger with a quote and a confidence grade, lists gaps as "Evidence needed:", and maps findings to PRD sections.
  - Three modes: full pass, quick check, and gap fill for an existing PRD.
  - Seven frameworks with guidance on which fits which decision: jobs to be done, positioning map, five forces, PESTLE, business model, moats and a competitor gap table.
  - A verification pass before the report is written: quotes checked against their context, numbers against what they measure, absence claims against named searches, plus a guide to sources that look reliable and aren't.
  - Contrarian questions, a pressure test on the biggest gap, and a "What the research contradicts" section.
  - Research plan with search patterns per stage, a source ladder and stopping rules, a report template, and a 26-point quality checklist.
- Each skill's README now stands alone, with a prompt to try, an example and install steps for that skill.
  - Showcase: a real research run on the fictional Shiftplate's market that fills the Evidence needed lines in its PRD.

## 0.3.0 · 2026-11-07
- Repo renamed to **rohit-skills**, grouped by discipline: `rohit-skills › product › prd-generator`. Install with `/plugin install product@rohit-skills` or `npx skills add subrro11/rohit-skills`.
- Added an end-to-end showcase (`examples/shiftplate/`): a real quiz run, its PRD and its prototype prompt, on a fictional product.
- Added a demo GIF and a "Try this first" prompt to the README.

## 0.2.0 · 2026-11-07
- Renamed to **PRD Generator and Product Quiz Agent** (`skills/prd-generator`).
- Quiz mode: asks the five product questions one at a time, grades each answer, and ends with a scorecard that turns into a PRD.
- README and manifests no longer refer to release dates.

## 0.1.0 · 2026-11-06
- `prd`: work through a product problem and write or review a PRD.
  - Product thinking: problem framing, PMF hypothesis and stage, north star tree, goals and non-goals, RICE prioritisation with logged overrides.
  - Lite and Standard templates, a 41-point quality checklist, review mode with numbered feedback.
  - Prototype handoff: a coding-agent prompt that tests the riskiest assumption.
  - Fictional worked example plus its prototype prompt.
  - Works in Claude Code (plugin), Claude.ai, Codex and Cursor (`~/.agents/skills/`), and Grok Bot / Grok Build.
  - Uses research output as its evidence base, so it pairs well with a deep-research pass.
