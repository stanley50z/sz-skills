---
name: t3code-file-links
description: Use when returning, linking, or displaying local files in T3 Code, especially Windows paths, generated artifacts, screenshots, and images the user needs to open or view.
---

# T3 Code file handoff

Treat these as separate outcomes:

- **Open:** a clickable link navigates to a local file.
- **Locate:** a native absolute path lets the user copy the location into Explorer, Finder, or a terminal.
- **View:** an image is attached to the response with the local image-viewing tool.

## Handoff

Before returning a file, verify that the resolved path exists. Provide one representation for the requested outcome:

- For opening a file, provide only a clickable Markdown link. Use an absolute target with forward slashes. When the target contains spaces, wrap it in angle brackets: `[file.png](</C:/Project Folder/file.png>)`.
- For locating a file, or when a clickable link is unavailable, provide only the native absolute path as unformatted plain text. On Windows, preserve backslashes and spaces; do not percent-encode it.
- Include both forms only when the user explicitly requests both opening and locating the file.
- When the user asks to see, show, preview, or view a local image, attach the image with the local image-viewing tool. A path or Markdown link alone does not display it.

The handoff is complete when the requested outcome is present without an unrequested duplicate representation.
