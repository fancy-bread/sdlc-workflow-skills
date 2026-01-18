# Feature: Commands (Cursor)

> **ASDLC Pattern**: [The Spec](https://asdlc.io/patterns/the-spec/)  
> **Status**: Active  
> **Last Updated**: 2026-01-18

---

## Blueprint

### Context

This repo is built for **Cursor IDE**. The **commands** (the `.md` files Cursor executes as `/command-name`) are the primary product—not compiled code. A short, top-level path makes the canonical source obvious and simplifies install instructions.

**Problem:** Commands lived under `implementations/cursor/commands/`, which added nesting without benefit and made “copy from X” longer than necessary.

**Solution:** Canonical path is **`commands/`** at repo root. Users copy from `commands/` into `.cursor/commands/` or `~/.cursor/commands/`. The **`implementations/` tree is removed entirely**. MCP setup and other Cursor docs live under `docs/` (e.g. `docs/mcp-setup.md`, `docs/command-files.md`).

### Architecture

- **Canonical path:** `commands/` at repository root.
- **Contents:** Command `.md` files and `README.md`:
  - `complete-task.md`, `create-plan.md`, `create-task.md`, `create-test.md`, `decompose-task.md`, `mcp-status.md`, `refine-task.md`, `review-code.md`, `start-task.md`, `README.md`
- **Install targets:**
  - Project: `.cursor/commands/`
  - Global: `~/.cursor/commands/`
- **Format:** Plain markdown; no compilation. Cursor loads these as natural-language instructions.
- **Docs:** User-facing command docs stay in `docs/commands/`. The “Command Files” (install, canonical source) page is `docs/command-files.md`. MCP setup is `docs/mcp-setup.md`. Both are relocated from `docs/implementations/cursor/`; that tree is removed.
- **Dependencies:** MCP servers (Jira, GitHub, etc.) are required at runtime; setup is documented in `docs/mcp-setup.md`. Updating those instructions for recent MCP implementation changes is handled in a separate story.

### Anti-Patterns

- **Don’t nest commands under `implementations/`** — `commands/` at root is the contract.
- **Don’t put non-command files in `commands/`** — e.g. `mcp-setup.md` lives in `docs/`, not in `commands/`.
- **Don’t change command behavior in a pure relocation** — only paths and references change; instruction content is preserved.

---

## Contract

### Definition of Done

- [ ] All command `.md` files and `README.md` moved from `implementations/cursor/commands/` to `commands/`.
- [ ] **`implementations/` tree removed entirely** (no repo-root `implementations/`). Before removal: `mcp-setup.md` in `implementations/cursor/` is **deleted** (redundant with `docs/implementations/cursor/mcp-setup.md`); that docs file is **relocated** to `docs/mcp-setup.md`. The “Command Files” page `docs/implementations/cursor/commands/README.md` is **relocated** to `docs/command-files.md`. Then `docs/implementations/` is removed.
- [ ] All references to `implementations/cursor/commands`, `implementations/cursor`, and `implementations/` updated across: `docs/`, `AGENTS.md`, root `README.md`, `mkdocs.yml`, `.github/workflows/`, `specs/`, and in-command example paths. MCP Setup and Command Files links point to `docs/mcp-setup.md` and `docs/command-files.md`.
- [ ] `mkdocs build --strict` passes.
- [ ] Create-release workflow updated: `CHANGELOG_FILE=commands/CHANGELOG.md`, and archives built from `commands/` (not `implementations/`).

### Regression Guardrails

- **Install instructions must work** — `cp -r commands/* ~/.cursor/commands/` (and project variant) must produce working commands.
- **Docs must build** — `mkdocs build --strict` must succeed with no broken links or invalid nav.
- **AGENTS.md “Command Source”** must point at `commands/` (and `.cursor/commands/` when installed).
- **Release assets** — Tagged releases must include archives of `commands/` (e.g. `commands-{tag}.tar.gz`, `commands-{tag}.zip`).

### Scenarios

**Scenario: User installs from new path**
- **Given:** Repo with `commands/` at root
- **When:** User runs `cp -r commands/* ~/.cursor/commands/` and restarts Cursor
- **Then:** `/start-task`, `/create-task`, etc. are available and run correctly

**Scenario: MkDocs build**
- **Given:** All references updated from `implementations/cursor/commands` to `commands`
- **When:** `mkdocs build --strict` is run
- **Then:** Build succeeds and “Command Files” (and linked command source URLs) point to `commands/`

**Scenario: Release creates commands archive**
- **Given:** Create-release workflow updated to use `commands/` and `commands/CHANGELOG.md`
- **When:** A version tag (e.g. `v1.0.0`) is pushed
- **Then:** Release includes `commands-{tag}.tar.gz` and `commands-{tag}.zip` containing the contents of `commands/`

**Scenario: No leftover references to implementations**
- **Given:** Relocation, doc moves, and reference updates are done
- **When:** Grep for `implementations/` (excluding `.git` and `/.plans/` for historical plans)
- **Then:** No matches in active code, docs, or config; repo-root `implementations/` and `docs/implementations/` do not exist
