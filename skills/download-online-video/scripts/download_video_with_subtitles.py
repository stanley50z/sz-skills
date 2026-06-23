#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from urllib.parse import parse_qs, urlparse, urlunparse
from urllib.request import Request, urlopen


SUBTITLE_LANGS = "en.*,zh.*,ai-en,ai-zh"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Download a YouTube or Bilibili video with sidecar SRT subtitles.")
    parser.add_argument("--url", required=True)
    parser.add_argument("--target-path", required=True)
    parser.add_argument("--provider", choices=["auto", "youtube", "bilibili"], default="auto")
    parser.add_argument("--cookies-path")
    parser.add_argument("--ffmpeg-location")
    parser.add_argument("--yt-dlp-path")
    parser.add_argument("--no-cookies", action="store_true")
    parser.add_argument("--skip-download", action="store_true")
    parser.add_argument("--print-command", action="store_true")
    return parser.parse_args()


def host_without_www(hostname: str | None) -> str:
    host = (hostname or "").lower()
    return host[4:] if host.startswith("www.") else host


def normalize_source(raw_url: str, requested_provider: str) -> tuple[str, str]:
    parsed = urlparse(raw_url)
    if not parsed.scheme or not parsed.netloc:
        raise ValueError(f"Url must be an absolute YouTube or Bilibili URL: {raw_url}")

    host = host_without_www(parsed.hostname)
    allow_youtube = requested_provider in ("auto", "youtube")
    allow_bilibili = requested_provider in ("auto", "bilibili")

    if allow_youtube and (host == "youtube.com" or host.endswith(".youtube.com") or host == "youtu.be"):
        video_id = ""
        if host == "youtu.be":
            video_id = parsed.path.strip("/").split("/")[0]
        else:
            video_id = parse_qs(parsed.query).get("v", [""])[0]
        if not video_id:
            raise ValueError(f"YouTube URL does not include a video id: {raw_url}")
        return "youtube", f"https://www.youtube.com/watch?v={video_id}"

    if allow_bilibili and host == "b23.tv":
        return "bilibili", raw_url

    if allow_bilibili and (host == "bilibili.com" or host.endswith(".bilibili.com")):
        normalized = parsed._replace(scheme="https", netloc="www.bilibili.com", params="", query="", fragment="")
        return "bilibili", urlunparse(normalized)

    raise ValueError(f"Url must be a supported YouTube or Bilibili URL for provider '{requested_provider}': {raw_url}")


def format_selector(provider: str) -> str:
    if provider == "bilibili":
        return "bv*[vcodec^=avc1][format_id!*=112]+ba/bv*[format_id!*=112]+ba/best"
    return "bestvideo*+bestaudio/best"


def documents_dir() -> Path:
    return Path.home() / "Documents"


def default_cookie_path(provider: str) -> Path:
    name = "bilibili_cookie.txt" if provider == "bilibili" else "youtube_cookie.txt"
    return documents_dir() / name


def resolve_yt_dlp_command(explicit_path: str | None, print_command: bool) -> list[str]:
    if explicit_path:
        return [explicit_path]

    executable = shutil.which("yt-dlp")
    if executable:
        return [executable]

    probe = subprocess.run(
        [sys.executable, "-m", "yt_dlp", "--version"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    if probe.returncode == 0:
        return [sys.executable, "-m", "yt_dlp"]

    if print_command:
        return ["yt-dlp"]

    raise RuntimeError("yt-dlp is not on PATH. Install it with 'python -m pip install --user yt-dlp[default]' or pass --yt-dlp-path.")


def resolve_ffmpeg_location(explicit_location: str | None, print_command: bool) -> str:
    if explicit_location:
        return explicit_location

    env_location = os.environ.get("SZ_VIDEO_FFMPEG_LOCATION")
    if env_location:
        return env_location

    executable = shutil.which("ffmpeg")
    if executable:
        return executable

    try:
        import imageio_ffmpeg

        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        if print_command:
            return "ffmpeg"
        raise RuntimeError(
            "ffmpeg was not found locally. Install ffmpeg, install imageio-ffmpeg, set SZ_VIDEO_FFMPEG_LOCATION, or pass --ffmpeg-location."
        )


def cookie_header_from_netscape_file(cookie_path: Path) -> str:
    pairs: list[str] = []
    for raw_line in cookie_path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("# Netscape") or line.startswith("# This"):
            continue
        if line.startswith("#HttpOnly_"):
            line = line[len("#HttpOnly_") :]
        elif line.startswith("#"):
            continue

        parts = line.split("\t")
        if len(parts) >= 7:
            pairs.append(f"{parts[5]}={parts[6]}")

    return "; ".join(pairs)


def bilibili_cookie_is_logged_in(cookie_path: Path) -> bool:
    cookie_header = cookie_header_from_netscape_file(cookie_path)
    if not cookie_header:
        return False

    request = Request(
        "https://api.bilibili.com/x/web-interface/nav",
        headers={
            "Cookie": cookie_header,
            "User-Agent": "Mozilla/5.0",
        },
    )
    with urlopen(request, timeout=20) as response:
        payload = json.loads(response.read().decode("utf-8"))
    return bool(payload.get("data", {}).get("isLogin"))


def quote_arg(value: str) -> str:
    if re.fullmatch(r"[A-Za-z0-9_./:\\?=&,%@+-]+", value):
        return value
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def command_line(command: list[str]) -> str:
    return " ".join(quote_arg(part) for part in command)


def build_command(args: argparse.Namespace) -> tuple[str, Path | None, list[str]]:
    provider, normalized_url = normalize_source(args.url, args.provider)
    target_path = Path(args.target_path).expanduser().resolve()
    yt_dlp_command = resolve_yt_dlp_command(args.yt_dlp_path, args.print_command)
    ffmpeg_location = resolve_ffmpeg_location(args.ffmpeg_location, args.print_command)

    cookies_path = None
    if not args.no_cookies:
        cookies_path = Path(args.cookies_path).expanduser().resolve() if args.cookies_path else default_cookie_path(provider)

    command = [
        *yt_dlp_command,
        "--js-runtimes",
        "node",
        "--no-playlist",
        "-f",
        format_selector(provider),
        "-P",
        str(target_path),
        "-o",
        "%(title).200B.%(ext)s",
        "--ffmpeg-location",
        ffmpeg_location,
    ]

    if cookies_path:
        command += ["--cookies", str(cookies_path)]

    command += [
        "--write-subs",
        "--write-auto-subs",
        "--sub-langs",
        SUBTITLE_LANGS,
        "--convert-subs",
        "srt",
        "--newline",
        "--print",
        "after_move:filepath",
    ]

    if args.skip_download:
        command.append("--skip-download")

    command.append(normalized_url)
    return provider, cookies_path, command


def validate_runtime(provider: str, cookies_path: Path | None, target_path: Path, ffmpeg_location: str) -> None:
    target_path.mkdir(parents=True, exist_ok=True)

    ffmpeg_path = Path(ffmpeg_location).expanduser()
    if not shutil.which(ffmpeg_location) and not ffmpeg_path.exists():
        raise RuntimeError(f"ffmpeg location does not exist: {ffmpeg_location}")

    if cookies_path and not cookies_path.exists():
        raise RuntimeError(f"Cookies file does not exist: {cookies_path}. Pass --cookies-path or --no-cookies explicitly.")

    if provider == "bilibili" and cookies_path and not bilibili_cookie_is_logged_in(cookies_path):
        raise RuntimeError(
            f"Bilibili cookies are present but not logged in according to https://api.bilibili.com/x/web-interface/nav. "
            f"Refresh {cookies_path} before downloading Bilibili subtitles locally."
        )


def main() -> int:
    args = parse_args()
    try:
        provider, cookies_path, command = build_command(args)
        if args.print_command:
            print(command_line(command))
            return 0

        target_path = Path(args.target_path).expanduser().resolve()
        ffmpeg_location = command[command.index("--ffmpeg-location") + 1]
        validate_runtime(provider, cookies_path, target_path, ffmpeg_location)
        completed = subprocess.run(command, check=False)
        return completed.returncode
    except Exception as error:
        print(str(error), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
