# Feature: /refine-task (Refine Task to Definition of Ready)

> **ASDLC Pattern**: [The Spec](https://asdlc.io/patterns/the-spec/)  
> **Practice Guide**: [Living Specs](https://asdlc.io/practices/living-specs/)  
> **Status**: Active  
> **Last Updated**: 2026-01-25

---

## Blueprint

### Context

Tasks often enter the backlog under-specified or poorly organized. Refinement ensures Definition of Ready (DoR): clear description, complete AC, dependencies identified, and well-organized structure. `/refine-task` fetches the task, validates PBI structure (4-part anatomy), checks spec existence, enhances clarity and organization, removes fluff, and updates the issue via MCP. It does not run on already completed tasks. The goal is to produce clean, scannable task descriptions that are ready for human refinement meetings.

### Architecture

- **Skill location**: `skills/refine-task/SKILL.md`. Executed as `/refine-task` when installed in `.cursor/skills/` or `~/.cursor/skills/`.
- **Inputs**: `{TASK_KEY}` (e.g. `FB-15`). DoR: clear description, AC, dependencies, well-organized structure. PBI structure validation (4-part anatomy: Directive, Context Pointer, Verification Pointer, Refinement Rule).
- **Flow**: (1) MCP validation; (2) fetch task; if status is Done/Completed, STOP; (3) validate PBI structure (4-part anatomy); (4) detect feature domain and check spec existence; (5) refine title, description, AC for clarity and organization, remove fluff; (6) update issue via `mcp_atlassian_editJiraIssue`.
- **MCP**: Atlassian (getAccessibleAtlassianResources, getJiraIssue, editJiraIssue). cloudId resolved at runtime.
- **Dependencies**: Issue tracker, Specs at `specs/{feature-domain}/spec.md` (optional - graceful degradation if missing). PBI template: `skills/create-task/assets/pbi-anatomy.md` (refine-task references create-task's asset). **Outbound**: Refined tasks are ready for `/start-task` or human refinement meetings.

### Anti-Patterns

- **Don’t refine completed tasks** — If status is Done/Completed, STOP and report that the task cannot be refined.
- **Don’t assume Story Points exists** — Check for the field (e.g. `customfield_10036`); if absent, skip estimation and only do DoR.
- **Don’t overwrite without user context** — Refinements should be consistent with the user’s intent; when in doubt, present options rather than silently changing large sections.

---

## Contract

### Definition of Done

- [ ] MCP validated; task exists and is not in Done/Completed.
- [ ] PBI structure validated (4-part anatomy checked, guidance provided if missing).
- [ ] Feature domain detected and spec existence checked (warn if spec referenced but missing).
- [ ] Title, description, AC refined for clarity and organization; fluff removed; content organized for easy scanning; issue updated via MCP.
- [ ] `python schemas/validate_all.py` passes when skills are changed.

### Regression Guardrails

- **Completed tasks are not refined** — Do not update tasks in Done/Completed.
- **Backward compatibility** — Tasks without PBI structure should still be refinable (graceful degradation).
- **Spec optional** — Commands work without specs; warn if spec referenced but missing, but don't block refinement.

### Scenarios

**Scenario: Task with complete PBI structure refined**
- **Given**: MCP OK, FB-15 is not Done, task has complete PBI 4-part anatomy, spec exists at `specs/user-authentication/spec.md`
- **When**: The user runs `/refine-task FB-15`
- **Then**: The command validates PBI structure, checks spec existence, enhances clarity, removes fluff, organizes content, and updates FB-15 with improved description and AC.

**Scenario: Task without PBI structure refined (graceful degradation)**
- **Given**: MCP OK, FB-15 is not Done, task does not follow PBI structure
- **When**: The user runs `/refine-task FB-15`
- **Then**: The command notes PBI structure is missing, provides guidance, but still refines task for clarity and organization.

**Scenario: Task already completed — STOP**
- **Given**: FB-15 is in status "Done"
- **When**: The user runs `/refine-task FB-15`
- **Then**: The command reports "Task FB-15 is already completed and cannot be refined." and does not change the issue.
