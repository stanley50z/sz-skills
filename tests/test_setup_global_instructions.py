import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch

import setup


class GlobalInstructionInstallTests(unittest.TestCase):
    def test_default_agents_file_targets_every_supported_harness(self):
        agents_targets = {
            target.relative_to(setup.HOME).as_posix()
            for source, target in setup.GLOBAL_INSTRUCTION_LINKS
            if source.name == "AGENTS.md"
        }

        self.assertEqual(
            agents_targets,
            {
                ".codex/AGENTS.md",
                ".pi/agent/AGENTS.md",
                ".config/opencode/AGENTS.md",
            },
        )

    def test_explicit_github_username_takes_precedence(self):
        with patch.dict("os.environ", {"SZ_GITHUB_USERNAME": "environment-user"}):
            with patch.object(setup.subprocess, "run") as run:
                username = setup.resolve_github_username("explicit-user")

        self.assertEqual(username, "explicit-user")
        run.assert_not_called()

    def test_github_username_comes_from_environment_when_not_explicit(self):
        with patch.dict("os.environ", {"SZ_GITHUB_USERNAME": "environment-user"}):
            with patch.object(setup.subprocess, "run") as run:
                username = setup.resolve_github_username()

        self.assertEqual(username, "environment-user")
        run.assert_not_called()

    def test_github_username_comes_from_authenticated_gh_cli(self):
        completed = setup.subprocess.CompletedProcess(
            args=["gh", "api", "user", "--jq", ".login"],
            returncode=0,
            stdout="cli-user\n",
        )
        with patch.dict("os.environ", {}, clear=True):
            with patch.object(setup.subprocess, "run", return_value=completed) as run:
                username = setup.resolve_github_username()

        self.assertEqual(username, "cli-user")
        run.assert_called_once_with(
            ["gh", "api", "user", "--jq", ".login"],
            capture_output=True,
            check=True,
            text=True,
        )

    def test_missing_gh_cli_leaves_github_username_unresolved(self):
        with patch.dict("os.environ", {}, clear=True):
            with patch.object(setup.subprocess, "run", side_effect=FileNotFoundError):
                username = setup.resolve_github_username()

        self.assertIsNone(username)

    def test_renders_github_identity_into_installed_agents_file(self):
        with tempfile.TemporaryDirectory() as repo_tmp, tempfile.TemporaryDirectory() as home_tmp:
            source_root = Path(repo_tmp) / "global"
            target_root = Path(home_tmp)
            source_root.mkdir()

            agents_source = source_root / "AGENTS.md"
            claude_source = source_root / "CLAUDE.md"
            agents_source.write_text("agents v1\n", encoding="utf-8")
            claude_source.write_text("@~/.codex/AGENTS.md\n", encoding="utf-8")

            links = [
                (agents_source, target_root / ".codex" / "AGENTS.md"),
                (agents_source, target_root / ".pi" / "agent" / "AGENTS.md"),
                (agents_source, target_root / ".config" / "opencode" / "AGENTS.md"),
                (claude_source, target_root / ".claude" / "CLAUDE.md"),
            ]

            with redirect_stdout(StringIO()):
                installed = setup.install_global_instructions(
                    links,
                    github_username="octocat",
                )

            self.assertEqual(installed, 4)
            expected_agents = "## User Identity\n\n- GitHub username: `octocat`.\n\nagents v1\n"
            for target in (
                target_root / ".codex" / "AGENTS.md",
                target_root / ".pi" / "agent" / "AGENTS.md",
                target_root / ".config" / "opencode" / "AGENTS.md",
            ):
                self.assertEqual(target.read_text(encoding="utf-8"), expected_agents)
            self.assertEqual((target_root / ".claude" / "CLAUDE.md").read_text(encoding="utf-8"), "@~/.codex/AGENTS.md\n")

            agents_source.write_text("agents v2\n", encoding="utf-8")

            for target in (
                target_root / ".codex" / "AGENTS.md",
                target_root / ".pi" / "agent" / "AGENTS.md",
                target_root / ".config" / "opencode" / "AGENTS.md",
            ):
                self.assertEqual(target.read_text(encoding="utf-8"), expected_agents)

    def test_installs_generic_agents_file_when_identity_is_unresolved(self):
        with tempfile.TemporaryDirectory() as repo_tmp, tempfile.TemporaryDirectory() as home_tmp:
            source = Path(repo_tmp) / "AGENTS.md"
            target = Path(home_tmp) / ".codex" / "AGENTS.md"
            source.write_text("generic instructions\n", encoding="utf-8")

            with redirect_stdout(StringIO()):
                installed = setup.install_global_instructions(
                    [(source, target)],
                    github_username=None,
                )

            self.assertEqual(installed, 1)
            self.assertEqual(target.read_text(encoding="utf-8"), "generic instructions\n")

            source.write_text("changed source\n", encoding="utf-8")

            self.assertEqual(target.read_text(encoding="utf-8"), "generic instructions\n")

    def test_setup_cli_passes_explicit_github_username_to_global_install(self):
        with (
            patch.object(setup, "discover_skills", return_value=["alpha"]),
            patch.object(setup, "remove_retired_skills"),
            patch.object(setup, "install_skills"),
            patch.object(setup, "install_global_instructions", return_value=2) as install_globals,
            patch.object(setup, "sync_codex_hook_plugin_hooks", return_value=0),
            patch.object(setup, "install_plugin_hooks"),
            patch.object(setup, "install_git_hooks", return_value=False),
            redirect_stdout(StringIO()),
        ):
            setup.main(["--github-username", "explicit-user"])

        install_globals.assert_called_once_with(github_username="explicit-user")


if __name__ == "__main__":
    unittest.main()
