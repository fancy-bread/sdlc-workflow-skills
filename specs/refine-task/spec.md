# Feature: /refine-task (Refine Task to Definition of Ready, Optionally Estimate)

> **ASDLC Pattern**: [The Spec](https://asdlc.io/patterns/the-spec/)  
> **Practice Guide**: [Living Specs](https://asdlc.io/practices/living-specs/)  
> **Status**: Active  
> **Last Updated**: 2026-01-17

---

## Blueprint

### Context

Tasks often enter the backlog under-specified. Refinement ensures Definition of Ready (DoR): clear description, complete AC, dependencies identified, and optionally story points. `/refine-task` fetches the task, enriches title/description/AC, optionally estimates using historical similar tasks (JQL, similarity scoring) when the project uses story points, and updates the issue via MCP. It does not run on already completed tasks.

### Architecture

- **Command location**: `commands/refine-task.md`. Executed as `/refine-task` when installed in `.cursor/commands/` or `~/.cursor/commands/`.
- **Inputs**: `{TASK_KEY}` (e.g. `FB-15`). DoR: clear description, AC, dependencies, optional story points. If the project has a Story Points field, historical completed tasks (Scrum: ~6 sprints; Kanban: ~3 months) are queried for similarity-based estimation.
- **Flow**: (1) MCP validation; (2) fetch task; if status is Done/Completed, STOP; (3) determine board type (Scrum/Kanban) for historical range; (4) if project uses story points: run JQL for completed tasks with points, find similar tasks (title/description/context), suggest estimate; (5) refine title, description, AC, dependencies; (6) update issue via `mcp_atlassian_editJiraIssue` (and story points if applicable).
- **MCP**: Atlassian (getAccessibleAtlassianResources, getJiraIssue, editJiraIssue, searchJiraIssuesUsingJql). cloudId and project-specific custom fields (e.g. Story Points) resolved at runtime.
- **Dependencies**: Issue tracker. **Outbound**: Refined tasks are ready for `/start-task` or sprint planning.

### Anti-Patterns

- **Don’t refine completed tasks** — If status is Done/Completed, STOP and report that the task cannot be refined.
- **Don’t assume Story Points exists** — Check for the field (e.g. `customfield_10036`); if absent, skip estimation and only do DoR.
- **Don’t overwrite without user context** — Refinements should be consistent with the user’s intent; when in doubt, present options rather than silently changing large sections.

---

## Contract

### Definition of Done

- [ ] MCP validated; task exists and is not in Done/Completed.
- [ ] Title, description, AC, and dependencies refined toward DoR; issue updated via MCP.
- [ ] If project uses story points: historical similar tasks considered and estimate suggested/applied; otherwise estimation steps skipped.
- [ ] `python schemas/validate_all.py` passes when commands are changed.

### Regression Guardrails

- **Completed tasks are not refined** — Do not update tasks in Done/Completed.
- **Story points conditional** — Estimation logic runs only when the project has a Story Points–like field and completed history.

### Scenarios

**Scenario: Task refined and story points suggested**
- **Given**: MCP OK, FB-15 is not Done, project has Story Points and completed tasks in the historical range
- **When**: The user runs `/refine-task FB-15`
- **Then**: The command updates FB-15 with improved description and AC, and suggests or sets story points based on similar completed tasks.

**Scenario: Task already completed — STOP**
- **Given**: FB-15 is in status "Done"
- **When**: The user runs `/refine-task FB-15`
- **Then**: The command reports "Task FB-15 is already completed and cannot be refined." and does not change the issue.
