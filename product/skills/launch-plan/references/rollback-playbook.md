# Rollback playbook

Decide this before launch. Rehearse the mechanism before anyone outside the team has access.

## Three responses

| Response | What it means | Use when |
|---|---|---|
| **Pause** | Turn one feature off with a flag; the rest keeps working | One path is wrong and the rest is safe |
| **Roll back** | Return everyone to the last good build or config | A release broke something broad |
| **Stop** | End the stage; nobody new joins, existing users are told | The core idea causes harm, or trust is broken |

## Trigger table

| Trigger | Threshold | Response | Decides | Time to act | Mechanism | Users see |
|---|---|---|---|---|---|---|

Rules for the table:

- **Harm triggers have a threshold of one.** One user exposed to unsafe advice, one data leak.
- **Every trigger has a decider and a stand-in** for when the decider is asleep or away. If the product is used at night, someone must be able to act at night.
- **Time to act** runs from detection to the mechanism taking effect, not to a meeting.
- **Mechanisms are named**: which flag, which build, which config value. "Roll back" alone isn't a mechanism.
- **Users see a message written in advance** (see `comms-plan.md`).

## Mobile notes

A mobile build can't be pulled back from a phone once installed. Server-side flags and remote config are the fast lever; a new build is the slow one. If the rollback depends on a flag, the app must read it on launch and at sensible intervals, and work safely if it can't reach the server (fail closed for risky features).

## After a rollback

1. Confirm the mechanism took effect (the watch list signal stops).
2. Send the user message.
3. Write down what happened, when, and who decided, while it's fresh.
4. Decide, with the named decider, whether to fix and resume or stop. Resuming needs the gate for that stage to pass again.
