import subprocess
import tempfile
import unittest
from pathlib import Path

import setup


class GitHooksInstallTests(unittest.TestCase):
    def test_sets_core_hookspath_to_githooks_dir(self):
        with tempfile.TemporaryDirectory() as repo_tmp:
            repo_root = Path(repo_tmp)
            subprocess.run(["git", "init", str(repo_root)], check=True, capture_output=True)
            hooks_dir = repo_root / "githooks"
            hooks_dir.mkdir()
            (hooks_dir / "post-commit").write_text("#!/bin/sh\n", encoding="utf-8")

            self.assertTrue(setup.install_git_hooks(repo_root=repo_root))

            configured = subprocess.run(
                ["git", "-C", str(repo_root), "config", "core.hooksPath"],
                check=True,
                capture_output=True,
                text=True,
            ).stdout.strip()
            self.assertEqual(configured, "githooks")

    def test_skips_when_not_a_git_repo(self):
        with tempfile.TemporaryDirectory() as repo_tmp:
            repo_root = Path(repo_tmp)
            (repo_root / "githooks").mkdir()

            self.assertFalse(setup.install_git_hooks(repo_root=repo_root))

    def test_skips_when_githooks_dir_missing(self):
        with tempfile.TemporaryDirectory() as repo_tmp:
            repo_root = Path(repo_tmp)
            subprocess.run(["git", "init", str(repo_root)], check=True, capture_output=True)

            self.assertFalse(setup.install_git_hooks(repo_root=repo_root))


if __name__ == "__main__":
    unittest.main()
