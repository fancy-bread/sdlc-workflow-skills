# Commands Reference

**Canonical command definitions for Cursor.** The `.md` files in this folder are the source of truth. Cursor loads them as natural-language instructions that AI agents execute with context.

## Install

Copy `commands/*` to `~/.cursor/commands/` (global) or `.cursor/commands/` (per-project). See [Installation](../docs/getting-started.md#step-2-install-commands).

## Where to learn

- [Commands](../docs/commands/index.md) — What each command does, usage, examples
- [Quick Reference](../docs/commands/quick-reference.md) — Copy-paste cheat sheet
- [By Role](../docs/commands/by-role.md) — Commands organized by role

## Example Workflow

```bash
/create-plan for TASK-123
/start-task TASK-123
/complete-task TASK-123
```

[Full workflows →](../docs/getting-started.md#try-a-development-workflow)

## How to change commands

Edit files in `commands/`, then copy to `.cursor/commands/` (or `~/.cursor/commands/`). Validate with `python schemas/validate.py commands/<name>.md`; see [schemas/README](../schemas/README.md).

## Troubleshooting

[Getting Started — Troubleshooting](../docs/getting-started.md#troubleshooting)

## Learn more

- [MCP Setup](../docs/mcp-setup.md) — Configure MCP servers
- [Cursor Commands Docs](https://cursor.com/docs/agent/chat/commands) — Official Cursor documentation
