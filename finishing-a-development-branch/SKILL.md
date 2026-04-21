---
name: finishing-a-development-branch
description: Use when implementation is complete, all tests pass, and you need to finalize the work - verifies tests, asks user to test manually, then commits using the commit skill
---

# Finishing a Development Branch

## Overview

Guide completion of development work by verifying tests, getting user confirmation, and committing.

**Core principle:** Verify tests → User tests manually → Commit with commit skill.

**Announce at start:** "I'm using the finishing-a-development-branch skill to complete this work."

## The Process

### Step 1: Verify Tests

**Before anything else, verify tests pass:**

```bash
# Run project's test suite
npm test / cargo test / pytest / go test ./...
```

**If tests fail:**
```
Tests failing (<N> failures). Must fix before completing:

[Show failures]

Cannot proceed until tests pass.
```

Stop. Don't proceed to Step 2.

**If tests pass:** Continue to Step 2.

### Step 2: User Testing Gate

**After automated tests pass, ask the user to test the feature themselves:**

> "All automated tests pass. Please test the feature yourself before I commit. Let me know when you're done and whether everything works as expected."

**Wait for the user's response.** Do not proceed until the user confirms.

- If the user reports issues or requests changes: treat each change as a new **User Requirement**. Propagate it to all artifacts — update the spec (User Requirements section), update the plan, update tests (remove/rewrite tests for old behavior, add tests for new), and update implementation. Then re-run automated tests and ask the user to test again.
- If the user confirms it works: continue to Step 3.

### Step 3: Commit

**Use the `commit` skill to create a commit on the current branch/worktree.**

Invoke the commit skill — it handles staging, message drafting, and the commit itself. Do not manually run git commit.

## Common Mistakes

**Skipping test verification**
- **Problem:** Commit broken code
- **Fix:** Always verify automated tests before anything else

**Skipping user testing**
- **Problem:** Automated tests pass but the feature doesn't work as the user expected
- **Fix:** Always ask the user to test manually before committing

**Committing before user confirms**
- **Problem:** User hasn't verified the feature works
- **Fix:** Wait for explicit user confirmation after manual testing

## Red Flags

**Never:**
- Proceed with failing tests
- Commit without user testing confirmation
- Skip the commit skill (don't manually run git commit)

**Always:**
- Verify automated tests first
- Ask user to test the feature themselves
- Wait for user confirmation before committing
- Use the commit skill for the final commit

## Integration

**Called by:**
- **subagent-driven-development** — After all tasks complete
- **executing-plans** — After all batches complete

**Uses:**
- **commit** — For creating the final commit
