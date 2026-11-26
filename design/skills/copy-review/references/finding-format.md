# Severity scale and finding format

## Severity

Rank by what the words cost the user, not by how many rules they break.

| Severity | What it means | Examples |
|---|---|---|
| **Blocker** | The copy misleads, causes a wrong action, or hides something the user needs to know. Includes missing messages for things that matter (safety, money, lost data). | A banner that says a plan needs regenerating when it has already changed. Expired food dropped from a plan with no message. A field that defaults silently. |
| **Major** | The copy confuses or slows the main task, or leaves the user unable to recover without guessing. | One error message for three different problems. Jargon on the main button. Single-letter controls with no accessible name. Dates in database format. |
| **Minor** | Inconsistent, off-tone or longer than it needs to be, but the user still gets through. | Three words for one concept. Title Case. "Success!". A meta explanation under a heading. |
| **Polish** | Small craft fixes. | "+" and "&" mixed in names. Page title says "prototype". |

Rules:

- **A missing string is ranked like a wrong one.** Silence where the user needs to know something is usually a Blocker.
- **Frequency raises severity.** A Minor problem on a string seen ten times a day can be Major.
- **Main path raises severity.** The same problem is worse on the main button than in settings.
- **When in doubt, rank lower** and say why in the reason.

## Inventory format

Every string, screen by screen, in reading order.

| ID | Screen | Element | String (exact) | Finding |
|---|---|---|---|---|
| S1 | Home | Eyebrow | `Step 1 · Rota` | C4 |
| S2 | Home | Heading | `Welcome to Shiftplate!` | C9 |
| S14 | Plan | Missing | *(nothing said when a dish is past its use-by date)* | C2 |

- Quote strings exactly, in backticks, including punctuation and case.
- Mark generated strings with their pattern: `{n} servings stored`.
- Mark missing strings in italics with what should be there.
- Strings with no problem get "OK" in the Finding column, so the reader can see they were checked.

## Finding format

```markdown
### C1 · Blocker · <short name of the problem>

**Where:** <screen> › <element> (S5, S12)
**Before:** `<exact string>`
**After:** `<rewrite, ready to paste>`
**Why:** <what it costs the user, in one or two sentences>
**Rule:** <rule name from copy-rules.md>
```

- **One finding per problem.** A string that breaks three rules gets one finding and one rewrite. A rule broken in many places with the same fix gets one finding listing every place.
- **Before is exact.** **After is complete**: the actual words, at the length the space allows. Deletions are written `(delete)`.
- **Why names the user's cost.** "A nurse can't tell which field to fix" beats "unclear error".
- **Guesses are marked.** If the rewrite depends on behaviour you couldn't confirm, add *guess: confirm with the team* and say what to confirm.
- **Alternatives only when a product decision decides it**, written as "Or, if <decision>: `<rewrite>`".

## Apply list format

After the findings, a flat list someone can work through or an agent can apply:

```markdown
| # | Finding | File | Before | After |
|---|---|---|---|---|
| 1 | C1 | index.html | `Rota mutation detected. Regenerate plan?` | `Shifts changed. Meal plan updated.` |
```

Order by severity. One row per string change, so one finding can have several rows.
