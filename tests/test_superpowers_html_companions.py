import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
BRAINSTORMING = REPO_ROOT / "skills" / "brainstorming" / "SKILL.md"
TO_TICKETS = REPO_ROOT / "skills" / "to-tickets" / "SKILL.md"
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

    def test_to_tickets_identifies_html_plan_companion_uses(self):
        source = TO_TICKETS.read_text(encoding="utf-8")

        self.assertIn("HTML Plan Companion", source)
        self.assertIn("Markdown ticket files remain the source of truth", source)
        expected_uses = [
            "ticket dependency maps",
            "file-change maps",
            "requirement-to-ticket traceability",
            "plan overview dashboards",
            "docs/plans/<artifact-id>/plan.html",
        ]
        for use in expected_uses:
            with self.subTest(use=use):
                self.assertIn(use, source)

    def test_customization_rationale_documents_html_companions(self):
        source = RATIONALE.read_text(encoding="utf-8")

        self.assertIn("Structured HTML Companions", source)
        self.assertIn("brainstorming", source)
        self.assertIn("to-tickets", source)


class ExecutionHalfMigrationTests(unittest.TestCase):
    RETIRED = [
        "writing-plans",
        "executing-plans",
        "subagent-driven-development",
        "requesting-code-review",
        "receiving-code-review",
        "verification-before-completion",
    ]

    def test_retired_execution_skills_are_gone_from_repo(self):
        for skill in self.RETIRED:
            with self.subTest(skill=skill):
                self.assertFalse((REPO_ROOT / "skills" / skill).exists())

    def test_retired_execution_skills_are_listed_for_removal(self):
        import setup

        for skill in self.RETIRED:
            with self.subTest(skill=skill):
                self.assertIn(skill, setup.RETIRED_SKILLS)

    def test_replacement_skills_are_patched_vendor_skills(self):
        import update

        for skill in ("to-tickets", "implement"):
            with self.subTest(skill=skill):
                self.assertTrue((REPO_ROOT / "skills" / skill / "SKILL.md").exists())
                self.assertIn(skill, update.UPSTREAM)
                self.assertIn(skill, update.PATCHED)

    def test_brainstorming_hands_off_to_to_tickets(self):
        source = BRAINSTORMING.read_text(encoding="utf-8")

        self.assertIn("to-tickets", source)
        self.assertNotIn("writing-plans", source)


if __name__ == "__main__":
    unittest.main()
