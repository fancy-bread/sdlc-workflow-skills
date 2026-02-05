---
title: Releases
---

# Releases

All releases of the SDLC Workflow Skills (SDLC workflow skills).

---

## Latest Release

## [v1.1.5](https://github.com/fancybread-com/sdlc-workflow-skills/releases/tag/v1.1.5) - 2026-02-01

[**Download**](https://github.com/fancybread-com/sdlc-workflow-skills/releases/tag/v1.1.5) | [Release Notes](https://github.com/fancybread-com/sdlc-workflow-skills/releases/tag/v1.1.5)

---

## Release History

## [v1.1.5](https://github.com/fancybread-com/sdlc-workflow-skills/releases/tag/v1.1.5) - 2026-02-01

[**Download**](https://github.com/fancybread-com/sdlc-workflow-skills/releases/tag/v1.1.5) | [Release Notes](https://github.com/fancybread-com/sdlc-workflow-skills/releases/tag/v1.1.5)

## [v1.1.4](https://github.com/fancybread-com/sdlc-workflow-skills/releases/tag/v1.1.4) - 2026-01-31

[**Download**](https://github.com/fancybread-com/sdlc-workflow-skills/releases/tag/v1.1.4) | [Release Notes](https://github.com/fancybread-com/sdlc-workflow-skills/releases/tag/v1.1.4)

## [v1.1.3](https://github.com/fancybread-com/sdlc-workflow-skills/releases/tag/v1.1.3) - 2026-01-28

[**Download**](https://github.com/fancybread-com/sdlc-workflow-skills/releases/tag/v1.1.3) | [Release Notes](https://github.com/fancybread-com/sdlc-workflow-skills/releases/tag/v1.1.3)

## [v1.1.2](https://github.com/fancybread-com/sdlc-workflow-skills/releases/tag/v1.1.2) - 2026-01-28

**[Download](https://github.com/fancybread-com/sdlc-workflow-skills/releases/tag/v1.1.2)** | [Release Notes](https://github.com/fancybread-com/sdlc-workflow-skills/releases/tag/v1.1.2)

## [v1.1.1](https://github.com/fancybread-com/sdlc-workflow-skills/releases/tag/v1.1.1) - 2026-01-27

**[Download](https://github.com/fancybread-com/sdlc-workflow-skills/releases/tag/v1.1.1)** | [Release Notes](https://github.com/fancybread-com/sdlc-workflow-skills/releases/tag/v1.1.1)

## [v1.1.0](https://github.com/fancybread-com/sdlc-workflow-skills/releases/tag/v1.1.0) - 2026-01-25

**[Download](https://github.com/fancybread-com/sdlc-workflow-skills/releases/tag/v1.1.0)** | [Release Notes](https://github.com/fancybread-com/sdlc-workflow-skills/releases/tag/v1.1.0)

## [v1.0.1](https://github.com/fancybread-com/sdlc-workflow-skills/releases/tag/v1.0.1) - 2025-12-22

**[Download](https://github.com/fancybread-com/sdlc-workflow-skills/releases/tag/v1.0.1)** | [Release Notes](https://github.com/fancybread-com/sdlc-workflow-skills/releases/tag/v1.0.1)

## [v1.0.0](https://github.com/fancybread-com/sdlc-workflow-skills/releases/tag/v1.0.0) - 2025-12-22

**[Download](https://github.com/fancybread-com/sdlc-workflow-skills/releases/tag/v1.0.0)** | [Release Notes](https://github.com/fancybread-com/sdlc-workflow-skills/releases/tag/v1.0.0)

---

## Download

Releases include skills packaged as:
- **`.tar.gz`** - For Unix/Linux/macOS
- **`.zip`** - For Windows

Download the latest release from the [GitHub Releases page](https://github.com/fancybread-com/sdlc-workflow-skills/releases).

---

## Installation

### Install from GitHub (Cursor)

In Cursor you can load skills directly from this repo: **Settings → Rules → Add Rule → Remote Rule (Github)** and enter:

```text
https://github.com/fancybread-com/sdlc-workflow-skills
```

See [Cursor docs: Installing skills from GitHub](https://cursor.com/docs/context/skills#installing-skills-from-github). No download or copy step; Cursor loads from the repo.

### Install from a release (Cursor, Claude, Codex)

The same **`skills/`** layout works for Cursor, Claude, and Codex. After downloading a release, extract and copy into your environment’s skills directory:

```bash
# Extract the archive
tar -xzf skills-vX.X.X.tar.gz  # Unix/Linux/macOS
# OR
unzip skills-vX.X.X.zip  # Windows

# Cursor (global or per-project):
cp -r skills/* ~/.cursor/skills/
# OR: mkdir -p .cursor/skills && cp -r skills/* .cursor/skills/

# Claude (global or per-project):
cp -r skills/* ~/.claude/skills/
# OR: mkdir -p .claude/skills && cp -r skills/* .claude/skills/

# Codex (global or per-project):
cp -r skills/* ~/.codex/skills/
# OR: mkdir -p .codex/skills && cp -r skills/* .codex/skills/
```

See the [Getting Started guide](getting-started.md) for detailed setup instructions.

---

## Changelog

For detailed changes in each release, see the [GitHub Releases](https://github.com/fancybread-com/sdlc-workflow-skills/releases) page.
