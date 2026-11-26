# Experiment: one-tap check-in

> Fictional product, real method. Shiftplate is the made-up product from the [PRD Generator showcase](../../../prd-generator/examples/shiftplate/). Every baseline here is *assumed*. The numbers in the sample-size section were computed by [`sample-size.py`](sample-size.py); rerun it to check them. Results are filled in only after the experiment runs.

**Decision:** Should Shiftplate's 20-nurse pilot use a one-tap end-of-shift check-in, and can the PRD's waste metric be trusted at gate G2 if it does?
**Assumption:** A one-tap check-in raises completion without making the waste data wrong.
Numbers are *assumed* unless a source or measurement is named. Results are filled in only after the experiment runs.

## Why this experiment

A usability test with 5 nurses found the re-plan is the hook and the end-of-shift check-in is the weakest link: 3 of 5 said they wouldn't do it after a real 12-hour shift, and one said she would if it were one tap (*user-supplied*). The PRD measures food waste through check-ins (R5, R6), so low completion breaks its primary metric. The pilot is the only chance to fix that before G2.

## Hypothesis

If we replace the per-meal check-in (R5: eaten / binned / still in fridge, with an "all eaten" shortcut) with a one-tap prompt, **"All eaten?"** with a quiet **"Something binned"** option, for pilot nurses, then check-ins completed per worked shift rise by at least **20 points** within 4 weeks, because after a 12-hour shift any prompt that needs more than one decision gets skipped.

**Null result:** if completion rises by less than 5 points, effort isn't the reason nurses skip the check-in (timing or relevance might be), and the waste metric needs a source that doesn't depend on check-ins.

**Why 20 points:** at the assumed 40% baseline, fewer than half of shifts produce waste data. The PRD's week-1 versus week-4 comparison needs most shifts covered, so 60% is the floor worth acting on.

**One design rule:** "All eaten" is the highlighted button, but it is never filled in automatically. A check-in counts only when the nurse taps. Otherwise completion would rise by itself and the waste data would quietly say nothing was binned.

## Method

**Crossover with alternating weeks.** Every nurse uses both versions. Half are drawn at random to sequence ABAB (current, one-tap, current, one-tap), half to BABA. Each nurse is compared with herself.

- **Why not an A/B test by nurse:** 10 nurses per group can detect only a 36-point rise at 80% power (ICC 0.3, *assumed*). Simulated power for a true 20-point rise is 32%. Maths below.
- **Why not randomise each shift:** flipping the prompt every shift would confuse tired nurses and blur the two habits together. A week is long enough to settle into each version.
- **Bonus:** weeks 1 and 4 each have half the nurses on each version, so the PRD's week-1 versus week-4 waste comparison isn't skewed by the experiment.

## Unit, metrics and baselines

**Unit of randomisation:** the nurse (her sequence). **Unit of analysis:** the nurse's difference in completion between versions.

| Metric | Definition | Baseline | Threshold |
|---|---|---|---|
| **Primary:** check-in completion | Worked shifts with a check-in tapped within 24 h of shift end ÷ worked shifts (from the R1 rota) | 40% on the current version (*assumed*: 2 of 5 usability-test nurses said they'd do it) | +20 points (MDE) |
| **Guardrail:** binned capture | Binned portions found by the audit that the check-in also recorded as binned ÷ binned portions found by the audit | Unknown; measured in week 1 | One-tap ≥ 80%, and no more than 10 points below current |
| Guardrail: re-plans | Re-plans per rota change (PRD PMF signal) | Measured in pilot | Not lower in one-tap weeks by more than 10 points |
| Secondary | Time from prompt to tap; share of one-tap check-ins that used "Something binned" | None | Explanation only |

**The audit (weeks 1 and 4):** each nurse photographs her fridge once a day, and has a 5-minute call at the end of the week walking through every logged portion that left the fridge: eaten, binned or given away. That walk-through is the reference for "binned". It relies on recall, so it's a check, not ground truth.

## Sample size and duration

**Inputs (all *assumed*):** α = 0.05 two-sided, power 80%, baseline 40%, MDE +20 points, 20 nurses, 3 twelve-hour shifts a week for 4 weeks, so 12 worked shifts per nurse and 240 in total.

**1. If shifts were independent:** two-proportion formula, 40% → 60%:

```
n = [1.960·√(2·0.5·0.5) + 0.842·√(0.24 + 0.24)]² / 0.20² = 96.9 → 97 shifts per group
```

The pilot has 120 shifts per group, so it looks big enough. It isn't.

**2. Why an A/B test by nurse fails:** shifts from the same nurse are correlated. Some nurses check in every time, some never do. Correcting with the design effect, 1 + (m − 1) · ICC with m = 12:

| ICC (*assumed*) | Design effect | 120 shifts behave like | Reachable MDE | Nurses needed per group for +20 |
|---|---|---|---|---|
| 0.1 | 2.10 | 57 | 26 points | 17 |
| 0.2 | 3.20 | 38 | 32 points | 26 |
| 0.3 | 4.30 | 28 | 36 points | 35 |
| 0.5 | 6.50 | 19 | 43 points | 53 |

At any plausible ICC, the pilot needs 34 to 106 nurses for a parallel A/B test. It has 20. Simulated at ICC 0.3, a true 20-point rise is detected 32% of the time.

**3. The crossover:** each nurse's difference between versions is compared with zero (paired t-test, 19 degrees of freedom). With 6 shifts per version and τ, the spread of the true effect between nurses:

```
σd = √(0.24/6 + 0.24/6 + τ²)
MDE = (2.093 + 0.861) · σd / √20
```

| Nurses | τ = 0 | τ = 0.10 | τ = 0.15 |
|---|---|---|---|
| 20 | 18.7 points | 19.8 points | 21.1 points |
| 16 (4 drop out) | 21.2 points | 22.5 points | 24.0 points |

Simulated (ICC 0.3, τ 0.10, 3,000 runs): a true +20 is detected 88% of the time with 20 nurses and 79% with 16. A true +15 is detected 67% of the time. With no effect, 6% of runs come out significant, close to the 5% expected.

**Honest reading:** the crossover can detect the effect worth acting on, about 20 points, and not much smaller. A 10-point rise would probably be missed. That's acceptable, because a 10-point rise wouldn't fix the waste metric anyway.

**Duration:** 4 weeks (the pilot), 2 weeks per version, every weekday covered in both versions.

**Guardrail precision:** if nurses bin about 1 portion a week each (*assumed*), the two audit weeks give about 40 binned portions per version. A measured capture of 80% then has a 95% interval of about ±12 points. The guardrail is a threshold rule, not a significance test, and the readout reports the interval.

## Decision rule

Written before launch. Not edited afterwards.

**Analysis:** per-nurse completion in one-tap weeks minus current weeks; mean difference with a 95% confidence interval from a paired t-test. Every nurse with at least one worked shift in each version is included. Dropouts are reported by sequence. A model with nurse, period and version is run as a check, not as the decision.

| Outcome | Primary | Guardrails | Action |
|---|---|---|---|
| **Ship** | Difference ≥ +15 points and the interval's lower end above 0 | Capture ≥ 80% and within 10 points of current; re-plans hold | One-tap becomes the only check-in for the rest of the pilot and for v1 |
| **Iterate** | Between +5 and +15, or the interval crosses 0 | Capture 70–80% | Keep both versions; change the prompt (for example, ask "Something binned?" first when a portion is near its use-by day) and rerun a 2-week crossover |
| **Kill** | Below +5 points | Capture below 70%, or more than 10 points below current | Keep the current check-in; find a waste source that doesn't rely on check-ins (the re-plan confirmation in R6 alone, or a weekly fridge photo) |

**Link to the PRD's gates:** the PRD's waste goal (binned share halves from week 1 to week 4) is read at G2 only if check-ins cover at least 60% of worked shifts in weeks 1 and 4 and the capture guardrail holds. If not, the waste goal is recorded as "not measurable", which counts as **iterate** for that goal, never as pass. The PMF signal (10 of 20 re-plan through two rota changes for pass, 5–9 iterate, under 5 stop) comes from re-plan events, so this experiment doesn't change it.

## Threats to validity

| Threat | How the design handles it |
|---|---|
| Peeking | Fixed 4 weeks; nobody reads the comparison before the end of week 4. Weekly checks look only at whether events are firing |
| Sample ratio | Nurses are split 10 and 10 by a draw. Shifts come from rotas, so check worked shifts per version: a split outside about 44–56% of 240 shifts is a warning, and a chi-square p below 0.01 stops the readout until explained |
| Novelty | One-tap could win just for being new. Compare the effect in its first and second weeks |
| Carryover | The one-tap habit could leak into current-version weeks, which shrinks the measured effect. Compare current-version completion in week 1 (BABA nurses haven't seen one-tap) with week 3 |
| Period effect | Balanced sequences; period is in the check model. Rota flips and fatigue both drift over 4 weeks |
| Contamination | All nurses work at one hospital and will talk. Both groups use both versions, so talk matters less than in a parallel test |
| Metric gaming | "All eaten" is highlighted. No auto-fill, and the capture guardrail checks whether binned food is going unreported |
| Hawthorne | The audit weeks (1 and 4) may raise completion in both versions. Compare audit weeks with weeks 2 and 3 |
| External validity | One hospital, volunteer nurses who already meal prep. The result applies to them; PRD gate G1 wanted more than one hospital, so say this at G2 |

## Instrumentation

| Event | Properties | Why |
|---|---|---|
| `shift_worked` | nurse, shift date, day or night, source (rota) | The denominator |
| `checkin_prompt_shown` | nurse, shift, version, time shown | Exposure, and checks the prompt fired in both versions |
| `checkin_completed` | nurse, shift, version, taps, seconds from prompt, answer (all eaten / something binned / per meal) | The numerator |
| `portion_marked` | portion, mark, source (check-in or re-plan confirmation) | Waste data, and which path recorded it |
| `replan_completed` | nurse, trigger (rota change or not) | The re-plan guardrail |
| `sequence_assigned` | nurse, ABAB or BABA, date | Sample ratio check |
| Audit sheet | nurse, week, portion, audit outcome | Capture guardrail |

Before week 1: a dry run on two test phones, one per sequence, to confirm every event fires with the version attached.

## Timeline and owners

| When | What | Owner |
|---|---|---|
| Week 0 | Build the one-tap prompt; draw sequences; dry run | Founder |
| Week 1 | Pilot starts; audit week | Founder |
| Weeks 2–3 | Event checks only, no comparisons | Founder |
| Week 4 | Audit week; pilot data closes | Founder |
| Week 5 | Readout against the rule; decision recorded at G2 | Founder |

## Readout

To fill in after week 4, using the readout template. Empty until then.

| Check | Result |
|---|---|
| Sample ratio (shifts per version) | |
| Dropouts by sequence | |
| Completion: current version | |
| Completion: one-tap | |
| Difference (95% interval) | |
| Effect in first vs second week of one-tap | |
| Capture: current / one-tap (95% interval) | |
| Re-plans per rota change by version | |
| Row of the rule it lands in | |
| Decision | |

## Sources

- Usability test findings and PRD figures: *user-supplied*, from the [Shiftplate PRD](../../../prd-generator/examples/shiftplate/2-PRD.md).
- Sample-size method, design effect and crossover logic: see [`references/sample-size-and-power.md`](../../references/sample-size-and-power.md).
