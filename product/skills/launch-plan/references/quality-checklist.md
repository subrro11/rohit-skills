# Launch plan quality checklist

Score each item **pass / weak / fail** with a one-line reason. Run it before handing over.

## Inputs

1. **What's launching and what isn't** are stated, matching the PRD's scope.
2. **The decision rule** is copied from the PRD (or proposed and marked so).
3. **Every PRD release gate** before this stage is listed with its status.
4. **Conflicts between inputs** are listed, with which one the plan follows.

## Tier and stages

5. **The tier comes from the higher of reach and risk**, with a one-line reason.
6. **Each stage names its cohort**, how people are chosen, how many, and how they get access.
7. **Each stage runs long enough** to see the core action repeat.
8. **Every flag** has a type, default, who can flip it, and a removal point.

## Gates and owners

9. **Every gate check is pass/fail** with a measure, a threshold and a source.
10. **Every gate has stop conditions** as well as go conditions.
11. **Owners are roles**, one owner and one decider per item, and no role is empty.

## Readiness and comms

12. **Readiness covers product, engineering, support, legal and privacy, data, docs**, each item with an owner and a due point.
13. **Support hears first**, and support hours cover when users use the product.
14. **Consent wording** covers what's kept, what's never collected, deletion, how to leave and how to get help.
15. **Pause, rollback and deletion messages** are written in advance.
16. **Partners who could be surprised** are listed with a decision on whether to tell them.

## Metrics and watch list

17. **Success metrics come from the PRD**, with their labels kept.
18. **The watch list** has health, use and harm signals, each with a threshold, a source, a frequency and an owner.
19. **Harm signals have a threshold of one.**
20. **Small cohorts are counted in people.**

## Rollback and review

21. **Every rollback trigger** has a response, a decider, a stand-in, a time to act, a named mechanism and a user message.
22. **The rollback mechanism is rehearsed** before outside users get access.
23. **The review has a date, a data cut-off and a decider**, and applies the decision rule as written.

## Output

24. **Dates are relative to launch day**, with one real date at the top.
25. **No invented results**, no personal data, no names.
26. **Any external fact** (store limits, review times) cites a page that was read, or says to check it.
