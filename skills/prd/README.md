# prd

Takes a product idea from "we should build X" to a PRD a team can commit to and a coding agent can prototype from the same day.

Most PRD templates start at requirements. This skill starts one step earlier, with the product questions that decide whether the requirements are worth writing.

**Who it's for:** PMs spinning up a PRD for the product or feature they're working on now.

**Best with deep research:** run a research pass first, and `prd` turns the evidence into decisions, citing what's sourced and labelling what's assumed. Use a deep-research skill or your agent's own research tool, or paste in research you already have.

## The loop

```
 Problem ──▶ Product thinking ──▶ PRD ──▶ Prototype with a coding agent ──▶ Test with users
    ▲                                                                            │
    └──────────────────────────── revise the PRD with what you learned ◀─────────┘
```

1. **Problem**: who is stuck, what they do today instead, and what it costs them.
2. **Product thinking**: five questions answered in order (below).
3. **PRD**: Lite, Standard or Full, sized to the stage.
4. **Prototype**: a `PROTOTYPE-PROMPT.md` you hand to a coding agent (Claude Code, Codex, Cursor, Grok Build) to build the thinnest version of the core loop that tests your riskiest assumption.
5. **Test and revise**: five users, one signal, then a new PRD version with a changelog.

The skill covers steps 1–3 and writes the handoff for step 4. **After the PRD, the next step is a prototype.**

## The five product questions

| Question | What the skill gives you | Lands in the PRD as |
|---|---|---|
| **What's the product problem?** | A one-line frame (user, job, obstacle, workaround, cost) and a check that it isn't a solution in disguise | Users and problem |
| **Is there product–market fit, or a path to it?** | A falsifiable PMF hypothesis, the stage you're at (problem, solution, product–market or scale fit), and the signal and threshold that would prove it | Recommendation, metrics, release gates |
| **What's the north star?** | A value metric (not an activity metric), the 2–3 inputs that feed it, and guardrails. The feature's primary metric must move an input | Metrics |
| **What are the goals and non-goals?** | 3–5 outcome goals, plus non-goals of three kinds: deferred (with a trigger), out of scope (positioning), and not optimising for (the tradeoff) | Goals and scope |
| **What do we build first?** | RICE scores for contested items, deliberate overrides for the core loop, the riskiest assumption and basic expectations, and every override logged | Requirements (priority) and the decision log |

You can ask any one of these on its own. For example, *"What should the north star be for a marketplace for home tutors?"* or *"Prioritise these eight features"* gets you a recommendation without a full PRD.

## Use it

Once installed (see the [repo README](../../README.md)), talk to it normally:

- *"Write a PRD for …"* plus your notes, a brief or a call transcript
- *"Do we have product–market fit? Here's our retention and survey data …"*
- *"Help me prioritise this backlog"*
- *"What are the goals and non-goals for …"*
- *"Review this PRD"* returns a scored critique, the top five fixes, and a revised version with numbered feedback (FB1, FB2…)
- *"Write the prototype prompt"* produces a handoff you can paste into a coding agent

It asks at most five questions in one round, each with a default answer, and shows its product thinking in one line per question so you can push back before the full draft.

## What you get

- **It leads with a recommendation.** It names the option that lost, and why.
- **It labels evidence.** Every number is sourced, assumed or fictional, and missing evidence becomes an "Evidence needed:" line. It never invents research.
- **Scope has three lists: in scope, deferred and out of scope.** The out-of-scope list does the positioning work.
- **Acceptance criteria are tests.** Words like "intuitive" or "seamless" aren't allowed without a threshold.
- **Release gates are pass/fail checks.**
- **It ends with a prototype**: the riskiest assumption, the fidelity (clickable, working slice or Wizard of Oz), what to fake, and when it's done.

## Files

| File | Purpose |
|---|---|
| [`SKILL.md`](SKILL.md) | The skill itself |
| [`references/product-thinking.md`](references/product-thinking.md) | Problem framing, PMF stages and signals, north star trees, goals and non-goals, prioritisation |
| [`references/template-lite.md`](references/template-lite.md) | 1–2 page PRD for deciding whether to invest |
| [`references/template-standard.md`](references/template-standard.md) | Full PRD for a team build, plus optional sections for a Full PRD |
| [`references/quality-checklist.md`](references/quality-checklist.md) | 41 checks used both before handover and in review mode |
| [`references/prototype-handoff.md`](references/prototype-handoff.md) | How to choose what to prototype, and the template for the coding-agent prompt |
| [`examples/quiet-hours-lite.md`](examples/quiet-hours-lite.md) | Worked Lite PRD (fictional) |
| [`examples/quiet-hours-prototype-prompt.md`](examples/quiet-hours-prototype-prompt.md) | Its prototype handoff (fictional) |
