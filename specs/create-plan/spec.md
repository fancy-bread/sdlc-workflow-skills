# Feature: /create-plan (Create Spec or Plan from Story)

> **ASDLC Pattern**: [The Spec](https://asdlc.io/patterns/the-spec/)  
> **Practice Guide**: [Living Specs](https://asdlc.io/practices/living-specs/)  
> **Status**: Active  
> **Last Updated**: 2026-01-23

---

## Blueprint

### Context

Teams need either a **Spec** (permanent Blueprint+Contract at `specs/{FEATURE_DOMAIN}/spec.md`) or a **Plan** (transient implementation guide at `.plans/{TASK_KEY}-*.plan.md`) before implementation. Without a decision and a document, agents may guess scope or duplicate work. `/create-plan` fetches the story from the issue tracker, analyzes the codebase, decides Spec vs Plan (or both), and generates the document; for Plans it also posts a summary to the issue.

### Architecture

- **Command location**: `commands/create-plan.md`. Executed as `/create-plan` when installed in `.cursor/commands/` or `~/.cursor/commands/`.
- **Inputs**: `{TASK_KEY}`. Optional: `{FEATURE_DOMAIN}` for Spec (kebab-case). **Spec** when: new feature domain, API contracts, cross-team deps. **Plan** when: bug, task-level implementation, transient work.
- **Flow**: (1) MCP validation; (2) fetch story (Jira `getJiraIssue` or GitHub `issue_read`); (3) validate story (description, ≥3 AC; if not, STOP or ask); (4) extract keywords from story for ASDLC pattern queries; (5) analyze codebase (codebase_search, grep, patterns); (6) query ASDLC knowledge base (`mcp_asdlc_search_knowledge_base`) for relevant patterns (3-5 most relevant); (7) design: for Spec — Blueprint (Context, Architecture, Anti-Patterns) + Contract (DoD, Guardrails, Scenarios); for Plan — Story, Context, Scope, AC, Technical Design, Implementation Steps, Testing, Dependencies, Referenced ASDLC Patterns, Status; (8) create file: `specs/{FEATURE_DOMAIN}/spec.md` or `.plans/{TASK_KEY}-{kebab}.plan.md`; (9) for Plan: post summary comment to issue (if posting fails, note but do not fail).
- **MCP**: Atlassian (getAccessibleAtlassianResources, getJiraIssue, addCommentToJiraIssue), GitHub (issue_read, add_issue_comment), ASDLC (search_knowledge_base, get_article) for pattern lookup.
- **Dependencies**: Issue tracker, `specs/`, `.plans/`, codebase. **Outbound**: Spec/plan consumed by `/start-task` and `/complete-task`.

### Anti-Patterns

- **Don’t proceed without MCP or story** — If MCP fails or story does not exist, STOP. If story lacks sufficient detail (e.g. &lt;3 AC), STOP and ask.
- **Don’t skip codebase analysis** — Search for similar implementations and patterns before designing; do not reinvent existing approaches.
- **Don’t fail on comment post** — If posting the plan summary to the issue fails, note it; file creation is the primary goal.

---

## Contract

### Definition of Done

- [ ] MCP validation performed; story fetched and validated (exists, sufficient detail).
- [ ] Keywords extracted from story for ASDLC pattern queries.
- [ ] ASDLC knowledge base queried for relevant patterns (3-5 most relevant); patterns discovered and stored (or gracefully handled if ASDLC MCP unavailable).
- [ ] Codebase analyzed; Spec or Plan (or both) designed and written.
- [ ] **If Spec**: `specs/{FEATURE_DOMAIN}/spec.md` created with Blueprint and Contract. **If Plan**: `.plans/{TASK_KEY}-{kebab}.plan.md` created with required sections including "Referenced ASDLC Patterns" (if patterns found); summary posted to issue (or noted if post fails).
- [ ] Document is coherent (no unfulfilled placeholders for Spec; Plan has Implementation Steps and Testing).
- [ ] `python schemas/validate_all.py` passes when commands are touched.

### Regression Guardrails

- **MCP and story first** — Do not generate a spec or plan until MCP is OK and story is validated.
- **Spec vs Plan** — Spec = State (how it works); Plan = Delta (what changes). Do not duplicate large blocks between them.

### Scenarios

**Scenario: Plan created and summary posted**
- **Given**: MCP OK, FB-44 exists with description and ≥3 AC, codebase has `.plans/` and `commands/`
- **When**: The user runs `/create-plan FB-44` and the outcome is a Plan
- **Then**: `.plans/FB-44-create-specs-for-8-commands.plan.md` exists with Story, Scope, AC, Technical Design, Implementation Steps, and a plan summary is posted to FB-44.

**Scenario: Story not found — STOP**
- **Given**: MCP OK, story `FB-999` does not exist in Jira
- **When**: The user runs `/create-plan FB-999`
- **Then**: The command reports "Story FB-999 not found" and does not create a spec or plan.
