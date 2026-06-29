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
        self.assertIn("graphify install --platform claude", source)
        self.assertIn("graphify claude install", source)
        self.assertIn("graphify hook install", source)
        self.assertNotIn("repo_structure", source)
        self.assertNotIn("repo visualizer", source.lower())
        self.assertNotIn("spawn_agent", source)
        self.assertNotIn("wait_agent", source)

    def test_init_graphify_means_install_git_hooks(self):
        source = SKILL.read_text(encoding="utf-8")

        self.assertIn("init graphify", source.lower())
        self.assertIn("graphify hook install", source)
        self.assertIn("git hooks", source.lower())

    def test_existing_graph_routes_codebase_questions_to_graphify_first(self):
        source = SKILL.read_text(encoding="utf-8")
        lower = source.lower()

        self.assertIn("any question about a codebase", lower)
        self.assertIn("architecture", lower)
        self.assertIn("file relationship", lower)
        self.assertIn("dependency", lower)
        self.assertIn("data-flow", lower)
        self.assertIn("project content", lower)
        self.assertIn("graphify-out/graph.json exists", lower)
        self.assertIn("first run `graphify query", lower)
        self.assertIn("before broad `rg`, `grep`, or multi-file reads", lower)
        self.assertIn("graphify path", source)
        self.assertIn("graphify explain", source)
        self.assertIn("stale or incorrect graph output", lower)

    def test_repo_visualizer_is_cataloged_as_separate_human_report_skill(self):
        readme = README.read_text(encoding="utf-8")
        repo_visualizer = REPO_ROOT / "skills" / "repo-visualizer" / "SKILL.md"
        repo_visualizer_source = repo_visualizer.read_text(encoding="utf-8")

        self.assertIn("[graphify](skills/graphify/)", readme)
        self.assertIn("[repo-visualizer](skills/repo-visualizer/)", readme)
        self.assertIn("name: repo-visualizer", repo_visualizer_source)
        self.assertIn("docs/repo_structure.html", repo_visualizer_source)
        self.assertNotIn("docs/repo_structure.htmnel", repo_visualizer_source)
        self.assertIn("human-readable", repo_visualizer_source)
        self.assertIn("purpose", repo_visualizer_source)
        self.assertIn("inputs", repo_visualizer_source)
        self.assertIn("outputs", repo_visualizer_source)

    def test_repo_visualizer_is_not_retired_from_install_targets(self):
        setup_py = (REPO_ROOT / "setup.py").read_text(encoding="utf-8")

        self.assertNotIn('"repo-visualizer"', setup_py)
        self.assertNotIn("'repo-visualizer'", setup_py)

    def test_graphify_wrapper_is_not_vendor_updated(self):
        update_py = UPDATE_PY.read_text(encoding="utf-8")

        self.assertNotIn('"graphify"', update_py)
        self.assertNotIn("safishamsi/graphify", update_py)


if __name__ == "__main__":
    unittest.main()
