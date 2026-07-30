from pathlib import Path


SKILL_TEXT = (
    Path(__file__).parents[1] / "skills" / "pr-codex-review" / "SKILL.md"
).read_text(encoding="utf-8")


def test_skill_remains_user_invoked_only() -> None:
    assert "disable-model-invocation: true" in SKILL_TEXT
    assert "user-invoked" in SKILL_TEXT
    assert "Assume automatic Codex reviews are disabled" in SKILL_TEXT


def test_post_push_wait_uses_one_ten_minute_wakeup() -> None:
    assert "one 10-minute wait" in SKILL_TEXT
    assert "Do not implement the wait as repeated one-minute sleeps" in SKILL_TEXT


def test_manual_review_request_is_sent_once_per_exact_head() -> None:
    assert "Only post `@codex review`" in SKILL_TEXT
    assert "exact head SHA" in SKILL_TEXT
    assert "Never post a duplicate request" in SKILL_TEXT


def test_manual_mode_posts_focused_initial_and_follow_up_requests_immediately() -> None:
    assert "Post the initial request immediately" in SKILL_TEXT
    assert "Report only P0/P1 correctness regressions introduced by this PR" in SKILL_TEXT
    assert "Post the follow-up request immediately after pushing" in SKILL_TEXT
    assert "<HEAD_SHA>" in SKILL_TEXT
    assert "<PREVIOUS_REVIEWED_SHA>" in SKILL_TEXT
    assert "Do not start a fresh search of unrelated untouched parts" in SKILL_TEXT


def test_rounds_are_sha_scoped_and_reviewer_failures_stop_the_loop() -> None:
    assert "Match reviews and review comments to the exact current head SHA" in SKILL_TEXT
    assert "do not use timestamp alone" in SKILL_TEXT
    assert "Process at most one completed substantive round per head SHA" in SKILL_TEXT
    assert "usage limit" in SKILL_TEXT
    assert "Stop immediately and report the blocker" in SKILL_TEXT
    assert "Do not retry until the user explicitly resumes" in SKILL_TEXT


def test_convergence_guard_checkpoints_and_stops_unstable_review_loops() -> None:
    assert "**Valid, design unstable**" in SKILL_TEXT
    assert "Group findings by root cause before changing code" in SKILL_TEXT
    assert "After 3 substantive rounds" in SKILL_TEXT
    assert "Hard-stop after 5 substantive rounds" in SKILL_TEXT
    assert "same missing invariant or core area in two consecutive rounds" in SKILL_TEXT
    assert "2 hours of wall-clock loop time" in SKILL_TEXT
    assert "max(500 changed lines, 25% of the initial changed-line count)" in SKILL_TEXT
    assert "explicitly authorizes continuation with a new budget" in SKILL_TEXT


def test_merge_requires_a_clean_review_of_the_unchanged_head() -> None:
    assert "Before merging" in SKILL_TEXT
    assert "the head SHA has not changed since the clean review" in SKILL_TEXT
    assert "no unresolved P0/P1 findings remain" in SKILL_TEXT
    assert "required validation is green" in SKILL_TEXT
