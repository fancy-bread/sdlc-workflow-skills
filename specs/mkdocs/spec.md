# Feature: MkDocs Documentation Site

> **ASDLC Pattern**: [The Spec](https://asdlc.io/patterns/the-spec/)
> **Practice Guide**: [Living Specs](https://asdlc.io/practices/living-specs/)
> **Status**: Active
> **Last Updated**: 2026-02-14

---

## Blueprint

### Context

The documentation site is the user-facing entry point for this repo. It needs a single source of truth for how the site is built, configured, and deployed so that agents and developers can change `mkdocs.yml`, add pages, or adjust theme/plugins without breaking the build or deployment.

**Problem:** Without a spec, changes to MkDocs config (nav, theme, plugins, extensions) can inadvertently break the build, link check, or GitHub Pages deployment.

**Solution:** This spec defines the MkDocs setup as the contract for the docs site: config layout, required plugins and extensions, nav structure, and deployment flow.

### Architecture

- **Config:** `mkdocs.yml` at repo root. Defines: `site_name`, `site_description`, `theme` (Material), `nav`, `plugins`, `markdown_extensions`, `extra`, `extra_css`.
- **Content:** `docs/` — user-facing markdown. Nav entries point under `docs/` (e.g. `docs/skills/index.md` → nav `Skills: skills/index.md`). `specs/` is **not** in the nav; specs are internal living docs.
- **Theme:** Material for MkDocs. Palette (light/dark), font (Roboto, Roboto Mono), features (navigation, search, toc, content) are configured in `mkdocs.yml`.
- **Plugins:** `search` (required for site search). Optional plugins (e.g. `git-revision-date-localized`, `minify`, `mermaid2`) may be added; document in this spec if they become required.
- **Markdown extensions:** Python Markdown + pymdownx (admonition, def_list, tables, toc, superfences with mermaid, tasklist, etc.). See `mkdocs.yml`; `includes/abbreviations.md` is auto-appended via pymdownx.snippets.
- **Build:** `mkdocs build --strict` (CI and local). Strict mode fails on broken nav or missing files.
- **Link check:** Lychee runs in CI (`.github/workflows/build-docs.yml`) over `./site/**/*.html` with exclusions for external domains (e.g. asdlc.io, github.com/fancybread-com/...).
- **Deployment:** GitHub Pages via Actions. Deploy runs only on `workflow_dispatch` with `ref == refs/heads/main`; artifact from build job is uploaded and deployed with `actions/deploy-pages`.
- **Dependencies:** `requirements.txt` — MkDocs 1.5+ (&lt;2), mkdocs-material 9.5+ (&lt;10). Same venv can be used for `schemas/validate.py` (AGENTS.md §5).

### Anti-Patterns

- **Don’t remove required plugins or break nav** — Removing `search` or breaking the `nav` structure breaks the site. Adding or reordering nav entries is fine if links and paths stay valid.
- **Don’t hardcode environment-specific URLs in the spec** — Use relative paths or document that `site_url` / edit_uri are set in `mkdocs.yml` for the canonical deployment (e.g. GitHub).
- **Don’t add `specs/` to the public nav** — Specs are for agents and maintainers; they live in `specs/` but are not linked from the docs site nav.
- **Don’t change theme or major extensions without updating this spec** — If Material version or critical pymdownx extensions change, update Blueprint and Contract so the spec stays the source of truth.

---

## Contract

### Definition of Done

- [ ] `mkdocs.yml` exists at repo root and defines site_name, theme (Material), nav, plugins, markdown_extensions.
- [ ] `mkdocs build --strict` succeeds from repo root with `pip install -r requirements.txt`.
- [ ] Link check (Lychee in CI or equivalent) passes for built HTML under `site/` with documented exclusions.
- [ ] Docs content lives under `docs/`; nav entries reference paths under `docs/` (e.g. `skills/index.md`).
- [ ] Deployment to GitHub Pages is via `.github/workflows/build-docs.yml` (build job + deploy on workflow_dispatch + main).
- [ ] This spec (Blueprint + Contract) is updated in the same commit when MkDocs config or deployment behavior changes (Same-Commit Rule).

### Regression Guardrails

- **Build must stay strict** — `mkdocs build --strict` is the baseline; do not remove `--strict` without updating this spec and CI.
- **Nav and content paths** — Every nav entry must resolve to an existing file under `docs/` (or documented exception).
- **Required plugins** — `search` is required; if others become required, list them in the Blueprint and Guardrails.

### Scenarios

**Scenario: Local build succeeds**
- **Given:** Repo root, Python venv with `requirements.txt` installed
- **When:** The user runs `mkdocs build --strict`
- **Then:** Build completes with no errors; `site/` contains generated HTML and assets.

**Scenario: CI build and link check**
- **Given:** PR targeting `main` or push to `main`
- **When:** `.github/workflows/build-docs.yml` runs (build job)
- **Then:** `mkdocs build --strict` passes; Lychee link check passes for `./site/**/*.html` (with configured exclusions).

**Scenario: Deploy to GitHub Pages**
- **Given:** `workflow_dispatch` on branch `main`
- **When:** Build job and deploy job run
- **Then:** Site artifact is uploaded and deployed to GitHub Pages; published site reflects `docs/` and `mkdocs.yml` from `main`.

**Scenario: Nav entry points to missing file**
- **Given:** A new nav entry in `mkdocs.yml` that references a path under `docs/` that does not exist
- **When:** The user runs `mkdocs build --strict`
- **Then:** Build fails with a clear error about the missing file.
