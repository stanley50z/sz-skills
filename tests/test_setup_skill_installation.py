import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

import setup


class SkillInstallationTests(unittest.TestCase):
    def test_copies_codex_root_and_mirrors_agents_root_to_that_copy(self):
        with tempfile.TemporaryDirectory() as repo_tmp, tempfile.TemporaryDirectory() as home_tmp:
            skills_dir = Path(repo_tmp) / "skills"
            skill_dir = skills_dir / "alpha"
            skill_dir.mkdir(parents=True)
            (skill_dir / "SKILL.md").write_text("# alpha\n", encoding="utf-8")
            (skill_dir / "reference.txt").write_text("copied too\n", encoding="utf-8")

            claude_root = Path(home_tmp) / ".claude" / "skills"
            codex_root = Path(home_tmp) / ".codex" / "skills"
            agents_root = Path(home_tmp) / ".agents" / "skills"

            with redirect_stdout(StringIO()):
                installed = setup.install_skills(
                    ["alpha"],
                    skills_dir=skills_dir,
                    target_roots=[claude_root, codex_root, agents_root],
                    copy_target_roots=[codex_root],
                    mirror_target_roots={agents_root: codex_root},
                )

            self.assertEqual(installed, 3)
            self.assertTrue(setup._is_link_or_junction(claude_root / "alpha"))

            copied_skill = codex_root / "alpha"
            self.assertFalse(setup._is_link_or_junction(copied_skill))
            self.assertEqual((copied_skill / "SKILL.md").read_text(encoding="utf-8"), "# alpha\n")
            self.assertEqual((copied_skill / "reference.txt").read_text(encoding="utf-8"), "copied too\n")

            mirrored_skill = agents_root / "alpha"
            self.assertTrue(setup._is_link_or_junction(mirrored_skill))
            self.assertEqual(mirrored_skill.resolve(), copied_skill.resolve())
            self.assertEqual((mirrored_skill / "SKILL.md").read_text(encoding="utf-8"), "# alpha\n")

    def test_removes_retired_repo_managed_skills_from_target_roots(self):
        with tempfile.TemporaryDirectory() as home_tmp:
            target_roots = [
                Path(home_tmp) / ".claude" / "skills",
                Path(home_tmp) / ".codex" / "skills",
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
                removed = setup.remove_retired_skills(
                    ["old-skill"],
                    target_roots=target_roots,
                    mirror_target_roots={target_roots[2]: target_roots[1]},
                )

            self.assertEqual(removed, 3)
            for root in target_roots:
                self.assertFalse((root / "old-skill").exists())
            self.assertTrue(unrelated.exists())


if __name__ == "__main__":
    unittest.main()
