---
name: audit-skills
description: Audit all skills in skills/ against ASDLC alignment and Agent Skills format; output a single markdown report to .plans/ for human review. Read-only—does not edit skills.
disable-model-invocation: true
---

# Audit Skills

## Overview
Run an on-demand audit of every skill in `skills/` against ASDLC alignment (Factory Architecture, Standardized Parts, Quality Control) and Agent Skills format. Produce one markdown report in `.plans/` (e.g. `.plans/skill-audit-YYYY-MM-DD.md`) for human review. The skill does **not** modify any file in `skills/`.

## Definitions

- **skills/**: Project directory containing one folder per skill, each with `SKILL.md` (source of truth for this repo).
- **Agent Skills format**: SKILL.md with YAML frontmatter (`name`, `description`, `disable-model-invocation`) and required body sections—Overview, Definitions, Prerequisites, Steps, Tools, Guidance (per AGENTS.md).
- **ASDLC pillars**: Factory Architecture (skill stations, phase boundaries), Standardized Parts (schemas, AGENTS.md), Quality Control (gates, validation).
- **Audit report path**: Single file per run in `.plans/` with date stamp, e.g. `.plans/skill-audit-2026-02-16.md`.
- **Spec**: `specs/skill-audit/spec.md` — Blueprint (methodology, skills in scope, anti-patterns) and Contract (DoD, deliverable structure).

## Prerequisites

- **Spec and AGENTS.md**: `specs/skill-audit/spec.md` and `AGENTS.md` must exist at repo root. If either is missing, STOP and report.
- **skills/ present**: Directory `skills/` with at least one `*/SKILL.md`. If empty or missing, STOP and report.
- **Read-only**: Do not edit, move, or delete any file under `skills/`. Only create or overwrite one file in `.plans/`.

## Steps

1. **Load authority documents**
   - Read `specs/skill-audit/spec.md` (Blueprint: Audit Methodology, Skills in Scope, ASDLC Artifacts, Anti-Patterns; Contract: Deliverable Structure).
   - Read `AGENTS.md` (skill structure requirements, Operational Boundaries). Use these as the checklist for Agent Skills format (Overview, Definitions, Prerequisites, Steps, Tools, Guidance; frontmatter).

2. **Discover skills**
   - List all `skills/*/SKILL.md` (e.g. via glob `skills/*/SKILL.md` or list directory). Use the spec's "Skills in Scope" table as the canonical list; if extra skills exist, include them. If a listed skill is missing, note it in the report.

3. **Audit each skill**
   - For each `skills/<name>/SKILL.md`:
     - **Purpose & Phase**: What SDLC phase? What responsibility? (Map to spec table.)
     - **Artifact Analysis**: What does it consume/produce? (Spec, PBI, AGENTS.md, plans, etc.)
     - **Pattern Implementation**: Which ASDLC patterns does it implement? (Context Gates, Constitutional Review, etc.)
     - **Field Manual Alignment**: How does it align with Factory Architecture, Standardized Parts, Quality Control?
     - **Agent Skills format**: Does it have frontmatter (`name`, `description`, `disable-model-invocation`) and all required sections (Overview, Definitions, Prerequisites, Steps, Tools, Guidance)? Note missing or weak sections.
     - **Gap**: What's missing (e.g. no Definitions, vague Steps)?
     - **Recommendation**: Keep, refine, merge, remove, or add—be specific and actionable.

4. **Aggregate findings**
   - Summarize alignment level (e.g. count of skills fully aligned vs partial vs gaps).
   - Build Skill-to-ASDLC mapping (Phase, Artifact, Pattern per skill).
   - List gaps (missing practices, severity).
   - Prioritize recommendations (Critical / High / Medium) with rationale.

5. **Write report (only output)**
   - Ensure `.plans/` exists (create directory if necessary). Do **not** create or change any file under `skills/`.
   - Write exactly **one** markdown file: `.plans/skill-audit-YYYY-MM-DD.md` (use today's date in ISO format). If the file exists from a prior run same day, overwrite it.
   - Report structure (per spec Deliverable Structure):
     1. **Executive Summary** — Alignment assessment, key findings, critical gaps, go/no-go for FB-18 if applicable.
     2. **Skill-by-Skill Analysis** — For each skill, the analysis from step 3 (purpose, artifacts, patterns, format check, gap, recommendation).
     3. **Gap Analysis** — Missing practices, severity.
     4. **Skill-to-ASDLC Mapping** — Phase, Artifact, Pattern tables.
     5. **Recommendations** — Refine, merge, remove, add; specific and ordered by priority.
     6. **Next Steps** — Suggested stories or follow-ups.
   - After writing, confirm: "Report written to `.plans/skill-audit-YYYY-MM-DD.md`. No files in `skills/` were modified."

## Tools

### Filesystem (read-only for skills/)
- **read_file** — Read `specs/skill-audit/spec.md`, `AGENTS.md`, and each `skills/<name>/SKILL.md`. Do not write to `skills/`.
- **glob_file_search** — Find all `skills/*/SKILL.md`.

### Filesystem (write only to .plans/)
- **write** — Create or overwrite exactly one file: `.plans/skill-audit-YYYY-MM-DD.md`. Do not use write (or any tool) to modify `skills/`.

### Optional MCP
- **ASDLC (user-asdlc)** — `mcp_asdlc_list_articles`, `mcp_asdlc_search_knowledge_base`, `mcp_asdlc_get_article` to resolve pattern references or validate alignment. If MCP is unavailable, proceed using spec and AGENTS.md only; note in report that ASDLC MCP was not queried.

## Guidance

### Role
Act as an **audit executor** that assesses skill alignment to ASDLC and Agent Skills format and produces a single, actionable report for humans. You do not change any skill files.

### Instruction
Execute the audit per `specs/skill-audit/spec.md`: load spec and AGENTS.md, enumerate skills, apply the Audit Methodology and Agent Skills format check per skill, aggregate, then write one report to `.plans/skill-audit-YYYY-MM-DD.md`. Never edit `skills/`.

### Context
- This skill is a **project skill** (like prepare-changelog) and lives in `.cursor/skills/audit-skills/` (project-local). It is not shipped in `skills/` or documented in the docs site.
- The spec was updated for an executable audit (FB-74); the previous one-time spike was FB-36.
- ASDLC patterns: [The Spec](asdlc://the-spec), [Context Gates](asdlc://context-gates). The audit itself is a read-only gate (output validation: one file in `.plans/`).

### Constraints
- **Read-only for skills/**: Do not use search_replace, write, or any tool to modify, create, or delete files under `skills/`. Only write the report to `.plans/`.
- **Single output file**: Exactly one report file per run; path `.plans/skill-audit-YYYY-MM-DD.md`.
- **Actionable recommendations**: Every gap must have a concrete recommendation (per spec Regression Guardrails).
- **No scope creep**: Do not audit CI/CD or docs; focus on `skills/*/SKILL.md` only.

### Output
1. One markdown report at `.plans/skill-audit-YYYY-MM-DD.md` with the six sections above.
2. A short confirmation: "Report written to `.plans/skill-audit-YYYY-MM-DD.md`. No files in `skills/` were modified."
