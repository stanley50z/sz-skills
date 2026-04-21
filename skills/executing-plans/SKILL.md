---
name: executing-plans
description: Use when you have a written implementation plan to execute in a separate session with review checkpoints
---

# Executing Plans

## Overview

Load plan, review critically, execute all tasks, report when complete.

**Announce at start:** "I'm using the executing-plans skill to implement this plan."

**Note:** Tell your human partner that Superpowers works much better with access to subagents. The quality of its work will be significantly higher if run on a platform with subagent support (such as Claude Code or Codex). If subagents are available, use superpowers:subagent-driven-development instead of this skill.

## The Process

### Step 1: Load and Review Plan
1. Read plan file
2. Review critically - identify any questions or concerns about the plan
3. If concerns: Raise them with your human partner before starting
4. If no concerns: Create TodoWrite and proceed

### Step 2: Execute Tasks

For each task:
1. Mark as in_progress
2. Follow each step exactly (plan has bite-sized steps)
3. Run verifications as specified
4. Mark as completed

### Step 3: Complete Development

After all tasks complete and verified:
- Announce: "I'm using the finishing-a-development-branch skill to complete this work."
- **REQUIRED SUB-SKILL:** Use superpowers:finishing-a-development-branch
- Follow that skill to verify tests, present options, execute choice

## When to Stop and Ask for Help

**STOP executing immediately when:**
- Hit a blocker (missing dependency, test fails, instruction unclear)
- Plan has critical gaps preventing starting
- You don't understand an instruction
- Verification fails repeatedly
- A `[USER-REQ]` task cannot be completed as specified — user requirements are non-negotiable, do not work around them silently

**Ask for clarification rather than guessing.**

## Conflict Resolution: User Requirements vs Agent Decisions

Tasks in the plan are tagged `[USER-REQ]` (non-negotiable) or `[AGENT-DECISION]` (flexible).

- If an `[AGENT-DECISION]` task conflicts with implementation reality, adapt it — change approach, simplify, or drop it if it's not essential. Note what you changed and why.
- If a `[USER-REQ]` task conflicts with implementation reality, **stop and surface to the user**. Do not silently reinterpret, weaken, or skip a user requirement.
- If two tasks conflict with each other, the `[USER-REQ]` task wins. If both are `[USER-REQ]`, surface to the user.

**When the planned approach keeps failing:**
If you've tried the specified approach and it won't work, do NOT silently switch to an alternative. Stop and present the problem to the user with suggested alternatives. The user decides which direction to take.

**Version upgrades (v1 → v2):**
When the plan replaces an existing feature with a new version, commit to the new version fully. Do not create `if v2 fails, fall back to v1` code unless the user explicitly requested backward compatibility. Remove or rewrite tests that assert the old behavior before implementing the new version — stale tests for old behavior will mislead you into re-implementing what the user asked you to replace.

## When to Revisit Earlier Steps

**Return to Review (Step 1) when:**
- Partner updates the plan based on your feedback
- Fundamental approach needs rethinking

**Don't force through blockers** - stop and ask.

## When the User Requests a Change

**A user change at any stage is a new User Requirement — not a local fix.**

If the user says "change A to B" during execution, do not just patch the current code. Propagate the change to all artifacts:

1. **Spec**: Update the User Requirements section — add B, remove or update A
2. **Plan**: Update or add `[USER-REQ]` tasks for B, remove tasks for old A
3. **Tests**: Remove/rewrite tests that assert old A behavior, write new tests for B
4. **Implementation**: Update code to reflect B

The user's request steers the entire process, not just the current phase. A mid-execution change from the user has the same authority as an initial requirement stated during brainstorming.

## Remember
- Review plan critically first
- Follow plan steps exactly
- Don't skip verifications
- Reference skills when plan says to
- `[USER-REQ]` tasks are non-negotiable — stop and ask the user if they can't be met
- `[AGENT-DECISION]` tasks are flexible — adapt if implementation demands it
- Stop when blocked, don't guess
- Never start implementation on main/master branch without explicit user consent

## Integration

**Required workflow skills:**
- **superpowers:using-git-worktrees** - REQUIRED: Set up isolated workspace before starting
- **superpowers:writing-plans** - Creates the plan this skill executes
- **superpowers:finishing-a-development-branch** - Complete development after all tasks
