"""Check Windows launch flags without opening any subprocess windows."""

import importlib.util
import os
from pathlib import Path
import subprocess
import unittest
from unittest.mock import Mock, patch


spec = importlib.util.spec_from_file_location(
    'openwiki_runner', Path(__file__).resolve().parents[1] / 'scripts/openwiki_post_commit.py')
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


@unittest.skipUnless(os.name == 'nt', 'Windows console creation policy')
class WindowsLaunchTests(unittest.TestCase):
    def test_git_generation_and_timeout_cleanup_suppress_console_windows(self):
        process = Mock(pid=123, returncode=0)
        process.communicate.side_effect = [subprocess.TimeoutExpired('openwiki', 1), (b'', b'')]
        with patch.object(runner.subprocess, 'run', return_value=Mock(returncode=0, stdout='')) as run:
            with patch.object(runner.subprocess, 'Popen', return_value=process) as launch:
                runner.git(Path.cwd(), 'status', env={})
                runner.clean_git_env()
                with self.assertRaises(subprocess.TimeoutExpired):
                    runner.generate('openwiki', Path.cwd(), {}, 1)
        for call in [*run.call_args_list, *launch.call_args_list]:
            self.assertTrue(call.kwargs.get('creationflags', 0) & subprocess.CREATE_NO_WINDOW,
                            f'Console window allowed for {call.args[0][0]}')


if __name__ == '__main__':
    unittest.main()
