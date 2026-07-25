from pathlib import Path


SKILL_TEXT = (
    Path(__file__).parents[1] / "skills" / "pr-codex-review" / "SKILL.md"
).read_text(encoding="utf-8")


def test_post_push_wait_uses_one_ten_minute_wakeup() -> None:
    assert "one 10-minute wait" in SKILL_TEXT
    assert "Do not implement the wait as repeated one-minute sleeps" in SKILL_TEXT


def test_manual_review_request_is_only_a_no_response_fallback() -> None:
    assert "Only post `@codex review`" in SKILL_TEXT
    assert "reaction on the PR" in SKILL_TEXT
    assert "review-thread reply" in SKILL_TEXT
    assert "Never post a duplicate request" in SKILL_TEXT
