# Experiment quality checklist

Score each item **pass / weak / fail** with a one-line reason. Run it before handing over.

## Decision and hypothesis

1. **The decision and the assumption are named** at the top, and the assumption is the riskiest one, not the easiest to test.
2. **The hypothesis has all six parts**: change, segment, metric, N, time and mechanism.
3. **The null result is written**, with what you'd do if it happens.
4. **N is the smallest effect worth acting on**, with a reason, not the effect you hope for.

## Method

5. **The method fits the question**: demand, value or behaviour change.
6. **The method fits the sample.** If an A/B test was rejected, the maths showing why is in the plan.
7. **One line says why the method beats the next-best one.**
8. **Deception is handled**: fake doors and Wizard of Oz tests say how participants are told.

## Unit and metrics

9. **The unit of randomisation is named** and matches where contamination happens.
10. **The analysis is at the unit of randomisation**, or clustering is corrected with the design effect.
11. **Exactly one primary metric**, with numerator, denominator and window.
12. **The primary metric can't be gamed by the change itself** (defaults, auto-fill, nagging).
13. **Two to four guardrails**, each with a threshold that blocks shipping.
14. **Every baseline says where it came from**, and guesses are labelled *assumed*.

## Sample size and duration

15. **The formula and every input are shown**: α, power, baseline, MDE (absolute or relative, stated), and any ICC or variance assumed.
16. **The numbers were run**, with code or a named calculator, not estimated by eye.
17. **Duration covers whole weeks**, at least one, using real arrival rates.
18. **The MDE the sample can reach is stated**, and compared with plausible effects.
19. **Sensitivity is shown** for each assumed input that drives the answer.

## Decision rule

20. **Written before launch**, with ship, iterate and kill thresholds.
21. **Guardrails can veto a ship.**
22. **The analysis method, stopping rule and dropout handling are stated.**
23. **The rule feeds an existing product gate** (a PRD's pass/iterate/stop, a release gate).

## Validity and instrumentation

24. **Every applicable threat has a block or a detection**: at least peeking, sample ratio, novelty, contamination and seasonality; carryover and period for crossovers.
25. **Instrumentation lists the denominator event** and puts the version on every event.
26. **A dry run or A/A check** is planned if the pipeline is new.

## Output

27. **The readout section is empty**, or holds only real results. Nothing imagined.
28. **The chat reply** gives the method, the reachable MDE, the decision rule and the file path.
29. **Plain words.** A decision-maker who has never run a test can follow the sample-size section.
