# Feature: Skill Audit (ASDLC Alignment)

> **ASDLC Pattern**: [The Spec](https://asdlc.io/patterns/the-spec/)
> **Status**: Active
> **Last Updated**: 2026-02-16

---

## Blueprint

### Context
Before defining schemas for our Cursor skills (FB-18), we need to validate that their design aligns with ASDLC principles. An **executable audit skill** runs on demand to check skill coverage, artifact alignment, and pattern implementation, and writes a single report for human review.

**Business Problem**: Skills (formerly commands) were designed organically for workflow automation. Without validating against ASDLC patterns first, we risk locking down schemas for misaligned structures.

**Solution**: A project skill (like prepare-changelog) that audits all skills in `skills/` against ASDLC's Factory Architecture, Standardized Parts, and Quality Control pillars, and against Agent Skills format (SKILL.md structure, frontmatter). The skill is **read-only**: it does not edit skills; it produces one markdown report in `.plans/` per run.

### Architecture

#### Skills in Scope
| Skill (slash command) | Path | Primary Purpose | SDLC Phase |
|------------------------|------|-----------------|------------|
| `/mcp-status` | `skills/mcp-status/SKILL.md` | Verify MCP connections | Infrastructure |
| `/create-task` | `skills/create-task/SKILL.md` | Create work items | Product |
| `/decompose-task` | `skills/decompose-task/SKILL.md` | Break epics into stories | Product |
| `/refine-task` | `skills/refine-task/SKILL.md` | Add detail, estimate points | Product |
| `/create-plan` | `skills/create-plan/SKILL.md` | Create implementation plan | Planning |
| `/start-task` | `skills/start-task/SKILL.md` | Begin development | Development |
| `/complete-task` | `skills/complete-task/SKILL.md` | Commit, push, create PR | Development |
| `/create-test` | `skills/create-test/SKILL.md` | Write tests | Quality |
| `/review-code` | `skills/review-code/SKILL.md` | AI code review | Quality |
| `/setup-asdlc` | `skills/setup-asdlc/SKILL.md` | Initialize repo for ASDLC | Utilities |

#### ASDLC Artifacts
- **Spec**: Blueprint + Contract (permanent living specification)
- **PBI**: Product Backlog Item (transient execution unit)
- **AGENTS.md**: Agent Constitution (behavioral directives)

#### ASDLC Patterns Referenced
- **The Spec**: Living documents as permanent source of truth
- **The PBI**: Transient execution unit (delta vs state)
- **Context Gates**: Architectural checkpoints (input/output validation)
- **Ralph Loop**: Self-correcting worker pattern
- **Adversarial Code Review**: Critic agent review pattern
- **Constitutional Review**: Validation against Spec + Constitution
- **Living Specs**: Practical guide for evolving specifications

#### Audit Methodology
For each skill, perform structured analysis:
1. **Purpose & Phase**: What SDLC phase? What responsibility?
2. **Artifact Analysis**: What does it consume/produce?
3. **Pattern Implementation**: Which ASDLC patterns does it implement?
4. **Field Manual Alignment**: Factory Architecture, Standardized Parts, Quality Control?
5. **Gap Identification**: What's missing?
6. **Recommendation**: Keep, refine, merge, remove, or add new skill?

#### Dependencies
- **ASDLC.io MCP server**: Required for pattern queries
- **ASDLC Field Manual v0.9.3**: Reference documentation
- **AGENTS.md (FB-17)**: Context on current skill structure
- **All skills**: Located in `skills/` (each `skills/<name>/SKILL.md`)

#### Dependency Directions
- **Inbound**: Consumed by FB-18 (schema definition)
- **Outbound**: Depends on ASDLC MCP server, AGENTS.md
- **Blocks**: FB-18 and other Phase 1 refinement stories

#### Executable Audit Skill (When Invoked)
- **Purpose**: On-demand audit of all skills against ASDLC alignment and Agent Skills format.
- **Inputs**: This spec (`specs/skill-audit/spec.md`), `AGENTS.md`, and all `skills/*/SKILL.md`.
- **Steps**: For each skill in `skills/`: apply Audit Methodology (Purpose & Phase, Artifact Analysis, Pattern Implementation, Field Manual Alignment, Gap Identification, Recommendation). Also validate Agent Skills format (Overview, Definitions, Prerequisites, Steps, Tools, Guidance; frontmatter). Aggregate findings.
- **Output**: One markdown report per run, written to `.plans/` (e.g. `.plans/skill-audit-YYYY-MM-DD.md`). Report structure: Executive Summary, Skill-by-Skill Analysis, Gap Analysis, Skill-to-ASDLC Mapping, Recommendations, Next Steps. The skill **does not edit** any file in `skills/`.
- **Placement**: Project skill in `.cursor/skills/audit-skills/` (project-local; same as prepare-changelog). Not in `skills/` and not in docs.

### Anti-Patterns

**❌ Analysis Paralysis**
Don't over-research. Time-box the spike. Focus on actionable findings, not academic perfection.

**❌ Editing Skills From the Audit**
The audit skill is read-only. It must not modify any file in `skills/`. It only produces a report in `.plans/` for human review.

**❌ Vague Recommendations**
"Command needs improvement" is not actionable. Provide specific changes: "Rename `/create-plan` to `/create-spec` and update output to Blueprint + Contract format."

**❌ Ignoring Practical Workflow**
ASDLC alignment is important, but so is developer productivity. Balance theoretical purity with real-world usability.

**❌ Scope Creep**
Don't audit adjacent systems (CI/CD, documentation). Focus on the skills only.

---

## Contract

### Definition of Done
- [ ] Audit skill exists and is invocable (e.g. `/audit-skills` or project command).
- [ ] When invoked, the skill produces one markdown report in `.plans/` (e.g. `.plans/skill-audit-YYYY-MM-DD.md`) for human review.
- [ ] Report contains: Executive Summary, Skill-by-Skill Analysis, Gap Analysis, Skill-to-ASDLC Mapping, Recommendations, Next Steps.
- [ ] Skill does not edit any file in `skills/` (read-only audit).
- [ ] Each skill in `skills/` is checked for ASDLC alignment and Agent Skills format (Overview, Definitions, Prerequisites, Steps, Tools, Guidance; frontmatter).
- [ ] Spec updated to describe executable audit workflow and output path (this document).

### Regression Guardrails
- **Findings must be actionable**: Every gap identified must have a concrete recommendation
- **Go/No-Go decision required**: FB-18 cannot proceed without clear guidance
- **Skill count stability**: Don't recommend adding 10+ new skills (keep skill set minimal)
- **Backward compatibility**: Refinements must not break existing workflow without migration path
- **Audit is read-only**: The audit skill must not modify any file in `skills/`; output is a single report in `.plans/`

### Scenarios

**Scenario: Audit identifies misaligned skill**
- **Given**: A skill that doesn't produce/consume ASDLC artifacts
- **When**: Audit analysis is performed
- **Then**: Recommendation provided with specific refinement (e.g., "Update `/create-plan` to produce Spec instead of plan file")

**Scenario: Audit identifies missing ASDLC practice**
- **Given**: ASDLC pattern not implemented by any skill
- **When**: Gap analysis is performed
- **Then**: Either recommend new skill OR recommend adding practice to existing skill (with rationale)

**Scenario: Go/No-Go decision for FB-18**
- **Given**: Audit complete with findings
- **When**: Synthesizing recommendations
- **Then**: Clear decision: "Go" (proceed with schemas) OR "No-Go" (refine skills first), with rationale and timeline

**Scenario: Deliverables are accessible**
- **Given**: Audit complete
- **When**: Stakeholder reviews findings
- **Then**: Audit report is readable, well-structured, and actionable for next steps

**Scenario: Audit skill writes report to .plans/**
- **Given**: The audit skill is invoked (e.g. `/audit-skills`)
- **When**: The skill runs to completion
- **Then**: Exactly one markdown file is created in `.plans/` (e.g. `.plans/skill-audit-YYYY-MM-DD.md`) with the Deliverable Structure; no files in `skills/` are modified

**Scenario: Audit validates ASDLC artifact lifecycle**
- **Given**: Skills claim to implement ASDLC artifacts (Spec, PBI, AGENTS.md)
- **When**: Audit analyzes artifact creation, consumption, and evolution
- **Then**: Each artifact has clear owner skills (create, read, update), lifecycle is validated

**Scenario: Recommendations are prioritized**
- **Given**: Multiple gaps and misalignments identified
- **When**: Synthesizing recommendations
- **Then**: Recommendations are ordered by: Critical (blocks FB-18) > High (ASDLC core) > Medium (nice-to-have), with rationale

### Expected Outcomes

**Likely Findings**:
- `/create-plan` needs refinement to produce Specs (not just plans)
- `/complete-task` may need Constitutional Review integration
- `/review-code` should implement Adversarial Code Review pattern
- Plan files (`.plans/`) should become Specs (`specs/`)
- Skills need better Spec vs PBI distinction

**Likely Gaps**:
- No explicit Constitutional Review skill
- No Ralph Loop support (agent self-correction)
- No Spec maintenance/evolution skill
- Quality gates not enforced deterministically

**Likely Recommendations**:
- Refine 3-5 skills to better align with ASDLC
- Add 1-2 new skills for missing practices (or merge into existing)
- Restructure plan files to Spec files (separate story: FB-24)
- Proceed with FB-18 after refinements complete

### Deliverable Structure

**Audit Report** (output of the audit skill; one file per run in `.plans/`, e.g. `.plans/skill-audit-YYYY-MM-DD.md`):
1. Executive Summary (alignment assessment, key findings, critical gaps, go/no-go)
2. Skill-by-Skill Analysis (for each skill)
3. Gap Analysis (missing practices, severity)
4. Skill-to-ASDLC Mapping (Phase, Artifact, Pattern tables)
5. Recommendations (refine, merge, remove, add)
6. Next Steps (stories to create, FB-18 decision)

The audit skill writes this report to `.plans/` for human review. It does not write to `docs/asdlc-audit/` or modify any skill files.

---

**Status**: Active (executable audit skill per FB-74)
**Last Updated**: 2026-02-16
**Pattern**: The Spec (living spec for on-demand audit); Context Gates (read-only validation)
