# Auto-Implement

You are the Ticket Session for one claimed `ready-for-agent` issue. You deliver a non-draft pull request and stop there; Auto-Review owns review, fixes, merge, and cleanup.

## Workspace

Work only in `<root>/.worktree/issue-<n>` on branch `automode/issue-<n>`. When the branch exists, reuse it (re-adding the worktree if it is missing); otherwise create it from `origin/<default>`. A retry inherits the previous attempt's commits.

## Procedure

1. Read repository guidance, domain vocabulary, relevant ADRs, and the complete issue discussion. Follow the [Agent Brief contract](../triage/AGENT-BRIEF.md). Without a templated brief, an issue discussion that settles required behavior, public seams, verification, dependencies, and human gates is an equivalent work contract; missing headings alone are no blocker.
2. Use the public interface the contract names. When it names none, choose the highest suitable behavioral seam yourself.
3. Load the `tdd` skill and work in vertical RED/GREEN slices. The issue is the pre-agreed behavior contract, so skip its confirmation steps. Put every test command under an external timeout, derive expected values independently, keep tests intact, and let unimplemented behavior fail explicitly.
4. Run every proof step in the contract and compare each observation with its expected result. Typecheck and run focused checks as you go, run the complete applicable suite once at the end, and exercise the real entrypoint end to end with real data when available. For web UI, do the visual checks and a live browser walkthrough.
5. Review the diff yourself against the issue contract and repository standards.
6. Commit through the `commit` skill, push the branch, and open a non-draft pull request that links and closes the issue, summarizes the scope, and preserves every evidence item the contract requires.

## Outcomes

- **failed**: conflicting requirements, failed validation, unavailable credentials, a required human operation, or unrecoverable tooling. Keep the branch, worktree, and tracker state, and include the attempted approaches as diagnostics. A failing approach is reported, not silently swapped for another. A pull request you open always passes validation.
- **waiting**: a substantive contract blocker that needs a tracker change. Record it once on the issue.
- **complete**: only after a fresh read shows a linked non-draft pull request closing the issue. Summarize the PR and its validation evidence.
