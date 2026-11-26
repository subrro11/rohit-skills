# Hypothesis and metrics

## The hypothesis

> If we **change X** for **segment Y**, then **metric Z** moves by at least **N** within **time T**, because **mechanism M**.

| Part | Good | Weak |
|---|---|---|
| **Change X** | One change, described so an engineer could build it | "Improve the check-in" |
| **Segment Y** | Who's eligible, and who's excluded | "Users" |
| **Metric Z** | Numerator, denominator, window | "Engagement" |
| **N** | The smallest change worth acting on, absolute or relative, stated | "A lift" or the change you hope for |
| **Time T** | Long enough for the behaviour to settle | Whatever the sprint allows |
| **Mechanism M** | Why this change should move this metric, from evidence | Missing, or restates the change |

Then write the **null result**: "If Z doesn't move by N, we conclude M is wrong or too weak, and we will…" If you can't say what you'd do, the experiment can't change a decision.

**Example:** If we replace the three-option check-in with a one-tap "All eaten?" for pilot users, check-ins completed per worked shift rise by at least 20 points within 4 weeks, because tired users skip anything that needs more than one decision.

## The primary metric

One metric decides the result. It should:

- **Move if the hypothesis is true.** Closest to the mechanism, not a distant business outcome.
- **Be hard for the change to game.** If the change sets a default, auto-fills, or nags, the metric must count only real actions. A default that fills itself in will "raise completion" without anyone doing anything.
- **Have a clear denominator.** Per eligible user, per exposure, per occasion. Name the event that defines eligibility.
- **Be measurable in the time available.** A 90-day retention metric can't decide a 2-week test.
- **Have a baseline**, measured or labelled *assumed* with where the guess came from.

## Guardrails

Two to four metrics that must not get worse. Each gets a threshold that blocks shipping, written before launch.

Common guardrails:

- **Data quality**: does the change make the data wrong? (A simpler form may be completed more often and less accurately.)
- **Downstream outcome**: the metric the primary was meant to serve.
- **User cost**: time taken, errors, complaints, opt-outs, uninstalls.
- **System health**: latency, crashes, failed requests.

When a guardrail can't be measured from product events, plan an **audit**: a small independent check (a sample of records verified by hand, a photo, a short interview) that gives a reference to compare against.

## Secondary metrics

For explanation only. They can tell you *why* the primary moved, but they never decide the result. Keep them few. If one jumps and the primary doesn't, that's a new hypothesis, not a win.

## Baselines

| Source | How to label it |
|---|---|
| Measured in the product, recent | Cite the query and date |
| From research or a test with a handful of people | *assumed*, with the source ("3 of 5 in a usability test said…") |
| A guess | *assumed*, with the reasoning, and how the experiment will replace it |

If the baseline is assumed, plan to measure it in the first period and recheck the sample size. Don't change the decision rule after seeing it.
