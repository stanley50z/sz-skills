# AGENTS.md

This repo is the source of truth for coding-harness skills that get linked into:

- `~/.claude/skills/`
- `~/.codex/skills/`
- `~/.config/opencode/skills/`

`setup.py` auto-discovers every directory under `skills/` that contains a `SKILL.md` file, then links those skills into the harness directories. Do not add skills anywhere else in this repo.

## Repo Model

There are exactly three skill types in this repo:

1. Personal skills
2. Original vendor skills
3. Customized vendor skills

Always keep `README.md` and `update.py` aligned with the chosen type.

## Naming Rules

- The local skill directory name should match the skill name used in `SKILL.md`.
- For vendor skills, keep the official upstream skill name unchanged.
- Do not rename a vendor skill to a simplified local alias.

## Personal Skills

Use this when the skill is authored locally and is not synced from any upstream vendor repo.

Required steps:

1. Create `skills/<skill-name>/SKILL.md`.
2. Add any supporting files inside that same `skills/<skill-name>/` directory.
3. Add the skill to the `My Skills` section in `README.md`.
4. Do not add it to `UPSTREAM` in `update.py`.
5. Do not add it to `PATCHED` in `update.py`.

## Original Vendor Skills

Use this when the skill should stay auto-updatable from its upstream source.

Required steps:

1. Create or keep the local directory as `skills/<official-upstream-skill-name>/`.
2. Add or update the matching `UPSTREAM["<skill-name>"]` entry in `update.py`.
3. If the upstream content comes from multiple paths, keep that logic in `UPSTREAM`.
4. Add the skill to the `Vendor Skills` section in `README.md` with its source link.
5. Do not add it to `PATCHED` in `update.py`.

Result:

- `python update.py` should keep refreshing this skill from upstream.

## Customized Vendor Skills

Use this only for a vendor skill that is already installed in this repo as an original vendor skill.

Do not create a brand-new customized vendor skill from scratch. The expected flow is:

1. The skill already exists locally as an original vendor skill.
2. You make local edits to that installed vendor skill.
3. You convert it into a customized vendor skill so future updates do not overwrite those edits.

Required steps:

1. Keep the existing local directory and upstream skill name.
2. Keep its provenance in `UPSTREAM` in `update.py`.
3. Add the skill name to `PATCHED` in `update.py` so `python update.py` skips it.
4. Move or list the skill in the `Vendor Skills (customized)` section in `README.md`.
5. If useful, document the customization reason in `README.md` or a repo doc.

Result:

- `python update.py` preserves the local customized version instead of overwriting it.

## File Update Rules

- `README.md` is the human-facing catalog and should always reflect the current classification.
- `update.py` is the machine-facing source of truth for vendor-backed skills.
- `setup.py` installs every discovered skill folder; it does not decide skill type.

## Verification Checklist

After adding or reclassifying a skill:

1. Confirm the skill directory contains `SKILL.md`.
2. Confirm the directory name matches the intended skill name.
3. Update `README.md` for the correct category.
4. Update `update.py` if the skill is vendor-backed.
5. Run `python setup.py`.
6. Verify the skill appears in:
   - `~/.claude/skills/`
   - `~/.codex/skills/`
   - `~/.config/opencode/skills/`

## Common Mistakes To Avoid

- Adding a vendor skill to `PATCHED` before it exists locally.
- Renaming a vendor skill away from its official upstream name.
- Forgetting to update `README.md` after changing skill type.
- Editing `setup.py` to special-case one skill type.
- Putting skill files outside `skills/<skill-name>/`.
