# Showcase: Shiftplate prototype test

A fictional usability test, synthesised. Shiftplate is the meal-planning app for nurses on rotating 12-hour shifts from the [PRD Generator showcase](../../../prd-generator/examples/shiftplate/). Its PRD sets a prototype gate (G0) and a pass, iterate or stop rule. Five nurses tried v0.2; this run turns the moderator's notes into a readout.

- [NOTES.md](NOTES.md): the raw input, one block of moderator notes per participant
- [SYNTHESIS.md](SYNTHESIS.md): the output, in test readout mode

Moments worth looking at:

- **Half a gate.** The re-plan meets its G0 bar (4 of 5 under a minute); logging misses it (3 of 5 within 2 minutes, where 4 are needed), even though its median of 1:52 meets the PRD's own target. The readout reports both.
- **Said beats did, for once.** Everyone completed the check-in, but three said they wouldn't after a real shift. The sessions ran on days off, so the readout weights the statements and says why.
- **The top opportunity isn't the strongest theme.** Logging has the stronger evidence, but check-in carries the waste metric. A one-tap "all eaten" default could hide the binned food the pilot exists to count, so it goes forward as an assumption to test, not a fix.
- **Outliers are kept, not acted on.** A request for partner sharing is counted towards the PRD's trigger. A request for calories is recorded against the product's "never a diet app" line.
- **Every claim traces back.** 40 observations, each with a participant ID and, where there was one, the exact words from the notes.
