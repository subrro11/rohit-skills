# Showcase: Shiftplate test plan

A full moderated test plan for a fictional product. Shiftplate is the meal-planning app for nurses on rotating 12-hour shifts from the [PRD Generator showcase](../../../prd-generator/examples/shiftplate/). Its PRD ends with gate G0: test the riskiest assumption with 5 nurses. This plan sets that test up for the v0.2 prototype, before any session has run.

[Read the plan](TEST-PLAN.md)

Moments worth looking at:

- **Timings come from the PRD, with their IDs.** The 20-second rota entry (R1), 2-minute fridge log (R2, G0) and under-a-minute re-plan (R3, G0) are copied, not invented. Every threshold the plan adds is marked *proposed*.
- **Timed tasks are silent.** Thinking aloud slows people down, so T1 to T3 are done quietly and talked through afterwards. T4 and T5 are think-aloud.
- **The scenario avoids the button's name.** The app says "Log prep", so the T2 scenario asks people to get the dishes into the app.
- **One fridge card serves two tasks.** The pasta bake was prepped 5 days ago, so T5 has the same answer under the PRD's 4-day use-by default and the 3-day default from the [research pass](../../../deep-research/examples/shiftplate/).
- **The plan asks the build for what it needs.** Testing the check-in without moving the date needs a test flag, so the plan lists it rather than changing the date mid-session and breaking T5.
- **No results.** Pass, iterate and stop are set before testing, and the grid is empty.

Previous: [the research pass](../../../deep-research/examples/shiftplate/).
