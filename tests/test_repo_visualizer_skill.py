import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL = REPO_ROOT / "skills" / "repo-visualizer" / "SKILL.md"


class RepoVisualizerSkillTests(unittest.TestCase):
    def test_default_output_lives_under_docs(self):
        source = SKILL.read_text(encoding="utf-8")

        self.assertIn("`docs/repo_structure.htmnel`", source)
        self.assertIn("creating `docs/` if needed", source)
        self.assertNotIn("`doc/repo_structure.htmnel`", source)
        self.assertNotIn("creating `doc/` if needed", source)


if __name__ == "__main__":
    unittest.main()
