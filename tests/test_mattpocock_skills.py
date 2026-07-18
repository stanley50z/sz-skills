import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
TO_SPEC = REPO_ROOT / "skills" / "to-spec" / "SKILL.md"
TO_TICKETS = REPO_ROOT / "skills" / "to-tickets" / "SKILL.md"
RATIONALE = REPO_ROOT / "docs" / "mattpocock-customization-rationale.md"


class HtmlCompanionGuidanceTests(unittest.TestCase):
    def test_to_spec_identifies_structured_html_companion_uses(self):
        source = TO_SPEC.read_text(encoding="utf-8")

        self.assertIn("Structured HTML Companion", source)
        self.assertIn("review aid, not the canonical spec", source)
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
        self.assertIn("to-spec", source)
        self.assertIn("to-tickets", source)


class MattpocockMigrationTests(unittest.TestCase):
    RETIRED = [
        "writing-plans",
        "executing-plans",
        "subagent-driven-development",
        "requesting-code-review",
        "receiving-code-review",
        "verification-before-completion",
        "brainstorming",
        "systematic-debugging",
        "test-driven-development",
        "using-superpowers",
        "dispatching-parallel-agents",
        "using-git-worktrees",
        "finishing-a-development-branch",
    ]
    SUITE = [
        "ask-matt", "code-review", "codebase-design", "diagnosing-bugs",
        "domain-modeling", "grill-me", "grill-with-docs", "grilling",
        "implement", "improve-codebase-architecture", "prototype", "research",
        "resolving-merge-conflicts", "setup-matt-pocock-skills", "tdd",
        "to-spec", "to-tickets", "triage", "wayfinder",
    ]
    PATCHED_SUITE = ["implement", "setup-matt-pocock-skills", "tdd", "to-spec", "to-tickets"]

    def test_retired_skills_are_gone_from_repo(self):
        for skill in self.RETIRED:
            with self.subTest(skill=skill):
                self.assertFalse((REPO_ROOT / "skills" / skill).exists())

    def test_retired_skills_are_listed_for_removal(self):
        import setup

        for skill in self.RETIRED:
            with self.subTest(skill=skill):
                self.assertIn(skill, setup.RETIRED_SKILLS)

    def test_mattpocock_suite_is_vendored(self):
        import update

        for skill in self.SUITE:
            with self.subTest(skill=skill):
                self.assertTrue((REPO_ROOT / "skills" / skill / "SKILL.md").exists())
                self.assertIn(skill, update.UPSTREAM)

    def test_customized_suite_skills_are_patched(self):
        import update

        for skill in self.PATCHED_SUITE:
            with self.subTest(skill=skill):
                self.assertIn(skill, update.PATCHED)

    def test_restored_upstream_skills_are_not_patched(self):
        import update

        for skill in ("grill-with-docs", "improve-codebase-architecture"):
            with self.subTest(skill=skill):
                self.assertNotIn(skill, update.PATCHED)

    def test_to_spec_omits_requirement_source_sections(self):
        source = TO_SPEC.read_text(encoding="utf-8")

        self.assertNotIn("## User Requirements", source)
        self.assertNotIn("## Agent Design Decisions", source)
        self.assertNotIn("USER-REQ", TO_TICKETS.read_text(encoding="utf-8"))

    def test_spec_and_tickets_publish_to_configured_tracker(self):
        to_spec = TO_SPEC.read_text(encoding="utf-8")
        to_tickets = TO_TICKETS.read_text(encoding="utf-8")

        self.assertIn("publish it to the project issue tracker", to_spec)
        self.assertNotIn("docs/specs/<artifact-id>-design.md", to_spec)
        self.assertIn("Publish the tickets to the configured tracker", to_tickets)
        self.assertIn("ready-for-agent", to_tickets)
        self.assertNotIn("Default medium is local ticket files", to_tickets)

    def test_setup_skill_is_non_interactive_with_standing_defaults(self):
        source = (
            REPO_ROOT / "skills" / "setup-matt-pocock-skills" / "SKILL.md"
        ).read_text(encoding="utf-8")

        self.assertIn("non-interactive", source.lower())
        self.assertIn("apply the standing defaults", source)
        self.assertIn("If neither exists, create `AGENTS.md`", source)
        self.assertNotIn("Present findings and ask", source)
        self.assertNotIn("Let them edit before writing", source)

    def test_setup_requires_github_without_tracker_fallbacks(self):
        skill_dir = REPO_ROOT / "skills" / "setup-matt-pocock-skills"
        source = (skill_dir / "SKILL.md").read_text(encoding="utf-8")

        self.assertTrue((skill_dir / "issue-tracker-github.md").exists())
        self.assertFalse((skill_dir / "issue-tracker-gitlab.md").exists())
        self.assertFalse((skill_dir / "issue-tracker-local.md").exists())
        self.assertIn("### 2. Require GitHub", source)
        self.assertIn("gh repo view --json nameWithOwner,url", source)
        self.assertIn("Do not fall back to local Markdown", source)

    def test_tdd_uses_upstream_name(self):
        source = (REPO_ROOT / "skills" / "tdd" / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("name: tdd", source)


if __name__ == "__main__":
    unittest.main()
