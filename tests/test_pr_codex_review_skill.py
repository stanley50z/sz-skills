from pathlib import Path


SKILL_TEXT = (
    Path(__file__).parents[1] / "skills" / "pr-codex-review" / "SKILL.md"
).read_text(encoding="utf-8")


def test_skill_remains_user_invoked_only() -> None:
    assert "disable-model-invocation: true" in SKILL_TEXT
    assert "user-invoked" in SKILL_TEXT
    assert "Assume automatic Codex reviews are disabled" in SKILL_TEXT
    assert "Keep the cycle contract in these review comments" in SKILL_TEXT


def test_post_push_wait_uses_one_ten_minute_wakeup() -> None:
    assert "one 10-minute wait" in SKILL_TEXT
    assert "Do not implement the wait as repeated one-minute sleeps" in SKILL_TEXT


def test_manual_review_request_is_sent_once_per_exact_head() -> None:
    assert "Post exactly one custom review request for each head SHA" in SKILL_TEXT
    assert "Never post a duplicate request" in SKILL_TEXT


def test_manual_mode_posts_focused_initial_and_follow_up_requests_immediately() -> None:
    assert "Post the initial request immediately" in SKILL_TEXT
    assert "Report only P0/P1 correctness regressions introduced by this PR" in SKILL_TEXT
    assert "Post the follow-up request immediately after pushing" in SKILL_TEXT
    assert "<HEAD_SHA>" in SKILL_TEXT
    assert "<PREVIOUS_REVIEWED_SHA>" in SKILL_TEXT
    assert "This is a verification pass, not a fresh review" in SKILL_TEXT


def test_rounds_are_sha_scoped_and_reviewer_failures_stop_the_loop() -> None:
    assert "Match reviews and review comments to the exact current head SHA" in SKILL_TEXT
    assert "do not use timestamp alone" in SKILL_TEXT
    assert "Process at most one completed substantive round per head SHA" in SKILL_TEXT
    assert "usage limit" in SKILL_TEXT
    assert "Stop immediately and report the blocker" in SKILL_TEXT
    assert "Do not retry until the user explicitly resumes" in SKILL_TEXT


def test_custom_prompts_drive_the_review_cycle_to_convergence() -> None:
    assert "**Valid, design unstable**" in SKILL_TEXT
    assert "Never send a bare `@codex review` request" in SKILL_TEXT
    assert "Treat this as the complete initial review pass" in SKILL_TEXT
    assert "Report all independent P0/P1 root causes you can substantiate now" in SKILL_TEXT
    assert "This is a verification pass, not a fresh review" in SKILL_TEXT
    assert "Do not report unrelated defects from untouched original code" in SKILL_TEXT
    assert "return no findings now so this review closes cleanly" in SKILL_TEXT
    assert "`DESIGN STOP`" in SKILL_TEXT


def test_review_cycle_has_no_arbitrary_size_time_or_round_caps() -> None:
    assert "Hard-stop after 5 substantive rounds" not in SKILL_TEXT
    assert "2 hours of wall-clock loop time" not in SKILL_TEXT
    assert "initial changed-line count" not in SKILL_TEXT


def test_merge_requires_a_clean_review_of_the_unchanged_head() -> None:
    assert "Before merging" in SKILL_TEXT
    assert "the head SHA has not changed since the clean review" in SKILL_TEXT
    assert "no unresolved P0/P1 findings remain" in SKILL_TEXT
    assert "required validation is green" in SKILL_TEXT
