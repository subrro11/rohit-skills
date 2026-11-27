# Example: Shiftplate

Shiftplate is a made-up meal-planning app for nurses on rotating 12-hour shifts. Nurses check in after each shift to say what they ate and what they binned, and that's the only source of waste data. In early tests most said they wouldn't bother after a real shift.

So the question for the 20-nurse pilot: does a one-tap check-in get more of them to do it, without hiding the food they bin?

[Read the plan](EXPERIMENT.md) · [Run the maths](sample-size.py)

What's worth a look:

- 240 shifts looks like plenty next to the 97 per group a basic formula asks for. But shifts from the same nurse move together, and once you correct for that, an A/B test could only spot a 36-point jump.
- A crossover fixes it. Every nurse uses both versions in alternating weeks and is compared with herself, which gets the detectable change down to about 20 points.
- "All eaten" is the highlighted button but never filled in for you, and a fridge-photo audit checks that binned food still gets logged.
- The readout is empty. Nothing in it is invented.
