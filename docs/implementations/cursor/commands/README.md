# Cursor Commands

Natural language commands for Cursor IDE. Type `/command-name` in Cursor chat to trigger workflows.

## Quick Reference

### Product
| Command | Usage |
|---------|-------|
| `/create-task` | Create task in tracker (story, epic, bug, task, etc.) |
| `/decompose-task` | Decompose large task into subtasks |

### Planning
| Command | Usage |
|---------|-------|
| `/create-plan` | Create technical implementation plan |

### Development
| Command | Usage |
|---------|-------|
| `/start-task` | Start working on story |
| `/complete-task` | Create PR and push |

### Quality
| Command | Usage |
|---------|-------|
| `/create-test` | Generate unit tests (adapts for backend/frontend) |
| `/review-code` | AI code review |

### Utilities
| Command | Usage |
|---------|-------|
| `/mcp-status` | Check MCP server authentication status |

## Installation

### Option 1: Project Commands

```bash
cp -r implementations/cursor/commands/* /path/to/project/.cursor/commands/
```

### Option 2: Global Commands

```bash
cp -r implementations/cursor/commands/* ~/.cursor/commands/
```

### Option 3: Team Commands

For Cursor Team/Enterprise:
1. Go to [Cursor Dashboard → Team Content → Commands](https://cursor.com/dashboard?tab=team-content&section=commands)
2. Create team commands from these files
3. Commands auto-sync to team members

## Example Workflow

**Development Cycle:**
```
/create-task --type=story for [feature]
/decompose-task EPIC-123  # If breaking down large work
/create-plan for PROJ-123
/start-task PROJ-123
/create-test --type=unit for [component]  # As needed
/complete-task PROJ-123
/review-code for PR #42
```

**Epic to Story Flow:**
```
/create-task --type=epic from phase-one.md
/decompose-task EPIC-123
/create-plan for STORY-10
/start-task STORY-10
/complete-task STORY-10
```

## Command Files

All commands are markdown files in the `commands/` directory:
- Each `.md` file contains instructions that Cursor's AI interprets to execute the workflow
- Commands adapt to your project's structure, frameworks, and conventions

Each `.md` file contains instructions that Cursor's AI interprets to execute the workflow.

## Configuration

Commands require MCP servers for Jira/ADO and GitHub. See [MCP Setup](../mcp-setup.md).

## Troubleshooting

**Commands not showing?**
Restart Cursor after copying files.

**Command fails?**
Check MCP servers are configured in Cursor Settings.

**Integration error?**
Verify credentials and permissions in MCP settings.
