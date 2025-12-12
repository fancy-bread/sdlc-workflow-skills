# Create Task

## Overview
Create a task in the issue tracker with a specified type (epic, story, bug, task, etc.). The command adapts its workflow based on the task type.

## Usage

The command supports two syntax styles:

### Natural Language Style
```
/create-task [type] [description or source]
```

### Explicit Flag Style
```
/create-task --type=[type] [description or source]
```

**Examples:**

**Natural Language:**
- `/create-task story for user authentication`
- `/create-task epic from phase-one.md`
- `/create-task bug: login fails with OAuth`
- `/create-task task: refactor auth service`

**Explicit Flag:**
- `/create-task --type=story for user authentication`
- `/create-task --type=epic from phase-one.md`
- `/create-task --type=bug login fails with OAuth`
- `/create-task --type=task refactor auth service`

## Task Types

### Epic
High-level initiative or phase plan that contains multiple stories.

**Usage:**
- `/create-task --type=epic from [plan-file.md]`
- `/create-task epic from [plan-file.md]`
- `/create-task --type=epic [description]`
- `/create-task epic: [description]`

**Workflow:**
1. **Read the epic plan** (if from file)
   - Review plan document (e.g., `.plans/phase-one.md`)
   - Understand goals and scope
   - Identify major tasks and milestones

2. **Create the epic**
   - Generate epic title and description
   - Set priority and labels
   - Create epic in issue tracker

3. **Break down into stories** (optional, if plan contains tasks)
   - Identify individual work items
   - Create child stories for each task
   - Link stories to parent epic
   - Set priorities for each story

**Epic Checklist:**
- [ ] Epic plan reviewed and understood (if from file)
- [ ] Epic created with clear description
- [ ] Goals and scope documented
- [ ] Child stories identified (if applicable)
- [ ] All stories created and linked to epic (if applicable)
- [ ] Priorities set for epic and stories
- [ ] Stories ready for team pickup (if applicable)

---

### Story
User story or feature request that represents a single piece of functionality.

**Usage:**
- `/create-task --type=story for [feature]`
- `/create-task story for [feature]`
- `/create-task --type=story [description]`
- `/create-task story: [description]`

**Workflow:**
1. **Analyze the request**
   - Understand the feature scope and goals
   - Identify acceptance criteria
   - Determine priority level

2. **Generate story details**
   - Write clear, descriptive title
   - Create comprehensive description
   - Define acceptance criteria
   - Add relevant labels and tags

3. **Create in issue tracker**
   - Create story with generated content
   - Set appropriate priority
   - Link to parent epic if applicable
   - Leave unassigned in "To Do" status

**Story Checklist:**
- [ ] Title is clear and descriptive
- [ ] Description includes context and motivation
- [ ] Acceptance criteria are well-defined
- [ ] Priority is set appropriately
- [ ] Labels/tags are added
- [ ] Linked to epic if applicable
- [ ] Status is "To Do" (unassigned)

---

### Bug
Defect or issue that needs to be fixed.

**Usage:**
- `/create-task --type=bug [description]`
- `/create-task bug: [description]`
- `/create-task --type=bug for [description]`
- `/create-task bug for [description]`

**Workflow:**
1. **Analyze the bug report**
   - Understand the problem and symptoms
   - Identify reproduction steps
   - Determine severity and priority
   - Identify affected components/systems

2. **Generate bug details**
   - Write clear, descriptive title
   - Create detailed description
   - Document reproduction steps
   - Add expected vs actual behavior
   - Include environment details if available

3. **Create in issue tracker**
   - Create bug with generated content
   - Set appropriate severity and priority
   - Add relevant labels (e.g., "bug", component tags)
   - Link to related stories/epics if applicable
   - Leave unassigned in "To Do" status

**Bug Checklist:**
- [ ] Title clearly describes the problem
- [ ] Description includes symptoms and impact
- [ ] Reproduction steps are documented
- [ ] Expected vs actual behavior is clear
- [ ] Severity and priority are set appropriately
- [ ] Labels/tags are added (bug, component, etc.)
- [ ] Linked to related tasks if applicable
- [ ] Status is "To Do" (unassigned)

---

### Task
Technical work item or chore that doesn't fit into story/bug categories.

**Usage:**
- `/create-task --type=task [description]`
- `/create-task task: [description]`
- `/create-task --type=task for [description]`
- `/create-task task for [description]`

**Workflow:**
1. **Analyze the task**
   - Understand the work to be done
   - Identify technical requirements
   - Determine priority and effort

2. **Generate task details**
   - Write clear, descriptive title
   - Create detailed description
   - Document technical requirements
   - Add relevant labels and tags

3. **Create in issue tracker**
   - Create task with generated content
   - Set appropriate priority
   - Link to parent epic if applicable
   - Leave unassigned in "To Do" status

**Task Checklist:**
- [ ] Title is clear and descriptive
- [ ] Description includes technical context
- [ ] Requirements are well-defined
- [ ] Priority is set appropriately
- [ ] Labels/tags are added
- [ ] Linked to epic if applicable
- [ ] Status is "To Do" (unassigned)

---

### Other Types
For any other task type (e.g., "subtask", "improvement", "spike", etc.), the command will:

1. **Analyze the request**
   - Understand the work scope
   - Identify requirements
   - Determine priority

2. **Generate task details**
   - Write clear, descriptive title
   - Create comprehensive description
   - Add relevant labels and tags

3. **Create in issue tracker**
   - Create task with generated content
   - Set appropriate priority
   - Link to parent task if applicable
   - Leave unassigned in "To Do" status

## General Steps

1. **Parse command arguments**
   - Extract task type from command
   - Extract description or source file
   - Validate task type is supported

2. **Gather context** (if applicable)
   - Read source file if provided
   - Check for related tasks/epics
   - Review project conventions for task creation

3. **Execute type-specific workflow**
   - Follow the workflow for the specified task type
   - Generate appropriate content based on type
   - Create task in tracker

4. **Verify creation**
   - Confirm task was created successfully
   - Display task key/ID
   - Provide link to created task

## Type Detection

The command supports multiple ways to specify the task type:

**Explicit Flag Style (Recommended for clarity):**
- `/create-task --type=story for ...`
- `/create-task --type=bug ...`
- `/create-task --type=epic from ...`

**Natural Language Style:**
- `/create-task story for ...`
- `/create-task bug: ...` (colon syntax)
- `/create-task epic from ...`

**Type Parsing Priority:**
1. Check for `--type=` flag first (most explicit)
2. Look for type as first word before "for", "from", or colon
3. If no type specified, prompt user or default to "story"

**Type Validation:**
- Validate type against supported task types for the tracker
- Suggest similar types if typo detected (e.g., "stroy" → "story")
- Case-insensitive matching (e.g., `--type=BUG` = `--type=bug`)

## Common Task Types

- **epic** - High-level initiative
- **story** - User story or feature
- **bug** - Defect or issue
- **task** - Technical work item
- **subtask** - Child of another task
- **improvement** - Enhancement request
- **spike** - Research or investigation
- **technical-debt** - Code quality improvement

*Note: Available types may vary by issue tracker. The command should adapt to the tracker's supported types.*

