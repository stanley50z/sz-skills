import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import setup


class PluginHookSetupTests(unittest.TestCase):
    def _run_hook_script(self, script_name, hooks_dir=None):
        bash_candidates = [
            Path("C:/Program Files/Git/bin/bash.exe"),
            Path("C:/Program Files (x86)/Git/bin/bash.exe"),
        ]
        bash_path = next((path for path in bash_candidates if path.exists()), None)
        bash = str(bash_path) if bash_path else shutil.which("bash")
        if bash is None or (os.name == "nt" and "system32" in bash.lower()):
            self.skipTest("bash is required to execute hook scripts")

        repo_root = Path(setup.REPO_ROOT)
        hooks_dir = hooks_dir or (repo_root / "hooks")
        env = os.environ.copy()
        env["PLUGIN_ROOT"] = str(repo_root)
        result = subprocess.run(
            [bash, str(hooks_dir / script_name)],
            check=True,
            capture_output=True,
            text=True,
            timeout=30,
            env=env,
        )
        payload = json.loads(result.stdout)
        return (
            payload.get("hookSpecificOutput", {}).get("additionalContext")
            or payload.get("additionalContext")
            or payload.get("additional_context")
            or ""
        )

    def _run_stop_hook(self, payload):
        repo_root = Path(setup.REPO_ROOT)
        hook_script = repo_root / "hooks" / "stop-cdp-session-reminder.py"
        result = subprocess.run(
            [sys.executable, str(hook_script)],
            input=json.dumps(payload),
            check=True,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return json.loads(result.stdout or "{}")

    def _write_transcript(self, path, entries):
        path.write_text(
            "\n".join(json.dumps(entry) for entry in entries) + "\n",
            encoding="utf-8",
        )

    def _function_call_entry(self, name, turn_id):
        return {
            "timestamp": "2026-06-26T00:00:00Z",
            "type": "response_item",
            "payload": {
                "type": "function_call",
                "name": name,
                "arguments": "{}",
                "call_id": "call_test",
                "internal_chat_message_metadata_passthrough": {
                    "turn_id": turn_id,
                },
            },
        }

    def test_registers_codex_local_plugin_in_config(self):
        with tempfile.TemporaryDirectory() as repo_tmp, tempfile.TemporaryDirectory() as home_tmp:
            repo_root = Path(repo_tmp)
            codex_plugin_root = repo_root / setup.CODEX_HOOK_PLUGIN_DIR
            config_path = Path(home_tmp) / ".codex" / "config.toml"
            config_path.parent.mkdir(parents=True)
            config_path.write_text('model = "gpt-5.5"\n', encoding="utf-8")

            changed = setup.install_codex_plugin_config(config_path=config_path, repo_root=repo_root)

            self.assertTrue(changed)
            config = config_path.read_text(encoding="utf-8")
            self.assertIn("[marketplaces.sz-skills]", config)
            self.assertIn('source_type = "local"', config)
            self.assertIn(f"source = '{codex_plugin_root}'", config)
            self.assertNotIn(f"source = '{repo_root}'", config)
            self.assertIn('[plugins."sz-skills@sz-skills"]', config)
            self.assertIn("enabled = true", config)

            second_changed = setup.install_codex_plugin_config(config_path=config_path, repo_root=repo_root)

            self.assertFalse(second_changed)

    def test_registers_claude_local_plugin_state(self):
        with tempfile.TemporaryDirectory() as repo_tmp, tempfile.TemporaryDirectory() as home_tmp:
            repo_root = Path(repo_tmp)
            claude_root = Path(home_tmp) / ".claude"
            settings_path = claude_root / "settings.json"
            installed_path = claude_root / "plugins" / "installed_plugins.json"
            known_path = claude_root / "plugins" / "known_marketplaces.json"

            changed = setup.install_claude_plugin_config(
                settings_path=settings_path,
                installed_plugins_path=installed_path,
                known_marketplaces_path=known_path,
                repo_root=repo_root,
                now_iso="2026-06-24T00:00:00Z",
                git_commit_sha="abc123",
            )

            self.assertTrue(changed)
            settings = json.loads(settings_path.read_text(encoding="utf-8"))
            self.assertTrue(settings["enabledPlugins"]["sz-skills@sz-skills"])

            installed = json.loads(installed_path.read_text(encoding="utf-8"))
            install_record = installed["plugins"]["sz-skills@sz-skills"][0]
            self.assertEqual(install_record["scope"], "user")
            self.assertEqual(install_record["installPath"], str(repo_root))
            self.assertEqual(install_record["version"], setup.PLUGIN_VERSION)
            self.assertEqual(install_record["gitCommitSha"], "abc123")

            known = json.loads(known_path.read_text(encoding="utf-8"))
            self.assertEqual(known["sz-skills"]["source"]["source"], "local")
            self.assertEqual(known["sz-skills"]["source"]["path"], str(repo_root))

            second_changed = setup.install_claude_plugin_config(
                settings_path=settings_path,
                installed_plugins_path=installed_path,
                known_marketplaces_path=known_path,
                repo_root=repo_root,
                now_iso="2026-06-24T00:00:00Z",
                git_commit_sha="abc123",
            )

            self.assertFalse(second_changed)

    def test_repo_contains_plugin_hook_entrypoints(self):
        repo_root = Path(setup.REPO_ROOT)
        codex_plugin_root = repo_root / setup.CODEX_HOOK_PLUGIN_DIR

        self.assertTrue((codex_plugin_root / ".codex-plugin" / "plugin.json").is_file())
        self.assertTrue((codex_plugin_root / "hooks" / "hooks-codex.json").is_file())
        self.assertTrue((codex_plugin_root / "hooks" / "session-start-codex").is_file())
        self.assertTrue((codex_plugin_root / "hooks" / "stop-cdp-session-reminder").is_file())
        self.assertTrue((codex_plugin_root / "hooks" / "stop-cdp-session-reminder.py").is_file())
        self.assertTrue((codex_plugin_root / "hooks" / "run-hook.cmd").is_file())
        self.assertFalse((codex_plugin_root / "skills").exists())
        hook_marketplace = json.loads((codex_plugin_root / ".agents" / "plugins" / "marketplace.json").read_text(encoding="utf-8"))
        self.assertEqual(hook_marketplace["plugins"][0]["source"]["path"], ".")
        repo_marketplace = json.loads((repo_root / ".agents" / "plugins" / "marketplace.json").read_text(encoding="utf-8"))
        self.assertEqual(repo_marketplace["plugins"][0]["source"]["path"], f"./{setup.CODEX_HOOK_PLUGIN_DIR}")
        self.assertTrue((repo_root / ".claude-plugin" / "plugin.json").is_file())
        self.assertTrue((repo_root / ".agents" / "plugins" / "marketplace.json").is_file())
        self.assertTrue((repo_root / ".claude-plugin" / "marketplace.json").is_file())
        self.assertTrue((repo_root / "hooks" / "hooks-codex.json").is_file())
        self.assertTrue((repo_root / "hooks" / "hooks.json").is_file())
        self.assertTrue((repo_root / "hooks" / "session-start-codex").is_file())
        self.assertTrue((repo_root / "hooks" / "session-start").is_file())
        self.assertTrue((repo_root / "hooks" / "stop-cdp-session-reminder").is_file())
        self.assertTrue((repo_root / "hooks" / "stop-cdp-session-reminder.py").is_file())
        self.assertTrue((repo_root / "hooks" / "run-hook.cmd").is_file())

    def test_claude_hook_definition_remains_session_start_context_only(self):
        repo_root = Path(setup.REPO_ROOT)
        hooks = json.loads((repo_root / "hooks" / "hooks.json").read_text(encoding="utf-8"))["hooks"]

        self.assertEqual(set(hooks), {"SessionStart"})
        rendered = json.dumps(hooks)
        self.assertNotIn("Stop", rendered)
        self.assertNotIn("cleanup", rendered.lower())
        self.assertNotIn("chrome", rendered.lower())

    def test_codex_hook_definition_adds_stop_without_tool_loop_hooks(self):
        repo_root = Path(setup.REPO_ROOT)

        for hook_file in [
            repo_root / "hooks" / "hooks-codex.json",
            repo_root / setup.CODEX_HOOK_PLUGIN_DIR / "hooks" / "hooks-codex.json",
        ]:
            hooks = json.loads(hook_file.read_text(encoding="utf-8"))["hooks"]

            self.assertEqual(set(hooks), {"SessionStart", "Stop"})
            rendered = json.dumps(hooks)
            self.assertNotIn("PreToolUse", rendered)
            self.assertNotIn("PostToolUse", rendered)
            self.assertIn("stop-cdp-session-reminder", rendered)

    def test_session_start_hooks_inject_chrome_devtools_context_only_guidance(self):
        repo_root = Path(setup.REPO_ROOT)
        codex_plugin_hooks_dir = repo_root / setup.CODEX_HOOK_PLUGIN_DIR / "hooks"

        for script_name, hooks_dir in [
            ("session-start-codex", repo_root / "hooks"),
            ("session-start-codex", codex_plugin_hooks_dir),
            ("session-start", repo_root / "hooks"),
        ]:
            context = self._run_hook_script(script_name, hooks_dir=hooks_dir)

            self.assertIn("Chrome DevTools MCP browser ownership", context)
            self.assertIn("context-only guidance", context)
            self.assertIn("Do not add or run cleanup scripts from hooks", context)
            self.assertIn("browser-url, ws-endpoint, autoConnect", context)

    def test_stop_hook_allows_turns_without_chrome_devtools_tool_calls(self):
        with tempfile.TemporaryDirectory() as tmp:
            transcript_path = Path(tmp) / "transcript.jsonl"
            self._write_transcript(
                transcript_path,
                [self._function_call_entry("shell_command", "turn-current")],
            )

            payload = {
                "transcript_path": str(transcript_path),
                "turn_id": "turn-current",
                "last_assistant_message": "Done.",
            }

            result = self._run_stop_hook(payload)

            self.assertTrue(result["continue"])
            self.assertNotIn("decision", result)

    def test_stop_hook_blocks_after_current_turn_chrome_devtools_usage_without_cleanup_decision(self):
        with tempfile.TemporaryDirectory() as tmp:
            transcript_path = Path(tmp) / "transcript.jsonl"
            self._write_transcript(
                transcript_path,
                [self._function_call_entry("mcp__chrome_devtools__take_screenshot", "turn-current")],
            )

            payload = {
                "transcript_path": str(transcript_path),
                "turn_id": "turn-current",
                "last_assistant_message": "Verification is complete.",
            }

            result = self._run_stop_hook(payload)

            self.assertEqual(result["decision"], "block")
            self.assertIn("Chrome DevTools MCP", result["reason"])
            self.assertIn("owned isolated profile", result["reason"])
            self.assertIn("do not close", result["reason"])

    def test_stop_hook_allows_when_cleanup_decision_is_already_in_final_message(self):
        with tempfile.TemporaryDirectory() as tmp:
            transcript_path = Path(tmp) / "transcript.jsonl"
            self._write_transcript(
                transcript_path,
                [self._function_call_entry("mcp__chrome_devtools__click", "turn-current")],
            )

            payload = {
                "transcript_path": str(transcript_path),
                "turn_id": "turn-current",
                "last_assistant_message": (
                    "I checked Chrome DevTools MCP browser ownership: this was "
                    "attached via browser-url, so I left the browser open and "
                    "closed only the task tab."
                ),
            }

            result = self._run_stop_hook(payload)

            self.assertTrue(result["continue"])
            self.assertNotIn("decision", result)

    def test_stop_hook_ignores_chrome_devtools_usage_from_other_turns(self):
        with tempfile.TemporaryDirectory() as tmp:
            transcript_path = Path(tmp) / "transcript.jsonl"
            self._write_transcript(
                transcript_path,
                [
                    self._function_call_entry("mcp__chrome_devtools__evaluate_script", "turn-old"),
                    self._function_call_entry("shell_command", "turn-current"),
                ],
            )

            payload = {
                "transcript_path": str(transcript_path),
                "turn_id": "turn-current",
                "last_assistant_message": "Done.",
            }

            result = self._run_stop_hook(payload)

            self.assertTrue(result["continue"])
            self.assertNotIn("decision", result)

    def test_stop_hook_allows_active_stop_hook_continuation_to_avoid_loops(self):
        with tempfile.TemporaryDirectory() as tmp:
            transcript_path = Path(tmp) / "transcript.jsonl"
            self._write_transcript(
                transcript_path,
                [self._function_call_entry("mcp__chrome_devtools__click", "turn-current")],
            )

            payload = {
                "transcript_path": str(transcript_path),
                "turn_id": "turn-current",
                "stop_hook_active": True,
                "last_assistant_message": "Done.",
            }

            result = self._run_stop_hook(payload)

            self.assertTrue(result["continue"])
            self.assertNotIn("decision", result)


if __name__ == "__main__":
    unittest.main()
