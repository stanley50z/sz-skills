import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
BRAINSTORMING = REPO_ROOT / "skills" / "brainstorming" / "SKILL.md"
WRITING_PLANS = REPO_ROOT / "skills" / "writing-plans" / "SKILL.md"
RATIONALE = REPO_ROOT / "docs" / "superpowers-customization-rationale.md"


class SuperpowersHtmlCompanionGuidanceTests(unittest.TestCase):
    def test_brainstorming_identifies_structured_html_companion_uses(self):
        source = BRAINSTORMING.read_text(encoding="utf-8")

        self.assertIn("Structured HTML Companion", source)
        self.assertIn("HTML companion is a review aid, not the canonical spec", source)
        expected_uses = [
            "option comparison cards",
            "decision matrices",
            "architecture sketches",
            "requirement grouping",
            "Approach Comparison",
            "Risks / Tradeoffs",
        ]
        for use in expected_uses:
            with self.subTest(use=use):
                self.assertIn(use, source)

    def test_writing_plans_identifies_html_plan_companion_uses(self):
        source = WRITING_PLANS.read_text(encoding="utf-8")

        self.assertIn("HTML Plan Companion", source)
        self.assertIn("Markdown implementation plan remains the source of truth", source)
        expected_uses = [
            "task dependency maps",
            "file-change maps",
            "requirement-to-task traceability",
            "plan overview dashboards",
            "same basename with `.html`",
        ]
        for use in expected_uses:
            with self.subTest(use=use):
                self.assertIn(use, source)

    def test_customization_rationale_documents_html_companions(self):
        source = RATIONALE.read_text(encoding="utf-8")

        self.assertIn("Structured HTML Companions", source)
        self.assertIn("brainstorming", source)
        self.assertIn("writing-plans", source)


if __name__ == "__main__":
    unittest.main()
