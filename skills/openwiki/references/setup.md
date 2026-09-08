# First-time setup

Create/clone the GitHub Wiki into `<project>/openwiki/`, then generate directly into that clone using OpenWiki's default code-mode output directory.

## Machine

Install the CLI if missing:

```powershell
npm install --global openwiki
```

The machine's first initialization captures the ChatGPT-subscription login in `~/.openwiki/.env`; later repositories reuse it. Select the provider and model from the parent skill's durable decisions. Complete user-only authentication when required, without exposing saved tokens.

## Create and clone the GitHub Wiki

Keep `/openwiki/` in the main project's `.gitignore`, even if the global Git ignore already covers it. Preserve existing entries and add the rule only once.

If `openwiki/` exists, confirm that it has its own Git repository with this project's Wiki as `origin`. For existing generated docs without a Wiki clone or a legacy layout, use the migration section below. Preserve existing content; stop on unrelated path collisions.

GitHub creates `<repo>.wiki.git` only after Wikis are enabled and the first page is saved. If the remote is unavailable, invoke `browser-harness`:

1. Enable **Wikis** under **Features** on the repository's **Settings** page.
2. In the **Wiki** tab, create `Home` with the temporary body `Initializing OpenWiki publication.` and save it.
3. Verify that the Wiki remote resolves, then clone it from the main project root:

   ```powershell
   git clone https://github.com/<owner>/<repo>.wiki.git openwiki
   ```

Use the existing GitHub browser session according to browser-harness login rules. Stop for user-only authentication or confirmation, missing administration permission, or a plan without Wikis. Report the exact blocker. If a saved first page exists but the remote remains unavailable, investigate Wiki enablement, repository access, and Git credentials separately.

Done when `openwiki/` is the correct separate Git repository and `git check-ignore --no-index openwiki/Home.md` confirms the main repository ignores it.

## Generate and publish

From the main project root, run `openwiki code --init` with the parent skill's provider/model settings. The CLI generates directly into the `openwiki/` clone by default. Keep the main project as the source root; running from inside the Wiki clone would document the wrong repository.

Follow the parent skill's generation review and in-place GitHub Wiki synchronization steps. Keep the generation prompt and internal state local to the clone and excluded from publication. Both project agent files must reference `openwiki/`.

Done when `openwiki/Home.md` renders on GitHub with its sidebar, Wiki local and remote revisions agree, no second documentation tree exists, and no OpenWiki CI workflow was introduced.

## Existing docs and legacy layouts

The destination is always `<project>/openwiki/`. A `wiki/` clone or sibling `../<repo>.wiki` clone is a legacy location, not a second supported output directory.

- Inspect existing docs, clone remotes, and both repositories' Git state before migrating. Existing `openwiki/` docs without their own Wiki Git repository need migration too; their folder name is already correct.
- Report a migration plan and obtain authorization before moving/deleting files or removing tracked docs from the main repository. Preserve unique pages, generation instructions, metadata, Wiki history, and uncommitted work. Resolve conflicting versions explicitly.
- If the correct Wiki clone exists at a legacy location and `openwiki/` is absent, move that clone into `openwiki/` during the authorized migration. If the destination already contains docs, reconcile them with the clone without overwriting either version or discarding Git history.
- Finish with one Wiki tree at `openwiki/`, project agent-file references to it, and update hooks using the CLI's default output from the main project root. A new `.gitignore` rule does not untrack existing files.

Do not perform a migration merely because an update discovered an old layout. Stop the update and report the required migration rather than generating into an unconfigured directory.

GitHub references:

- <https://docs.github.com/en/communities/documenting-your-project-with-wikis/adding-or-editing-wiki-pages>
- <https://docs.github.com/en/communities/documenting-your-project-with-wikis/creating-a-footer-or-sidebar-for-your-wiki>
