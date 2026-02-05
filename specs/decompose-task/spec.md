# Feature: /decompose-task (Break Epic or Large Story into Subtasks)

> **ASDLC Pattern**: [The Spec](https://asdlc.io/patterns/the-spec/)  
> **Practice Guide**: [Living Specs](https://asdlc.io/practices/living-specs/)  
> **Status**: Active  
> **Last Updated**: 2026-01-17

---

## Blueprint

### Context

Epics and large stories need to be split into smaller, actionable subtasks with clear AC and sizing. Without decomposition, work is unclear or too large to deliver. `/decompose-task` fetches the parent from the issue tracker, checks information density, and creates child issues (subtasks or linked stories) via MCP, inheriting `{FEATURE_DOMAIN}` from the parent for spec linkage.

### Architecture

- **Skill location**: `skills/decompose-task/SKILL.md`. Executed as `/decompose-task` when installed in `.cursor/skills/` or `~/.cursor/skills/`.
- **Inputs**: `{TASK_KEY}` — epic or large story key (e.g. `FB-6`, `PROJ-100`). Subtask criteria: clear AC (3–5), appropriate size (1–2 days / 1–2 points), standalone or explicit deps, testable.
- **Flow**: (1) MCP validation; (2) fetch task via `mcp_atlassian_getJiraIssue` or GitHub equivalent; (3) validate information density (goals, scope, context, success criteria, constraints); if &lt;3 elements or too vague, STOP and ask 3–5 questions; (4) analyze scope and boundaries; (5) design subtasks (titles, descriptions, AC); (6) create children via MCP (`createJiraIssue` with `parent` or equivalent), inheriting `{FEATURE_DOMAIN}` from parent when applicable; (7) link and optionally estimate.
- **MCP**: Atlassian (getJiraIssue, getJiraProjectIssueTypesMetadata, createJiraIssue, searchJiraIssuesUsingJql), GitHub (issue_read, create_issue). cloudId from getAccessibleAtlassianResources.
- **Dependencies**: Issue tracker, `specs/` (for PBI/feature domain). **Outbound**: Subtasks are consumed by `/start-task`, `/refine-task`.

### Anti-Patterns

- **Don’t decompose without sufficient parent detail** — If information density is &lt;3 elements or description is &lt;50 words and vague, STOP and ask; do not create subtasks from thin content.
- **Don’t skip MCP** — Fetch and create must go through MCP; do not assume IDs or project structure.
- **Don’t create huge or vague subtasks** — Each child must have clear AC, be testable, and be sized for 1–2 days (or project equivalent).

---

## Contract

### Definition of Done

- [ ] MCP validated; parent task exists and is fetched.
- [ ] Parent information density checked; if insufficient, user is asked and decomposition does not proceed until improved.
- [ ] Subtasks created in the tracker with correct parent link, clear AC, and inherited `{FEATURE_DOMAIN}` when applicable.
- [ ] Each subtask is standalone or has explicit dependencies and is testable.
- [ ] `python schemas/validate_all.py` passes when commands are changed.

### Regression Guardrails

- **Parent must exist and be sufficiently specified** — No decomposition when the task is missing or too vague.
- **Child linkage** — Children must be correctly linked to the parent (e.g. Jira `parent` or GitHub issue links).

### Scenarios

**Scenario: Epic decomposed into stories**
- **Given**: MCP OK, epic FB-10 exists with goals, scope, and success criteria
- **When**: The user runs `/decompose-task FB-10`
- **Then**: The command creates linked child stories with titles, descriptions, 3–5 AC each, and `{FEATURE_DOMAIN}` inherited where applicable.

**Scenario: Parent too vague — STOP**
- **Given**: FB-10 has a short, generic description ("improve system") and &lt;3 density elements
- **When**: The user runs `/decompose-task FB-10`
- **Then**: The command asks 3–5 specific questions and does not create subtasks until the user provides sufficient detail.
