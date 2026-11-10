---
name: one-off
description: Fix a small bug or add a small feature, then commit, push, and restart the app in one pass.
disable-model-invocation: true
---

# One-off

The user spotted a small bug or wants a small feature and has already decided it ships. Invoking this skill is their approval to implement, commit, push to the current branch (the default branch included), and restart the app. Run all three steps without stopping to ask.

1. **Fix.** Make the smallest change that delivers the behavior the user described. Then run the project's typecheck, lint, and the tests covering the touched code. Done when the behavior is in place and those checks pass. If the change turns out larger than a one-off (a design decision, a migration, a change across many modules), stop and tell the user what you found before writing more.

2. **Commit and push.** Load the `commit` skill and follow it. This invocation counts as the user's push request, including in a linked worktree. Done when the commit is on the remote, or when you can name the exact push blocker.

3. **Restart.** Stop the running app and start it again with the project's own launch commands: `stop.py` then `start.py` when they exist, otherwise the restart path the project documents (a project skill, `README.md`, package scripts, a service manager). Done when the new process is up and answers its health check, port, or main screen, showing the change live. If the project has no launch command, say so; the commit stays pushed.

Report in a few lines: what changed, the commit hash and branch, and how you confirmed the restarted app runs.
