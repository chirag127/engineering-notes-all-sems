A source code review is a systematic examination of software source code, intended to find bugs and to estimate the code quality. The code review process contains the following stages:

- Best practice - identifying more efficient ways of completing any task.
- Error detection - finding logical errors.
- Code style - ensuring consistency and readability of the code.
- Documentation - checking the adequacy and accuracy of the code comments and documentation.
- Security - verifying the compliance with security standards and guidelines.

The following diagram illustrates the basic architecture of a source code review process using a tool-assisted approach:

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|   Developer    |      |   Reviewer     |      |   Code Review  |
|                |      |                |      |     Tool       |
+----------------+      +----------------+      +----------------+
       |                      |                      |
       |  Submit code         |                      |
       |--------------------->|                      |
       |                      |  Request review      |
       |                      |--------------------->|
       |                      |                      |
       |                      |  Perform review      |
       |                      |<---------------------|
       |                      |                      |
       |                      |  Provide feedback    |
       |<---------------------|                      |
       |                      |                      |
       |  Address feedback    |                      |
       |--------------------->|                      |
       |                      |                      |
       |  Merge code          |                      |
       |<--------------------------------------------|
       |                      |                      |
       V                      V                      V
```