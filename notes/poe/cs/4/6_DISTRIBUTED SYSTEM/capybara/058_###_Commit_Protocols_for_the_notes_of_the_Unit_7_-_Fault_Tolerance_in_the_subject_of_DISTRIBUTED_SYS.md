### Commit Protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

Commit protocols are used to ensure that transactions are executed correctly in a distributed system. A commit protocol is responsible for ensuring that a transaction either completes successfully or is aborted when there is a failure.

There are two types of commit protocols: two-phase commit (2PC) and three-phase commit (3PC).

#### Two-Phase Commit (2PC)

- In 2PC, there is a coordinator node that manages the transaction and multiple participant nodes that are involved in the transaction.
- The protocol involves two phases: a prepare phase and a commit phase.
- During the prepare phase, the coordinator node sends a message to all participant nodes asking them to prepare for the commit. The participant nodes reply with either a vote to commit or a vote to abort.
- If all participant nodes vote to commit, the coordinator node sends a commit message to all participant nodes. If any participant node votes to abort, the coordinator node sends an abort message to all participant nodes.
- The main advantage of 2PC is that it ensures atomicity (all or nothing) of the transaction. However, it has a major drawback of being blocking (the entire system waits for the commit decision).

#### Three-Phase Commit (3PC)

- 3PC is an improvement over 2PC that addresses the blocking issue.
- Instead of two phases, 3PC involves three phases: a prepare phase, a ready phase, and a commit phase.
- During the prepare phase, the coordinator node sends a message to all participant nodes asking them to prepare for the commit. The participant nodes reply with either a vote to commit or a vote to abort.
- In the ready phase, the coordinator node sends a message to all participant nodes asking if they are ready to commit. The participant nodes reply with a message indicating their readiness.
- In the commit phase, the coordinator node sends a commit message to all participant nodes. If any participant node is not ready to commit, the coordinator node sends an abort message to all participant nodes.
- 3PC reduces the blocking issue of 2PC by allowing participant nodes to act independently. However, it has a higher likelihood of failure due to its three-phase nature.

Mnemonic: "2PC is like a binary decision (commit or abort), while 3PC is like a triple check (prepare, ready, and commit)."

In conclusion, commit protocols are essential for ensuring the correctness of transactions in a distributed system. Both 2PC and 3PC have advantages and disadvantages that must be considered when choosing a commit protocol for a system.