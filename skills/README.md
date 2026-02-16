# Skills Reference

**SDLC workflow skills (Agent Skills format).** The `SKILL.md` files in each folder are the source of truth. The same layout works for **Cursor**, **Claude**, and **Codex** (Cursor is the primary tested environment).

## Install

- **Cursor:** **Settings → Rules → Add Rule → Remote Rule (Github)** and enter `https://github.com/fancy-bread/sdlc-workflow-skills`. See [Installing skills from GitHub](https://cursor.com/docs/context/skills#installing-skills-from-github).
- **Or** copy `skills/*` to your environment’s skills directory:
  - **Cursor:** `~/.cursor/skills/` or `.cursor/skills/`
  - **Claude:** `~/.claude/skills/` or `.claude/skills/`
  - **Codex:** `~/.codex/skills/` or `.codex/skills/`

See [Installation](../docs/getting-started.md#step-2-install-skills) in the docs.

## Where to learn

- [Skills Reference](../docs/skills/index.md) — What each skill does, usage, examples
- [Quick Reference](../docs/skills/quick-reference.md) — Copy-paste cheat sheet

## Example Workflow

```bash
/create-plan for TASK-123
/start-task TASK-123
/complete-task TASK-123
```

[Full workflows →](../docs/getting-started.md#try-a-development-workflow)

## How to change skills

Edit files in `skills/<name>/SKILL.md`, then copy to your environment’s skills directory (Cursor `.cursor/skills/`, Claude `.claude/skills/`, Codex `.codex/skills/`). Validate with `python schemas/validate.py skills/<name>/SKILL.md`; see [schemas/README](../schemas/README.md).

## Troubleshooting

[Getting Started — Troubleshooting](../docs/getting-started.md#troubleshooting)

## Learn more

- [MCP Setup](../docs/mcp-setup.md) — Configure MCP servers
- [Cursor Skills Docs](https://cursor.com/docs/context/skills) — Agent Skills format (Cursor); other environments may adopt the same format
