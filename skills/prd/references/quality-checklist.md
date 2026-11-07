# PRD quality checklist

Score each item **pass / weak / fail** with a one-line reason that quotes the document. Use this list both before handing over a draft and in review mode.

## Decision

1. **Recommendation first.** The first section says what to build and why now, in 5 sentences or fewer.
2. **A rejected alternative is named**, with the reason it lost.
3. **Why now** is concrete: a change in tech, market, regulation, data or strategy, not "users want it".

## Problem

4. **One primary user**, specific enough to recruit for an interview.
5. **The current workaround is named.** If nobody has a workaround, ask whether the problem is real.
6. **The cost of the problem** is quantified, or labelled as assumed with a plan to measure it.
7. **The problem comes before the solution.** No feature names appear before the problem is stated.

## Evidence

8. **Every number is labelled** as sourced, assumed or fictional.
9. **No invented research.** No uncited quotes or survey results.
10. **Gaps are explicit**: "Evidence needed:" lines say what would settle each one.

## Product thinking

11. **PMF hypothesis is stated** with a segment, a value, an alternative, a signal and a threshold. The stage is named.
12. **North star measures value delivered** (for example, projects shipped), and this feature's primary metric moves one of its inputs.
13. **Goals are outcomes** you could check at the end; there are no more than 5.
14. **Non-goals include a "not optimising for" tradeoff** as well as deferred items.
15. **Prioritisation method is named**, scores are shown for contested items, and every override is logged with a reason.
16. **Items with confidence below 50% are framed as experiments.**
17. **The prototype next step targets the riskiest assumption.**

## Scope

18. **In scope, Deferred and Out of scope** all exist.
19. **Deferred items have a trigger**: what would bring them in.
20. **The out-of-scope list does positioning work**: it rules out something a reasonable stakeholder might ask for.

## Requirements

21. **Every requirement has an ID and a priority.**
22. **Every P0 has a testable acceptance criterion.** Banned words: intuitive, seamless, fast, robust, easy, user-friendly, unless a threshold follows.
23. **Requirements are verbs, features are nouns**, and the two aren't mixed up.
24. **Non-functional requirements have thresholds**: latency, accessibility level, uptime, privacy.
25. **Edge and failure states are covered** for each P0: empty, error, offline, permission denied, partial data.

## Success

26. **One primary metric** that moves if and only if the user problem is solved.
27. **Baselines and floors** exist, or "measure in week 1" is stated.
28. **At least one guardrail metric** protects against the obvious way to game the primary metric.
29. **Instrumentation gaps are listed.**

## Delivery

30. **Release gates are pass/fail checks.**
31. **The first vertical slice is defined**, and it is thin and end to end.
32. **Dependencies and third-party terms are listed**: APIs, licences, platform rules, costs.

## Governance

33. **Every open question has an owner** and a needed-by date or milestone.
34. **The decision log records the tradeoff** accepted for each decision.
35. **Version, date, status and owner** are at the top; revisions carry a changelog.

## Readability

36. **A smart outsider can follow it.** Internal terms are defined at first use.
37. **Nothing is filler.** Every section changes what gets built or how it gets judged.

## AI features (only when the product uses a model)

38. **Failure modes are named**, along with what the user sees when the model is wrong.
39. **An eval plan exists**: test set, graders (code, model, human), and the pass threshold for each release gate.
40. **The human-in-the-loop point is explicit**: which actions need approval and which are automatic.
41. **Cost per task is estimated** and has a ceiling.
