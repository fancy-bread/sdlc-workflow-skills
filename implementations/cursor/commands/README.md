# Commands Reference

**Natural language instructions that AI agents execute with context.**

## What Are Commands?

Commands are **not scripts**. They're markdown files containing instructions that tell AI agents:

- **What** to achieve (the goal)
- **What context** to gather (story, codebase, plans)
- **What decisions** to make (or ask you about)
- **What artifacts** to create (branches, commits, PRs)

The AI reads these instructions and executes them contextually based on your specific project.

### Example: How `/start-task` Works

**The command file says:**
> "Read the story from issue tracker, create a branch following project conventions, read the implementation plan, implement the code matching the project style."

**For a Python Flask project, AI might:**
- Create branch `feature/auth-123`
- Add code to `app/routes/auth.py`
- Write tests in `tests/test_auth.py` using pytest
- Update `requirements.txt`

**For a React TypeScript project, AI might:**
- Create branch `feature/auth-123`
- Add component in `src/components/Auth.tsx`
- Write tests in `src/components/Auth.test.tsx` using Jest
- Update `package.json`

**Same command. Different execution. Context drives behavior.**

---

## How to Use Commands

### 1. Type `/command-name` in Cursor Chat

```
/start-task PROJ-123
```

### 2. AI Reads the Command File

Cursor loads `start-task.md` and understands the workflow.

### 3. AI Gathers Context

- Reads story from Jira
- Checks your codebase structure
- Reviews implementation plan
- Understands your coding patterns

### 4. AI Executes Contextually

Implements the feature using your frameworks, style, and conventions.

### 5. You Review and Approve

At key decision points, AI asks for your approval (plans, major changes).

---

## Available Commands

### 📦 Product (2 commands)

Define and create work items.

| Command | What It Does | Example |
|---------|--------------|---------|
| `/create-task` | Creates task in tracker with specified type (epic, story, bug, task, etc.) | `/create-task --type=story for OAuth login`<br>`/create-task --type=epic from phase-one.md`<br>`/create-task --type=bug login fails`<br><br>*Also supports natural language: `/create-task story for ...`* |
| `/decompose-task` | Decomposes large task into well-defined subtasks | `/decompose-task TASK-123`<br><br>*Critical planning activity - ensures proper task decomposition* |

---

### 📋 Planning (2 commands)

Refine tasks and create technical implementation plans.

| Command | What It Does | Example |
|---------|--------------|---------|
| `/refine-task` | Refines task to meet Definition of Ready with story points | `/refine-task FB-15` |
| `/create-plan` | Creates detailed technical design | `/create-plan for AUTH-10` |

---

### 🛠️ Development (2 commands)

Implement and ship features.

| Command | What It Does | Example |
|---------|--------------|---------|
| `/start-task` | Begins development (branch, context) | `/start-task AUTH-123` |
| `/complete-task` | Commits, pushes, creates PR | `/complete-task AUTH-123` |

---

### ✅ Quality (2 commands)

Test and review code.

| Command | What It Does | Example |
|---------|--------------|---------|
| `/create-test` | Generates unit tests (adapts for backend/frontend) | `/create-test --type=unit for AuthService` |
| `/review-code` | AI code review | `/review-code for PR #42` |

---

### 🔧 Utilities (1 command)

System and integration management.

| Command | What It Does | Example |
|---------|--------------|---------|
| `/mcp-status` | Check MCP server authentication status | `/mcp-status` |

---

## Installation

Choose where you want commands available:

```bash
# Option 1: Global (all projects)
cp -r implementations/cursor/commands/* ~/.cursor/commands/

# Option 2: Per-project
mkdir -p .cursor/commands
cp -r implementations/cursor/commands/* .cursor/commands/

# Option 3: Team (Cursor Enterprise)
# Use Cursor Dashboard → Team Content → Commands
```

**Restart Cursor after installing.**

[Detailed setup guide →](../mcp-setup.md)

## Complete Workflows

### Development Cycle

```bash
# Create and plan work
/create-task --type=story for [feature]
/decompose-task EPIC-123  # If decomposing large work
/create-plan for AUTH-10

# Development
/start-task AUTH-10
/create-test --type=unit for [component]  # As needed during implementation
/complete-task AUTH-10

# Review
/review-code for PR #42
```

### Epic to Story Flow

```bash
# Create epic and break it down
/create-task --type=epic from phase-one.md
/decompose-task EPIC-123

# Plan and implement each story
/create-plan for AUTH-10
/start-task AUTH-10
/complete-task AUTH-10
```

## Key Concepts

### Planning and Development Flow

1. **Task Creation**: Use `/create-task` to create epics, stories, bugs, or tasks in your issue tracker
2. **Task Breakdown**: Use `/decompose-task` to decompose large tasks into manageable subtasks
3. **Backlog Refinement**: Use `/refine-task` to ensure tasks meet Definition of Ready (before sprint planning)
4. **Technical Planning**: Use `/create-plan` to create detailed implementation plans before coding
5. **Implementation**: Use `/start-task` and `/complete-task` to implement work
6. **Quality**: Use `/create-test` and `/review-code` to ensure code quality

### Task Types

Commands support different task types from your issue tracker:
- **Epic**: High-level initiatives containing multiple stories
- **Story**: User-facing features or functionality
- **Bug**: Defects that need fixing
- **Task**: Technical work or chores

The `/create-task` command adapts its workflow based on task type, ensuring appropriate validation and structure for each.

## How Commands Work: An Example

You type: `/start-task AUTH-123`

**What happens:**

1. **AI reads command file** - Understands the start-task workflow
2. **Gathers context** - Fetches story from Jira, reads implementation plan, checks codebase
3. **Validates prerequisites** - Checks MCP connections, verifies plan exists, ensures story status
4. **Sets up environment** - Creates feature branch, transitions story to "In Progress"
5. **Implements work** - Follows the plan, writes code and tests matching project patterns
6. **Commits progress** - Makes logical commits using conventional format

**Output:**
```
✓ MCP servers connected
✓ Plan file found: .plans/AUTH-123-user-authentication.plan.md
✓ Story AUTH-123 transitioned to "In Progress"
✓ Branch created: feat/AUTH-123
✓ Implementation started...

[Code changes made following the plan]
[Tests written]
[Documentation updated]
```

**This is context-aware automation, not scripted automation.**

## What Commands Need to Work

Commands connect to your tools via **adapters**:

| Adapter Type | Tools | What It Does |
|--------------|-------|--------------|
| **Issue Management** | Jira, Azure DevOps | Read/create stories, update status |
| **Version Control** | GitHub, GitLab | Create branches, PRs |
| **Plan Storage** | Filesystem | Store plans in `.plans/` |

**Configuration:** Set up via MCP servers. [Setup guide →](../mcp-setup.md)

---

## Customizing Commands

Commands are markdown files. Edit them to match your workflow.

**Example:** Modify `/complete-task` to require specific commit format

```markdown
# Complete Task

## Steps
1. Verify tests pass
2. Create commit with format: `type(scope): message`
   - Types: feat, fix, docs, test, refactor
3. Push and create PR
...
```

Save in `.cursor/commands/complete-task.md`

**Keep it declarative** - Describe *what* to achieve, not *how*.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| **Command not found** | Restart Cursor. Check `.cursor/commands/` or `~/.cursor/commands/` |
| **Command fails** | Verify MCP servers connected (use `/mcp-status` or Settings → MCP) |
| **Jira errors** | Check story exists, you have permissions |
| **GitHub errors** | Verify token has `repo` scope, check write access |
| **Plan not found** | Run `/create-plan` first before `/start-task` |
| **Story missing detail** | Commands will ask for clarification if information is insufficient |

[Detailed troubleshooting →](../README.md#troubleshooting)

---

## Quick Reference

**Most Common Commands:**

```bash
# Create work
/create-task --type=story for [feature]
/create-task --type=bug [description]
/decompose-task [EPIC-123]

# Plan
/create-plan for [TASK-123]

# Develop
/start-task [TASK-123]
/create-test --type=unit for [component]
/complete-task [TASK-123]

# Review
/review-code for PR #42

# Utilities
/mcp-status
```

**Typical Flow:** `/create-task` → `/decompose-task` → `/create-plan` → `/start-task` → `/complete-task`

---

## Learn More

- [Setup Guide](../mcp-setup.md) - Configure MCP servers
- [Implementation Guide](../README.md) - Cursor-specific details
- [Core Methodology](../../../core/index.md) - Understand the approach
- [Workflows](../../../core/workflows/) - Detailed workflow guides
- [Cursor Commands Docs](https://cursor.com/docs/agent/chat/commands) - Official Cursor documentation
