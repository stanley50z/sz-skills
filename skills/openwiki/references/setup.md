# First-time setup

Three independent first-times: each machine, each repository, and each repository's wiki needs its own.

## Machine: install the CLI

```powershell
npm install --global openwiki
```

The ChatGPT-subscription login is captured during the machine's first `--init` and saved to `~/.openwiki/.env`; later runs in any repository reuse it, and the access token refreshes itself on expiry.

## Repository: generate the docs

From the repository root:

```powershell
$env:OPENWIKI_PROVIDER = 'openai-chatgpt'
openwiki code --init
```

Complete the browser login at `auth.openai.com` — the wizard also prints the URL for headless use, where you open it on another machine and paste the redirect URL back into the terminal — then select the model. The run generates `openwiki/` and writes the `<!-- OPENWIKI:START/END -->` blocks into `AGENTS.md` and `CLAUDE.md`, creating those files if absent.

Review `git status --short`, `git diff --check`, and `git diff` before committing.

Done when `openwiki/quickstart.md` exists, both agent files carry an OPENWIKI block, and no OpenWiki CI workflow was added.

## Wiki: create and clone

The `<repo>.wiki.git` remote only comes into existence once the wiki has a saved first page — creating that page manually is the prerequisite that unblocks the clone.

If the remote is not yet available, stop and explicitly notify the user that publication is blocked until they complete steps 1 and 2 below in GitHub's web interface. Do not keep retrying the clone or report only a generic git/authentication failure.

1. Enable **Wikis** in the GitHub repository settings.
2. Create and save a first page in the Wiki tab.
3. Clone the wiki as a sibling of the main repository:

   ```powershell
   git clone https://github.com/<owner>/<repo>.wiki.git ..\<repo>.wiki
   ```

GitHub's documentation:

- <https://docs.github.com/en/communities/documenting-your-project-with-wikis/adding-or-editing-wiki-pages>
- <https://docs.github.com/en/communities/documenting-your-project-with-wikis/creating-a-footer-or-sidebar-for-your-wiki>
