# Workflow: learning tasks and reviews

## Roles

- **Student:** writes solutions, runs tests, explains decisions and owns final code.
- **Assistant:** formulates assignments, reviews changes and updates documentation with clear evidence; does not mark PASS by assumption.

## Work cycle

1. Read `PROJECT_STATE.md`, `ROADMAP.md` and the relevant assignment.
2. Create a branch, e.g. `task/17`, from up-to-date `main`.
3. Implement without copying an AI-generated solution. Record any assistance used.
4. Run targeted checks and capture command plus meaningful output.
5. Push and open a Pull Request. Link task, summarize approach and unresolved questions.
6. Review diff and discuss boundary cases, independent decisions and regressions.
7. Merge only after the owner accepts the result. Update `LEARNING_LOG.md` and `PROJECT_STATE.md`.

## GitHub access boundaries

- **Only repository:** `xoxacc-ribinja/nz_sdet`.
- **Only connection:** GitHub account `xoxacc-ribinja` (ChatGPT connection `Xoxacc_SDET`).
- Never modify repositories owned by `rpgarchive`.
- Before each write, verify the exact owner/repository and target branch.
- Prefer PRs to direct commits to `main`. Never force-push or rewrite historical submissions without explicit agreement.

## Evidence and reporting

- A failing test can be correct when it exposes a defect in code under test.
- A saved log is historical evidence, not a guarantee of current CI health.
- Publish only technical information safe for a public repository.
- Use `reports/templates/` for public, concise summaries. Keep private notes outside Git.

## Restoring context

Read in this order: `README.md` → `PROJECT_STATE.md` → `LEARNING_LOG.md` → `DECISIONS.md` → current task and PR.
