import subprocess
import tempfile
import unittest
from pathlib import Path

import setup


REPO_ROOT = Path(__file__).resolve().parents[1]


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

    def test_post_merge_hook_runs_setup_script(self):
        with tempfile.TemporaryDirectory() as repo_tmp:
            repo_root = Path(repo_tmp)
            subprocess.run(["git", "init", str(repo_root)], check=True, capture_output=True)
            subprocess.run(
                ["git", "-C", str(repo_root), "config", "user.name", "Test User"],
                check=True,
            )
            subprocess.run(
                ["git", "-C", str(repo_root), "config", "user.email", "test@example.com"],
                check=True,
            )

            hooks_dir = repo_root / "githooks"
            hooks_dir.mkdir()
            (hooks_dir / "post-merge").write_text(
                (REPO_ROOT / "githooks" / "post-merge").read_text(encoding="utf-8"),
                encoding="utf-8",
            )
            (repo_root / "setup.py").write_text(
                "from pathlib import Path\nPath('setup-ran').write_text('yes', encoding='utf-8')\n",
                encoding="utf-8",
            )
            (repo_root / "tracked.txt").write_text("main\n", encoding="utf-8")
            subprocess.run(
                ["git", "-C", str(repo_root), "add", "setup.py", "tracked.txt"],
                check=True,
            )
            subprocess.run(
                ["git", "-C", str(repo_root), "commit", "-m", "initial"],
                check=True,
                capture_output=True,
            )
            main_branch = subprocess.run(
                ["git", "-C", str(repo_root), "branch", "--show-current"],
                check=True,
                capture_output=True,
                text=True,
            ).stdout.strip()
            subprocess.run(
                ["git", "-C", str(repo_root), "checkout", "-b", "hook-test"],
                check=True,
                capture_output=True,
            )
            (repo_root / "tracked.txt").write_text("hook test\n", encoding="utf-8")
            subprocess.run(
                ["git", "-C", str(repo_root), "add", "tracked.txt"],
                check=True,
            )
            subprocess.run(
                ["git", "-C", str(repo_root), "commit", "-m", "hook test"],
                check=True,
                capture_output=True,
            )
            subprocess.run(
                ["git", "-C", str(repo_root), "checkout", main_branch],
                check=True,
                capture_output=True,
            )

            self.assertTrue(setup.install_git_hooks(repo_root=repo_root))
            merge_result = subprocess.run(
                ["git", "-C", str(repo_root), "merge", "hook-test"],
                check=True,
                capture_output=True,
                text=True,
            )

            self.assertTrue(
                (repo_root / "setup-ran").is_file(),
                merge_result.stdout + merge_result.stderr,
            )
            self.assertEqual(
                (repo_root / "setup-ran").read_text(encoding="utf-8"),
                "yes",
            )


if __name__ == "__main__":
    unittest.main()
