# Showcase: Shiftplate experiment

A full experiment design for a fictional product. Shiftplate is the meal-planning app for nurses on rotating 12-hour shifts from the [PRD Generator showcase](../../../prd-generator/examples/shiftplate/). A usability test found the end-of-shift check-in is the weakest link, and the PRD's waste metric depends on it. This run designs the test of a one-tap check-in inside the 20-nurse pilot.

[Read the plan](EXPERIMENT.md) · [Run the maths](sample-size.py)

Moments worth looking at:

- **The A/B test is ruled out with numbers.** 240 shifts looks like plenty against the 97 per group a naive formula asks for. Correct for shifts coming from the same nurses and the pilot can only detect a 36-point rise.
- **A crossover takes its place.** Each nurse uses both versions in alternating weeks, which brings the detectable rise down to about 20 points, the size worth acting on.
- **The default can't game the metric.** "All eaten" is highlighted but never filled in automatically, and a fridge-photo audit checks that binned food still gets reported.
- **The rule lands in the PRD.** If check-ins don't cover enough shifts, the waste goal is recorded as "not measurable" at the pilot gate, not as a pass.
- **The readout is empty.** Every baseline is labelled *assumed*, and no result is invented.
