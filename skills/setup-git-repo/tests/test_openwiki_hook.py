"""Exercise the bundled hook through real commits and a local bare Wiki remote."""

import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time
import unittest


SKILL = Path(__file__).resolve().parents[1]
NO_WINDOW = subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0


class WikiHookTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / 'project with spaces'
        self.remote = self.base / 'wiki.git'
        self.peer = self.base / 'peer'
        self.root.mkdir()
        self.env = os.environ.copy()
        for key in list(self.env):
            if key.startswith('GIT_'):
                self.env.pop(key)
        self.env.update({
            'GIT_CONFIG_GLOBAL': str(self.base / 'gitconfig'),
            'GIT_CONFIG_NOSYSTEM': '1',
            'GIT_AUTHOR_NAME': 'Test User', 'GIT_COMMITTER_NAME': 'Test User',
            'GIT_AUTHOR_EMAIL': 'test@example.com', 'GIT_COMMITTER_EMAIL': 'test@example.com',
            'OPENWIKI_PROVIDER': 'wrong', 'OPENWIKI_MODEL_ID': 'wrong',
        })
        self.git(self.base, 'config', '--global', 'url.' + self.remote.as_uri() + '.insteadOf',
                 'https://github.com/test/project.wiki.git')
        self.git(self.base, 'init', '--bare', '-b', 'published', str(self.remote))
        self.git(self.base, 'clone', str(self.remote), str(self.peer))
        (self.peer / 'Home.md').write_text('# Project\n', encoding='utf-8')
        self.git(self.peer, 'add', 'Home.md')
        self.git(self.peer, 'commit', '-m', 'initial wiki')
        self.git(self.peer, 'push', '-u', 'origin', 'published')
        self.git(self.root, 'init', '-b', 'main')
        self.git(self.root, 'remote', 'add', 'origin', 'https://github.com/test/project.git')
        (self.root / '.gitignore').write_text('/openwiki/\n', encoding='utf-8')
        (self.root / 'README.md').write_text('# Project\n', encoding='utf-8')
        self.git(self.root, 'add', '.gitignore', 'README.md')
        self.git(self.root, 'commit', '-m', 'initial project')
        self.git(self.root, 'clone', 'https://github.com/test/project.wiki.git', 'openwiki')
        self.wiki = self.root / 'openwiki'
        self.before = self.git(self.root, 'rev-parse', 'HEAD').stdout.strip()
        self.remote_before = self.git(self.remote, 'rev-parse', 'HEAD').stdout.strip()
        self.bin = self.base / 'bin'
        self.bin.mkdir()
        self.env['PATH'] = str(self.bin) + os.pathsep + self.env['PATH']
        self.stub = self.bin / 'generate.py'
        self.stub.write_text(
            "import os, sys\nfrom pathlib import Path\n"
            "assert sys.argv[1:] == ['code', '--update', '--print']\n"
            "assert os.environ['OPENWIKI_PROVIDER'] == 'openai-chatgpt'\n"
            "assert os.environ['OPENWIKI_MODEL_ID'] == 'gpt-5.6-luna'\n"
            "root = Path.cwd()\nassert (root / 'README.md').exists()\n"
            "wiki = root / 'openwiki'\n"
            "assert (wiki / 'Remote.md').exists(), 'Wiki must be pulled before generation'\n"
            "(wiki / 'Guide.md').write_text('# Guide\\n\\n[Home](Home.md)\\n', encoding='utf-8')\n",
            encoding='utf-8',
        )
        if os.name == 'nt':
            (self.bin / 'openwiki.cmd').write_text(
                '@echo off\n"' + sys.executable + '" "' + str(self.stub) + '" %*\n',
                encoding='utf-8',
            )
        else:
            launcher = self.bin / 'openwiki'
            launcher.write_text('#!/bin/sh\nexec "' + sys.executable + '" "' + str(self.stub) + '" "$@"\n', encoding='utf-8')
            launcher.chmod(0o755)
        # A remote-only page proves the hook pulls before it launches the generator.
        (self.peer / 'Remote.md').write_text('# Remote update\n', encoding='utf-8')
        self.git(self.peer, 'add', 'Remote.md')
        self.git(self.peer, 'commit', '-m', 'remote update')
        self.git(self.peer, 'push')

    def git(self, cwd, *args):
        return subprocess.run(['git', '-C', str(cwd), *args], env=self.env,
                              text=True, encoding='utf-8', capture_output=True,
                              check=True, timeout=30, creationflags=NO_WINDOW)

    def install(self):
        hooks = self.root / '.githooks'
        hooks.mkdir(exist_ok=True)
        for name in ['openwiki_post_commit.py', 'openwiki-sync']:
            shutil.copyfile(SKILL / 'scripts' / name, hooks / name)
        # The existing behavior deliberately exits. The new invocation must not replace it.
        (hooks / 'post-commit').write_text(
            '#!/bin/sh\nsh "$(git rev-parse --show-toplevel)/.githooks/openwiki-sync"\n'
            "printf '%s\\n' existing-hook-ran\nexit 0\n", encoding='utf-8',
        )
        (hooks / 'post-commit').chmod(0o755)
        self.git(self.root, 'add', '.githooks')
        self.git(self.root, 'config', 'core.hooksPath', '.githooks')

    def commit(self):
        result = self.git(self.root, 'commit', '--allow-empty', '-m', 'project change')
        return self.wait_background(result)

    def wait_background(self, result):
        """Wait only in tests, then expose the detached worker's diagnostics to assertions."""
        output = result.stdout + result.stderr
        self.assertIn('OpenWiki sync started in background (PID ', output)
        pid = int(output.split('OpenWiki sync started in background (PID ')[1].split(')')[0])
        log = self.wiki / '.git/openwiki-background.log'
        deadline = time.monotonic() + 30
        while time.monotonic() < deadline:
            text = log.read_text(encoding='utf-8') if log.exists() else ''
            if f'OpenWiki sync process {pid} finished ' in text:
                return subprocess.CompletedProcess(result.args, result.returncode, result.stdout + text, result.stderr)
            time.sleep(0.05)
        if os.name == 'nt':
            subprocess.run(['taskkill', '/PID', str(pid), '/T', '/F'], capture_output=True, timeout=10, creationflags=NO_WINDOW)
        else:
            import signal
            os.killpg(pid, signal.SIGKILL)
        self.fail('Background Wiki job did not finish within 30 seconds')

    def test_commit_returns_before_generation_finishes_without_inheriting_output_pipes(self):
        release = self.base / 'release-generator'
        expired = self.base / 'generator-expired'
        with self.stub.open('a', encoding='utf-8') as script:
            script.write(
                'import time\n'
                'deadline = time.monotonic() + 5\n'
                'while not Path(' + repr(str(release)) + ').exists():\n'
                '    if time.monotonic() > deadline:\n'
                '        Path(' + repr(str(expired)) + ').touch()\n'
                '        break\n'
                '    time.sleep(0.05)\n'
            )
        self.install()
        try:
            # Captured pipes make this hang if the worker inherits Git's output handles.
            result = self.git(self.root, 'commit', '--allow-empty', '-m', 'project change')
            self.assertFalse(expired.exists(), 'git commit waited for Wiki generation')
            self.assertIn('existing-hook-ran', result.stdout + result.stderr)
            self.assertNotIn('Wiki synced', result.stdout + result.stderr)
        finally:
            release.touch()
            if 'result' in locals() and 'started in background' in result.stdout + result.stderr:
                self.wait_background(result)
        self.assertEqual(self.git(self.wiki, 'rev-parse', 'HEAD').stdout,
                         self.git(self.remote, 'rev-parse', 'HEAD').stdout)

    def test_commit_pulls_generates_commits_and_pushes_only_wiki(self):
        self.install()
        result = self.commit()
        output = result.stdout + result.stderr
        self.assertIn('existing-hook-ran', output)
        self.assertIn('Wiki synced', output)
        self.assertEqual(self.git(self.root, 'log', '-1', '--format=%s').stdout.strip(), 'project change')
        self.assertEqual(self.git(self.root, 'rev-list', '--count', self.before + '..HEAD').stdout.strip(), '1')
        self.assertEqual(self.git(self.root, 'status', '--porcelain').stdout, '')
        self.assertEqual(self.git(self.wiki, 'status', '--porcelain').stdout, '')
        self.assertEqual(self.git(self.wiki, 'rev-parse', 'HEAD').stdout,
                         self.git(self.remote, 'rev-parse', 'HEAD').stdout)
        self.assertEqual(self.git(self.remote, 'show', 'HEAD:Guide.md').stdout,
                         '# Guide\n\n[Home](Home)\n')
        self.assertIn('[Guide](Guide)', self.git(self.remote, 'show', 'HEAD:_Sidebar.md').stdout)
        self.assertIn('Remote.md', self.git(self.remote, 'ls-tree', '--name-only', 'HEAD').stdout)

    def test_prepares_nested_pages_links_and_keeps_generator_state_private(self):
        with self.stub.open('a', encoding='utf-8') as script:
            script.write(
                "(wiki / 'architecture').mkdir(exist_ok=True)\n"
                "(wiki / 'architecture/overview.md').write_text('# Architecture\\n\\n[Start](../quickstart.md)\\n', encoding='utf-8')\n"
                "(wiki / 'quickstart.md').write_text('# Quickstart\\n\\n[Architecture](architecture/overview.md#flow)\\n[API `Widget`](architecture/overview.md#flow)\\n`[inline example](missing.md)`\\n[Source](../README.md)\\n\\n[details]: architecture/overview.md#flow\\n\\n```md\\n[example](missing.md)\\n```\\n', encoding='utf-8')\n"
                "(wiki / 'INSTRUCTIONS.md').write_text('private instructions', encoding='utf-8')\n"
                "(wiki / '.last-update.json').write_text('{}', encoding='utf-8')\n"
                "(wiki / '_plan.md').write_text('private plan', encoding='utf-8')\n"
            )
        self.install()
        output = self.commit()
        self.assertIn('Wiki synced', output.stdout + output.stderr)
        quickstart = self.git(self.remote, 'show', 'HEAD:quickstart.md').stdout
        self.assertIn('[Architecture](architecture-overview#flow)', quickstart)
        self.assertIn('[API `Widget`](architecture-overview#flow)', quickstart)
        self.assertIn('`[inline example](missing.md)`', quickstart)
        self.assertIn('[Source](https://github.com/test/project/blob/main/README.md)', quickstart)
        self.assertIn('[details]: architecture-overview#flow', quickstart)
        self.assertIn('[example](missing.md)', quickstart)
        files = self.git(self.remote, 'ls-tree', '-r', '--name-only', 'HEAD').stdout.splitlines()
        self.assertIn('architecture-overview.md', files)
        self.assertNotIn('architecture/overview.md', files)
        for name in ['INSTRUCTIONS.md', '.last-update.json', '_plan.md']:
            self.assertNotIn(name, files)
            self.assertTrue((self.wiki / name).exists())
        self.assertEqual(self.git(self.wiki, 'status', '--porcelain').stdout, '')
        # A second update may regenerate the original nested path. Keep its mapping stable.
        previous = self.git(self.remote, 'rev-parse', 'HEAD').stdout
        result = self.commit()
        self.assertIn('Wiki synced', result.stdout + result.stderr)
        self.assertEqual(self.git(self.remote, 'rev-parse', 'HEAD').stdout, previous)

    def test_does_not_run_wiki_hooks_or_inherit_project_index(self):
        marker = self.base / 'wiki-hook-ran'
        for name in ['post-commit', 'post-merge', 'pre-push']:
            hook = self.wiki / '.git/hooks' / name
            hook.write_text('#!/bin/sh\nprintf bad > "' + marker.as_posix() + '"\n', encoding='utf-8')
            hook.chmod(0o755)
        self.install()
        self.env['GIT_INDEX_FILE'] = str(self.root / '.git/index')
        result = self.commit()
        self.assertIn('Wiki synced', result.stdout + result.stderr)
        self.assertFalse(marker.exists(), 'Nested Wiki Git operations must not run hooks')
        self.env.pop('GIT_INDEX_FILE')
        self.assertEqual(self.git(self.root, 'status', '--porcelain').stdout, '')

    def test_keeps_project_instruction_changes_uncommitted_and_removes_new_ci(self):
        with self.stub.open('a', encoding='utf-8') as script:
            script.write(
                "(root / 'AGENTS.md').write_text('See openwiki/quickstart.md', encoding='utf-8')\n"
                "(root / '.github/workflows').mkdir(parents=True, exist_ok=True)\n"
                "(root / '.github/workflows/openwiki-update.yml').write_text('generated CI', encoding='utf-8')\n"
            )
        self.install()
        result = self.commit()
        self.assertIn('Wiki synced', result.stdout + result.stderr)
        self.assertFalse((self.root / '.github/workflows/openwiki-update.yml').exists())
        self.assertEqual(self.git(self.root, 'status', '--porcelain').stdout.strip(), '?? AGENTS.md')
        self.assertNotIn('AGENTS.md', self.git(self.root, 'ls-tree', '--name-only', 'HEAD').stdout)
        self.assertNotIn('AGENTS.md', self.git(self.remote, 'ls-tree', '--name-only', 'HEAD').stdout)
        self.assertIn('uncommitted', result.stdout + result.stderr)

    def test_unexpected_project_changes_stop_publication(self):
        with self.stub.open('a', encoding='utf-8') as script:
            script.write("(root / 'README.md').write_text('unexpected rewrite', encoding='utf-8')\n")
        self.install()
        before = self.git(self.remote, 'rev-parse', 'HEAD').stdout
        result = self.commit()
        self.assertIn('unexpected project changes', (result.stdout + result.stderr).lower())
        self.assertNotIn('Wiki synced', result.stdout + result.stderr)
        self.assertEqual(self.git(self.remote, 'rev-parse', 'HEAD').stdout, before)
        self.assertEqual((self.root / 'README.md').read_text(encoding='utf-8'), 'unexpected rewrite')
        self.assertEqual(self.git(self.root, 'log', '-1', '--format=%s').stdout.strip(), 'project change')

    def test_refuses_a_different_wiki_push_remote(self):
        self.git(self.wiki, 'config', 'remote.origin.pushurl', 'https://github.com/other/project.wiki.git')
        self.stub.write_text("raise SystemExit('must not generate')\n", encoding='utf-8')
        self.install()
        result = self.commit()
        self.assertIn('origin', result.stdout + result.stderr)
        self.assertNotIn('generation failed', result.stdout + result.stderr)

    def test_dirty_wiki_skips_without_losing_edits(self):
        (self.wiki / 'Home.md').write_text('local edit', encoding='utf-8')
        self.install()
        result = self.commit()
        self.assertIn('sync skipped', result.stdout + result.stderr)
        self.assertEqual((self.wiki / 'Home.md').read_text(encoding='utf-8'), 'local edit')
        self.assertFalse((self.wiki / 'Guide.md').exists())

    def test_dirty_project_skips(self):
        (self.root / 'README.md').write_text('unstaged edit', encoding='utf-8')
        self.install()
        result = self.commit()
        self.assertIn('sync skipped', result.stdout + result.stderr)
        self.assertFalse((self.wiki / 'Guide.md').exists())

    def test_generation_failure_leaves_project_commit_and_remote_unchanged(self):
        with self.stub.open('a', encoding='utf-8') as script:
            script.write("print('generator detail', file=sys.stderr)\nprint('Authorization: Bearer fake-secret-token', file=sys.stderr)\nraise SystemExit(7)\n")
        self.install()
        remote = self.git(self.remote, 'rev-parse', 'HEAD').stdout
        result = self.commit()
        self.assertIn('generation failed (exit 7)', result.stdout + result.stderr)
        log = (self.wiki / '.git/openwiki-sync.log').read_text(encoding='utf-8')
        self.assertIn('generator detail', log)
        self.assertNotIn('fake-secret-token', log)
        self.assertNotIn('fake-secret-token', result.stdout + result.stderr)
        self.assertIn('openwiki-sync.log', result.stdout + result.stderr)
        self.assertIn('existing-hook-ran', result.stdout + result.stderr)
        self.assertEqual(self.git(self.remote, 'rev-parse', 'HEAD').stdout, remote)
        self.assertEqual(self.git(self.root, 'log', '-1', '--format=%s').stdout.strip(), 'project change')
        self.assertTrue((self.wiki / 'Guide.md').exists(), 'Keep partial generated work for inspection')
        self.assertEqual(self.git(self.wiki, 'diff', '--cached', '--name-only').stdout, '')

    def test_divergent_wiki_stops_before_generation(self):
        (self.wiki / 'Local.md').write_text('# Local\n', encoding='utf-8')
        self.git(self.wiki, 'add', 'Local.md')
        self.git(self.wiki, 'commit', '-m', 'local divergence')
        self.install()
        result = self.commit()
        self.assertIn('Git pull failed', result.stdout + result.stderr)
        self.assertFalse((self.wiki / 'Guide.md').exists())

    def test_rejected_push_preserves_local_wiki_commit_for_retry(self):
        server_hook = self.remote / 'hooks/pre-receive'
        server_hook.write_text('#!/bin/sh\nexit 1\n', encoding='utf-8')
        server_hook.chmod(0o755)
        self.install()
        remote = self.git(self.remote, 'rev-parse', 'HEAD').stdout
        result = self.commit()
        self.assertIn('Git push failed', result.stdout + result.stderr)
        self.assertNotIn('Wiki synced', result.stdout + result.stderr)
        self.assertEqual(self.git(self.remote, 'rev-parse', 'HEAD').stdout, remote)
        local = self.git(self.wiki, 'rev-parse', 'HEAD').stdout
        self.assertNotEqual(local, remote)
        self.assertEqual(self.git(self.wiki, 'status', '--porcelain').stdout, '')
        server_hook.unlink()
        result = self.commit()
        self.assertIn('Wiki synced', result.stdout + result.stderr)
        self.assertEqual(self.git(self.remote, 'rev-parse', 'HEAD').stdout, local)

    def test_unresolved_links_stop_before_staging(self):
        with self.stub.open('a', encoding='utf-8') as script:
            script.write("(wiki / 'Bad.md').write_text('[missing](missing.md)', encoding='utf-8')\n")
        self.install()
        remote = self.git(self.remote, 'rev-parse', 'HEAD').stdout
        result = self.commit()
        self.assertIn('Unresolved local link', result.stdout + result.stderr)
        self.assertEqual(self.git(self.remote, 'rev-parse', 'HEAD').stdout, remote)
        self.assertEqual(self.git(self.wiki, 'diff', '--cached', '--name-only').stdout, '')

    def test_existing_sync_lock_prevents_overlapping_generation(self):
        (self.wiki / '.git/openwiki-sync.lock').mkdir()
        self.install()
        result = self.commit()
        self.assertIn('already running', result.stdout + result.stderr)
        self.assertFalse((self.wiki / 'Guide.md').exists())
        self.assertTrue((self.wiki / '.git/openwiki-sync.lock').exists())

    def test_generator_staged_nonpage_is_never_published(self):
        with self.stub.open('a', encoding='utf-8') as script:
            script.write(
                "import subprocess\n"
                "(wiki / 'secret.txt').write_text('not a Wiki page', encoding='utf-8')\n"
                "subprocess.run(['git', '-C', str(wiki), 'add', 'secret.txt'], check=True, creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0))\n"
            )
        self.install()
        remote = self.git(self.remote, 'rev-parse', 'HEAD').stdout
        result = self.commit()
        self.assertIn('Unexpected Wiki changes', result.stdout + result.stderr)
        self.assertEqual(self.git(self.remote, 'rev-parse', 'HEAD').stdout, remote)
        self.assertTrue((self.wiki / 'secret.txt').exists())

    def test_project_commit_advancing_during_generation_stops_publication(self):
        with self.stub.open('a', encoding='utf-8') as script:
            script.write(
                "import subprocess\n"
                "subprocess.run(['git', '-c', 'core.hooksPath=', 'commit', '--allow-empty', '-m', 'concurrent change'], check=True, creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0))\n"
            )
        self.install()
        remote = self.git(self.remote, 'rev-parse', 'HEAD').stdout
        result = self.commit()
        self.assertIn('HEAD changed', result.stdout + result.stderr)
        self.assertEqual(self.git(self.remote, 'rev-parse', 'HEAD').stdout, remote)

    def test_does_not_push_unrelated_local_wiki_history(self):
        self.git(self.wiki, 'pull', '--ff-only', 'origin', 'published')
        (self.wiki / 'private.txt').write_text('private local commit', encoding='utf-8')
        self.git(self.wiki, 'add', 'private.txt')
        self.git(self.wiki, 'commit', '-m', 'private local work')
        self.install()
        remote = self.git(self.remote, 'rev-parse', 'HEAD').stdout
        result = self.commit()
        self.assertIn('unpublished Wiki commits', result.stdout + result.stderr)
        self.assertEqual(self.git(self.remote, 'rev-parse', 'HEAD').stdout, remote)
        self.assertFalse((self.wiki / 'Guide.md').exists())

    def test_remote_configuration_changes_during_generation_stop_publication(self):
        with self.stub.open('a', encoding='utf-8') as script:
            script.write(
                "import subprocess\n"
                "subprocess.run(['git', '-C', str(wiki), 'config', 'remote.origin.pushurl', " + repr(str(self.remote)) + "], check=True, creationflags=getattr(subprocess, 'CREATE_NO_WINDOW', 0))\n"
            )
        self.install()
        remote = self.git(self.remote, 'rev-parse', 'HEAD').stdout
        result = self.commit()
        self.assertIn('Wiki configuration or branch changed', result.stdout + result.stderr)
        self.assertEqual(self.git(self.remote, 'rev-parse', 'HEAD').stdout, remote)

    def test_generation_timeout_stops_the_process_tree(self):
        marker = self.base / 'orphan-wrote'
        self.stub.write_text(
            'import subprocess, sys, time\n'
            'subprocess.Popen([sys.executable, "-c", ' + repr("import time; from pathlib import Path; time.sleep(3); Path(" + repr(str(marker)) + ").write_text('orphan')") + '], creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))\n'
            'time.sleep(60)\n', encoding='utf-8',
        )
        # Commit installation before invoking the public retry CLI with a short timeout.
        self.install()
        self.git(self.root, '-c', 'core.hooksPath=', 'commit', '-m', 'install hook')
        result = subprocess.run(
            [sys.executable, str(self.root / '.githooks/openwiki_post_commit.py'),
             '--root', str(self.root), '--generation-timeout', '1'],
            env=self.env, capture_output=True, text=True, timeout=15, creationflags=NO_WINDOW,
        )
        self.assertEqual(result.returncode, 1)
        self.assertIn('generation timed out', result.stderr)
        import time
        time.sleep(3)
        self.assertFalse(marker.exists(), 'The generator child must not survive the timeout')
        self.assertFalse((self.wiki / '.git/openwiki-sync.lock').exists())


if __name__ == '__main__':
    unittest.main()
