# Usability Test Plan

Turn a prototype, a prototype prompt or a PRD into a moderated usability test you can run tomorrow. It names the one belief the test has to settle, writes the screener and the session script, and sets pass and fail for every task before anyone sits down.

Tasks are written as scenarios with no button names or hints. Timings and thresholds come from the PRD with their IDs, and the whole test ends in a pass, iterate or stop decision.

**Who it's for:** PMs, designers and founders who have something clickable and need to put it in front of five real people this week, without a research team.

## Try it

```
Write a usability test plan for this prototype. PRD and prototype prompt attached.
```

Other prompts:

- *"How many users do I need to test this?"*
- *"Write a screener for <who>"* gives just the screener
- *"Turn these into non-leading task scenarios"*
- *"Write the script for a 30-minute remote test"* gives just the script
- *"Make an unmoderated version of this test"*

You can also call it directly: `/product:usability-test-plan` in Claude Code, `$usability-test-plan` in Codex.

## How it works

```
Inputs ─▶ Riskiest assumption ─▶ Research questions ─▶ Who and how many ─▶ Tasks ─▶ Success criteria ─▶ Script ─▶ Notes and scoring
```

| Step | What it produces | What keeps it honest |
|---|---|---|
| **Riskiest assumption** | The one belief the test has to settle | Taken from the PRD's hypothesis and gates, not chosen for convenience |
| **Research questions** | Three to five things to learn | Each one answerable by watching, and each one covered by a task |
| **Who and how many** | Participants by behaviour, a screener, a number with a reason | Five per group for a qualitative round, tested again after fixes; no claim that five gives a reliable rate |
| **Tasks** | Scenarios with a goal, the details needed, a start state and a reset | No interface labels, no steps, act rather than describe |
| **Success criteria** | Pass, pass with help and fail per task, targets and timings | Set before testing; PRD numbers cite their IDs; new ones marked *proposed* |
| **Script** | Intro, consent, warm-up, tasks, comprehension check, debrief, timed to the minute | Neutral prompts, a "don't say" list, and a rule for when someone is stuck |
| **Notes and scoring** | A note-taking grid, outcome levels and a severity scale | Counts, not averages; timed tasks run without think-aloud |

## What you get

A `TEST-PLAN.md` with:

- **The riskiest assumption** in one line, and why.
- **Research questions** mapped to tasks.
- **Participants**: who, how many, exclusions, incentive, and a screener with a rule for every question.
- **Task cards and scenarios**, each with a start state, an end state, pass and fail signals and a target.
- **A decision rule**: what counts as pass, iterate or stop.
- **The session script**, word for word, with minutes per block.
- **A note-taking grid** and scoring rules.
- **An unmoderated variant**, if you ask for one.

## See it work

[Shiftplate test plan](examples/shiftplate/) sets up the 5-nurse prototype test from the [PRD Generator](../prd-generator/) showcase. It copies the PRD's timings with their IDs, runs the timed tasks silently, and lists what the prototype has to support before the test can run.

## Install just this skill

**Any agent:** `npx skills add subrro11/rohit-skills`, then choose `usability-test-plan`.

**Claude Code:** `/plugin marketplace add subrro11/rohit-skills`, then `/plugin install product@rohit-skills` (installs every product skill).

**Codex, Cursor, Grok Build:** clone the repo and link this folder into `~/.agents/skills/usability-test-plan` (or `~/.grok/skills/` for Grok Build).

**Claude.ai:** zip this folder, keeping the name `usability-test-plan`, and upload it under Customize → Skills.

## Files

| File | Purpose |
|---|---|
| [`SKILL.md`](SKILL.md) | The skill itself |
| [`references/task-writing.md`](references/task-writing.md) | Good and leading tasks side by side, probes to ask afterwards |
| [`references/script-template.md`](references/script-template.md) | The session script, neutral prompts and what not to say |
| [`references/screener-template.md`](references/screener-template.md) | Screener rules and template |
| [`references/note-grid-and-scoring.md`](references/note-grid-and-scoring.md) | Roles, the note-taking grid, outcome levels, severity, timings |
| [`references/quality-checklist.md`](references/quality-checklist.md) | 27 checks to run before handover |
| [`examples/shiftplate/`](examples/shiftplate/) | A full plan for a fictional product's prototype |

## Further reading

Pages this skill's guidance draws on. Read them for the full argument.

- Jakob Nielsen, [Why you only need to test with 5 users](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/), Nielsen Norman Group. Five per round for qualitative testing, as part of several small rounds; three or so per group when groups differ; larger samples for quantitative studies.
- Marieke McCloskey, [Turn user goals into task scenarios for usability testing](https://www.nngroup.com/articles/task-scenarios-usability-testing/), Nielsen Norman Group. Realistic, actionable scenarios without clues or interface terms.
- Jakob Nielsen, [Thinking aloud: the #1 usability tool](https://www.nngroup.com/articles/thinking-aloud-the-1-usability-tool/), Nielsen Norman Group. How think-aloud works, its limits, and prompting without steering.
- Jakob Nielsen and Raluca Budiu, [Success rate: the simplest usability metric](https://www.nngroup.com/articles/success-rate-the-simplest-usability-metric/), Nielsen Norman Group. Scoring completion on levels, why not to average them, and why think-aloud distorts timings.
- Kathryn Whitenton, [How to use screening questions to select the right participants](https://www.nngroup.com/articles/screening-questions-select-research-participants/), Nielsen Norman Group. Hiding the study's purpose, distractors, and avoiding yes/no questions.
- GOV.UK Service Manual, [Using moderated usability testing](https://www.gov.uk/service-manual/user-research/using-moderated-usability-testing). Planning, discussion guides, putting participants at ease, and using dummy data.
