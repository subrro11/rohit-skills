# UX Review

Review a screen, a flow, a prototype or a live product for usability, and get a ranked list of what to fix. It starts from who the user is and what they're trying to do, walks each task step by step, then checks heuristics, states and accessibility basics.

Every finding names the task it gets in the way of, the heuristic it breaks, the evidence on screen, and a fix you could build. The review ends with a prioritised fix list.

**Who it's for:** PMs, designers and engineers who want to catch the problems before a usability test or a release, and anyone with a screen that "feels off" who wants to know why.

## Try it

```
Review the UX of <prototype, URL or screenshot>. The user is <who, and in what conditions>. Their top tasks are <task 1>, <task 2>, <task 3>.
```

Other prompts:

- *"Why is this checkout confusing?"* reviews one flow
- *"Critique this screen"* with a screenshot gives a quick pass in chat
- *"Run a heuristic evaluation on <URL>"*
- *"Check this prototype for mobile usability at 390 px"*
- *"Review this before we test it with users"*

You can also call it directly: `/design:ux-review` in Claude Code, `$ux-review` in Codex.

## How it works

```
User and tasks ─▶ Task walks ─▶ Heuristics ─▶ States ─▶ Accessibility basics ─▶ Rank ─▶ Fix list
```

| Stage | What it checks | What keeps it honest |
|---|---|---|
| **User and tasks** | Who uses it, in what conditions, and the three to five things they must be able to do | Tasks come from the brief, or are marked *assumed* |
| **Task walks** | Every step of every task: can they see it, do it, tell it worked, and get back | Done in the real thing at the target width, with taps counted |
| **Heuristics** | The ten usability heuristics, hierarchy and layout, plus reach, target size, gestures and keyboards on mobile | Each one produces a finding with evidence, or is skipped |
| **States** | Empty, first run, loading, partial, success, errors, offline, permission, edge data, delete, interruptions | Each is triggered, or marked not triggered and why |
| **Accessibility basics** | Contrast, target size, focus, labels | Ratios and sizes are measured, not eyeballed |
| **Rank** | Severity from how many hit it, how hard it is to get past, and whether it repeats | Silent wrong results rank above loud errors |

Copy wording is out of scope: it notes each copy issue in one line and hands it to `copy-review`.

## What you get

A `UX-REVIEW.md` with:

- **A verdict first.** Is it ready, and the one thing most likely to fail.
- **Task walk tables.** Each step, what happened, and the finding it led to.
- **Findings by severity**: blocker, major, minor, cosmetic. Each has a task, heuristic, evidence, fix and size.
- **States and accessibility tables.**
- **Copy, handed off**, and **what works**.
- **A prioritised fix list**: fix before testing, fix next, later.

Screenshots go in a `screens/` folder beside it.

## See it work

[Shiftplate UX review](examples/shiftplate/) is a real review of a fictional meal-planning prototype for nurses on 12-hour shifts. It finds a dead end that only shows up when you press back, ranks a silently dropped dish above a loud error, and measures every tap target and contrast ratio it reports.

## Install just this skill

**Any agent:** `npx skills add subrro11/rohit-skills`, then choose `ux-review`.

**Claude Code:** `/plugin marketplace add subrro11/rohit-skills`, then `/plugin install design@rohit-skills` (installs every design skill).

**Codex, Cursor, Grok Build:** clone the repo and link this folder into `~/.agents/skills/ux-review` (or `~/.grok/skills/` for Grok Build).

**Claude.ai:** zip this folder, keeping the name `ux-review`, and upload it under Customize → Skills.

It works best with an agent that can open a browser and take screenshots. Without one, it reviews screenshots and designs you share and says what it couldn't check.

## Files

| File | Purpose |
|---|---|
| [`SKILL.md`](SKILL.md) | The skill itself |
| [`references/heuristics.md`](references/heuristics.md) | The ten heuristics in plain words, layout and hierarchy, and mobile specifics |
| [`references/states-checklist.md`](references/states-checklist.md) | Every state to check, what good looks like, and how to trigger it |
| [`references/severity-and-format.md`](references/severity-and-format.md) | The severity scale, finding format, task walk table and fix list |
| [`references/quality-checklist.md`](references/quality-checklist.md) | 24 checks to run before handover |
| [`references/sources.md`](references/sources.md) | Further reading: the public guidance behind the references |
| [`examples/shiftplate/`](examples/shiftplate/) | A real review of a fictional product's prototype |
