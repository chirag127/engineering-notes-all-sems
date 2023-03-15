 Here is the content in markdown format:

### Atomic Commit protocols for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

Atomic commit protocols are used to ensure that all distributed transactions are executed successfully or none at all in distributed database systems. This helps to maintain database consistency. Some of the popular atomic commit protocols are:

1. Two-phase commit protocol:
- Consists of two phases - commit request phase and commit phase
- In commit request phase, the coordinator asks all participants to prepare to commit
- In commit phase, the coordinator asks all participants to commit if all were successful in preparing to commit else abort
- Uses voting to decide on commit or abort
- Ensures atomicity but reduces performance due to two phases
- Can lead to blocked processes in case of coordinator failure

2. Three-phase commit protocol:
- Adds an extra phase - pre-commit phase before the two phases of two-phase commit protocol
- In pre-commit phase, the coordinator asks all participants to prepare to prepare to commit
- Ensures higher commitment probability but reduces performance due to an extra phase

3. Commitment ordering protocol:
- Orders transactions in commit request order to avoid deadlocks
- Does not have a separate commit phase
- Uses a commit manager to track transactions and commit order
- Can reduce blocking but increases overhead of maintaining commit order

Advantages: Ensures database consistency by atomic execution of distributed transactions.
Disadvantages: Can reduce performance due to multiple phases and additional overhead.
Applications: Databases, transaction processing systems, etc.

Does this help? Let me know if you would like me to elaborate on any part of the answer.