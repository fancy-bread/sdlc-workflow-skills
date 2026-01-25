---
title: Setup ASDLC Command
---

# `/setup-asdlc`

Prepare your repository for ASDLC adoption by creating AGENTS.md template, directory structure, and basic configuration.

| | |
|---|---|
| **Roles** | All Roles |
| **Frequency** | Once per repository (or when adding ASDLC to existing repo) |
| **Prerequisites** | None (optional command) |

---

## What It Does

Initializes a repository for ASDLC adoption by creating the foundational structure needed for ASDLC workflows. The command generates an AGENTS.md template with 3-tier Operational Boundaries, creates the specs/ directory for permanent living specifications, creates the .plans/ directory for transient task-level plans, and optionally creates the schemas/ directory if the project indicates a need for schema validation. The command intelligently detects when schemas/ is needed by checking AGENTS.md for keywords like "Standardized Parts", "schema", or "validation". It never overwrites existing files, performs optional non-blocking MCP verification, and is idempotent—safe to run multiple times. The command is optional—other commands work without running setup, maintaining flexibility for teams at different adoption stages.

---

## ASDLC

- **Patterns**: [Agent Constitution](https://asdlc.io/patterns/agent-constitution/), [The Spec](https://asdlc.io/patterns/the-spec/)
- **Pillars**: Factory Architecture, Standardized Parts, Quality Control

---

## Usage

```bash
/setup-asdlc
```

No arguments needed. Creates foundational structure for ASDLC workflows.

---

## Example Output

**Fresh repository setup:**
```
🚀 ASDLC Setup Complete

Created:
  ✅ AGENTS.md template
  ✅ specs/ directory with README.md
  ✅ .plans/ directory
  ⚠️  schemas/ not needed (no indicators found)

MCP Status:
  ⚠️  MCP setup not detected (optional, can be configured later)
  ⚠️  Issue tracker connection not available (optional, can be configured later)

Next steps:
  1. Customize AGENTS.md with your project details
  2. Configure MCP servers (see docs/mcp-setup.md)
  3. Create your first spec with /create-plan
```

**Partial setup (AGENTS.md exists):**
```
🚀 ASDLC Setup Complete

Skipped:
  ⚠️  AGENTS.md already exists

Created:
  ✅ specs/ directory with README.md
  ✅ .plans/ directory
  ✅ schemas/ directory (detected: Standardized Parts in AGENTS.md)

MCP Status:
  ✅ MCP setup detected
  ✅ Issue tracker connection verified

Next steps:
  1. Create your first spec with /create-plan
```

---

## When to Use

| Scenario | Why |
|----------|-----|
| **New repository** | Set up ASDLC structure from scratch |
| **Existing repository** | Add ASDLC structure to existing project |
| **Team onboarding** | Standardize setup across team members |
| **ASDLC adoption** | Begin using ASDLC patterns and workflows |

---

## Related Commands

- **[`/mcp-status`](mcp-status.md)** - Verify MCP server connections
- **[`/create-plan`](create-plan.md)** - Create living specifications or implementation plans
- **[`/create-task`](create-task.md)** - Create tasks in your issue tracker

---

## See Also

- [Living Specifications](../../specs/README.md) - Guide to creating and maintaining specs
- [Agent Constitution Pattern](https://asdlc.io/patterns/agent-constitution/) - AGENTS.md specification
- [MCP Setup](../mcp-setup.md) - Configure Model Context Protocol servers

---

[:octicons-arrow-left-24: Back to Commands](index.md)
