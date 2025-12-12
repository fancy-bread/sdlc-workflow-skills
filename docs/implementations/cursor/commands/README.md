# Cursor Commands

Natural language commands for Cursor IDE. Type `/command-name` in Cursor chat to trigger workflows.

## Quick Reference

### Product
| Command | Usage |
|---------|-------|
| `/create-task` | Create task in tracker (story, epic, bug, task, etc.) |
| `/breakdown-tasks` | Break down large task into subtasks |

### Planning
| Command | Usage |
|---------|-------|
| `/estimate-stories` | Estimate effort |
| `/prioritize-backlog` | Prioritize work |
| `/plan-sprint` | Plan sprint (Scrum) |
| `/refine-backlog` | Refine backlog (Kanban) |
| `/create-plan` | Create technical plan |
| `/refine-plan` | Update existing plan |

### Development
| Command | Usage |
|---------|-------|
| `/start-task` | Start working on story |
| `/complete-task` | Create PR and push |

### Testing
| Command | Usage |
|---------|-------|
| `/create-test` | Generate unit tests (adapts for backend/frontend) |
| `/run-tests` | Execute test suite |
| `/watch-tests` | Run tests on file changes |
| `/fix-failing-tests` | Fix test failures |
| `/check-coverage` | Analyze coverage |

### Code Quality
| Command | Usage |
|---------|-------|
| `/review-code` | AI code review |
| `/fix-linting` | Fix linting errors |

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

**Scrum:**
```
/estimate-stories in EPIC-1
/plan-sprint 23
/create-plan for PROJ-123
/start-task PROJ-123
/complete-task PROJ-123
```

**Kanban:**
```
/refine-backlog
/create-plan for PROJ-123
/start-task PROJ-123
/complete-task PROJ-123
```

## Command Files

Commands are organized in subdirectories:
- `product/` - Story and epic creation
- `planning/` - Estimation, prioritization, sprint planning
- `development/` - Task execution workflow
- `quality/` - Testing and code quality

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
