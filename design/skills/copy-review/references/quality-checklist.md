# Copy review quality checklist

Score each item **pass / weak / fail** with a one-line reason. Run it before handing over, and again after applying fixes.

## Context

1. **The product, the user and their state are named** at the top, and the tone of the rewrites matches that state.
2. **The source of truth is named** (PRD, spec, style guide), or the review says there wasn't one.

## Inventory

3. **Every screen in scope was covered**, and the review says which screens or states it couldn't see.
4. **Generated strings are in the inventory**: text written by script, plurals, counts and formatted dates.
5. **Event strings are in the inventory**: errors, toasts, banners, dialogs, empty, loading and offline states.
6. **Hidden strings are in the inventory**: page titles, accessible names, `alt` text, and controls whose only text is a letter or an icon.
7. **Missing strings are listed**: states that say nothing when the user needs to know something.
8. **Every string is quoted exactly**, and every one is either linked to a finding or marked OK.

## Glossary

9. **Every concept with more than one name is in the glossary**, with one chosen term and the words to retire.
10. **Chosen terms are the user's words**, not internal, spec or code names.
11. **No rewrite uses a retired term**, including toasts, errors and accessible names.

## Findings

12. **Every finding has an exact before, a complete after and a reason.** No "make this clearer".
13. **Every reason names the user's cost**, not just the rule.
14. **Severity follows the scale**, and every Blocker either misleads, causes a wrong action, or hides something that matters.
15. **One finding per problem**: no duplicates for the same string, and repeated problems are grouped.
16. **Rewrites that depend on unconfirmed behaviour are marked as guesses**, with what to confirm.
17. **No taste-only findings** above Polish.

## House rules in the rewrites

18. **No eyebrow text** survives, and no rewrite adds one.
19. **No meta explanation** survives, and no rewrite adds one. Anything that truly needs explaining is a tooltip or hint.
20. **Headings are nouns, buttons are specific verbs**, and there are no decorative counters.
21. **Sentence case** in every rewrite, including buttons and headings.
22. **Errors say what happened and what to do next**, one per problem, with no blame, codes, "invalid", "please" or "sorry".
23. **Empty states say how to fill them** and offer the action.
24. **Dates and numbers are in human format**, with plurals handled.
25. **Every rewrite is true** to what the product does.

## Scope and output

26. **UX and accessibility problems are one line each under Out of scope**, not written up as copy findings.
27. **The summary comes first**: the biggest problem, counts by severity, what to fix first.
28. **The apply list has one row per string change**, ordered by severity, with exact before and after.
29. **No content was sent outside the session**, and no personal data from screenshots or seed data is repeated.
30. **After applying**, the changed screens were inventoried again and no new string breaks a rule.
