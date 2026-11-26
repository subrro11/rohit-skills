# Opportunity mapping

Insights become decisions through an opportunity map. The shape follows an opportunity solution tree:

```
Outcome (one metric the team is trying to move)
├── Opportunity: a need, pain or desire, in the user's terms     ← from insights
│   ├── Candidate solution
│   │   └── Assumption to test
│   └── Candidate solution
└── Opportunity
```

## Outcome

Start from one outcome the team already owns: a product metric that measures what users do, such as "share of prepped portions binned" or "nurses who re-plan through two rota changes". Take it from the PRD or the brief. If there isn't one, say so and propose one; don't map against "engagement".

## Opportunities

An opportunity is a need, pain or desire, phrased the way a participant would say it.

- **Test: could more than one solution meet it?** "I need a one-tap check-in" is a solution in disguise. "After a 12-hour shift I'm too tired to report what I ate" is an opportunity.
- **Every opportunity cites insights or themes.** No evidence, no opportunity. If the team has one in mind that the data doesn't back, list it under "not supported by this round".
- **Nest them.** A broad opportunity ("keeping the plan up to date is effort") can hold narrower ones ("logging prep feels like homework", "check-in after a shift is too much"). Act on the narrow ones.
- **Rank on evidence and on how much moving it moves the outcome**, not on effort. Effort comes later, when comparing solutions.

## Candidate solutions

- **At least two per opportunity you're prioritising**, ideally three, so the first idea has competition.
- **Ideas from participants are inputs, not specs.** P5 suggesting "assume I ate it unless I say" is a good candidate; it still needs testing.
- Mark each solution as *new*, *already in the PRD*, or *deferred in the PRD* with its trigger.

## Assumptions to test

For the top one or two solutions, list what must be true for them to work, and pick the riskiest:

| Kind | Question |
|---|---|
| Desirable | Will people do it? |
| Usable | Can they do it without help, in the context that matters? |
| Feasible | Can it be built well enough? |
| Viable | Does it still serve the outcome and the business? |
| Measurable | Does it break the metric we use to judge it? |

The last row matters more than it looks. A solution that removes friction by guessing on the user's behalf can quietly corrupt the metric the whole test is judged on.

For each risky assumption, write the smallest test that would show it's wrong, and what result would count as a fail. If an `experiment-design` skill is available, hand these over.

## Output table

| Opportunity | Backed by | Candidate solutions | Riskiest assumption | Test |
|---|---|---|---|---|
| After a 12-hour shift I'm too tired to report what I ate | I2 (Strong) | One-tap "all eaten"; ask at next re-plan only | Nurses will mark the exceptions, so binned isn't under-counted | … |

## Parked

Outliers and out-of-stance requests go below the table with the PRD rule that covers them (a deferral trigger, an out-of-scope line). They're visible, not acted on.
