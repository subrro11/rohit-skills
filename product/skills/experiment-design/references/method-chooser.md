# Method chooser

Pick the cheapest method that can answer the question with the sample you actually have. Start from two questions:

1. **What are you testing?** Demand (will they want it), value (does the outcome help), or behaviour change (does this version beat that one)?
2. **How many independent units can you get in the time the decision can wait?** Run the numbers in `sample-size-and-power.md` before choosing.

## The methods

| Method | Tests | Needs | Gives you | Watch out for |
|---|---|---|---|---|
| **A/B test** | Behaviour change between two versions | Enough units to reach the sample size in a few weeks; a way to randomise and log the version | A causal estimate with an interval | Peeking, sample ratio mismatch, novelty, contamination |
| **Multi-variant (A/B/n)** | Several versions at once | Even more units: each extra arm needs its own sample, and more comparisons need a stricter α | Which of several versions wins | Splitting traffic too thin |
| **Crossover (within-subject)** | Behaviour change when people are few | A change you can switch on and off; an effect that doesn't linger | A causal estimate from far fewer people, since each is their own control | Carryover, period effects, dropouts mid-sequence |
| **Event-level randomisation** (session, shift, order) | Behaviour change per occasion | Many occasions per person; a change people won't be confused by when it flips | More randomised units | Confusion from switching; correlation within a person (correct for clustering) |
| **Cluster randomisation** (team, site, ward) | Changes that spread inside a group | Many clusters, not just many people | Protection from contamination | Few clusters means little power; correct with the design effect |
| **Pilot with holdout** | Whether a launch moves the metric | A small launch; a random group kept on the old version | A real-world estimate, usually wide | Holdout too small to compare; people in the holdout hearing about it |
| **Fake door (painted door)** | Demand before building | A visible entry point (button, menu item, pricing tier) and an honest "not ready yet" page | Click-through as a signal of intent | Measures curiosity, not use. Tell people what happened; don't do it on anything they depend on |
| **Concierge** | Whether the outcome is valuable | A person who delivers the service by hand, openly | Deep learning from a handful of users | Doesn't scale or test the product's own effort |
| **Wizard of Oz** | Whether the experience works before automating it | A person behind an interface that looks automated | Realistic reactions to the full experience | Deception: debrief participants afterwards |
| **Before/after** | Change over time with no comparison group | A stable baseline period | A weak signal, at best | Seasonality, other launches, regression to the mean, novelty. Use only when nothing else is possible, and name each confound |
| **Qualitative** (interviews, usability, diary) | Why, and what's wrong | 5–12 people | Mechanisms, wording, failure points | Not an estimate of how many. Don't count it as one |

## Rules of thumb

- **Demand before value before behaviour.** Don't A/B test the wording of a feature nobody wants. A fake door or concierge test is cheaper and answers the earlier question.
- **If the reachable MDE is bigger than any plausible effect, the A/B test is off.** Show the maths, then choose from the small-sample methods.
- **Randomise at the level of contamination.** If people in the same team, ward or household will see each other's version, randomise the group.
- **Prefer within-subject when people are few and the change is reversible.** Prefer parallel groups when the change is a one-way door (onboarding, learning something) or when switching would confuse people.
- **A pilot is not a failed A/B test.** It's a different tool: it estimates, it doesn't prove. Report it with an interval and the word "estimate".

## Write the choice down

In the plan, one paragraph:

> **Method:** crossover, alternating weeks, random order per person.
> **Why not an A/B test:** 10 people per group can only detect a 36-point change at 80% power (maths in Sample size).
> **Why not event-level randomisation:** switching every occasion would confuse tired users and leak habits between versions.
