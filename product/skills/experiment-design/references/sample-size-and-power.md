# Sample size and power

## In plain words

An experiment compares two noisy numbers. Even if the change does nothing, the groups will differ a little by chance. The sample size is how much data you need so that a real effect of the size you care about stands out from that noise most of the time.

- **Significance level (α)**: how often you're willing to call a winner when the change actually does nothing. 5% is the usual default.
- **Power (1 − β)**: how often you'll detect a real effect of the size you care about. 80% is the usual default, which means one in five real effects of that size will be missed.
- **Minimum detectable effect (MDE)**: the smallest effect the test is built to detect at that power. Smaller effects can still be real; the test just isn't sized to see them reliably. Pick the MDE from the decision: the smallest change that would make you act. Not the change you hope for.
- **Baseline**: the current value of the metric. For a rate, the noise depends on it, so the same MDE needs different samples at different baselines.

Say the MDE as **absolute** (40% → 50% is +10 points) or **relative** (+10 points on 40% is +25%) and never leave it ambiguous. Calculators accept both; a mix-up changes the sample several-fold.

## The formula for two proportions

For a rate metric (conversion, completion, retention), equal groups, two-sided test:

```
n per group = [ z(1−α/2) · √(2·p̄·(1−p̄))  +  z(1−β) · √(p1·(1−p1) + p2·(1−p2)) ]²  /  (p2 − p1)²
```

- p1 = baseline rate, p2 = baseline + MDE, p̄ = (p1 + p2) / 2
- z(1−α/2) = 1.960 for α = 0.05 two-sided; z(1−β) = 0.842 for 80% power

A quick cross-check is the rule of thumb **n ≈ 16 · σ² / δ²** per group, where σ² = p(1 − p) for a rate and δ is the absolute MDE. The 16 is roughly 2 × (1.96 + 0.84)². For a 40% baseline and +20 points: 16 × 0.24 / 0.04 = 96, against 97 from the full formula.

**Sample size scales with 1 / MDE².** Halve the MDE and you need about four times the sample. This is why "let's detect a 1-point lift" is rarely affordable.

### Worked calculation

Baseline 40%, MDE +20 points (to 60%), α = 0.05 two-sided, power 80%:

- p̄ = 0.50, so 1.960 × √(2 × 0.25) = 1.386
- 0.842 × √(0.24 + 0.24) = 0.583
- (1.386 + 0.583)² = 3.877, divided by 0.20² = 0.04, gives **96.9, so 97 per group**

Checked by simulation: 20,000 simulated tests with 97 per group at 40% vs 60% rejected the null 80.8% of the time.

## Lookup table

Sample **per group**, α = 0.05 two-sided, 80% power, absolute MDE, pooled formula above, rounded up. Computed in Python; spot-checked by simulation (the 20% → 25% cell gave 79.3% power over 4,000 simulated tests).

| Baseline | +1 point | +2 points | +5 points | +10 points | +20 points |
|---|---|---|---|---|---|
| 5% | 8,158 | 2,213 | 435 | 141 | 49 |
| 10% | 14,751 | 3,841 | 686 | 199 | 62 |
| 20% | 25,583 | 6,510 | 1,094 | 294 | 82 |
| 40% | 37,827 | 9,493 | 1,534 | 388 | 97 |
| 50% | 39,240 | 9,806 | 1,565 | 388 | 93 |

Different calculators give slightly different answers depending on whether they pool the variance, use one- or two-sided tests, or default to other power levels. Check the settings before comparing.

## From sample to duration

1. Count the eligible units that arrive per week (users who reach the screen, not all users).
2. Duration = sample per group × number of groups ÷ weekly arrivals.
3. Round up to whole weeks so every day of the week appears in both groups. Run at least one full week even if the sample arrives sooner.
4. If the duration is longer than the decision can wait, either accept a larger MDE (and say so) or change the method.

## When the unit of analysis isn't the unit of randomisation

If you randomise people but count events (shifts, sessions, orders), events from the same person are correlated. Treating them as independent overstates the sample. Correct with the **design effect**:

```
design effect = 1 + (m − 1) · ICC
effective sample = number of events ÷ design effect
```

- m = average events per randomised unit
- ICC (intracluster correlation) = how much of the variation is between units rather than within them, from 0 (people are interchangeable) to 1 (each person always does the same thing)

Unequal cluster sizes make the design effect larger still. The ICC is rarely known for a new product: assume a range, label it *assumed*, and show the result for each value.

Example: 10 people per group, 12 events each, ICC 0.3 → design effect 4.3, so 120 events behave like about 28 independent ones.

## Small samples: within-subject designs

When there are too few people for parallel groups, give each person both versions in a random order (a crossover) and compare each person with themselves. Differences between people drop out, which is usually most of the noise.

For a paired comparison of per-person rates:

```
MDE ≈ (t(1−α/2, n−1) + t(1−β, n−1)) · σd / √n
σd² ≈ p1(1−p1)/k + p2(1−p2)/k + τ²
```

- n = people, k = events per person per condition
- σd = standard deviation of each person's difference between versions
- τ = how much the true effect varies between people (*assumed* unless measured)
- for n = 20, t(0.975, 19) = 2.093 and t(0.80, 19) = 0.861

The cost: carryover (one version's effect leaks into the next period) and period effects (everything drifts over time). Balance the order across people, use periods long enough for the effect to settle, and check both in the readout.

## When none of it works

If even a within-subject design can't detect an effect you'd act on, don't run a test that will produce a coin flip. Instead:

- Run it as a **pilot** and report the effect with its interval, labelled as an estimate, not a verdict.
- Use **qualitative** methods (interviews, diary studies, usability sessions) to learn *why*, and save the quantitative test for when there's more traffic.
- **Raise the MDE honestly**: if only a large effect would be worth acting on, a small test that can detect only large effects is fine. Say that's the trade.

## Sources

- Evan Miller, "Sample Size Calculator" (evanmiller.org/ab-testing/sample-size.html). Defines the MDE as the smallest effect that will be detected (1−β)% of the time.
- Evan Miller, "How Not To Run an A/B Test", 2010 (evanmiller.org/how-not-to-run-an-ab-test.html). Source of the 16σ²/δ² rule of thumb.
- Qian Zhang, "Sample size calculations unpacked: Origins, hidden assumptions, and trade-offs", Optimizely, 12 December 2025 (optimizely.com/field-notes/articles/sample-size-calculations-for-experiments). Sample size scales with variance and with 1 / MDE².
- "Design effect", Wikipedia (en.wikipedia.org/wiki/Design_effect). Kish's design effect for clusters of equal size, 1 + (n − 1)ρ.
- "Crossover study", Wikipedia (en.wikipedia.org/wiki/Crossover_study). Each participant serves as their own control; carryover and order effects are the main risks.
