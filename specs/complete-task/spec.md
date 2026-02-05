# Feature: /complete-task (Commit, Push, PR, Transition to Code Review)

> **ASDLC Pattern**: [The Spec](https://asdlc.io/patterns/the-spec/)  
> **Practice Guide**: [Living Specs](https://asdlc.io/practices/living-specs/)  
> **Status**: Active  
> **Last Updated**: 2026-01-17

---

## Blueprint

### Context

Developers need a single command to finalize work: run tests and lint, stage changes, run Constitutional Review against AGENTS.md, commit with a conventional message, push, optionally create a PR with spec/plan and CR summary, and transition the issue to "Code Review". Without it, CR can be skipped, specs can drift from code, or the issue can be left In Progress. `/complete-task` gates on CR (blocking on Tier 3 violations) and enforces Same-Commit Rule for spec updates.

### Architecture

- **Skill location**: `skills/complete-task/SKILL.md`. Executed as `/complete-task` when installed in `.cursor/skills/` or `~/.cursor/skills/`.
- **Inputs**: `{TASK_KEY}`. Branch must match `{type}/{TASK_KEY}`. Uses spec at `specs/{FEATURE_DOMAIN}/spec.md` and plan at `.plans/{TASK_KEY}-*.plan.md` for PR body and CR context.
- **Flow**: (1) MCP validation, branch check, tests, lint; (2) if code changed contracts — check spec updated in staged changes (Same-Commit); (3) **Constitutional Review**: read AGENTS.md (Tier 1/2/3), spec (if exists), `git diff main...HEAD`; invoke Critic in a fresh context; PASS → continue, Tier 3 violations → STOP, no commit/PR; (4) commit with `{type}: {description} ({TASK_KEY})`; (5) push; (6) optionally create PR (Constitutional Review report, spec/plan summary, verification); (7) transition to "Code Review"; post completed checklist.
- **MCP**: Atlassian (getJiraIssue, getTransitionsForJiraIssue, transitionJiraIssue, addCommentToJiraIssue), GitHub (list_commits, create_pull_request, get_pull_request, etc.).
- **Dependencies**: `AGENTS.md`, `specs/`, `.plans/`, `mcps/`. **Outbound**: PR and Jira status drive code review and merge.

### Anti-Patterns

- **Don’t skip Constitutional Review** — CR must run before commit/push/PR. Tier 3 (NEVER) violations block PR creation; Tier 2/1 allow PR with warnings.
- **Don’t commit failing tests** — Run tests and lint first; if they fail, STOP.
- **Don’t skip spec update when behavior changes** — If code affects API contracts, data models, or quality targets and a spec exists, the spec must be updated in the same commit (Same-Commit Rule). Warn if spec exists but is not in staged changes.

---

## Contract

### Definition of Done

- [ ] MCP validation, branch format, tests, and lint pass.
- [ ] If code changed contracts and spec exists: spec updated and included in staged changes (or user warned).
- [ ] Constitutional Review run; no Tier 3 violations (Tier 2/1 permit proceed with warnings).
- [ ] Changes committed with conventional format `{type}: {description} ({TASK_KEY})`, pushed to remote.
- [ ] If PR created: PR includes CR report, spec/plan summary, verification; issue updated with PR link and transitioned to "Code Review". If PR skipped: issue updated with push confirmation and transitioned to "Code Review".
- [ ] `python schemas/validate_all.py` passes when skills/specs are changed.

### Regression Guardrails

- **Branch format** — Current branch must match `{type}/{TASK_KEY}`.
- **CR gate** — Tier 3 (NEVER) violations block commit/PR; do not proceed until remediated.
- **Same-Commit for spec** — Spec updates must be in the same commit as code that changes behavior or contracts.

### Scenarios

**Scenario: Constitutional Review passed and PR created**
- **Given**: On `feat/FB-44`, tests and lint pass, staged changes, no Tier 3 CR violations
- **When**: The user runs `/complete-task FB-44` and PR creation is chosen
- **Then**: Commit and push succeed, PR is created with CR report and spec/plan summary, issue is transitioned to "Code Review" and completed checklist with PR link is posted.

**Scenario: Tier 3 Constitutional Review violation — STOP**
- **Given**: CR finds a Tier 3 (NEVER) violation in the diff
- **When**: The user runs `/complete-task FB-44`
- **Then**: The command reports "❌ Constitutional Review FAILED. PR creation blocked due to Tier 3 violations.", shows the violation report and remediation, and does not commit, push, or create a PR.
