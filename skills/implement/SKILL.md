---
name: implement
description: "Implement work from a direct request, spec, or set of tickets."
disable-model-invocation: true
---

# Implement

Implement the work described by the user directly or in a spec or tickets.

## Establish the work record

Reuse an existing implementation issue or ticket when the user supplies one. Create no duplicate.

When the user gives the requirement directly and no implementation issue already exists, create one implementation issue on the configured tracker before coding. Summarize the requirement and validation plan. Apply only applicable category or metadata labels, such as `bug` or `enhancement`, and leave off `ready-for-agent`. This session owns the implementation; `ready-for-agent` hands work to Auto-Implement. Keep the issue reference for close-out.

Before coding, resolve the repository's default branch from Git or hosting metadata. For a fork, use the default branch of the repository that will receive the PR. Fetch it, then create and switch to a feature branch from its latest remote tip. Keep the resolved branch name and the branch's start commit for close-out.

Work one ticket at a time from the frontier (tickets whose blockers are all done). Read the ticket's **Requirement** before coding.

Build with the `tdd` skill at pre-agreed seams: load the `tdd` skill before the first test. It owns test policy, including UI checks, command timeouts, and the done gate's end-to-end run through the real entry point. Run typechecking regularly alongside it.

**No fallbacks, no silent failure.** The tdd skill's explicit-failure gate binds every change in this session, tested or not.

When the user changes a requirement mid-implementation, follow [REQUIREMENT-CHANGES.md](REQUIREMENT-CHANGES.md).

## Close Out

Once the tdd done gate passes:

1. Load the `code-review` skill with the branch's start commit as the resolved comparison point, plus the spec, ticket, or issue references. Its scope covers the uncommitted work. Address what it finds.
2. Commit to the current branch with the commit skill.
3. Push the feature branch and create a ready-to-review pull request that targets that same default branch explicitly. The PR must not be a draft. Give it a clear title, and load the `pr` skill to write the body. Its Evidence lists the validation performed. Add a line that links the relevant spec or tickets, with a closing reference for an implementation issue this session created so the merge closes it.
4. Ask the user to test the feature themselves before wrapping up. Passing automated tests does not mean it works as they expected.
