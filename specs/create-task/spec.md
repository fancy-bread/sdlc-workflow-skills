# Feature: /create-task (Create Work Items in Issue Tracker)

> **ASDLC Pattern**: [The Spec](https://asdlc.io/patterns/the-spec/)  
> **Practice Guide**: [Living Specs](https://asdlc.io/practices/living-specs/)  
> **Status**: Active  
> **Last Updated**: 2026-01-17

---

## Blueprint

### Context

Teams need to create well-formed work items (epic, story, bug, task, etc.) in Jira or GitHub Issues with validation. Vague or incomplete items cause rework. `/create-task` validates MCP and tracker access, parses type and description, applies type-specific information-density checks (0–2: INSUFFICIENT → STOP and ask; 3–4: MARGINAL → proceed with assumptions; 5+: SUFFICIENT), and creates the issue. For stories/epics it can use PBI structure and link to `specs/{FEATURE_DOMAIN}/spec.md`.

### Architecture

- **Skill location**: `skills/create-task/SKILL.md` (PBI template at `skills/create-task/assets/pbi-anatomy.md`; decompose-task and refine-task reference this asset). Executed as `/create-task` when installed in `.cursor/skills/` or `~/.cursor/skills/`.
- **Inputs**: `[type]` and description or source: e.g. `story for user auth`, `--type=bug login fails`, `epic from .plans/phase-one.md`. Types: epic, story, bug, task, subtask, improvement, spike, technical-debt. For Jira: `cloudId` from `getAccessibleAtlassianResources`; `projectKey`, `issueTypeName` from project metadata.
- **Flow**: (1) MCP and tracker access validation; (2) parse type and description/source; (3) gather context (plan file, parent); (3a) for story/epic: determine `{FEATURE_DOMAIN}` (kebab-case), check `specs/{FEATURE_DOMAIN}/spec.md`; (4) validate information density (type-specific); if INSUFFICIENT, STOP and ask 3–5 questions; (5) run type-specific workflow, generate title/description (for story/epic: use PBI template from `create-task/assets/pbi-anatomy.md`); (6) create via `mcp_atlassian_createJiraIssue` or `mcp_github_create_issue`; (7) verify and return key/link. Created issues are left unassigned in "To Do".
- **MCP**: Atlassian (getAccessibleAtlassianResources, getJiraIssue, getJiraProjectIssueTypesMetadata, createJiraIssue), GitHub (issue_read, create_issue).
- **Dependencies**: Issue tracker, `specs/`, `.plans/` or `.cursor/plans/`. PBI template: `skills/create-task/assets/pbi-anatomy.md`. **Outbound**: Created issues are picked up by `/start-task`, `/decompose-task`, `/refine-task`.

### Anti-Patterns

- **Don’t skip MCP or tracker checks** — If MCP fails or access is denied, STOP.
- **Don’t hardcode cloudId, projectKey, or site-specific IDs** — Use `getAccessibleAtlassianResources` and project/issue-type metadata.
- **Don’t create with INSUFFICIENT information** — 0–2 elements: STOP and ask; do not create.

---

## Contract

### Definition of Done

- [ ] MCP and tracker access validated; type and description/source parsed.
- [ ] Information density assessed; if INSUFFICIENT, user is asked and creation does not proceed until sufficient.
- [ ] Issue created with correct type, title, description, and required fields; left unassigned in "To Do". For story/epic: PBI structure and `feature:{domain}` label when applicable.
- [ ] Task key/ID and link returned. `python schemas/validate_all.py` passes when skills are changed.

### Regression Guardrails

- **MCP and dynamic config** — cloudId and project/issue-type must be resolved at runtime, not hardcoded.
- **Validation gate** — Do not create when information density is 0–2 for the relevant type.

### Scenarios

**Scenario: Story created with sufficient information**
- **Given**: MCP OK, Jira accessible, user provides "story for OAuth login" and then persona, AC, value
- **When**: The user runs `/create-task story for OAuth login` and supplies missing detail when asked
- **Then**: A story is created in Jira with title, description, AC; unassigned in "To Do"; key and link are shown.

**Scenario: Insufficient information — STOP and ask**
- **Given**: User runs `/create-task story for better UX`
- **When**: Information density is 0–2 (vague, no persona, no AC)
- **Then**: The command asks 3–5 type-specific questions and does not create the issue until the user provides sufficient information.
