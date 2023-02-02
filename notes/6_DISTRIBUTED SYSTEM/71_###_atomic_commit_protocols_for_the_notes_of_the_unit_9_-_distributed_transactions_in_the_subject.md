### Atomic Commit protocols for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM
Atomic Commit protocols ensure all-or-nothing execution of transactions in a distributed system, ensuring data consistency across multiple nodes.

Two-Phase Commit (2PC) is a widely used Atomic Commit protocol. It involves two phases:
1. Preparation: Each participant node votes either to commit or abort the transaction.
2. Decision: Coordinator node decides to commit or abort based on the votes received.

Three-Phase Commit (3PC) is an extension of 2PC with an additional phase to handle failures.
1. Preparation: Same as 2PC
2. Decision: Same as 2PC
3. Finalization: Ensure all nodes have executed the decision.

Practical Byzantine Fault Tolerance (PBFT) is a consensus algorithm for fault-tolerant distributed systems. It ensures all nodes agree on the same value.

In conclusion, Atomic Commit protocols ensure consistency and reliability in distributed transactions. 2PC and 3PC are widely used, while PBFT is used for highly available systems.
