---
name: t3code-file-links
description: Use when returning, linking, or displaying local files in T3 Code, especially Windows paths, generated artifacts, screenshots, images, and videos the user needs to open or view.
---

# T3 Code file handoff

Verify the resolved path exists, then give exactly one representation for the outcome the user asked for:

- **Open:** a Markdown link with an absolute target in forward slashes. Wrap targets containing spaces in angle brackets: `[file.ts](</C:/Project Folder/file.ts>)`.
- **Locate:** the native absolute path as plain text, backslashes and spaces intact, unencoded.
- **View** (an image or video the user wants to see): embed it with Markdown image syntax, `![screenshot](</C:/Project Folder/shot.png>)`. T3 Code renders it inline.

Give both Open and Locate only when the user asks for both.
