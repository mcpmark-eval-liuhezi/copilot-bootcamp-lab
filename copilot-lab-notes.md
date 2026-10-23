# copilot-lab-notes

> Running log for the Copilot bootcamp lab demo.
> NOTE: This log lives in the repo as `copilot-lab-notes.md` because the API token used
> to build this lab does not have gist permissions. If you want it as a real gist,
> create one from this file (or re-run with a token that has the `gist` scope).

## Summary

Demo setup for a hands-on session on how the GitHub Copilot coding agent fits into our
normal GitHub workflow. Throwaway repo — safe to delete after the session.

- **Repo:** `mcpmark-eval-liuhezi/copilot-bootcamp-lab`
- **Default branch:** `main`, initialized with a README

## Repo & CI setup

- `main` contains `README.md` plus `.github/workflows/ci.yml`.
- CI workflow (`ci.yml`), committed to the default branch and active right away:
  - Triggers: `push` and `pull_request` events
  - Runner: `ubuntu-latest`
  - Steps: check out code, set up Python 3.11 (`actions/setup-python@v5`), install
    `pytest`, run `pytest`
- The workflow file was double-checked and is confirmed present on `main`.

## Lab flow — results

- **Branch:** `feature/greeting` — contains `greet.py` with `greet(name)`
  - `greet('World')` → `"Hello, World!"`
  - `greet('')` → `"Hello, stranger!"`
- **Pull request:** #1 — "Add greeting module" (`feature/greeting` → `main`)
- **Issue:** #2 — "Add unit tests for the greeting module"
  - Duplicate check done before filing: no existing issue matched.
  - Issue types are not available on this account/org (403 from the API), so no
    issue type was tagged.
  - Copilot assignment: **failed** — Copilot is not available as an assignee for
    this issue (Copilot coding agent not enabled for this repo/org). The issue has
    a comment pointing Copilot at the PR branch for context anyway.
- **Workflow list:** shows exactly one workflow — "CI" at `.github/workflows/ci.yml`,
  state `active`. It has already run (4 runs): the latest, on the PR, failed with
  pytest exit code 5 ("no tests ran") because no tests exist yet — which is exactly
  what Issue #2 asks Copilot to fix.
- **Review dry run:** a draft review with one line comment on `greet.py` was started
  on PR #1 and then discarded without submitting. PR #1 ends up with **no** reviews
  and no review comments from this session.
