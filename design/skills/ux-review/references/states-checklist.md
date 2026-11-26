# States checklist

Most products are designed for the happy path with sample data. Users live in the other states. For each state below, decide whether the product can reach it, trigger it if you can, and record what the user sees.

| State | When it happens | What good looks like | Common failure |
|---|---|---|---|
| **First run** | A new user with no data | Says what this is for in one line and offers the first action | A blank screen, sample data that looks real, or a tour |
| **Empty** | A list or view with nothing in it | Says why it's empty and gives the action that fills it, right there | "No data." with no way forward |
| **Loading** | Waiting for data or a calculation | Skeleton or progress where the content will appear; layout doesn't jump | Blank screen, endless spinner, or content that pops in and moves buttons |
| **Partial** | Some data, not enough to fill the view | Shows what there is and makes clear what's missing or filled in | Gaps that look like bugs, or filler that looks like the user's data |
| **Success** | An action worked | Confirms in place and shows the new state; brief if routine | Nothing changes, or a toast that vanishes before it's read |
| **Error (user)** | Invalid input | Inline, at the field, plain words, keeps what was typed, says how to fix | One generic message for every field; input cleared |
| **Error (system)** | Something failed on our side | Says what failed, that it's not the user's fault, and what to do; keeps their work | Raw error codes, lost work, silent failure |
| **Offline / slow** | No or weak connection | Says so, keeps working where it can, queues changes | Spinners forever, or actions that seem to work and are lost |
| **Permission** | Needs access (camera, notifications, location) or a role | Asks at the moment of need with a reason; works without it where possible | Asking on launch; dead ends when declined |
| **Edge data** | The data the product is built around goes out of bounds: expired, over a limit, duplicate, very long, zero, negative | Handled visibly, with the reason | Silently dropped, truncated or miscounted |
| **Destructive** | Delete, reset, overwrite | Undo, or confirm only when it can't be undone | Instant and irreversible, with no undo |
| **Interrupted** | User leaves mid-task and returns | Work is kept; they land where they were | Form cleared, or dropped back to the start |

## How to trigger them

- **Clear storage** (localStorage, cookies) or use a private window for first run and empty.
- **Throttle the network** in browser dev tools for loading and offline.
- **Submit nothing, then nonsense** (empty fields, letters in numbers, past and future dates, very long text) for user errors.
- **Use the product's own test flags** where the brief provides them (for example a fixed "today" date to make data expire).
- **Delete something**, then look for the way back.
- **Leave and return**: reload mid-task, use the system back gesture, switch apps.

Record each as triggered, not triggered (why) or not applicable. Never describe a state you didn't see as if you had.
