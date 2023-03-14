 Here is the content in markdown format:

### Atomic Commit protocols for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

Atomic Commit protocols ensure that all distributed transactions are committed or aborted in an all-or-nothing fashion across multiple databases. This ensures consistency across the distributed system. The popular Atomic Commit protocols are:

1. Two-phase commit protocol:
- Consists of two phases: Commit-Request phase and Commit-Decision phase
- In Commit-Request phase, the coordinator (transaction manager) asks all participants (resource managers) to prepare to commit
- In Commit-Decision phase, the coordinator decides to either commit (if all participants voted to commit in the first phase) or abort (if any participant voted to abort in the first phase) and informs all participants of the decision
- Advantage: Ensures atomicity. Disadvantage: The protocol has a performance overhead as multiple rounds of messages are exchanged.

2. Three-phase commit protocol:
- Adds an extra pre-commit phase before the commit-request phase to reduce the blocking time of the transaction manager
- The pre-commit phase allows participants to prepare to commit but does not lock the resources
- If any participant aborts in the pre-commit phase, the transaction is immediately aborted without involving the commit-request phase
- Advantage: Better performance than two-phase commit. Disadvantage: More complex than two-phase commit and not widely used in practice.

[Include diagrams and examples if helpful]

The choice of the Atomic Commit protocol depends on the performance and consistency guarantees required by the application. Two-phase commit is more widely used in practice due to its simplicity though three-phase commit provides better performance.