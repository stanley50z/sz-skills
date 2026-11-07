import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

import setup


class SkillInstallationTests(unittest.TestCase):
    def test_links_claude_root_and_copies_agents_root(self):
        with tempfile.TemporaryDirectory() as repo_tmp, tempfile.TemporaryDirectory() as home_tmp:
            skills_dir = Path(repo_tmp) / "skills"
            skill_dir = skills_dir / "alpha"
            skill_dir.mkdir(parents=True)
            (skill_dir / "SKILL.md").write_text("# alpha\n", encoding="utf-8")
            (skill_dir / "reference.txt").write_text("copied too\n", encoding="utf-8")

            claude_root = Path(home_tmp) / ".claude" / "skills"
            agents_root = Path(home_tmp) / ".agents" / "skills"

            with redirect_stdout(StringIO()):
                installed = setup.install_skills(
                    ["alpha"],
                    skills_dir=skills_dir,
                    target_roots=[claude_root, agents_root],
                    copy_target_roots=[agents_root],
                )

            self.assertEqual(installed, 2)
            self.assertTrue(setup._is_link_or_junction(claude_root / "alpha"))

            copied_skill = agents_root / "alpha"
            self.assertFalse(setup._is_link_or_junction(copied_skill))
            self.assertEqual((copied_skill / "SKILL.md").read_text(encoding="utf-8"), "# alpha\n")
            self.assertEqual((copied_skill / "reference.txt").read_text(encoding="utf-8"), "copied too\n")

    def test_moves_old_codex_mirror_into_agents_copy_and_cleans_former_roots(self):
        with tempfile.TemporaryDirectory() as repo_tmp, tempfile.TemporaryDirectory() as home_tmp:
            skills_dir = Path(repo_tmp) / "skills"
            (skills_dir / "alpha").mkdir(parents=True)
            (skills_dir / "alpha" / "SKILL.md").write_text("# alpha\n", encoding="utf-8")

            home = Path(home_tmp)
            agents_root = home / ".agents" / "skills"
            codex_root = home / ".codex" / "skills"
            opencode_root = home / ".config" / "opencode" / "skills"
            for root in (agents_root, codex_root, opencode_root):
                root.mkdir(parents=True)

            # Layout left by the old setup.py: a Codex copy, an Agents link to it,
            # an Opencode link into the repo, and a retired skill.
            (codex_root / "alpha").mkdir()
            (codex_root / "alpha" / "SKILL.md").write_text("# old\n", encoding="utf-8")
            setup.make_link(codex_root / "alpha", agents_root / "alpha")
            setup.make_link(skills_dir / "alpha", opencode_root / "alpha")
            (codex_root / "ketch").mkdir()
            (codex_root / "unrelated").mkdir()

            with redirect_stdout(StringIO()):
                setup.install_skills(
                    ["alpha"],
                    skills_dir=skills_dir,
                    target_roots=[agents_root],
                    copy_target_roots=[agents_root],
                )
                removed = setup.remove_from_former_roots(
                    ["alpha"], former_roots=[codex_root, opencode_root]
                )

            self.assertEqual(removed, 3)
            self.assertFalse(setup._is_link_or_junction(agents_root / "alpha"))
            self.assertEqual((agents_root / "alpha" / "SKILL.md").read_text(encoding="utf-8"), "# alpha\n")
            self.assertFalse((codex_root / "alpha").exists())
            self.assertFalse((codex_root / "ketch").exists())
            self.assertFalse(setup._is_link_or_junction(opencode_root / "alpha"))
            self.assertTrue((skills_dir / "alpha" / "SKILL.md").exists())
            self.assertTrue((codex_root / "unrelated").exists())

    def test_ketch_is_retired_from_general_harness_roots(self):
        with tempfile.TemporaryDirectory() as home_tmp:
            target_roots = [
                Path(home_tmp) / ".claude" / "skills",
                Path(home_tmp) / ".agents" / "skills",
            ]
            for root in target_roots:
                stale = root / "ketch"
                stale.mkdir(parents=True)
                (stale / "SKILL.md").write_text("# ketch\n", encoding="utf-8")

            with redirect_stdout(StringIO()):
                removed = setup.remove_retired_skills(target_roots=target_roots)

            self.assertEqual(removed, 2)
            for root in target_roots:
                self.assertFalse((root / "ketch").exists())

    def test_removes_retired_repo_managed_skills_from_target_roots(self):
        with tempfile.TemporaryDirectory() as home_tmp:
            target_roots = [
                Path(home_tmp) / ".claude" / "skills",
                Path(home_tmp) / ".agents" / "skills",
            ]
            for root in target_roots:
                stale = root / "old-skill"
                stale.mkdir(parents=True)
                (stale / "SKILL.md").write_text("# old visualizer\n", encoding="utf-8")

            unrelated = target_roots[0] / "unrelated"
            unrelated.mkdir()
            (unrelated / "SKILL.md").write_text("# keep me\n", encoding="utf-8")

            with redirect_stdout(StringIO()):
                removed = setup.remove_retired_skills(["old-skill"], target_roots=target_roots)

            self.assertEqual(removed, 2)
            for root in target_roots:
                self.assertFalse((root / "old-skill").exists())
            self.assertTrue(unrelated.exists())


if __name__ == "__main__":
    unittest.main()
