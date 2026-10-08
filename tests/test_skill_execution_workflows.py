import re
import shlex
import subprocess
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS = REPO_ROOT / "skills"
CODE_REVIEW = SKILLS / "code-review" / "SKILL.md"
IMPLEMENT = SKILLS / "implement" / "SKILL.md"
IMPLEMENT_SPEC = SKILLS / "implement-spec" / "SKILL.md"
TO_SPEC = SKILLS / "to-spec" / "SKILL.md"
TO_TICKETS = SKILLS / "to-tickets" / "SKILL.md"
REQUIREMENT_CHANGES = SKILLS / "implement" / "REQUIREMENT-CHANGES.md"
OWNED = [CODE_REVIEW, IMPLEMENT, IMPLEMENT_SPEC, TO_SPEC, TO_TICKETS]
USER_INVOKED = ["implement", "implement-spec", "to-spec", "to-tickets", "retro"]


def read(path):
    return path.read_text(encoding="utf-8")


def git(cwd, *args):
    return subprocess.run(
        ["git", *args], cwd=cwd, capture_output=True, text=True, check=True, timeout=30
    ).stdout


def scope_commands():
    """Git commands that code-review's first step tells the reviewer to run."""
    source = read(CODE_REVIEW)
    step = source[source.index("### 1."):source.index("### 2.")]
    return [cmd for cmd in re.findall(r"`(git [^`]+)`", step)]


class CodeReviewScopeBehaviorTests(unittest.TestCase):
    """Runs the review-scope commands from code-review against real Git repos."""

    def make_repo(self, root):
        git(root, "init", "-q", "-b", "main")
        git(root, "config", "user.email", "t@example.com")
        git(root, "config", "user.name", "t")
        git(root, "config", "core.autocrlf", "false")
        (root / ".gitignore").write_text("build/\n", encoding="utf-8")
        (root / "app.txt").write_text("base\n", encoding="utf-8")
        (root / "notes.txt").write_text("base\n", encoding="utf-8")
        git(root, "add", ".")
        git(root, "commit", "-q", "-m", "base")
        git(root, "switch", "-q", "-c", "feature")

    def run_scope(self, root):
        base = git(root, "merge-base", "main", "HEAD").strip()
        outputs = []
        for command in scope_commands():
            command = command.replace("<fixed-point>", "main").replace("<base>", base)
            outputs.append(git(root, *shlex.split(command)[1:]))
        return "\n".join(outputs)

    def test_scope_covers_committed_staged_unstaged_and_untracked_work(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_repo(root)
            (root / "app.txt").write_text("base\ncommitted-change\n", encoding="utf-8")
            git(root, "commit", "-q", "-am", "committed")
            (root / "staged.txt").write_text("staged-change\n", encoding="utf-8")
            git(root, "add", "staged.txt")
            (root / "notes.txt").write_text("base\nunstaged-change\n", encoding="utf-8")
            (root / "new_module.txt").write_text("untracked-change\n", encoding="utf-8")
            (root / "build").mkdir()
            (root / "build" / "out.txt").write_text("ignored-output\n", encoding="utf-8")

            scope = self.run_scope(root)

        for marker in ("committed-change", "staged-change", "unstaged-change", "new_module.txt"):
            with self.subTest(marker=marker):
                self.assertIn(marker, scope)
        self.assertNotIn("build/out.txt", scope)

    def test_new_feature_on_unchanged_head_has_a_non_empty_scope(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_repo(root)
            (root / "app.txt").write_text("base\nfeature-edit\n", encoding="utf-8")
            (root / "feature.txt").write_text("feature-file\n", encoding="utf-8")

            scope = self.run_scope(root)

        self.assertIn("feature-edit", scope)
        self.assertIn("feature.txt", scope)

    def test_untracked_secret_contents_never_enter_the_scope(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_repo(root)
            (root / ".env").write_text("API_TOKEN=hunter2-secret\n", encoding="utf-8")

            scope = self.run_scope(root)

        self.assertNotIn("hunter2-secret", scope)


class CodeReviewContractTests(unittest.TestCase):
    def test_uses_a_caller_resolved_comparison_point_without_asking(self):
        source = read(CODE_REVIEW)

        self.assertIn("resolved comparison point", source)
        self.assertIn("without asking", source)

    def test_empty_scope_check_includes_working_tree_changes(self):
        source = read(CODE_REVIEW)

        self.assertIn("unchanged `HEAD`", source)
        self.assertIn("commit list may be empty", source)

    def test_untracked_secrets_are_named_never_shown(self):
        source = read(CODE_REVIEW)

        self.assertIn("`.env*`", source)
        self.assertIn("never its contents", source)
        self.assertIn("never quote the value", source)

    def test_standards_and_spec_stay_separate_bounded_reviews(self):
        source = read(CODE_REVIEW)

        self.assertIn("**Standards sub-agent prompt**", source)
        self.assertIn("**Spec sub-agent prompt**", source)
        self.assertEqual(source.count("Under 400 words."), 2)
        self.assertIn("Do **not** merge or rerank findings", source)


class ImplementCloseOutTests(unittest.TestCase):
    def test_review_covers_uncommitted_work_from_the_branch_start_before_commit(self):
        source = read(IMPLEMENT)
        close_out = source[source.index("## Close Out"):]

        self.assertIn("start commit", source)
        review = close_out.index("`code-review`")
        commit = close_out.index("commit skill")
        self.assertLess(review, commit)
        self.assertIn("start commit as the resolved comparison point", close_out)

    def test_pr_skill_writes_only_the_body_and_implement_keeps_pr_ownership(self):
        close_out = read(IMPLEMENT).split("## Close Out", 1)[1]

        self.assertIn("load the `pr` skill to write the body", close_out)
        for kept in (
            "targets that same default branch explicitly",
            "must not be a draft",
            "links the relevant spec or tickets",
            "validation performed",
            "closing reference",
            "Ask the user to test the feature themselves",
        ):
            with self.subTest(kept=kept):
                self.assertIn(kept, close_out)

    def test_test_policy_points_to_tdd_instead_of_restating_it(self):
        source = read(IMPLEMENT)

        self.assertIn("load the `tdd` skill", source)
        self.assertIn("done gate", source)
        for restated in ("DOM assertions", "snapshot tests", "Version upgrades"):
            with self.subTest(restated=restated):
                self.assertNotIn(restated, source)
        self.assertIn("No fallbacks, no silent failure", source)

    def test_requirement_changes_have_one_canonical_policy(self):
        policy = read(REQUIREMENT_CHANGES)

        steps = [policy.index(step) for step in ("**Spec**", "**Tickets**", "**Tests**", "**Implementation**")]
        self.assertEqual(steps, sorted(steps))
        self.assertIn("same authority as an initial requirement", policy)
        for path in (IMPLEMENT, IMPLEMENT_SPEC, TO_TICKETS):
            with self.subTest(path=path.parent.name):
                source = read(path)
                self.assertIn("REQUIREMENT-CHANGES.md", source)
                self.assertNotIn("same authority as an initial requirement", source)

    def test_requirement_changes_cover_direct_issues_and_landed_work(self):
        policy = read(REQUIREMENT_CHANGES)

        self.assertIn("implementation issue", policy)
        self.assertIn("no spec exists", policy)
        self.assertIn("already landed", policy)
        self.assertIn("pull request body and Evidence", policy)
        self.assertIn("rerun", policy)
        evidence = policy.index("pull request body and Evidence")
        self.assertGreater(evidence, policy.index("**Implementation**"))


class ReadmeClaimTests(unittest.TestCase):
    def test_implement_spec_row_describes_actual_ownership(self):
        row = next(line for line in read(REPO_ROOT / "README.md").splitlines() if "[implement-spec]" in line)

        self.assertNotIn("queue", row)
        for claim in ("tdd", "integration validation", "code review", "PR"):
            with self.subTest(claim=claim):
                self.assertIn(claim, row)


class ImplementSpecOrchestrationTests(unittest.TestCase):
    def test_stays_user_invoked(self):
        skill = SKILLS / "implement-spec"

        self.assertIn("disable-model-invocation: true", read(skill / "SKILL.md"))
        self.assertIn("allow_implicit_invocation: false", read(skill / "agents" / "openai.yaml"))

    def test_reuses_policy_without_running_single_ticket_implement(self):
        source = read(IMPLEMENT_SPEC)

        self.assertIn("load the `tdd` skill", source)
        self.assertIn("../implement/REQUIREMENT-CHANGES.md", source)
        self.assertNotIn("Skill tool", source)
        self.assertNotRegex(source, r"(load|run|use)s? (the )?`implement` skill")

    def test_integration_branch_starts_from_the_default_branch_tip(self):
        source = read(IMPLEMENT_SPEC)

        self.assertIn("repository's default branch", source)
        self.assertIn("latest remote tip", source)
        self.assertIn("targets the default branch", source)

    def test_workers_own_isolated_worktrees_and_commits(self):
        source = read(IMPLEMENT_SPEC)

        self.assertIn("task-owned", source)
        self.assertIn("staging exact paths", source)

    def test_cleanup_keeps_the_integration_branch_and_open_pr(self):
        steps = read(IMPLEMENT_SPEC).split("## Steps", 1)[1]
        cleanup = steps[steps.rindex("\n10."):]

        self.assertIn("Keep the integration branch and its open pull request", cleanup)
        self.assertIn("task-owned ticket and fix worktrees", cleanup)
        self.assertIn("after their work has landed", cleanup)

    def test_worktrees_get_inputs_securely_and_skips_are_not_green(self):
        source = read(IMPLEMENT_SPEC)

        self.assertIn("installs dependencies", source)
        self.assertIn("gitignored test inputs", source)
        self.assertIn("without committing", source)
        self.assertIn("../tdd/SKILL.md", source)

    def test_workers_defer_review_to_the_orchestrator(self):
        source = read(IMPLEMENT_SPEC)

        self.assertIn("caller owns the review phase", source)

    def test_landing_is_serialized_and_resyncs_the_latest_tip(self):
        source = read(IMPLEMENT_SPEC)

        self.assertIn("one landing at a time", source)
        self.assertIn("latest integration tip", source)

    def test_frontier_advances_on_landing_not_issue_closure(self):
        source = read(IMPLEMENT_SPEC)

        self.assertIn("once it lands on the integration branch", source)
        self.assertIn("not from issue state", source)

    def test_aggregate_validation_reruns_after_merges_and_review_fixes(self):
        source = read(IMPLEMENT_SPEC)
        steps = source[source.index("## Steps"):].lower()

        landed = steps.index("every ticket has landed")
        validate = steps.index("aggregate validation")
        review = steps.index("load the `code-review` skill")
        rerun = steps.index("rerun the aggregate validation")
        body = steps.index("load the `pr` skill to write the body")
        self.assertLess(landed, validate)
        self.assertLess(validate, review)
        self.assertLess(review, rerun)
        self.assertLess(rerun, body)
        self.assertIn("real entry point", steps)

    def test_unpinned_human_decisions_pause_instead_of_being_invented(self):
        source = read(IMPLEMENT_SPEC)

        self.assertIn("decision the spec and tickets do not pin", source)
        self.assertIn("ask the user, record the answer", source.lower())

    def test_close_out_keeps_links_closing_refs_and_user_testing(self):
        source = read(IMPLEMENT_SPEC)

        self.assertIn("closing reference for every implementation ticket", source)
        self.assertIn("ask the user to test", source.lower())


class SpecAndTicketTests(unittest.TestCase):
    def test_user_stories_ask_for_completeness_not_length(self):
        source = read(TO_SPEC)

        self.assertNotIn("A LONG", source)
        self.assertNotIn("extremely extensive", source)
        self.assertIn("every agreed requirement", source)

    def test_tickets_publish_only_to_github(self):
        source = read(TO_TICKETS)

        for local in ("Local files", "local-ticket-template", "local tracker"):
            with self.subTest(local=local):
                self.assertNotIn(local, source)
        self.assertIn("native parent/sub-issue relationship", source)
        self.assertIn("## Requirement", source)
        self.assertIn("For UI work, write acceptance criteria", source)

    def test_ticketing_changes_propagate_to_the_spec_first(self):
        source = read(TO_TICKETS)

        self.assertIn("new requirement", source)
        self.assertIn("spec first", source)

    def test_handoff_offers_both_execution_routes_for_the_user_to_choose(self):
        handoff = read(TO_TICKETS).split("## Handoff", 1)[1]

        self.assertIn("`/implement`", handoff)
        self.assertIn("`/implement-spec`", handoff)
        self.assertIn("user chooses", handoff)


class HarnessLoadingTests(unittest.TestCase):
    def test_owned_skills_use_the_global_load_policy(self):
        for path in OWNED:
            with self.subTest(skill=path.parent.name):
                self.assertNotIn("Skill tool", read(path))

    def test_user_invoked_skills_are_only_suggested_to_the_user(self):
        for path in OWNED:
            source = read(path)
            for name in USER_INVOKED:
                with self.subTest(skill=path.parent.name, target=name):
                    self.assertNotRegex(source, rf"[Ll]oad (the )?`{name}`")
                    for line in source.splitlines():
                        if re.search(rf"\b(use|run|invoke|call|with) `/{name}`", line, re.I):
                            self.assertIn("user", line.lower())


if __name__ == "__main__":
    unittest.main()
