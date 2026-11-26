# Threats to validity

For every threat that applies, write how the design blocks it, or how the readout will detect it. "Not applicable" needs a reason.

| Threat | What goes wrong | Block it | Detect it |
|---|---|---|---|
| **Peeking** | Checking a fixed-sample test repeatedly and stopping when it looks good inflates false positives | Fix the sample and the end date before launch, or use a sequential or Bayesian method built for interim looks | The readout states whether anyone stopped early, and why |
| **Sample ratio mismatch** | The groups end up a different size from the split you configured, so they're no longer comparable | Randomise in one place, log assignment before anything can filter users out | Chi-square test of observed vs configured counts before reading any result. If it fails, stop and find the cause |
| **Novelty** | People try something because it's new; the effect fades | Run long enough for the effect to settle; at least a full week | Plot the effect by week. A shrinking effect is novelty |
| **Primacy (change aversion)** | People resist a change at first; the effect grows later | Same as novelty | A growing effect by week |
| **Contamination** | People in one group see or hear about the other version | Randomise at the level where people talk (team, site) | Ask in exit interviews; compare effect in isolated vs connected units |
| **Seasonality and calendar** | Weekdays, holidays, pay cycles, rotas drive the metric | Run whole weeks; run groups at the same time, never one after the other | Check the effect by day of week and by period |
| **Clustering** | Events from the same person or group are treated as independent, so the result looks surer than it is | Analyse at the unit of randomisation, or apply the design effect | Report the number of units, not just events |
| **Carryover** (crossover designs) | One version's effect lingers into the next period | Periods long enough to settle; consider a washout; balance the order | Compare the effect in first vs later periods |
| **Period effect** (crossover designs) | Everything drifts over time (fatigue, learning) | Balance the order: half start on each version | Include period in the analysis |
| **Metric gaming** | The change inflates the metric without the behaviour (a default fills itself in) | Count only active actions; add a data-quality guardrail | Compare against an independent audit |
| **Hawthorne effect** | Being watched changes behaviour | Keep measurement the same in both groups | Note audit periods and compare with the rest |
| **Dropout and missing data** | People who leave differ from people who stay | Plan how dropouts count before launch (intention to treat) | Report dropout by group and by version |
| **Multiple comparisons** | Many metrics or segments, so something "wins" by luck | One primary metric; segments named in advance | List every comparison made; treat unplanned ones as exploratory |
| **External validity** | It works here but won't elsewhere (one site, one season, keen volunteers) | Say who the result applies to | State it in the readout |

## Notes

- **Run at least one full week.** Effects vary day to day more than their intervals suggest, and weekdays differ from weekends.
- **Sample ratio mismatch is a stop sign, not a footnote.** The users who go missing are often the ones most affected by the change, so a skewed split can flip the result's sign.
- **Novelty and primacy are not the only reasons an effect changes over time.** External events matter too, so a trend by week is a reason to look, not a diagnosis.

## Sources

- Evan Miller, "How Not To Run an A/B Test", 2010 (evanmiller.org/how-not-to-run-an-ab-test.html). "Repeated significance testing always increases the rate of false positives."
- Microsoft Experimentation Platform, "Diagnosing Sample Ratio Mismatch in A/B Testing", 14 September 2020 (microsoft.com/en-us/research/articles/diagnosing-sample-ratio-mismatch-in-a-b-testing/). Defines SRM, recommends a chi-square test on counts before analysis, and groups causes by stage (assignment, execution, log processing, analysis).
- Microsoft Experimentation Platform, "External validity of online experiments: can we predict the future?", 20 November 2024 (microsoft.com/en-us/research/articles/external-validity-of-online-experiments-can-we-predict-the-future/). "At ExP we warn customers that they should usually run their experiments for at least a week."
- "Crossover study", Wikipedia (en.wikipedia.org/wiki/Crossover_study). Carryover and order effects.
