import json
import subprocess
import sys
import unittest
from pathlib import Path

HOOK = Path(__file__).resolve().parent.parent / "hooks" / "shell-syntax-guard.py"


def run_hook(tool_name, command):
    payload = {"tool_name": tool_name, "tool_input": {"command": command}}
    return subprocess.run(
        [sys.executable, str(HOOK)],
        input=json.dumps(payload),
        capture_output=True,
        text=True,
        timeout=30,
    )


class ShellSyntaxGuardTests(unittest.TestCase):
    def assertBlocked(self, tool_name, command):
        result = run_hook(tool_name, command)
        self.assertEqual(result.returncode, 2, command)
        self.assertIn("Blocked", result.stderr)

    def assertAllowed(self, tool_name, command):
        result = run_hook(tool_name, command)
        self.assertEqual(result.returncode, 0, (command, result.stderr))

    def test_blocks_heredoc_in_powershell(self):
        self.assertBlocked("PowerShell", "python - <<'PY'\nprint(1)\nPY")
        self.assertBlocked("PowerShell", "cat > x.py <<EOF\nx\nEOF")

    def test_allows_normal_powershell(self):
        self.assertAllowed("PowerShell", "Get-ChildItem C:\\ | Select-Object Name")
        self.assertAllowed("PowerShell", "$a = 1 -shl 2; Write-Output $a")

    def test_blocks_cmdlets_in_bash(self):
        self.assertBlocked("Bash", "Get-ChildItem \"$env:USERPROFILE\" | Select-Object Name")
        self.assertBlocked("Bash", "cd ~ && Get-Content foo.txt")
        self.assertBlocked("Bash", "ls; Remove-Item -Recurse x")

    def test_allows_bash_that_launches_powershell(self):
        self.assertAllowed("Bash", "powershell.exe -NoProfile -Command 'Get-Item x; Get-ChildItem y'")
        self.assertAllowed("Bash", "pwsh -c \"Get-Process | Sort-Object CPU\"")

    def test_allows_cmdlets_inside_bash_heredoc_body(self):
        self.assertAllowed("Bash", "cat > s.ps1 <<'EOF'\nGet-ChildItem .\nEOF")

    def test_allows_ordinary_bash(self):
        self.assertAllowed("Bash", "git status && ls -la | grep Get-Thing.md")
        self.assertAllowed("Bash", "python - <<'PY'\nprint('hi')\nPY")

    def test_distinguishes_quoted_text_from_bash_commands(self):
        self.assertAllowed("Bash", "printf '%s' 'example; Get-ChildItem .' ")
        self.assertBlocked("Bash", "echo powershell; Get-ChildItem .")
        self.assertBlocked("Bash", "pwsh -c 'Get-Item x'; Get-Content foo.txt")

    def test_ignores_other_tools_and_bad_input(self):
        self.assertAllowed("Edit", "<<'EOF'")
        result = subprocess.run(
            [sys.executable, str(HOOK)], input="not json", capture_output=True, text=True, timeout=30
        )
        self.assertEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
