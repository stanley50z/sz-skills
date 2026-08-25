---
name: t3code-file-links
description: Use when returning, linking, or displaying local files in T3 Code, especially Windows paths, generated artifacts, screenshots, and images the user needs to open or view.
---

# T3 Code file handoff

Treat these as separate outcomes:

- **Open:** a clickable link navigates to a file inside the current thread's project.
- **Locate:** a native absolute path lets the user copy the location into Explorer, Finder, or a terminal.
- **View:** an image is attached to the response with the local image-viewing tool.

## Handoff

Before returning a file, verify that the resolved path exists and identify whether it is inside the current thread's project.

- Always print the native absolute path as unformatted plain text. On Windows, preserve backslashes and spaces; do not percent-encode it.
- For a file inside the project, also provide a clickable Markdown link when useful. Use an absolute target with forward slashes. When the target contains spaces, wrap it in angle brackets: `[file.png](</C:/Project Folder/file.png>)`.
- For a file outside the project, provide only the native absolute path. Do not present it as a clickable Markdown link.
- When the user asks to see, show, preview, or view a local image, attach the image with the local image-viewing tool. A path or Markdown link alone does not display it.

The handoff is complete when the response contains the exact native path and, when viewing was requested, the rendered image.
