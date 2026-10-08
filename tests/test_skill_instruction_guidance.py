import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
GLOBAL_AGENTS = REPO_ROOT / "global" / "AGENTS.md"
UI_GUIDELINES = REPO_ROOT / "global" / "UI-GUIDELINES.md"
UNSLOP = REPO_ROOT / "skills" / "unslop" / "SKILL.md"
CODEBASE_DESIGN = REPO_ROOT / "skills" / "codebase-design"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def frontmatter(source: str) -> str:
    match = re.match(r"---\n(.*?)\n---\n", source, re.S)
    assert match, "missing frontmatter"
    return match.group(1)


class UnslopGuidanceTests(unittest.TestCase):
    def test_targets_user_facing_writing(self):
        source = read(UNSLOP)

        self.assertIn("description: Cut AI tells from user-facing writing.", frontmatter(source))
        self.assertIn("## Scope", source)

    def test_preserves_exact_text_it_does_not_own(self):
        scope = read(UNSLOP).split("## Scope", 1)[1].split("\n## ", 1)[0]

        for protected in ("code", "logs", "quotations", "API", "identifiers", "domain terms"):
            with self.subTest(protected=protected):
                self.assertIn(protected, scope)

    def test_punctuation_is_judgment_not_a_ban(self):
        source = read(UNSLOP)

        self.assertNotIn("Avoid em dashes entirely", source)
        self.assertNotIn("no parentheses", source)
        self.assertNotIn("Use periods or commas only", source)
        self.assertIn("**Em dash overuse.**", source)
        self.assertIn("**Colon overuse.**", source)

    def test_jargon_list_keeps_precise_terms(self):
        source = read(UNSLOP)

        self.assertIn("**Abstract metaphor nouns.**", source)
        for hard_substitution in ('"Substrate" becomes "base"', '"Vector" becomes "way"', '"leverage" becomes "use"'):
            with self.subTest(hard_substitution=hard_substitution):
                self.assertNotIn(hard_substitution, source)
        self.assertIn("exact technical term", source)


class CodebaseDesignVocabularyTests(unittest.TestCase):
    def test_vocabulary_is_scoped_to_architectural_discussion(self):
        source = read(CODEBASE_DESIGN / "SKILL.md")

        self.assertNotIn("Use these terms exactly: don't substitute", source)
        self.assertIn("architectural discussion", source)

    def test_real_identifiers_and_domain_names_are_preserved(self):
        glossary = read(CODEBASE_DESIGN / "SKILL.md").split("## Glossary", 1)[1].split("\n## ", 1)[0]

        for preserved in ("React component", "API", "GLOSSARY.md"):
            with self.subTest(preserved=preserved):
                self.assertIn(preserved, glossary)

    def test_owned_files_point_at_glossary_not_context(self):
        owned = [*CODEBASE_DESIGN.rglob("*.md"), UNSLOP, GLOBAL_AGENTS, UI_GUIDELINES]

        for path in owned:
            with self.subTest(path=path.relative_to(REPO_ROOT).as_posix()):
                self.assertNotIn("CONTEXT.md", read(path))


class GlobalInstructionScopeTests(unittest.TestCase):
    UI_CHECKLIST = (
        "Use strong contrast",
        "convey unique information",
        "whitespace is preferable to filler",
        "Give each control an accessible name",
    )

    def test_detailed_ui_checklist_moves_to_one_reference(self):
        agents = read(GLOBAL_AGENTS)
        guidelines = read(UI_GUIDELINES)

        for item in self.UI_CHECKLIST:
            with self.subTest(item=item):
                self.assertNotIn(item, agents)
                self.assertIn(item, guidelines)
        self.assertIn("`~/sz-skills/global/UI-GUIDELINES.md`", agents)

    def test_sz_skills_pointers_resolve_to_source_files(self):
        pointers = re.findall(r"~/sz-skills/([\w./-]+\.md)", read(GLOBAL_AGENTS))

        self.assertIn("global/UI-GUIDELINES.md", pointers)
        for pointer in pointers:
            with self.subTest(pointer=pointer):
                self.assertTrue((REPO_ROOT / pointer).is_file())

    def test_keeps_operational_policy_and_core_ui_preferences(self):
        agents = read(GLOBAL_AGENTS)

        required = (
            "Limit destructive actions to targets explicitly authorized by the user.",
            "## Test server cleanup",
            "## Shell Commands on Windows",
            "## Windows UAC approval",
            "close every browser tab opened for the task",
            "## Localhost Ports",
            "Never use computer use unless the user explicitly requests it.",
            "as the sole visual-design skill",
            "UI testing targets desktop",
            "Mock first",
            "one self-contained HTML comparison page containing every option",
            "## HTML Reports",
            "`file:///C:/path/to/file`",
            "## Global Agent Instructions",
        )
        for text in required:
            with self.subTest(text=text):
                self.assertIn(text, agents)

    def test_skill_loading_is_harness_correct_and_respects_user_invocation(self):
        section = read(GLOBAL_AGENTS).split("## Loading Skills", 1)[1].split("\n## ", 1)[0]

        self.assertIn("native skill tool", section)
        self.assertIn("`SKILL.md`", section)
        self.assertIn("`disable-model-invocation: true`", section)


if __name__ == "__main__":
    unittest.main()
