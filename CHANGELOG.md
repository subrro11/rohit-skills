# Changelog

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
