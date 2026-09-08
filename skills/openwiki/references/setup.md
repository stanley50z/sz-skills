# First-time setup

Follow the parent skill's output-directory support check before generating docs. The order is verify CLI support, create/clone the GitHub Wiki into `wiki/`, then generate directly into that clone.

## Machine

Install the CLI if missing:

```powershell
npm install --global openwiki
```

The machine's first initialization captures the ChatGPT-subscription login in `~/.openwiki/.env`; later repositories reuse it. Select the provider and model from the parent skill's durable decisions. Complete user-only authentication when required, without exposing saved tokens.

## Create and clone the GitHub Wiki

Keep `/wiki/` in the main project's `.gitignore`, even if the global Git ignore already covers it. Preserve existing entries and add the rule only once.

If `wiki/` exists, confirm that it has its own Git repository with this project's Wiki as `origin`. Stop on a path collision instead of replacing its contents. For a legacy layout, use the migration section below.

GitHub creates `<repo>.wiki.git` only after Wikis are enabled and the first page is saved. If the remote is unavailable, invoke `browser-harness`:

1. Enable **Wikis** under **Features** on the repository's **Settings** page.
2. In the **Wiki** tab, create `Home` with the temporary body `Initializing OpenWiki publication.` and save it.
3. Verify that the Wiki remote resolves, then clone it from the main project root:

   ```powershell
   git clone https://github.com/<owner>/<repo>.wiki.git wiki
   ```

Use the existing GitHub browser session according to browser-harness login rules. Stop for user-only authentication or confirmation, missing administration permission, or a plan without Wikis. Report the exact blocker. If a saved first page exists but the remote remains unavailable, investigate Wiki enablement, repository access, and Git credentials separately.

Done when `wiki/` is the correct separate Git repository and `git check-ignore --no-index wiki/Home.md` confirms the main repository ignores it.

## Generate and publish

From the main project root, run code-mode initialization with the verified configuration targeting `<project>/wiki/`, not the CLI's default output. Use the parent skill's provider/model settings. Keep the main project as the source root; running from inside the Wiki clone would document the wrong repository.

Follow the parent skill's generation review and in-place GitHub Wiki synchronization steps. Keep the generation prompt and internal state local to the clone and excluded from publication. Both project agent files must reference `wiki/`.

Done when `wiki/Home.md` renders on GitHub with its sidebar, Wiki local and remote revisions agree, no separate `openwiki/` tree exists, and no OpenWiki CI workflow was introduced.

## Existing two-folder layouts

Treat a project-root `openwiki/` tree or a sibling `../<repo>.wiki` clone as legacy, not a second supported output location.

- If only the sibling clone exists, verify its `origin` before moving it into `wiki/`. Preserve its history and local changes; stop if the destination already exists or the remote does not match.
- When `openwiki/` exists, inspect both trees and their Git state. Report a migration plan and obtain authorization before moving/deleting files or removing tracked docs from the main repository. Preserve unique pages, generation instructions, metadata, and uncommitted work. Resolve conflicting versions explicitly.
- A migration must leave one Wiki tree at `wiki/`, update the output configuration and agent-file references, and reconfigure existing update hooks. A new `.gitignore` rule does not untrack existing files.

Do not perform a migration merely because an update discovered a legacy directory. Stop the update and report the required migration rather than continuing the two-folder workflow.

GitHub references:

- <https://docs.github.com/en/communities/documenting-your-project-with-wikis/adding-or-editing-wiki-pages>
- <https://docs.github.com/en/communities/documenting-your-project-with-wikis/creating-a-footer-or-sidebar-for-your-wiki>
