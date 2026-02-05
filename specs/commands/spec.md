# Feature: Skills (Cursor Agent Skills)

> **ASDLC Pattern**: [The Spec](https://asdlc.io/patterns/the-spec/)
> **Status**: Active
> **Last Updated**: 2026-02-03

---

## Blueprint

### Context

This repo is built for **Cursor IDE**. The **skills** (Agent Skills format: markdown with frontmatter in `skills/<name>/SKILL.md`) are the primary product—not compiled code. A short, top-level path makes the canonical source obvious and simplifies install instructions.

**Solution:** Canonical path is **`skills/`** at repo root. Each skill is a folder with `SKILL.md`. Users copy from `skills/` into `.cursor/skills/` or `~/.cursor/skills/`. MCP setup and other Cursor docs live under `docs/` (e.g. `docs/mcp-setup.md`). Release artifacts are `skills-{tag}.tar.gz` and `skills-{tag}.zip`.

### Architecture

- **Canonical path:** `skills/` at repository root.
- **Contents:** One folder per skill; each folder contains `SKILL.md` (markdown with YAML frontmatter: `name`, `description`, `disable-model-invocation: true`). Optional `skills/README.md` for install/instruction.
- **Install targets:**
  - Project: `.cursor/skills/`
  - Global: `~/.cursor/skills/`
- **Format:** Agent Skills—markdown with frontmatter; no compilation. Cursor loads these as skills (slash commands).
- **Docs:** User-facing skill docs stay in `docs/skills/` (nav label "Skills"). MCP setup is `docs/mcp-setup.md`.
- **Release:** CHANGELOG at repo root `CHANGELOG.md`. Workflow packages `skills/` as `skills-{tag}.tar.gz` and `.zip`.
- **Validation:** `schemas/validate.py` validates each `skills/*/SKILL.md` (body only; frontmatter stripped). `schemas/validate_all.py` runs over all skills, mcps, and MCP refs.

### Anti-Patterns

- **Don’t put non-skill files in `skills/`** — e.g. `mcp-setup.md` lives in `docs/`, not in `skills/`.
- **Don’t change skill behavior in a pure relocation** — only paths and references change; instruction content is preserved.

---

## Contract

### Definition of Done

- [ ] All skills live under `skills/<name>/SKILL.md`; no `commands/` directory.
- [ ] Docs nav and links use `docs/skills/` (not `docs/commands/`); references updated across `docs/`, `AGENTS.md`, root `README.md`, `mkdocs.yml`, `.github/workflows/`, `specs/`.
- [ ] `mkdocs build --strict` passes.
- [ ] Create-release workflow packages `skills/`; `CHANGELOG_FILE=CHANGELOG.md` at repo root.

### Regression Guardrails

- **Install instructions must work** — `cp -r skills/* ~/.cursor/skills/` (and project variant) must produce working skills.
- **Docs must build** — `mkdocs build --strict` must succeed with no broken links or invalid nav.
- **AGENTS.md “Skill Source”** must point at `skills/` (and `.cursor/skills/` when installed).
- **Release assets** — Tagged releases must include archives of `skills/` (e.g. `skills-{tag}.tar.gz`, `skills-{tag}.zip`).

### Scenarios

**Scenario: User installs from path**
- **Given:** Repo with `skills/` at root
- **When:** User runs `cp -r skills/* ~/.cursor/skills/` and restarts Cursor
- **Then:** `/start-task`, `/create-task`, etc. are available and run correctly

**Scenario: MkDocs build**
- **Given:** All references updated to `skills/`
- **When:** `mkdocs build --strict` is run
- **Then:** Build succeeds and Skills Reference (and linked skill source URLs) point to `skills/`

**Scenario: Release creates skills archive**
- **Given:** Create-release workflow uses `skills/` and root `CHANGELOG.md`
- **When:** A version tag (e.g. `v1.2.0`) is pushed
- **Then:** Release includes `skills-{tag}.tar.gz` and `skills-{tag}.zip` containing the contents of `skills/`
