# Changelog

All notable changes to the SDLC Workflow Skills (SDLC workflow skills) are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

## [2.1.0] - 2026-02-14

### Added

- **MCP discovery:** mcp-status skill now discovers project-level (`.cursor/mcp.json`) and extension-exposed MCP servers in addition to user-level config.
- **MkDocs spec:** New `specs/mkdocs/spec.md` for docs build and deployment.

### Changed

- **Schema:** Command schema renamed to `skill.schema.json`; validation and references updated (FB-71).
- **Specs:** `command-audit` and `commands` specs renamed to `skill-audit` and `skills` (FB-68).
- **CI:** Workflow renamed from command-validation to skill-validation.

## [2.0.0] - 2026-02-03

### Added

- **Agent Skills format:** Canonical source is `skills/` (each skill is `skills/<name>/SKILL.md` with YAML frontmatter). Same layout works for **Cursor**, **Claude**, and **Codex**.
- **Cursor: Install from GitHub** — Documented and verified; add repo as Remote Rule (Github). `scripts/verify_github_install.py` checks layout; runs in CI.
- **Claude / Codex** — Install paths documented (`.claude/skills/`, `~/.claude/skills/`, `.codex/skills/`, `~/.codex/skills/`). Release archives support copy-install for all three.
- **Platform-inclusive docs** — Wording updated so the project is not Cursor-only; Cursor remains primary tested environment.

### Changed

- **Project name:** Agent Command Library → **SDLC Workflow Skills**. Repo: `agent-command-library` → **sdlc-workflow-skills** (all URLs and references updated).
- **Docs structure:** `docs/commands/` → `docs/skills/`; MkDocs nav and internal links updated.
- **Release artifacts:** `skills-{tag}.tar.gz` and `skills-{tag}.zip` (unchanged); install instructions now include Cursor, Claude, and Codex copy paths.
- **Validation:** Runs on `skills/*/SKILL.md`; schema validates skill body (frontmatter stripped). MCP refs validated in `docs/skills/` as well as `skills/`.
- **AGENTS.md, README, getting-started, releases, mcp-setup:** Updated for skills, new name, GitHub install, and Cursor/Claude/Codex.

### Removed

- `commands/` directory; skills are the single source of truth.

---

## [1.1.5] - 2026-02-01

[Release notes](https://github.com/fancy-bread/sdlc-workflow-skills/releases/tag/v1.1.5)

---

[Unreleased]: https://github.com/fancy-bread/sdlc-workflow-skills/compare/v2.1.0...HEAD
[2.1.0]: https://github.com/fancy-bread/sdlc-workflow-skills/releases/tag/v2.1.0
[2.0.0]: https://github.com/fancy-bread/sdlc-workflow-skills/releases/tag/v2.0.0
[1.1.5]: https://github.com/fancy-bread/sdlc-workflow-skills/releases/tag/v1.1.5
