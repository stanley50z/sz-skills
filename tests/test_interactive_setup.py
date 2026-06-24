import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch

import interactive_setup


class ParseSelectionTests(unittest.TestCase):
    def test_accepts_numbers_ranges_all_and_duplicates(self):
        skills = ["alpha", "beta", "gamma", "delta"]

        selected = interactive_setup.parse_selection("2, 1-3, all, 2", skills)

        self.assertEqual(selected, skills)

    def test_rejects_out_of_range_selection(self):
        with self.assertRaises(ValueError) as ctx:
            interactive_setup.parse_selection("3", ["alpha", "beta"])

        self.assertIn("out of range", str(ctx.exception))


class InstallSelectionTests(unittest.TestCase):
    def test_installs_only_selected_skills_into_each_target_root(self):
        with tempfile.TemporaryDirectory() as repo_tmp, tempfile.TemporaryDirectory() as home_tmp:
            repo_root = Path(repo_tmp)
            skills_dir = repo_root / "skills"
            for skill in ("alpha", "beta", "gamma"):
                skill_dir = skills_dir / skill
                skill_dir.mkdir(parents=True)
                (skill_dir / "SKILL.md").write_text(f"# {skill}\n", encoding="utf-8")

            target_roots = [
                Path(home_tmp) / ".claude" / "skills",
                Path(home_tmp) / ".codex" / "skills",
                Path(home_tmp) / ".config" / "opencode" / "skills",
            ]

            with redirect_stdout(StringIO()):
                installed = interactive_setup.install_selected_skills(
                    ["beta"],
                    skills_dir=skills_dir,
                    target_roots=target_roots,
                )

            self.assertEqual(installed, 3)
            for root in target_roots:
                self.assertTrue((root / "beta").exists())
                self.assertFalse((root / "alpha").exists())
                self.assertFalse((root / "gamma").exists())

    def test_main_installs_global_instruction_links(self):
        target_roots = [
            Path("home") / ".claude" / "skills",
            Path("home") / ".codex" / "skills",
        ]
        global_links = [
            (Path("repo") / "global" / "AGENTS.md", Path("home") / ".codex" / "AGENTS.md"),
            (Path("repo") / "global" / "CLAUDE.md", Path("home") / ".claude" / "CLAUDE.md"),
        ]

        with (
            patch.object(interactive_setup, "discover_skills", return_value=["alpha"]),
            patch.object(interactive_setup, "prompt_for_skills", return_value=["alpha"]),
            patch.object(interactive_setup, "install_selected_skills", return_value=2),
            patch.object(interactive_setup, "install_global_instructions", return_value=2) as install_globals,
            patch.object(interactive_setup, "TARGET_ROOTS", target_roots),
            patch.object(interactive_setup, "GLOBAL_INSTRUCTION_LINKS", global_links),
            redirect_stdout(StringIO()),
        ):
            result = interactive_setup.main()

        self.assertEqual(result, 0)
        install_globals.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()
