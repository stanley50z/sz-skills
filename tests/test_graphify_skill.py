import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL = REPO_ROOT / "skills" / "graphify" / "SKILL.md"
README = REPO_ROOT / "README.md"
UPDATE_PY = REPO_ROOT / "update.py"


class GraphifySkillTests(unittest.TestCase):
    def test_graphify_wrapper_skill_is_personal_and_cli_focused(self):
        source = SKILL.read_text(encoding="utf-8")

        self.assertIn("name: graphify", source)
        self.assertIn("Use when", source)
        self.assertIn("graphifyy", source)
        self.assertIn("graphify .", source)
        self.assertIn("graphify query", source)
        self.assertIn("graphify export callflow-html", source)
        self.assertIn("docs/repo_structure.html", source)
        self.assertIn("graphify install --platform claude", source)
        self.assertIn("graphify claude install", source)
        self.assertIn("graphify hook install", source)
        self.assertNotIn("spawn_agent", source)
        self.assertNotIn("wait_agent", source)

    def test_repo_visualizer_is_no_longer_cataloged_or_installed(self):
        readme = README.read_text(encoding="utf-8")

        self.assertIn("[graphify](skills/graphify/)", readme)
        self.assertNotIn("[repo-visualizer](skills/repo-visualizer/)", readme)
        self.assertFalse((REPO_ROOT / "skills" / "repo-visualizer" / "SKILL.md").exists())

    def test_graphify_wrapper_is_not_vendor_updated(self):
        update_py = UPDATE_PY.read_text(encoding="utf-8")

        self.assertNotIn('"graphify"', update_py)
        self.assertNotIn("safishamsi/graphify", update_py)


if __name__ == "__main__":
    unittest.main()
