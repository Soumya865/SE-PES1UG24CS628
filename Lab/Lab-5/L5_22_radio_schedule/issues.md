# Lab 5: Static Code Analysis — Issues and Fixes

| Issue | Type | Line(s) Before Fix | Description | Fix Approach |
|---|---|---|---|---|
| SQL injection risk | Security — Medium | 11 | SQL query was constructed using string formatting, allowing potentially unsafe input. | Used parameterized SQL queries with placeholders. |
| Unsafe eval usage | Security — Medium | 21 | `eval()` could execute arbitrary Python expressions. | Replaced it with a restricted AST-based arithmetic and comparison evaluator. |
| Hardcoded password | Security — Low | 5 | A password was stored directly in the source code. | Removed the unused hardcoded password. |
| Broad exception handling | Code quality | 22 | Catching `Exception` could hide unexpected errors. | Caught specific exceptions relevant to expression evaluation. |
| Global statement | Code quality | 10 | A function modified global state. | Removed the global counter and calculated scheduled minutes from the database. |
| Missing docstrings | Code quality | 1, 9, 15, 19, 26, 31, 35 | The module and functions lacked documentation. | Added module and function docstrings. |
| Invalid naming style | Code quality | 6, 9, 15, 19, 26, 31 | Names did not follow Pylint naming conventions. | Used appropriate uppercase constants and snake_case function names. |
| Long lines | Formatting | 4, 11, 27 | Lines exceeded the configured length limits. | Split long statements across multiple lines. |
| Multiple statements on one line | Formatting | 27 | An `if` statement contained multiple statements on one line. | Separated the statements onto individual lines. |
| String formatting | Code quality | 11, 16 | Older string formatting was used where an f-string was suitable. | Used an f-string for the programme label and parameterized SQL for database input. |

## Verification

- Original Pylint score: 2.41/10
- Final Pylint score: 10.00/10
- Final Bandit report: No issues identified.
- Final Flake8 report: No violations displayed.
- The demonstration program ran successfully after the changes.

  ## Bandit Verification

- Original findings: 3 (1 Low and 2 Medium severity).
- Final findings: No issues identified.
- SQL queries use parameterized placeholders.
- Unsafe eval() was replaced with a restricted AST-based evaluator.
- The unused hardcoded password was removed.

  ## Flake8 Verification

- Original findings: 4 formatting violations.
- Final findings: No violations displayed.
- Long lines were split into shorter lines.
- Multiple statements on one line were separated.

  
