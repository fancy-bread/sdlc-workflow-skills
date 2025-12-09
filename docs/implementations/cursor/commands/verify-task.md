# Verify Task

## Overview
Run verification checks before completing a task. This step is optional - automated checks will run on push.

## Steps
1. **Build the project**
   - Run build command
   - Verify no compilation errors
   - Check for build warnings

2. **Run test suite**
   - Execute all tests
   - Verify all tests pass
   - Check test execution time

3. **Check code coverage**
   - Generate coverage report
   - Verify coverage meets requirements (e.g., ≥90%)
   - Identify any coverage gaps

4. **Run linting**
   - Execute linter
   - Fix any style violations
   - Verify no remaining warnings

## Verification Checklist
- [ ] Build completes successfully
- [ ] No compilation errors
- [ ] All tests pass
- [ ] Code coverage meets target
- [ ] No linting errors or warnings
- [ ] Ready for commit
