from __future__ import annotations

from pathlib import Path
import subprocess
import sys
import unittest


SCRIPT = Path(__file__).parents[1] / "scripts" / "download_video_with_subtitles.py"


class DownloadVideoCliTests(unittest.TestCase):
    def test_default_destination_is_the_user_downloads_folder(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--url",
                "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                "--no-cookies",
                "--print-command",
            ],
            capture_output=True,
            text=True,
            timeout=20,
        )

        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertIn(f"-P {Path.home() / 'Downloads'}", completed.stdout)
        self.assertNotIn("sz-video-downloads", completed.stdout)


if __name__ == "__main__":
    unittest.main()
