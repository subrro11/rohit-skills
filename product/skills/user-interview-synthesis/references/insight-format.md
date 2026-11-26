# Insight format

A theme says what happened. An insight says why it matters and what follows. Write one insight per theme that changes a decision. Themes that change nothing stay in the theme table and don't get an insight.

## Shape

```markdown
### I1. <the insight as one sentence a stakeholder could repeat>

**Observation:** what people did and said, with counts and IDs. (N3, N7, N12)
**Why it matters:** what this does to the goal, the metric, or the core loop. Name the goal or metric.
**Implication:** what to do, change, test or stop. Phrase it as a direction, not a spec.
**Strength:** Strong / Moderate / Weak, and the reason in a few words.
**Evidence:** P1 "…" · P3 "…" · P5 "…"
```

## Rules

- **The headline is a claim, not a topic.** "Check-in is where the loop breaks" beats "Check-in findings".
- **Observation comes with a count.** *3 of 5 said…*, *4 of 5 completed…*. Never "many", "most" or "users felt".
- **Separate did from said in the observation line.** If both are present, lead with the behaviour.
- **Why it matters names something real**: a goal, a metric, a gate, a requirement, a step in the loop. If you can't name one, the insight probably doesn't matter yet.
- **The implication is a direction, not a decision.** "Test a one-tap check-in" is an implication. "Ship a one-tap check-in" is a decision, and a five-person test rarely earns one.
- **Two or three verbatims at most**, each with its participant ID, each under 25 words, each copied exactly. Pick the plainest quote, not the most dramatic.
- **One insight, one idea.** If the "why it matters" has two unrelated parts, split it.

## Weak and strong examples

Weak:

> Users found logging tedious and want it to be faster.

No count, no IDs, "users" is everyone, "tedious" is the analyst's word, and the implication is a wish.

Strong:

> **Logging is the step people would skip, and the wording of "portions" adds to it.**
> **Observation:** 3 of 5 logged the fridge within 2 minutes (N8, N12, N17); P2 and P4 took 2:50 and 3:10 after misreading "portions" (N10, N14). 3 of 5 called logging homework (N9, N13, N16).
> **Why it matters:** misses gate G0 (needs 4 of 5) and the logging guardrail.
> **Implication:** reword portions as meals the dish makes, and test a faster repeat-last-week path.
> **Strength:** Strong: behaviour and statements agree, across 4 of 5 participants.

## Words to avoid

| Instead of | Write |
|---|---|
| Users love it | 4 of 5 completed it in under a minute, and 2 praised it unprompted |
| Many people | 3 of 5 |
| Users want X | P2 asked for X (unprompted) |
| Pain point | What it costs them, in their terms |
| Delightful, frustrating | What they did or said that shows it |
