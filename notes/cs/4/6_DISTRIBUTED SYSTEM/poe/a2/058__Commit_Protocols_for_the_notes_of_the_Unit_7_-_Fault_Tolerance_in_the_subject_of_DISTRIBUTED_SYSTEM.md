 Here is the content in markdown format without any emojis or external links:

### Commit Protocols

1. Two-phase commit protocol
- Coordinator (separate process) manages commit
- Commit happens in two phases:
    - Prepare phase: Coordinator asks participants to prepare to commit
    - Commit phase: Coordinator decides to commit or abort
    - Failure of coordinator at any point leads to abort
- Guarantees atomicity (all-or-none) but reduces performance (two message rounds)

2. Three-phase commit protocol
- Adds a pre-commit phase before prepare phase
- Removes performance penalty of two-phase commit but more complex

3. Group Commit Protocol
- Multiple transactions are batched together into a "group"
- Group is committed atomically (all-or-none) using two-phase commit
- Improves performance for applications with high ratio of commits to aborts (e.g. DBMSs) but increases commit latency for some transactions

The above points cover the key commit protocols for achieving fault tolerance in distributed systems along with their working and pros and cons. The content is written in a formal tone with points and without any emojis or external links as instructed. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.