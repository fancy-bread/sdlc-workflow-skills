# MCP Tool Definitions (mcps/)

**`mcps/` is the list of record** for which MCP tools this project supports. Each `mcps/<server>/tools/*.json` conforms to [schemas/mcp-tool.schema.json](../schemas/mcp-tool.schema.json). Commands, validators, and mcp-status use this directory (not a runtime MCP API) to know what tools exist.

**List all tools:** `python schemas/validate_mcps.py --list` (TSV) or `--list --json`.

**Layout:** `mcps/<server>/tools/<tool>.json` — e.g. `mcps/atlassian/tools/getJiraIssue.json` for `mcp_atlassian_getJiraIssue`.

**MCP combinations:** **GitHub + Jira** or **GitHub + ADO** (issue tracker). ASDLC optional.

**Curated for tool limits:** We only include tools that are referenced in `skills/*/SKILL.md` or `skills/mcp-status/SKILL.md`. This keeps the list small so developers with multiple MCP servers stay under IDE tool limits. Add a tool only when a skill or mcp-status uses it.

## Servers

| Server | Path | Tools |
|--------|------|-------|
| **atlassian** | `atlassian/tools/` | getAccessibleAtlassianResources, getJiraIssue, getTransitionsForJiraIssue, transitionJiraIssue, addCommentToJiraIssue, searchJiraIssuesUsingJql, editJiraIssue, getJiraProjectIssueTypesMetadata, getJiraIssueRemoteIssueLinks, createJiraIssue, atlassianUserInfo |
| **github** | `github/tools/` | list_branches, create_branch, issue_read, create_issue, add_issue_comment, list_commits, get_commit, get_pull_request, create_pull_request |
| **asdlc** | `asdlc/tools/` | list_articles |
| **ado** | `ado/tools/` | core_list_projects |

## Schema

Each tool file must validate against **`schemas/mcp-tool.schema.json`**:

- **Required:** `name`, `inputSchema` (with `type: "object"` and `properties`)
- **Optional:** `description`, `title`, `outputSchema`, `annotations`

## Resolve rule

`mcp_Server_Tool` → `mcps/Server/tools/Tool.json`. Example: `mcp_atlassian_getJiraIssue` → `mcps/atlassian/tools/getJiraIssue.json`.

## Validator and list of record

```bash
python schemas/validate_mcps.py              # validate all mcps/**/*.json
python schemas/validate_mcps.py --list       # list all tools (TSV: server, tool, ref, path)
python schemas/validate_mcps.py --list --json
python schemas/validate_mcps.py mcp_Server_Tool   # resolve one ref, validate that file
```

The `--list` output is derived from `mcps/` only (filesystem); no MCP calls. Use it as the canonical tool list.

## Adding or updating tools

1. **Only add tools that are referenced in `skills/*/SKILL.md` or `skills/mcp-status/SKILL.md`** (see “Curated for tool limits” above).
2. Create or edit `mcps/<server>/tools/<tool>.json`.
3. Ensure `name` and `inputSchema` (with `type: "object"` and `properties`) are present.
4. Run `python schemas/validate_mcps.py`.

See [specs/mcps/spec.md](../specs/mcps/spec.md) for the feature spec.
