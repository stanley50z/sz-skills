import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = REPO_ROOT / "skills" / "global-project-preferences"
SKILL = SKILL_DIR / "SKILL.md"
README = REPO_ROOT / "README.md"


class GlobalProjectPreferencesSkillTests(unittest.TestCase):
    def test_skill_exists_with_trigger_frontmatter(self):
        source = SKILL.read_text(encoding="utf-8")
        frontmatter = re.match(r"---\n(.*?)\n---", source, re.DOTALL)

        self.assertIsNotNone(frontmatter)
        self.assertIn("name: global-project-preferences", frontmatter.group(1))
        self.assertIn("description: Use when starting", frontmatter.group(1))
        self.assertIn("new project", frontmatter.group(1).lower())
        self.assertIn("extension", frontmatter.group(1).lower())
        self.assertIn("script", frontmatter.group(1).lower())

    def test_skill_contains_user_default_stack_and_override_rule(self):
        source = SKILL.read_text(encoding="utf-8")

        expected_defaults = [
            "GitHub Actions",
            "Stripe",
            "shadcn/ui",
            "Vercel",
            "Tailwind CSS",
            "Zustand",
            "Postgres",
            "Drizzle",
            "PNPM",
            "Vitest",
            "Resend",
            "Sentry",
            "TanStack Query",
            "better auth",
            "UploadThing",
            "Node.js",
        ]
        for default in expected_defaults:
            with self.subTest(default=default):
                self.assertIn(default, source)

        self.assertIn("strong, project-specific evidence", source)
        self.assertIn("Only suggest alternatives", source)
        self.assertIn("concrete and relevant", source)

    def test_readme_catalogs_skill_as_personal(self):
        readme = README.read_text(encoding="utf-8")

        self.assertIn("[global-project-preferences](skills/global-project-preferences/)", readme)
        self.assertLess(
            readme.index("[global-project-preferences](skills/global-project-preferences/)"),
            readme.index("## Vendor Skills"),
        )


if __name__ == "__main__":
    unittest.main()
