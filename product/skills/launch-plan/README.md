# Launch Plan

Turn a PRD into a launch plan a team can run on the day. It sizes the launch by risk and reach, stages the rollout, writes every go/no-go as a pass/fail check, and decides the rollback before anyone outside the team has access.

Every hard call (who gets it first, what counts as healthy, what makes it stop, who says so, what users see) is made in advance and owned by a role, so nobody has to make it for the first time on launch day.

**Who it's for:** PMs, founders and small teams shipping a pilot, a beta or a full release, and anyone asked "are we ready to launch?"

## Try it

```
Write a launch plan for <feature> from this PRD. <Anything from research, tests or experiments.>
```

Other prompts:

- *"Are we ready to launch?"* gives a readiness check: go, no-go or go with conditions, with each open item and its owner
- *"What tier is this launch?"*
- *"Write the rollback plan for <feature>"*
- *"Plan a beta for <feature> with feature flags"*
- *"Write the launch comms for <feature>"*
- *"Run the post-launch review"* with the real numbers, against the rule the plan set

You can also call it directly: `/product:launch-plan` in Claude Code, `$launch-plan` in Codex.

## How it works

```
PRD + evidence ─▶ Tier ─▶ Stages and flags ─▶ Gates ─▶ Owners and readiness ─▶ Comms ─▶ Watch list ─▶ Rollback ─▶ Review date
```

| Step | What it decides | What keeps it honest |
|---|---|---|
| **Read the inputs** | What's launching, the decision it feeds, gates still open, known risks | Conflicts between inputs are listed, never resolved quietly |
| **Tier** | How much plan this launch needs | Set by the higher of reach and risk, so small but sensitive is never the lightest tier |
| **Stages and flags** | Internal → pilot → beta → GA, cohorts, waves, distribution, every flag with a removal point | Small cohorts counted in people; stages long enough to see repeat use |
| **Gates** | When to move on, and when to stop | Every check is pass/fail, with a threshold and a source |
| **Owners and readiness** | Who does it and who decides, across product, engineering, support, legal and privacy, data, docs | Roles, not names; one decider per call |
| **Comms** | Every message, audience, sender, timing and channel | Support hears first; consent in plain words; bad-news messages written in advance |
| **Watch list** | The first-week signals and their alert thresholds | Health, use and harm; harm alerts at one |
| **Rollback** | Triggers, pause / roll back / stop, who decides, how fast, what users see | Decided and rehearsed before launch, with a stand-in for nights |
| **Review** | The date, the data cut-off, the decision rule | Applies the rule set before launch, as written |

## What you get

A `LAUNCH-PLAN.md` with:

- **Summary and tier**: what's launching, the decision rule, what to protect, and why this tier.
- **Rollout stages and gates**: cohorts, distribution, flags, and pass/fail checks with stop conditions.
- **Owners**: roles and a RACI-lite.
- **Readiness checklist** with owners, due points and status.
- **Comms plan**, including consent and the pause message.
- **Success metrics and the first-week watch list** with alert thresholds.
- **Rollback plan** with triggers, deciders, speed, mechanism and user message.
- **Post-launch review** date and template, and the open items that block go.

## See it work

[Shiftplate pilot](examples/shiftplate/) launches a fictional meal-planning app to 20 nurses. It's tier 2 because it's small but sensitive, it flags three conflicts with its own PRD, and a single portion planned past its use-by pauses the feature within an hour.

## Install just this skill

**Any agent:** `npx skills add subrro11/rohit-skills`, then choose `launch-plan`.

**Claude Code:** `/plugin marketplace add subrro11/rohit-skills`, then `/plugin install product@rohit-skills` (installs every product skill).

**Codex, Cursor, Grok Build:** clone the repo and link this folder into `~/.agents/skills/launch-plan` (or `~/.grok/skills/` for Grok Build).

**Claude.ai:** zip this folder, keeping the name `launch-plan`, and upload it under Customize → Skills.

It works from documents you paste or point to. It doesn't need web access, and it never sends messages, flips flags or publishes builds.

## Files

| File | Purpose |
|---|---|
| [`SKILL.md`](SKILL.md) | The skill itself |
| [`references/tier-chooser.md`](references/tier-chooser.md) | Scoring reach and risk, and what each tier needs |
| [`references/rollout-stages.md`](references/rollout-stages.md) | Stages, cohorts, mobile distribution, flag types, gate format |
| [`references/readiness-checklist.md`](references/readiness-checklist.md) | Readiness items by area and tier |
| [`references/comms-plan.md`](references/comms-plan.md) | Comms table, consent checklist, pause and rollback messages |
| [`references/rollback-playbook.md`](references/rollback-playbook.md) | Pause, roll back or stop; the trigger table; mobile notes |
| [`references/post-launch-review.md`](references/post-launch-review.md) | Review template and rules |
| [`references/quality-checklist.md`](references/quality-checklist.md) | 26 checks to run before handover |
| [`examples/shiftplate/`](examples/shiftplate/) | A full plan for a fictional product's pilot |

## Further reading

- martinfowler.com, [Feature Toggles](https://martinfowler.com/articles/feature-toggles.html): release, experiment, ops and permission toggles, and keeping their number down.
- Google SRE workbook, [Canarying releases](https://sre.google/workbook/canarying-releases/): sizing a canary, comparing it against a control, and when to roll back.
- Google SRE book, [Reliable product launches at scale](https://sre.google/sre-book/reliable-product-launches/): launch checklists, gradual rollouts and feature flag frameworks.
- Apple, [TestFlight](https://developer.apple.com/testflight/): internal and external testers, and review for external builds.
- Google Play Console Help, [open, closed and internal testing](https://support.google.com/googleplay/android-developer/answer/9845334): the three testing tracks and their limits.
