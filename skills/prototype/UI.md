# UI Prototype

Generate **several radically different UI options** as throwaway mocks and
show every option at once on one self-contained HTML comparison page. The
user compares them side by side, picks one (or steals bits from each), and
only then does anything touch the real components.

If the question is about logic/state rather than what something looks like,
this is the wrong branch. Use [LOGIC.md](LOGIC.md).

## When this is the right shape

- "What should this page look like?"
- "I want to see a few options for this dashboard before committing."
- "Try a different layout for the settings screen."
- Any time the user would otherwise spend a day picking between three vague
  mockups in their head.

## Process

### 1. State the question and pick N

Default to **3 options**. More than 5 stops being radically different and
starts being noise, so cap there. Write the question at the top of the page,
e.g. "Three options for the settings page: which layout makes the account
actions easiest to find?"

### 2. Design radically different options

Load `frontend-design` for the visual direction; it is the sole visual-design
skill. Use the native Skill tool when the harness has one, otherwise read its
`SKILL.md`. Follow the project's existing design tokens.

Options must be **structurally different**: different layout, information
hierarchy, and primary affordance, not just different colours. Three
slightly-tweaked card grids isn't a UI prototype, it's wallpaper. If two
drafts come out too similar, redo one with an explicitly different structure.

Mock each option **in context**: reproduce the host page's real header,
sidebar, and realistic data density around it. An option alone on a blank
canvas looks fine in a vacuum and hides the design problems a populated page
exposes.

### 3. Build the comparison page

One self-contained HTML comparison page: plain HTML/CSS/JS, everything inline,
opens by double-click from `file://`. Every option is rendered on the page at
once, each in its own panel with a clear label that matches the question
(`A: Sidebar layout`, `B: ...`). The user can see and compare all options
without clicking through them.

Name and locate the file per the [SKILL](SKILL.md) rules (next to the page it
is for, obviously a prototype). Leave the real components untouched until the
user picks an option.

Default to the static page. Use a dev server only when the comparison
genuinely needs one (for example, the mocks must run against the project's
build of its design system). Then:

- Pick the port from `~/LOCALHOST_PORTS.md`, verify it is free, and bind to
  all interfaces (`--host` / `0.0.0.0`) so the page is reachable over
  Tailscale as well as localhost.
- Surface both URLs: `http://localhost:<port>/...` and
  `http://<tailscale-hostname>:<port>/...` (hostname from `tailscale status`).
- Track the server's PID. Once you have verified the page, stop it and its
  children before handing off and verify the port is released, unless the
  user explicitly asks to leave it running. Restart it if the user wants to
  review again.

### 4. Hand it over

Verify the page in a desktop browser, then give the user a ctrl-clickable link
to it (and the server URLs, if the user asked to keep the server running) in
the message that asks them to choose, before asking which option they want.
Keep the page available until they decide; that means the file, not a running
process. The interesting feedback is usually **"I want the header from B with
the sidebar from C"**: that's the actual design they want.

### 5. Capture the answer and clean up

Once an option has won, capture the answer (which option and why), then
capture the prototype the way the [SKILL](SKILL.md) describes: the comparison
page lands on the throwaway branch as the primary source, not in main. Build
the winner into the real components properly; the mock was written under
prototype constraints.

## Anti-patterns

- **Options that differ only in colour or copy.** That's a tweak, not a
  prototype. Real options disagree about structure.
- **Sharing too much between options.** A shared header is fine; a shared
  layout defeats the point.
- **Wiring options to real mutations.** The question is "what should this
  look like", not "does the backend work".
- **Promoting the mock directly to production.** Rewrite it properly when you
  fold it in.
