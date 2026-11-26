# Severity and finding format

## Severity

Rate on four levels. The scale follows Nielsen's severity ratings (see `sources.md`), with level 0 dropped: if it isn't a problem, don't write it up.

| Level | Name | Means | Rule of thumb |
|---|---|---|---|
| **4** | Blocker | Many users can't finish a top task, or they finish it wrongly without knowing (bad data, unsafe outcome) | Fix before anyone tests or ships it |
| **3** | Major | Users finish, but slowly, with errors, or only after a guess; or it happens on every visit | Fix before testing if it touches a task with a success bar |
| **2** | Minor | Some users stumble once and recover | Fix next |
| **1** | Cosmetic | Polish: alignment, uneven spacing, small inconsistencies | Fix when nearby |

Decide with three questions:

1. **How often?** How many users hit it, and on how many visits?
2. **How hard to get past?** A pause, a wrong turn, a dead end, or a wrong result they never notice?
3. **Does it repeat?** A one-time hurdle, or every single time?

Then adjust for the context the brief names. If the user is exhausted and one-handed, a small target on the main task is major, not minor. If a task has a success bar (≤ 2 min), anything that can push a typical user over it is major at least.

Silent wrong results outrank loud errors. A user who sees an error can recover; a user who never learns their food was left out of the plan can't.

## Finding format

One finding per problem, numbered in severity order:

```
### F3 · Major · Change rota and re-plan

**Heuristic:** H6 Recognition rather than recall; mobile target size
**Evidence:** Day chips are 48 × 28 px with 4 px gaps (measured at 390 px). Labels are D / N / Off with no dates and no legend. Screenshot: screens/1-home.png
**Why it matters:** Users must count chips to find "Thursday", and a mis-tap cycles the wrong day.
**Fix:** Make chips at least 44 px tall, show the weekday and date on each, mark today, and add a one-line legend (Day · Night · Off).
**Size:** S
```

Fields:

- **Number, severity, task.** The task from step 1, or "all tasks".
- **Heuristic.** One or two from `heuristics.md`, by code and name, or a state from `states-checklist.md`, or an accessibility criterion.
- **Evidence.** What's on screen: element, measurement, behaviour, screenshot path. Mark anything you couldn't observe as *inference*.
- **Why it matters.** The consequence for this user on this task, in one line.
- **Fix.** A concrete change someone could build. If there are two good options, give both and say which you'd pick.
- **Size.** S (under a day), M (a few days), L (a redesign of the flow). Mark it *estimate*.

## Task walk table

Before the findings, one row per step of each task:

| Task | Step | What the user does | What happens | Finding |
|---|---|---|---|---|
| Log fridge | 1 | Taps "Manage Inventory" | Log screen opens | — |
| Log fridge | 2 | Types quantity | Full keyboard opens | F7 |

## Prioritised fix list

Group by when to fix, not by heuristic:

- **Fix before testing:** every blocker, and every major on a task with a success bar.
- **Fix next:** remaining majors and minors that are cheap.
- **Later:** cosmetic, and anything that needs research first.

Each line: finding number, the fix in a few words, size.
