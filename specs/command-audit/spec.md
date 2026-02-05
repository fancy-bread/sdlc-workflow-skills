# Feature: Skill Audit (ASDLC Alignment Spike)

> **ASDLC Pattern**: [The Spec](https://asdlc.io/patterns/the-spec/)
> **Status**: Active
> **Last Updated**: 2026-01-17

---

## Blueprint

### Context
Before defining schemas for our Cursor skills (FB-18), we need to validate that their design aligns with ASDLC principles. This spike investigates skill coverage, artifact alignment, and pattern implementation to identify gaps and provide actionable refinement recommendations.

**Business Problem**: Skills (formerly commands) were designed organically for workflow automation. Without validating against ASDLC patterns first, we risk locking down schemas for misaligned structures.

**Solution**: Systematic audit of all skills against ASDLC's Factory Architecture, Standardized Parts, and Quality Control pillars.

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

### Anti-Patterns

**❌ Analysis Paralysis**
Don't over-research. Time-box the spike. Focus on actionable findings, not academic perfection.

**❌ Implementation During Spike**
This is research only. Don't implement changes. Document recommendations for separate stories.

**❌ Vague Recommendations**
"Command needs improvement" is not actionable. Provide specific changes: "Rename `/create-plan` to `/create-spec` and update output to Blueprint + Contract format."

**❌ Ignoring Practical Workflow**
ASDLC alignment is important, but so is developer productivity. Balance theoretical purity with real-world usability.

**❌ Scope Creep**
Don't audit adjacent systems (CI/CD, documentation). Focus on the skills only.

---

## Contract

### Definition of Done
- [x] All skills audited with structured analysis
- [x] Gap analysis complete (missing ASDLC practices identified)
- [x] Recommendations provided (specific, actionable stories)
- [x] Skill-to-ASDLC mapping documented (Phase, Artifact, Pattern)
- [x] Go/No-Go decision for FB-18 with rationale
- [x] Audit report created and accessible
- [x] Summary posted to FB-36
- [x] Refinement stories created (if needed)

### Regression Guardrails
- **Findings must be actionable**: Every gap identified must have a concrete recommendation
- **Go/No-Go decision required**: FB-18 cannot proceed without clear guidance
- **Skill count stability**: Don't recommend adding 10+ new skills (keep skill set minimal)
- **Backward compatibility**: Refinements must not break existing workflow without migration path

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

**Audit Report** (`docs/asdlc-audit/command-audit-report.md`):
1. Executive Summary (alignment assessment, key findings, critical gaps, go/no-go)
2. Skill-by-Skill Analysis (for each skill)
3. Gap Analysis (missing practices, severity)
4. Skill-to-ASDLC Mapping (Phase, Artifact, Pattern tables)
5. Recommendations (refine, merge, remove, add)
6. Next Steps (stories to create, FB-18 decision)

---

**Status**: Completed (FB-36)
**Last Updated**: 2026-01-17
**Pattern**: ASDLC Spike for alignment validation
