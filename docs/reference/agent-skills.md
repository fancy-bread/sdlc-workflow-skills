# Agent Skills (agentskills.io)

[Agent Skills](https://agentskills.io/home) is an open format and specification for AI agent skills: markdown-based instructions that IDEs and agents can load as slash commands or reusable behaviors.

## Format

- **SKILL.md** — One markdown file per skill, with YAML frontmatter (`name`, `description`, optional `disable-model-invocation`).
- **Structure** — Overview, Definitions, Prerequisites, Steps, Tools, Guidance (per Agent Skills spec).
- **No compilation** — Skills are plain markdown; tools like the [skills CLI](https://github.com/vercel-labs/skills) install them by copy or symlink.

## Adoption

- **Cursor** — Loads skills from `.cursor/skills/` or `~/.cursor/skills/`. Prefer **Copy** (not Symlink) so Cursor lists and runs skills reliably. See [Getting Started](../getting-started.md) for install.
- **Other environments** — Check your IDE or agent docs for Agent Skills support.

## External Resources

- [agentskills.io](https://agentskills.io/specification) — Format specification and adoption
- [vercel-labs/skills](https://github.com/vercel-labs/skills) — CLI to add, remove, and manage skills
- [skills.sh](https://skills.sh) — Directory of skills (see [Skills Directory](skills-directory.md))
