import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = REPO_ROOT / "skills" / "start-sz-video"
SCRIPT = SKILL_DIR / "scripts" / "start-sz-video.ps1"


class StartSzVideoSkillTests(unittest.TestCase):
    def test_start_script_uses_reliable_non_docker_launch_path(self):
        source = SCRIPT.read_text(encoding="utf-8")

        self.assertIn("video-workflow-operator-ui", source)
        self.assertIn("corepack.cmd", source)
        self.assertIn("@sz-video/server", source)
        self.assertIn("@sz-video/web", source)
        self.assertNotIn("pnpm dev", source)
        self.assertNotIn("docker compose up", source.lower())
        self.assertNotIn("docker-compose up", source.lower())

    def test_skill_instructions_point_to_the_bundled_script(self):
        skill = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("scripts/start-sz-video.ps1", skill)
        self.assertIn("127.0.0.1:5173", skill)
        self.assertIn("127.0.0.1:5174", skill)


if __name__ == "__main__":
    unittest.main()
