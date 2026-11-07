# Prototype: Quiet Hours sender preview

Fictional example, paired with `quiet-hours-lite.md`.

## What we're testing
Senders will delay a non-urgent message when shown that the recipient is in quiet hours.
Success looks like: across 5 users × 6 scripted messages, at least 30% of previewed messages are scheduled rather than sent now, and no participant describes the preview as nagging.

## Build
A working-slice prototype of composing a message to someone in quiet hours.

Screens or steps:
1. Conversation list with four fake colleagues. Two show a moon icon (in quiet hours).
2. Open a conversation with a quiet-hours colleague and type a message.
3. Before sending, a preview line appears above the input: "Priya is in quiet hours · delivers 9:00".
4. The send button offers **Deliver at 9:00** (default) and **Send now anyway**.
5. Choosing either shows the message in the thread with its state (scheduled or sent as urgent).
6. A hidden `/results` page lists each choice with a timestamp, so the test moderator can count.

Include exactly these states: the happy path above; sending to a colleague who is *not* in quiet hours (no preview); and the empty conversation.

## Fake on purpose
- Data: four colleagues hard-coded with time zones; "now" is fixed at 22:40 local
- No real delivery, notifications, auth or settings screen
- Quiet-hours schedule is not editable (R1 is not under test)

## Constraints
- A single Vite + React app with local state only; `npm run dev` starts it
- Works at 390 px width
- Copy exactly as in the PRD; three variants of the override label are switchable with `?copy=a|b|c`

## Don't
- Don't build the digest (R5) or per-channel schedules (R6)
- Don't use guilt-trip copy anywhere (it's out of scope in the PRD)
- Never drop a message: every send ends up visibly scheduled or sent

## Done when
- [ ] `npm run dev` starts it locally
- [ ] Steps 1–6 can be clicked through end to end
- [ ] `/results` shows every choice made in the session
- [ ] The README says how to run it and what's fake

## Source
PRD: `quiet-hours-lite.md`, sections Recommendation, Scope and Requirements. Requirements in scope: R3, R4.
