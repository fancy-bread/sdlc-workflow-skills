# Feature: /setup-asdlc (Repository Initialization for ASDLC)

> **ASDLC Pattern**: [The Spec](https://asdlc.io/patterns/the-spec/)  
> **Practice Guide**: [Living Specs](https://asdlc.io/practices/living-specs/)  
> **Status**: Active  
> **Last Updated**: 2026-01-24

---

## Blueprint

### Context

Teams adopting ASDLC patterns need to set up foundational repository structure (AGENTS.md, specs/, .plans/) before using other commands. Manual setup is error-prone, inconsistent, and creates friction for adoption. `/setup-asdlc` automates this initialization while remaining optional—other commands work without running setup, maintaining flexibility for teams at different adoption stages.

**Problem**: Teams must manually create AGENTS.md, specs/, .plans/ directories, and understand ASDLC structure before using commands. This creates a barrier to entry and leads to inconsistent setups across teams.

**Solution**: A single skill that creates the foundational structure (AGENTS.md template, specs/, .plans/, optional schemas/) with intelligent detection and clear feedback. The skill is idempotent, never overwrites existing files, and provides optional MCP verification.

### Architecture

- **Skill location**: `skills/setup-asdlc/SKILL.md`. Executed as `/setup-asdlc` when installed in `.cursor/skills/` or `~/.cursor/skills/`.
- **Template sources**: 
  - AGENTS.md template based on existing `AGENTS.md` in this repository (if available)
  - `specs/README.md` copied from this repository (if available)
  - `schemas/README.md` template created when schemas/ is detected
- **Directory structure created**:
  - `AGENTS.md` (root) - Agent Constitution template with 3-tier Operational Boundaries
  - `specs/` - Directory for permanent living specifications
  - `specs/README.md` - Documentation for specs directory
  - `.plans/` - Directory for transient task-level plans (with .gitkeep)
  - `schemas/` (conditional) - Directory for JSON Schema validation (Standardized Parts pattern)
  - `schemas/README.md` (conditional) - Documentation for schemas directory
- **Detection logic**: 
  - Schema detection checks AGENTS.md for keywords: "Standardized Parts", "schema", "validation"
  - Only creates schemas/ if indicators found
- **MCP verification**: Optional, non-blocking checks for MCP setup and issue tracker connection
- **Dependencies**: 
  - **Inbound**: None (command is optional, no dependencies)
  - **Outbound**: Other commands can reference setup-asdlc in documentation; setup creates structure that other commands use
- **Idempotency**: Command checks for existing files/directories before creating; safe to run multiple times

### Anti-Patterns

- **Don't overwrite existing files** — Always check for existence before creating. If AGENTS.md, specs/, or .plans/ exist, skip creation and report.
- **Don't require MCP** — MCP verification is optional and must not block command execution. Command succeeds even if MCP is unavailable.
- **Don't create schemas/ unconditionally** — Only create schemas/ if AGENTS.md mentions "Standardized Parts", "schema", or "validation". Not all projects need schema validation.
- **Don't hardcode project-specific values** — AGENTS.md template uses placeholders, not hardcoded project names or values.
- **Don't assume Git repository** — Command works in Git repositories but doesn't require it. Don't fail if Git commands are unavailable.

---

## Contract

### Definition of Done

- [ ] Skill exists at `skills/setup-asdlc/SKILL.md` and body conforms to skill schema (`schemas/skill.schema.json`).
- [ ] Command checks for existing `AGENTS.md` before creating; if exists, skips and reports.
- [ ] Command generates `AGENTS.md` template with 3-tier Operational Boundaries (Tier 1: ALWAYS, Tier 2: ASK, Tier 3: NEVER) when missing.
- [ ] Command creates `specs/` directory with `specs/README.md` (copied from this repository if available) when missing.
- [ ] Command creates `.plans/` directory with `.plans/.gitkeep` when missing.
- [ ] Command detects need for `schemas/` by checking AGENTS.md for keywords ("Standardized Parts", "schema", "validation"); only creates if indicators found.
- [ ] Command creates `schemas/` directory with `schemas/README.md` template when indicators detected and directory missing.
- [ ] Command performs optional MCP verification (non-blocking); reports status but continues regardless of result.
- [ ] Command generates clear summary report showing what was created vs skipped.
- [ ] Command is idempotent—safe to run multiple times without side effects.
- [ ] `python schemas/validate_all.py` passes (skill file validates against schema).

### Regression Guardrails

- **Never overwrite existing files** — Command must always check for existence before creating. This is a critical invariant that prevents data loss.
- **Optional MCP** — MCP verification must never block command execution. Command must succeed even if all MCP checks fail.
- **Idempotent operations** — Running the command multiple times must produce the same result (no duplicate files, no errors).
- **Schema detection accuracy** — Only create schemas/ when AGENTS.md explicitly mentions schema-related keywords. False positives waste user time; false negatives require manual setup.

### Scenarios

**Scenario: Fresh repository setup**
- **Given**: Repository with no AGENTS.md, no specs/, no .plans/, no schemas/
- **When**: User runs `/setup-asdlc`
- **Then**: Command creates AGENTS.md template, specs/ directory with README.md, .plans/ directory with .gitkeep, reports "schemas/ not needed (no indicators found)", generates summary with next steps

**Scenario: Partial setup (AGENTS.md exists)**
- **Given**: Repository with existing AGENTS.md but no specs/ or .plans/
- **When**: User runs `/setup-asdlc`
- **Then**: Command skips AGENTS.md creation (reports "AGENTS.md already exists"), creates specs/ and .plans/, checks AGENTS.md for schema keywords, creates schemas/ if keywords found, generates summary

**Scenario: Full setup already exists**
- **Given**: Repository with AGENTS.md, specs/, .plans/ all exist
- **When**: User runs `/setup-asdlc`
- **Then**: Command reports all files/directories exist, skips all creation, performs optional MCP verification, reports "Repository is already set up for ASDLC!"

**Scenario: Schema detection - AGENTS.md mentions Standardized Parts**
- **Given**: Repository with AGENTS.md containing "Standardized Parts" but no schemas/ directory
- **When**: User runs `/setup-asdlc`
- **Then**: Command detects keyword in AGENTS.md, creates schemas/ directory with README.md template, reports "Detected need for schemas/ (found: Standardized Parts in AGENTS.md)"

**Scenario: Schema detection - no indicators found**
- **Given**: Repository with AGENTS.md that doesn't mention "Standardized Parts", "schema", or "validation"
- **When**: User runs `/setup-asdlc`
- **Then**: Command skips schemas/ creation, reports "No schemas/ needed (no indicators found)"

**Scenario: MCP not configured**
- **Given**: Repository with no MCP setup (validate_mcps.py unavailable or MCP servers not configured)
- **When**: User runs `/setup-asdlc`
- **Then**: Command creates all files/directories successfully, reports "MCP setup not detected (optional, can be configured later)", continues without error

**Scenario: Idempotent execution**
- **Given**: Repository where `/setup-asdlc` was already run successfully
- **When**: User runs `/setup-asdlc` again
- **Then**: Command reports all files/directories exist, skips all creation, generates summary showing no changes needed, exits successfully

---

## Good vs Bad

- ✅ **Do** check for file/directory existence before creating—prevents data loss and enables idempotency.
- ❌ **Don't** overwrite existing files even if they differ from template—user may have customized them.
- ✅ **Do** provide clear feedback on what was created vs skipped—helps users understand what happened.
- ❌ **Don't** require MCP or Git—command must work in minimal environments.
- ✅ **Do** use intelligent detection for optional features (schemas/)—only create when needed.
- ❌ **Don't** hardcode project-specific values in templates—use placeholders for customization.
