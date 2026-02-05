# Feature: /start-task (Begin Development)

> **ASDLC Pattern**: [The Spec](https://asdlc.io/patterns/the-spec/)  
> **Practice Guide**: [Living Specs](https://asdlc.io/practices/living-specs/)  
> **Status**: Active  
> **Last Updated**: 2026-01-17

---

## Blueprint

### Context

Developers need a consistent way to begin work on a task: run pre-flight checks (MCP, spec/plan, story status), create a feature branch, post a work checklist, and implement. Without this, agents may skip MCP validation, work without a spec or plan, or commit on the wrong branch. `/start-task` sets up the environment and ensures spec/plan and MCP are validated before implementation starts.

### Architecture

- **Skill location**: `skills/start-task/SKILL.md`. Executed as `/start-task` when installed in `.cursor/skills/` or `~/.cursor/skills/`.
- **Inputs**: `{TASK_KEY}` (e.g. `FB-6`). Branch format: `{type}/{TASK_KEY}` (e.g. `feat/FB-6`, `fix/PROJ-123`). Type from issue: Story→`feat/`, Bug→`fix/`, Task/Chore→`chore/`, Refactor→`refactor/`.
- **Flow**: (1) MCP status checks; (2) read spec (if `specs/{FEATURE_DOMAIN}/spec.md`) and/or plan (`.plans/{TASK_KEY}-*.plan.md`); (3) verify story in "In Progress" (transition via MCP if not); (4) create branch `{type}/{TASK_KEY}`; (5) post work checklist to Jira; (6) implement per spec/plan. Leaves changes uncommitted; `/complete-task` handles commit/push/PR.
- **MCP**: Atlassian (getJiraIssue, getTransitionsForJiraIssue, transitionJiraIssue, addCommentToJiraIssue), GitHub (list_branches, create_branch). cloudId from getAccessibleAtlassianResources.
- **Dependencies**: `mcps/`, MCP servers, `specs/`, `.plans/`. **Outbound**: `/complete-task` consumes the branch and uncommitted work.

### Anti-Patterns

- **Don’t skip MCP validation** — If any MCP server fails, STOP. Commands that use Jira/GitHub will fail later with unclear errors.
- **Don’t proceed without spec or plan** — If neither `specs/{FEATURE_DOMAIN}/spec.md` nor `.plans/{TASK_KEY}-*.plan.md` exists, STOP and suggest `/create-plan {TASK_KEY}`.
- **Don’t auto-commit** — `/start-task` leaves changes uncommitted. Committing is done in `/complete-task`.

---

## Contract

### Definition of Done

- [ ] MCP status validation performed; all required MCP servers connected.
- [ ] Spec and/or plan read; if neither exists, STOP and suggest `/create-plan {TASK_KEY}`.
- [ ] Story in "In Progress" and assigned to current user (transition via MCP if needed).
- [ ] Branch `{type}/{TASK_KEY}` created and checked out; work checklist posted to the issue with the actual branch name.
- [ ] Implementation performed per spec/plan; changes left uncommitted.
- [ ] `python schemas/validate_all.py` passes (when skills/specs are involved).

### Regression Guardrails

- **MCP before MCP-using steps** — MCP validation must pass before any Atlassian/GitHub MCP calls.
- **Branch format** — Use short form `{type}/{TASK_KEY}`; be consistent across the project.
- **Spec or plan required** — Do not start implementation without at least one of spec or plan.

### Scenarios

**Scenario: Pre-flight passes and branch created**
- **Given**: MCP connected, `.plans/FB-44-create-specs.plan.md` exists, FB-44 is in Backlog and assignable
- **When**: The user runs `/start-task FB-44`
- **Then**: The command transitions FB-44 to In Progress, creates `feat/FB-44`, posts a work checklist to FB-44, and proceeds to implementation (changes uncommitted).

**Scenario: No plan or spec — STOP**
- **Given**: MCP connected; neither `specs/foo/spec.md` nor `.plans/FB-99-*.plan.md` exists
- **When**: The user runs `/start-task FB-99`
- **Then**: The command reports "No plan or spec found for FB-99. Run `/create-plan FB-99` first." and does not create a branch or post a checklist.
