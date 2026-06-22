import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

import setup


class GlobalInstructionInstallTests(unittest.TestCase):
    def test_installs_global_instruction_files_as_links(self):
        with tempfile.TemporaryDirectory() as repo_tmp, tempfile.TemporaryDirectory() as home_tmp:
            source_root = Path(repo_tmp) / "global"
            target_root = Path(home_tmp)
            source_root.mkdir()

            agents_source = source_root / "AGENTS.md"
            claude_source = source_root / "CLAUDE.md"
            agents_source.write_text("agents v1\n", encoding="utf-8")
            claude_source.write_text("@~/.codex/AGENTS.md\n", encoding="utf-8")

            links = [
                (agents_source, target_root / ".codex" / "AGENTS.md"),
                (claude_source, target_root / ".claude" / "CLAUDE.md"),
            ]

            with redirect_stdout(StringIO()):
                installed = setup.install_global_instructions(links)

            self.assertEqual(installed, 2)
            self.assertEqual((target_root / ".codex" / "AGENTS.md").read_text(encoding="utf-8"), "agents v1\n")
            self.assertEqual((target_root / ".claude" / "CLAUDE.md").read_text(encoding="utf-8"), "@~/.codex/AGENTS.md\n")

            agents_source.write_text("agents v2\n", encoding="utf-8")

            self.assertEqual((target_root / ".codex" / "AGENTS.md").read_text(encoding="utf-8"), "agents v2\n")


if __name__ == "__main__":
    unittest.main()
