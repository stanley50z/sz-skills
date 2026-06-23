---
name: download-online-video
description: Use when downloading YouTube or Bilibili videos, audio, or subtitles with yt-dlp in sz-video, especially when the same command needs to run locally across Windows, macOS, Linux, and Docker.
---

# Download Online Video

Use one `yt-dlp` shape for YouTube and Bilibili downloads so local checks match the Docker-backed media-library route.

## Quick Start

From the repo root, download video plus sidecar subtitles locally:

```bash
python .agents/skills/download-online-video/scripts/download_video_with_subtitles.py \
  --url "https://www.youtube.com/watch?v=VIDEO_ID" \
  --target-path "$HOME/Movies/sz-video-downloads"
```

For Bilibili:

```bash
python .agents/skills/download-online-video/scripts/download_video_with_subtitles.py \
  --url "https://www.bilibili.com/video/BV..." \
  --target-path "$HOME/Movies/sz-video-downloads"
```

On Windows PowerShell, use the same Python script with backticks instead of backslashes if you split lines.

The helper defaults to `~/Documents/youtube_cookie.txt` for YouTube and `~/Documents/bilibili_cookie.txt` for Bilibili. Override with `--cookies-path`, or pass `--no-cookies` only for public videos that do not need cookies.

For Bilibili runs, the helper checks the cookie file against Bilibili's login API before invoking `yt-dlp`. If it says the cookies are logged out, refresh `~/Documents/bilibili_cookie.txt` from a logged-in browser session before testing subtitles again.

## Required Flags

Keep these flags aligned with `apps/server/src/routes.ts`:

| Purpose | Flags |
|---|---|
| Single video only | `--no-playlist` |
| YouTube quality | `-f "bestvideo*+bestaudio/best"` |
| Bilibili quality | `-f "bv*[vcodec^=avc1][format_id!*=112]+ba/bv*[format_id!*=112]+ba/best"` |
| Manual subtitles | `--write-subs` |
| YouTube auto captions | `--write-auto-subs` |
| English, Chinese, Bilibili AI subtitles | `--sub-langs "en.*,zh.*,ai-en,ai-zh"` |
| Premiere-friendly subtitle sidecars | `--convert-subs srt` |
| Local merge/subtitle conversion | `--ffmpeg-location <ffmpeg>` when `ffmpeg` is not on `PATH` |

Bilibili AI subtitles are exposed as ordinary subtitle tracks with `ai-*` language codes, so `--write-subs` and the `ai-en,ai-zh` language selector are required.

## Local Prerequisites

Check local tools before blaming Docker:

```bash
python -m yt_dlp --version
ffmpeg -version
```

If `ffmpeg` is not on `PATH`, install it or let the helper detect `imageio-ffmpeg`:

```bash
python -m pip install --user imageio-ffmpeg
python -c "import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())"
```

## Verification

Print the exact local command without running a download:

```bash
python .agents/skills/download-online-video/scripts/download_video_with_subtitles.py \
  --url "https://youtu.be/dQw4w9WgXcQ?si=share" \
  --target-path "$TMPDIR/sz-video-ytdlp-test" \
  --print-command
```

Fetch subtitles only:

```bash
python .agents/skills/download-online-video/scripts/download_video_with_subtitles.py \
  --url "https://www.youtube.com/watch?v=VIDEO_ID" \
  --target-path "$TMPDIR/sz-video-ytdlp-test" \
  --skip-download
```

Validate Bilibili cookies and subtitle selection without printing secret values:

```bash
python .agents/skills/download-online-video/scripts/download_video_with_subtitles.py \
  --url "https://www.bilibili.com/video/BV15v411g7VP" \
  --target-path "$TMPDIR/sz-video-ytdlp-test" \
  --skip-download
```

`BV15v411g7VP` is a known `yt-dlp` Bilibili subtitle fixture from upstream issue `yt-dlp/yt-dlp#6357`. A logged-out cookie file fails before download; valid cookies let `yt-dlp` request `ai-zh`/`ai-en` sidecars.

Omit `--skip-download` for the full video plus subtitles path.

## Common Mistakes

- Do not drop `--write-subs`; Bilibili AI captions are not covered by `--write-auto-subs` alone.
- Do not drop `ai-en,ai-zh`; those language selectors are what capture Bilibili AI subtitle tracks.
- Do not use the Docker cookie paths locally. Use `~/Documents/*_cookie.txt` or pass `--cookies-path`.
- Do not remove `--print "after_move:filepath"` from the server route; downstream path tracking depends on it.
