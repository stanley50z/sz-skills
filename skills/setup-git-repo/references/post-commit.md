# Install automatic Wiki synchronization

Use the bundled scripts as the implementation. Do not recreate their logic in a new hook or rely on the OpenWiki agent to invoke a coding-assistant skill.

## Prerequisites

Complete the `openwiki` skill's setup first:

- `<project>/openwiki/` is the separate GitHub Wiki clone, ignored and untracked by the main repository.
- The Wiki's `origin` fetch and push URLs identify the main project's `<owner>/<repo>.wiki.git` on GitHub. Both HTTPS and SSH URLs are supported.
- The Wiki is on its remote default branch and its pages are already published. Both repositories are clean. Resolve unrelated unpublished Wiki commits before enabling automation.
- `Home.md` is the Wiki landing page. Keep `quickstart.md` for the CLI's generated local references. In `openwiki/INSTRUCTIONS.md`, request flat filenames, standard Markdown links, and preservation of `Home.md` and existing page names.
- Git, Python 3.10+, and the authenticated OpenWiki CLI are available on the committing process's PATH. Configure the Wiki's Git author identity and any required signing to work unattended. Finish interactive login during setup, not in the hook.

## Copy and connect

1. Copy these files unchanged from this skill into the project:

   | Bundled file | Project destination |
   | --- | --- |
   | `scripts/openwiki_post_commit.py` | `.githooks/openwiki_post_commit.py` |
   | `scripts/openwiki-sync` | `.githooks/openwiki-sync` |

   Verify the runner's `PROVIDER` and `MODEL` constants match the `openwiki` skill's durable decisions. Stop on an unrelated destination-file collision; preserve local customizations when upgrading an existing copy.

2. Inspect the effective `core.hooksPath`, hook manager, and existing `post-commit`. Keep their current behavior. For a repository-local shell hook, insert this managed block once, after the shebang and before any existing early exit:

   ```sh
   # BEGIN sz-openwiki-sync
   sh "$(git rev-parse --show-toplevel)/.githooks/openwiki-sync"
   # END sz-openwiki-sync
   ```

   Replace an existing managed block when reinstalling, rather than appending another. Replace the old update-only OpenWiki invocation if present so generation runs exactly once. Leave unrelated hook commands intact. For a hook manager, register that same launcher through its supported configuration instead.

3. If no hook exists, create an executable repository-local `post-commit` with `#!/bin/sh` and the block above. Set a repository-local hooks path only when it does not bypass an existing manager or shared/global hooks behavior. If shared hooks are active, preserve their dispatch through the manager or report the integration blocker; never edit a shared directory in place.

4. Keep shell launchers and the effective shell hook LF-terminated. Add matching `text eol=lf` rules to the project's `.gitattributes` where needed, and set the effective hook's executable bit. Track the copied scripts and repository-local integration files in the main project, never the Wiki pages.

Done when the installed files match the bundle, Git invokes the launcher exactly once, and existing post-commit behavior still runs even when Wiki synchronization fails. Verify through temporary project/Wiki repositories and a stub CLI before enabling it on the real project. The bundle's regression suite is `python -m unittest discover -s <skill>/tests -v`; run with an external timeout.

## What runs automatically

The launcher starts a detached worker with redirected input/output and returns immediately so Git and other hooks can finish. On Windows the worker has no console, and every runner-launched Git, generator, and cleanup process uses `CREATE_NO_WINDOW` to prevent flashing windows; on POSIX the worker starts a new session. The committing agent commits, pushes, verifies the project revision, and finishes without waiting for, polling, or repairing Wiki work. The background worker performs:

1. Check repository identities and clean working trees; acquire a per-Wiki lock.
2. Pull the Wiki's actual remote default branch with `--ff-only`. Stop on divergence or unrelated unpublished local commits.
3. Run `openwiki code --update --print` from the main project root with the pinned provider/model.
4. Remove only newly generated OpenWiki GitHub CI workflow files. Preserve project `AGENTS.md`/`CLAUDE.md` changes uncommitted; stop publication on unexpected project changes.
5. Flatten nested Markdown pages in place, rewrite internal/source links, rebuild `_Sidebar.md`, and validate before staging. Keep generation instructions and dot-file metadata local and excluded. Unsupported links, filename collisions, and non-page changes require inspection, not a best-effort push.
6. Commit changed Wiki pages and push only the Wiki branch. A no-op creates no commit. Verify the remote revision. Disable nested Git hooks and clear inherited repository/index variables so Wiki commits cannot recurse into the project hook.

Generation and publication operate on the same `openwiki/` tree. The hook never commits, amends, or pushes the main project. Its Git commands are noninteractive and bounded; generation has a 30-minute limit and its process tree is stopped on timeout or interruption.

## Failures and retries

A failure leaves the completed project commit intact and preserves generated work for inspection. A rejected push also preserves the local Wiki commit; a private receipt allows the runner to retry its own unpublished commit, but not arbitrary local Wiki history. No force pushes or automatic conflict resolution.

Background status and failures are appended to `openwiki-background.log` in the Wiki's Git directory, with worker PIDs and exit status. Detailed generation/Git diagnostics are stored there as `openwiki-sync.log`, never in published pages. Common credential formats are redacted, but still treat this local log as sensitive. The page-name map and pending-push receipt also live in that Git directory. An interrupted process may leave `openwiki-sync.lock`; remove that lock only after confirming no sync is running.

After resolving the failure and reviewing pending changes, retry from the project root:

```sh
python .githooks/openwiki_post_commit.py --root .
```

Use `--generation-timeout <seconds>` to change the generation limit for a manual run. Manual runs stay synchronous and return nonzero on failure. `--background` starts a detached job instead; successful startup does not imply successful publication. Only the hook launcher deliberately returns success on startup failure to preserve other post-commit behavior.

Report the installed paths and automatic background workflow. Project commits and pushes do not wait for Wiki synchronization. Background failures and generated project instruction changes belong to a separately requested maintenance task, not commit closure.
