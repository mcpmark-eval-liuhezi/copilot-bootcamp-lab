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

## Lab flow

- Feature branch: `feature/greeting`, containing `greet.py`
- Results recorded in the next section once everything is in place.
