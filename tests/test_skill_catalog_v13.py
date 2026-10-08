import re
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

import setup
import update


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS = REPO_ROOT / "skills"
README = REPO_ROOT / "README.md"
RATIONALE = REPO_ROOT / "docs" / "mattpocock-customization-rationale.md"

# Skill directories whose glossary references and cross-skill loading this
# catalog change owns.
OWNED = [
    "ask-matt", "domain-modeling", "diagnosing-bugs", "wait-what", "grill-me",
    "grill-with-docs", "setup-matt-pocock-skills", "triage",
    "improve-codebase-architecture", "pr", "retro",
]
HARNESS_COMMANDS = {"clear", "compact"}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def frontmatter(skill: str) -> str:
    match = re.match(r"---\r?\n(.*?)\r?\n---", read(SKILLS / skill / "SKILL.md"), re.S)
    assert match, f"{skill} has no frontmatter"
    return match.group(1)


def is_user_invoked(skill: str) -> bool:
    return "disable-model-invocation: true" in frontmatter(skill)


def codex_hides(skill: str) -> bool:
    return "allow_implicit_invocation: false" in read(SKILLS / skill / "agents" / "openai.yaml")


def readme_section(heading: str) -> set[str]:
    body = read(README).split(f"\n## {heading}\n", 1)[1].split("\n## ", 1)[0]
    return set(re.findall(r"\]\(skills/([a-z0-9-]+)/\)", body))


class V13CatalogTests(unittest.TestCase):
    def test_new_skills_track_their_upstream_paths(self):
        for skill in ("pr", "retro", "implement-spec"):
            with self.subTest(skill=skill):
                self.assertEqual(
                    update.UPSTREAM[skill],
                    [{"repo": "mattpocock/skills", "path": f"skills/engineering/{skill}"}],
                )
                self.assertTrue((SKILLS / skill / "SKILL.md").is_file())

    def test_conflict_skill_is_retired_everywhere(self):
        self.assertNotIn("resolving-merge-conflicts", update.UPSTREAM)
        self.assertIn("resolving-merge-conflicts", setup.RETIRED_SKILLS)
        self.assertFalse((SKILLS / "resolving-merge-conflicts").exists())
        self.assertNotIn("resolving-merge-conflicts", read(README))
        self.assertNotIn("resolving-merge-conflicts", read(SKILLS / "ask-matt" / "SKILL.md"))

    def test_setup_removes_installed_conflict_skill_copies(self):
        with tempfile.TemporaryDirectory() as home:
            roots = [Path(home) / "claude", Path(home) / "codex"]
            for root in roots:
                (root / "resolving-merge-conflicts").mkdir(parents=True)
                (root / "resolving-merge-conflicts" / "SKILL.md").write_text("old", encoding="utf-8")
            (roots[0] / "pr").mkdir()

            with redirect_stdout(StringIO()):
                setup.remove_retired_skills(target_roots=roots, mirror_target_roots={})

            for root in roots:
                self.assertFalse((root / "resolving-merge-conflicts").exists())
            self.assertTrue((roots[0] / "pr").exists())

    def test_invocation_metadata_matches_upstream_roles(self):
        self.assertFalse(is_user_invoked("pr"))
        self.assertFalse(codex_hides("pr"))
        for skill in ("retro", "implement-spec"):
            with self.subTest(skill=skill):
                self.assertTrue(is_user_invoked(skill))
                self.assertTrue(codex_hides(skill))

    def test_setup_stays_model_invocable(self):
        self.assertFalse(is_user_invoked("setup-matt-pocock-skills"))
        self.assertFalse(codex_hides("setup-matt-pocock-skills"))

    def test_classification_follows_actual_local_edits(self):
        for skill in ("pr", "domain-modeling", "diagnosing-bugs", "wait-what"):
            with self.subTest(original=skill):
                self.assertIn(skill, update.UPSTREAM)
                self.assertNotIn(skill, update.PATCHED)
        customized = (
            "ask-matt", "grill-me", "grill-with-docs", "improve-codebase-architecture",
            "triage", "retro", "setup-matt-pocock-skills",
            "code-review", "codebase-design", "unslop", "implement-spec",
        )
        for skill in customized:
            with self.subTest(customized=skill):
                self.assertIn(skill, update.UPSTREAM)
                self.assertIn(skill, update.PATCHED)

    def test_readme_sections_match_updater_classification(self):
        customized = readme_section("Vendor Skills (customized)")
        original = readme_section("Vendor Skills")
        personal = readme_section("My Skills")

        self.assertEqual(customized, set(update.PATCHED))
        self.assertEqual(original, set(update.UPSTREAM) - set(update.PATCHED))
        installed = {d.name for d in SKILLS.iterdir() if (d / "SKILL.md").is_file()}
        self.assertEqual(installed, customized | original | personal)

    def test_rationale_covers_every_customized_skill_without_a_stale_count(self):
        source = read(RATIONALE)

        self.assertNotIn("Eight skills", source)
        for skill in update.PATCHED:
            with self.subTest(skill=skill):
                self.assertIn(f"`{skill}`", source)


class GlossaryMigrationTests(unittest.TestCase):
    def test_obsolete_context_format_is_replaced(self):
        domain = SKILLS / "domain-modeling"

        self.assertFalse((domain / "CONTEXT-FORMAT.md").exists())
        self.assertIn("# GLOSSARY.md Format", read(domain / "GLOSSARY-FORMAT.md"))
        self.assertIn("(./GLOSSARY-FORMAT.md)", read(domain / "SKILL.md"))

    def test_owned_skills_use_glossary_names(self):
        setup_skill = SKILLS / "setup-matt-pocock-skills" / "SKILL.md"
        for skill in OWNED:
            for path in (SKILLS / skill).rglob("*"):
                if not path.is_file() or path == setup_skill:
                    continue
                with self.subTest(path=path.relative_to(REPO_ROOT).as_posix()):
                    self.assertNotRegex(read(path), r"CONTEXT(-MAP|-FORMAT)?\.md")

    def test_setup_writes_glossary_layout(self):
        skill_dir = SKILLS / "setup-matt-pocock-skills"
        source = read(skill_dir / "SKILL.md")
        domain = read(skill_dir / "domain.md")

        self.assertIn("one `GLOSSARY.md` + `docs/adr/`", source)
        self.assertIn("a root `GLOSSARY-MAP.md` pointing to per-context `GLOSSARY.md` files", source)
        self.assertIn("**`GLOSSARY-MAP.md`** at the repo root", domain)
        self.assertIn("use the term as defined in `GLOSSARY.md`", domain)

    def test_setup_migrates_only_legacy_domain_glossaries(self):
        source = read(SKILLS / "setup-matt-pocock-skills" / "SKILL.md")
        migration = source.split("**Legacy glossary names:**", 1)[1].split("\n\n", 1)[0]

        self.assertIn("`git mv`", migration)
        self.assertIn("`CONTEXT.md`", migration)
        self.assertIn("`CONTEXT-MAP.md`", migration)
        self.assertIn("Leave any other `CONTEXT.md` untouched", migration)
        outside = source.replace(migration, "")
        self.assertNotRegex(outside, r"CONTEXT(-MAP)?\.md")


class SkillLoadingTests(unittest.TestCase):
    def test_skill_tool_calls_have_a_file_fallback_to_model_invoked_skills(self):
        for skill in OWNED:
            for line in read(SKILLS / skill / "SKILL.md").splitlines():
                if "Skill tool" not in line:
                    continue
                fallbacks = re.findall(r"`\.\./([a-z0-9-]+)/SKILL\.md`", line)
                with self.subTest(skill=skill, line=line[:60]):
                    self.assertIn("otherwise read", line)
                    self.assertTrue(fallbacks)
                    for target in fallbacks:
                        self.assertIn(f"`{target}`", line.split("otherwise read")[0])
                        self.assertFalse(is_user_invoked(target), target)

    def test_wrappers_load_their_shared_skills(self):
        expectations = {
            "grill-me": ["grilling"],
            "grill-with-docs": ["grilling", "domain-modeling"],
            "retro": ["writing-for-agents"],
        }
        for skill, targets in expectations.items():
            source = read(SKILLS / skill / "SKILL.md")
            for target in targets:
                with self.subTest(skill=skill, target=target):
                    self.assertIn(f"`../{target}/SKILL.md`", source)


class ArchitectureVocabularyTests(unittest.TestCase):
    def test_survey_follows_codebase_design_scope_rule(self):
        source = read(SKILLS / "improve-codebase-architecture" / "SKILL.md")

        self.assertNotIn("don't drift into", source)
        self.assertIn("as generic stand-ins", source)
        self.assertIn("keep their actual names", source)


class RouterTests(unittest.TestCase):
    ROUTER = SKILLS / "ask-matt" / "SKILL.md"

    def test_routes_only_to_installed_skills(self):
        routes = set(re.findall(r"`/([a-z][a-z0-9-]*)", read(self.ROUTER))) - HARNESS_COMMANDS

        self.assertTrue({"pr", "retro", "implement-spec"} <= routes)
        for route in routes:
            with self.subTest(route=route):
                self.assertTrue((SKILLS / route / "SKILL.md").is_file())

    def test_matches_the_github_only_stack(self):
        source = read(self.ROUTER)

        for stale in (".scratch", "local tracker", "Custom issue trackers", "post-mortem"):
            with self.subTest(stale=stale):
                self.assertNotIn(stale, source)
        self.assertIn("GitHub", source)

    def test_retro_stays_user_directed(self):
        source = read(self.ROUTER)

        self.assertIn("you can run **`/retro`**", source)
        self.assertNotIn("Once the fix is in, run **`/retro`**", source)

    def test_summaries_defer_to_skill_definitions(self):
        self.assertIn("read the skill itself", read(self.ROUTER))


class RetroIntegrationTests(unittest.TestCase):
    def test_finds_logs_for_each_harness(self):
        source = read(SKILLS / "retro" / "SKILL.md")

        for location in ("~/.pi/agent/sessions/", "~/.codex/sessions/", "~/.claude/projects/"):
            with self.subTest(location=location):
                self.assertIn(location, source)

    def test_stays_scoped_and_proposal_only(self):
        source = read(SKILLS / "retro" / "SKILL.md")

        self.assertIn("Read only the session the user names", source)
        self.assertIn("Keep raw transcripts local", source)
        self.assertIn("Change nothing until the user approves a proposal", source)


if __name__ == "__main__":
    unittest.main()
