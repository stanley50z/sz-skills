import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

import setup
import update


REPO_ROOT = Path(__file__).resolve().parents[1]
RETIRED_DESIGN_SKILLS = [
    "banner-design", "brand", "design", "design-system", "frontend-skill",
    "revealjs", "slides", "ui-styling", "ui-ux-pro-max",
]


class DesignSkillMigrationTests(unittest.TestCase):
    def test_setup_removes_old_design_skills_and_keeps_unrelated_skills(self):
        with tempfile.TemporaryDirectory() as home_tmp:
            roots = [Path(home_tmp) / name for name in ("claude", "codex", "opencode", "agents")]
            for root in roots:
                for name in [*RETIRED_DESIGN_SKILLS, "frontend-design", "codebase-design"]:
                    skill = root / name
                    skill.mkdir(parents=True)
                    (skill / "SKILL.md").write_text(f"name: {name}\n", encoding="utf-8")

            with redirect_stdout(StringIO()):
                removed = setup.remove_retired_skills(target_roots=roots, mirror_target_roots={})

            self.assertEqual(removed, len(roots) * len(RETIRED_DESIGN_SKILLS))
            for root in roots:
                for name in RETIRED_DESIGN_SKILLS:
                    self.assertFalse((root / name).exists())
                for name in ("frontend-design", "codebase-design"):
                    self.assertTrue((root / name / "SKILL.md").is_file())

    def test_catalog_and_updater_use_anthropic_frontend_design(self):
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        self.assertEqual(update.UPSTREAM.get("frontend-design"), [
            {"repo": "anthropics/skills", "path": "skills/frontend-design"},
        ])
        self.assertNotIn("frontend-design", update.PATCHED)
        skill_dir = REPO_ROOT / "skills" / "frontend-design"
        self.assertIn("name: frontend-design", (skill_dir / "SKILL.md").read_text(encoding="utf-8"))
        self.assertTrue((skill_dir / "LICENSE.txt").is_file())
        self.assertIn("[frontend-design](skills/frontend-design/)", readme)
        for name in RETIRED_DESIGN_SKILLS:
            with self.subTest(skill=name):
                self.assertFalse((REPO_ROOT / "skills" / name).exists())
                self.assertNotIn(name, update.UPSTREAM)
                self.assertNotIn(name, update.PATCHED)
                self.assertNotIn(f"](skills/{name}/)", readme)

    def test_ui_testing_guidance_no_longer_requires_mobile_viewports(self):
        for relative in ("skills/tdd/SKILL.md", "skills/tdd/visual-tests.md"):
            with self.subTest(file=relative):
                source = (REPO_ROOT / relative).read_text(encoding="utf-8").lower()
                self.assertNotRegex(source, r"\b(mobile|tablet|phone)\b")
                self.assertNotIn("responsive viewports", source)
                self.assertIn("desktop", source)
                self.assertIn("walkthrough", source)


if __name__ == "__main__":
    unittest.main()
