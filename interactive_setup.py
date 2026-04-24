#!/usr/bin/env python3
"""Interactive sz-skills setup script.

Run this when you want to choose which skills to install:
    python interactive_setup.py

Uses only Python's standard library so it works on macOS, Linux, and Windows.
"""

from __future__ import annotations

import sys
from pathlib import Path

from setup import (
    SKILLS_DIR,
    TARGET_ROOTS,
    _cyan,
    _green,
    _red,
    _yellow,
    discover_skills,
    install_skills,
)


def parse_selection(raw: str, skills: list[str]) -> list[str]:
    """Parse a comma-separated TUI selection into skill names."""
    text = raw.strip().lower()
    if text in {"all", "a"}:
        return list(skills)

    selected_indexes: list[int] = []
    for token in (part.strip().lower() for part in raw.split(",")):
        if not token:
            continue
        if token in {"all", "a"}:
            return list(skills)

        if "-" in token:
            start_text, end_text = token.split("-", 1)
            try:
                start = int(start_text)
                end = int(end_text)
            except ValueError as exc:
                raise ValueError(f"invalid range: {token}") from exc
            if start > end:
                raise ValueError(f"invalid descending range: {token}")
            selected_indexes.extend(range(start, end + 1))
            continue

        try:
            selected_indexes.append(int(token))
        except ValueError as exc:
            raise ValueError(f"invalid selection: {token}") from exc

    if not selected_indexes:
        raise ValueError("select at least one skill, or enter 'all'")

    selected: list[str] = []
    seen: set[str] = set()
    for index in selected_indexes:
        if index < 1 or index > len(skills):
            raise ValueError(f"selection out of range: {index}")
        skill = skills[index - 1]
        if skill not in seen:
            selected.append(skill)
            seen.add(skill)
    return selected


def render_menu(skills: list[str]) -> None:
    print(_cyan("Select skills to install"))
    print("Enter numbers separated by commas, ranges like 2-5, or 'all'.")
    print()
    for index, skill in enumerate(skills, start=1):
        print(f"  {index:2}. {skill}")
    print()


def prompt_for_skills(skills: list[str]) -> list[str]:
    while True:
        render_menu(skills)
        raw = input("Install: ").strip()
        try:
            return parse_selection(raw, skills)
        except ValueError as exc:
            print(_red(f"{exc}\n"))


def install_selected_skills(
    selected: list[str],
    *,
    skills_dir: Path = SKILLS_DIR,
    target_roots: list[Path] = TARGET_ROOTS,
) -> int:
    missing = [skill for skill in selected if not (skills_dir / skill / "SKILL.md").exists()]
    if missing:
        raise ValueError(f"selected skill not found: {', '.join(missing)}")
    return install_skills(selected, skills_dir=skills_dir, target_roots=target_roots)


def main() -> int:
    skills = discover_skills()
    if not skills:
        print(_red("No skills found."))
        return 1

    selected = prompt_for_skills(skills)
    print(_cyan(f"Creating links for: {', '.join(selected)}"))
    installed = install_selected_skills(selected)

    expected = len(selected) * len(TARGET_ROOTS)
    if installed != expected:
        print(_yellow(f"\nDone with warnings. Linked {installed} of {expected} targets."))
        return 1

    print(f"\n{_green('Done. Selected skills are linked.')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
