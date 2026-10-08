import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS = REPO_ROOT / "skills"
TDD = SKILLS / "tdd" / "SKILL.md"
VISUAL_TESTS = SKILLS / "tdd" / "visual-tests.md"
PROTOTYPE = SKILLS / "prototype" / "SKILL.md"
PROTOTYPE_UI = SKILLS / "prototype" / "UI.md"
PROTOTYPE_LOGIC = SKILLS / "prototype" / "LOGIC.md"
REPO_VISUALIZER = SKILLS / "repo-visualizer" / "SKILL.md"

COMPETING_BROWSER_TOOLS = ("Chrome DevTools", "DevTools MCP", "Chrome plugin")


def read_raw(path):
    return path.read_text(encoding="utf-8")


def read(path):
    """Text with hard-wrapped lines joined, so phrases match across wraps."""
    return re.sub(r"(?<!\n)\n(?!\n)", " ", read_raw(path))


def paragraphs(source):
    return [block for block in re.split(r"\n\s*\n", source) if block.strip()]


class SkillGuidanceAssertions(unittest.TestCase):
    def assertLoadsSkillPerHarness(self, source, skill):
        """A cross-skill reference uses the native Skill tool when present, else reads SKILL.md."""
        matching = [
            block for block in paragraphs(source)
            if f"`{skill}`" in block and "Skill tool" in block and "SKILL.md" in block
        ]
        self.assertTrue(
            matching,
            f"expected a paragraph loading `{skill}` via the Skill tool or its SKILL.md",
        )
        self.assertFalse(f"/{skill}" in source, f"/{skill}")

    def assertNoCompetingBrowserPreference(self, source):
        for tool in COMPETING_BROWSER_TOOLS:
            with self.subTest(tool=tool):
                self.assertFalse(tool in source, tool)


class TddEntryTests(SkillGuidanceAssertions):
    def test_entry_is_a_short_common_path(self):
        source = read_raw(TDD)
        self.assertLessEqual(len(source.splitlines()), 150)
        self.assertEqual(len(re.findall(r"^RED:", source, re.M)), 1)

    def test_entry_keeps_every_local_requirement(self):
        source = read(TDD)
        required = [
            "independent source of truth",
            "agreed seam",
            "already pins",
            "command-level timeout",
            "kills",
            "User-requirement tests",
            "Edge case",
            "fails explicitly",
            "backward compatibility",
            "stale",
            "real entry point",
            "real data",
            "full test suite",
        ]
        for phrase in required:
            with self.subTest(phrase=phrase):
                self.assertTrue(phrase in source, phrase)
        self.assertLoadsSkillPerHarness(source, "code-review")
        self.assertLoadsSkillPerHarness(source, "codebase-design")

    def test_caller_owned_review_is_deferred_and_red_is_never_refactored(self):
        source = read(TDD)
        after_green = source[source.index("## After green"):source.index("## Done gate")]

        self.assertIn("never refactor while RED", after_green)
        self.assertIn("caller owns the review phase", after_green)
        self.assertIn("defer review-driven refactoring to the caller", after_green)
        self.assertLoadsSkillPerHarness(after_green, "code-review")

    def test_unexpected_skips_fail_the_done_gate(self):
        gate = read(TDD).split("## Done gate", 1)[1]

        self.assertIn("unexpectedly skipped or uncollected", gate)
        self.assertIn("counts as failed", gate)

    def test_ui_reference_is_disclosed_only_behind_the_ui_pointer(self):
        source = read(TDD)
        self.assertRegex(source, r"UI[^\n]*\[visual-tests\.md\]\(visual-tests\.md\)")
        for ui_detail in ("clipp", "visual balance", "Tool priority"):
            with self.subTest(detail=ui_detail):
                self.assertFalse(ui_detail in source, ui_detail)
        self.assertNoCompetingBrowserPreference(source)


class VisualTestsReferenceTests(SkillGuidanceAssertions):
    def test_browser_work_points_to_browser_harness(self):
        source = read(VISUAL_TESTS)
        self.assertLoadsSkillPerHarness(source, "browser-harness")
        self.assertNoCompetingBrowserPreference(source)

    def test_keeps_visual_only_look_and_live_walkthrough_policy(self):
        source = read(VISUAL_TESTS).lower()
        for phrase in (
            "look-and-feel",
            "component",
            "dom",
            "snapshot",
            "desktop",
            "walkthrough",
            "real data",
            "do not replace",
        ):
            with self.subTest(phrase=phrase):
                self.assertTrue(phrase in source, phrase)


class PrototypeTests(SkillGuidanceAssertions):
    def test_ui_options_share_one_self_contained_comparison_page(self):
        ui = read(PROTOTYPE_UI)
        for path in (PROTOTYPE, PROTOTYPE_UI):
            source = read(path)
            with self.subTest(file=path.name):
                self.assertTrue("self-contained HTML comparison page" in source, "self-contained HTML comparison page")
                self.assertFalse("?variant=" in source, "?variant=")
                self.assertFalse("floating bottom bar" in source, "floating bottom bar")
                self.assertFalse("variant switch" in source, "variant switch")
        self.assertTrue("before asking" in ui, "before asking")
        self.assertTrue("every option" in ui, "every option")

    def test_ui_branch_uses_frontend_design_and_leaves_real_components_alone(self):
        ui = read(PROTOTYPE_UI)
        self.assertLoadsSkillPerHarness(ui, "frontend-design")
        self.assertTrue("real components" in ui, "real components")
        self.assertTrue("until the user picks" in ui, "until the user picks")

    def test_ui_server_stays_reachable_and_is_cleaned_up(self):
        ui = read(PROTOTYPE_UI)
        for phrase in ("0.0.0.0", "Tailscale", "tailscale status", "LOCALHOST_PORTS.md", "port is released"):
            with self.subTest(phrase=phrase):
                self.assertTrue(phrase in ui, phrase)

    def test_ui_server_is_stopped_before_handoff_unless_user_asks(self):
        ui = read(PROTOTYPE_UI)
        self.assertNotIn("keep it running until the user decides", ui)
        for phrase in ("static", "before handing off", "explicitly asks", "Keep the page available until they decide"):
            with self.subTest(phrase=phrase):
                self.assertTrue(phrase in ui, phrase)

    def test_logic_branch_and_primary_source_capture_remain(self):
        entry = read(PROTOTYPE)
        logic = read(PROTOTYPE_LOGIC)
        self.assertTrue("[LOGIC.md](LOGIC.md)" in entry, "[LOGIC.md](LOGIC.md)")
        self.assertTrue("primary source" in entry, "primary source")
        self.assertTrue("throwaway branch" in entry, "throwaway branch")
        for phrase in ("Free-play buttons", "Guided walkthroughs", "pure module"):
            with self.subTest(phrase=phrase):
                self.assertTrue(phrase in logic, phrase)


class RepoVisualizerTests(SkillGuidanceAssertions):
    def test_browser_verification_points_to_browser_harness(self):
        source = read(REPO_VISUALIZER)
        self.assertLoadsSkillPerHarness(source, "browser-harness")
        self.assertNoCompetingBrowserPreference(source)
        self.assertTrue("Mermaid renders" in source, "Mermaid renders")


class LocalLinkTests(unittest.TestCase):
    def test_relative_links_in_owned_skills_resolve(self):
        for skill in ("tdd", "prototype", "repo-visualizer"):
            for doc in (SKILLS / skill).glob("*.md"):
                for target in re.findall(r"\]\(([^)#:]+\.md)\)", read(doc)):
                    with self.subTest(doc=doc.name, target=target):
                        self.assertTrue((doc.parent / target).is_file())


if __name__ == "__main__":
    unittest.main()
