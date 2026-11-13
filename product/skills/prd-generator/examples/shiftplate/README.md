# Showcase: Shiftplate

Fictional product, real run. A made-up founder takes the quiz for Shiftplate, a meal-planning app for nurses on rotating 12-hour shifts. The skill then writes the PRD and the prototype prompt.

1. [Quiz transcript](1-quiz-transcript.md): five questions, with graded answers, pushback and a scorecard
2. [PRD](2-PRD.md): Lite PRD built from the quiz answers
3. [Prototype prompt](3-PROTOTYPE-PROMPT.md): ready to paste into a coding agent

Moments worth looking at:

- **Q1:** "costs them money and they feel bad" gets a *needs work* verdict, and the follow-up asks for a number and a source.
- **Q2:** the founder calls it problem fit, but the skill points out that the test checks solution fit. It also catches that the value claim doesn't fix the cost named in Q1.
- **Q5:** the skill adds a P0 the founder missed (manual rota entry), and logs why each override was made.
- **PRD:** "Why now" is marked *Evidence needed* because the inputs didn't support one, and the 4-day use-by default is flagged for checking against food-safety guidance.

Next: [the research pass](../../../deep-research/examples/shiftplate/) that fills this PRD's Evidence needed lines.
