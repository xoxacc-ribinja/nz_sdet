# Workflow: learning tasks and reviews

## Roles

- **Student:** writes solutions, runs tests, explains decisions and owns final code.
- **Assistant:** formulates assignments, reviews changes and updates documentation with clear evidence; does not mark PASS by assumption.

## Daily comprehension warm-up

On the student's first message of a calendar day in the learning chat, offer **3–4 short questions** on previously covered Python Core, pytest, Git and test-design concepts. Rotate subjects and occasionally revisit older material. Answers should be possible directly in chat **without writing or running code**; after the student answers, briefly review the reasoning and correct misconceptions.

These warm-ups are for retention, **not extra PASS criteria**, and must not change the contract of an active task. If the student explicitly wants to finish an ongoing task first, handle that work before the warm-up. Do not create a scheduled reminder or unsolicited notification: the warm-up is part of an active chat exchange.

## Workload and retention checks

- **Current weekly target: 12 hours from 2026-10-11**, explicitly chosen by the student instead of the former 3–5 hours. This is a flexible weekly target, not a daily schedule or catch-up quota. Do not increase hours automatically because recall is difficult. The target is an orientation, not a quota to compensate for missed days.
- Reduce nearly identical exercises. Reuse already taught tools in different problem contexts; do not increase difficulty or introduce unannounced syntax merely for novelty.
- Vary problem domains: alternate workplace QA/SDET scenarios, occasional game-development scenarios, and neutral everyday contexts. Test transfer of a familiar skill rather than recognition of recycled Task examples; no fixed domain ratio or new mandatory game-development track. Distinguish understanding a rule from reading/attention errors in feedback.
- Practice retrieval without hints through daily verbal warm-ups and revisit previously covered concepts after several days (spaced repetition).
- During review, report **correctness** separately from **independence**: solved without help / after a leading hint / after a full explanation. These labels are diagnostic, not extra acceptance criteria or grounds for retroactive regrading.
- In daily learning summaries distinguish time spent **writing code**, **engineering work** (requirements, test design, debugging, reviews, Git), and **process overhead** (resolving avoidable administrative mistakes). Do not present process overhead as coding practice. Do not invent precise splits where only estimates are available.
- Keep published task contracts and PASS criteria unchanged unless the student explicitly agrees to an update.

## Bug Investigation

Use Bug Investigation as a recurring exercise format alongside implementation and test design. Publish the full task contract first. The learner analyzes an unknown failure, reads the traceback and pytest output, proposes a root-cause hypothesis, finds and fixes the defect with a minimal change, and verifies by running tests. Distinguish detecting a defect from independently diagnosing it. Explain unfamiliar tools before requiring them.

Read small unfamiliar codebases only occasionally, without displacing the student's own coding. Do not require pytest internals, external open-source PRs, fixed weekly themes, or a day-by-day schedule. The agreed weekly target is 12 hours, with flexible distribution across days.

## Task publication and fixed acceptance criteria

**Before any new task is assigned for implementation**, the assistant must:

1. Read the repository guidance: `README.md`, `PROJECT_STATE.md`, `LEARNING_LOG.md`, `DECISIONS.md`, `docs/WORKFLOW.md`, `ROADMAP.md` and the relevant existing tasks.
2. Publish a numbered assignment Markdown file under `weekXX/documentation/task_NN.md` in GitHub, with an explicit contract, expected outputs/exceptions, scope, constraints, and PASS criteria. Provide its link to the student. The assignment must be available **before coding starts**, not reconstructed after completion.
3. Explain any new Python syntax, APIs or testing techniques **before** requiring them in an exercise. New constructs cannot appear as unannounced mandatory requirements.
4. Keep assessment against the published, agreed criteria. Do not introduce new mandatory edge cases, test counts, tools, or acceptance conditions mid-review.
5. If a change to requirements is genuinely needed, discuss it first, obtain agreement, and update the assignment in GitHub **before** evaluating against it. Never retroactively revoke an already accepted PASS.

## Work cycle

1. Confirm that the assignment is published in GitHub and review its fixed criteria.
2. Create a branch, e.g. `task/17`, from up-to-date `main`.
3. Implement without copying an AI-generated solution. Record any assistance used.
4. Run targeted checks and capture command plus meaningful output.
5. Push and open a Pull Request. Link the task and supply the code and actual test evidence; the student need not draft a separate explanatory essay.
6. Review the PR and conduct the explanation/defense interactively in the learning chat: test design, found defects, implementation choices, edge cases, and independence. The assistant gives concrete feedback and verifies results; do not replace the defense with a PR essay.
7. After the defense, the assistant prepares a concise, factual defense summary in a separate documentation branch/PR (normally in `LEARNING_LOG.md`, with `PROJECT_STATE.md` updated as appropriate). Record the contract/PR link, verdict, actual pytest command and results, detected defects, key reasoning, assistance used and follow-ups. Do not publish a verbatim chat transcript or invent evidence; do not require the student to write this summary.
8. Merge student and documentation PRs only after the owner accepts the result. Distinguish PR created from merged into `main`.


## Chat-first defense and GitHub summary (agreed 2026-10-12)

- Applies starting with Task 19 and to future tasks. The student defends the solution in the learning chat; the assistant leads the review and assesses understanding and independence there.
- The GitHub record is a concise **outcome of the defense**, not a prerequisite essay or full transcript. The assistant drafts it in a separate documentation PR after the discussion. It includes why any intentionally red tests are expected and the main implementation/test-design decisions.
- For Task 19, the published behavioral contract and PASS criteria stay unchanged. Its requirement to explain the defect in A and the algorithm in B is fulfilled by the chat defense plus the recorded summary, rather than a duplicate written explanation by the student in PR #17.
- The student owns the code and executes or supplies actual test evidence; the assistant must distinguish the student's log from a test run independently executed by the assistant. Never assert a run occurred when it did not.
- Documentation PRs are reviewed and merged by the repository owner; a documentation PR does not mean the learning task has already passed.

## Assistant documentation check

Before proposing a new task, reviewing a submission, recording PASS, or writing to GitHub, re-read the relevant repository documents and current assignment instead of relying only on chat context. If a document is outdated, flag it and propose a documentation change through a PR; do not silently assume it reflects the current state.

## GitHub access boundaries

- **Only repository:** `xoxacc-ribinja/nz_sdet`.
- **Only connection:** GitHub account `xoxacc-ribinja` (ChatGPT connection `Xoxacc_SDET`).
- Never modify repositories owned by `rpgarchive`.
- Before each write, verify the exact owner/repository and target branch.
- Prefer PRs to direct commits to `main`. Never force-push or rewrite historical submissions without explicit agreement.

## Hidden checks after defense

After a student submits a solution and completes code review and oral defense, the assistant may **occasionally** check the code with previously undisclosed input data. This is not mandatory for every task.

- Hidden inputs must follow the **original or explicitly agreed updated contract**; no surprise requirements or retroactive grading criteria.
- Do not disclose exact inputs before the defense. Keep the concrete cases out of the public assignment and PR until the check has been completed.
- Check meaningful boundaries and robustness, including empty collections, duplicates, ordering, invalid inputs and unwanted mutation **only when relevant to the contract**.
- If a runnable environment is available, execute the solution with the hidden inputs and record actual results. Otherwise describe the check as an unexecuted review or ask for a local run; never claim that unrun tests passed.
- After checking, explain failed cases and expected behavior. The student should diagnose and fix defects independently before another review.
- Record whether a hidden check was performed and its result in the learning log. Do not make every task a guessing game.

## Request decomposition and completion check

For a multi-part request, explicitly separate requested **actions**, **outputs** and **object-specific constraints**. A restriction on one output (e.g. “NZ Daily only in chat”) does not prohibit a separate requested GitHub documentation update.

Before closing a multi-step request, verify every deliverable against the request; distinguish prepared locally, written to a branch, PR opened, merged into main, and tests actually run. After GitHub writes, **read back** the target files from the target branch; inspect the PR file list, do not infer completion from a successful write API response.

When documenting earlier exercises, label original historical contracts separately from later reconstructions or reviews. Never change old PASS criteria retroactively or portray a retroactively published task as published before work.

## Reporting cadence and recovery

- **NZ DAILY**: produce a retrospective report for the preceding calendar day **daily on a morning schedule** (approximately 08:00 in the learner's local timezone, flexible delivery). Default destination is `reports/daily/YYYY-MM-DD.md` in GitHub, proposed through a separate branch and PR; verify the file and PR before reporting success. Do not claim the PR is merged until confirmed.
- **Chat-only exception**: if the learner explicitly asks for a specific report **only in chat**, do not publish that specific report in GitHub. Do not apply this exception to other reports or requested repository updates.
- **NZ WEEKLY** and monthly summaries remain on request unless separately changed. Reporting cadence does not impose a day-by-day study schedule. When activity evidence is unavailable, state the gap explicitly; do not fabricate time, tests or progress. Public reports must be anonymized.
- Distinguish real coding time, engineering work, and process overhead; do not treat missed study days as debt or automatically increase weekly hours.
- End-of-November check is a diagnostic skills gate (historically proposed 60–90 min unfamiliar Python task without AI and defense), not a rigid deadline or new PASS requirement.

## Evidence and reporting

- A failing test can be correct when it exposes a defect in code under test.
- A saved log is historical evidence, not a guarantee of current CI health.
- Publish only technical information safe for a public repository.
- Use `reports/templates/` for public, concise summaries. Keep private notes outside Git.

## Restoring context

Read in this order: `README.md` → `PROJECT_STATE.md` → `LEARNING_LOG.md` → `DECISIONS.md` → current task and PR.
