### Commit Protocols

Commit protocols are used in distributed systems to ensure that all nodes in the system agree on the final outcome of a transaction. This is important for maintaining consistency and fault tolerance in the system.

There are several types of commit protocols, including two-phase commit (2PC) and three-phase commit (3PC).

1. **Two-Phase Commit (2PC)**: In the first phase, the coordinator node sends a prepare message to all participant nodes, asking them to prepare to commit the transaction. In the second phase, the coordinator sends a commit message to all participants, instructing them to commit the transaction.

2. **Three-Phase Commit (3PC)**: This protocol adds an additional phase to the 2PC protocol. In the first phase, the coordinator sends a canCommit message to all participants, asking if they are ready to commit the transaction. In the second phase, the coordinator sends a preCommit message to all participants, instructing them to prepare to commit the transaction. In the third phase, the coordinator sends a doCommit message to all participants, instructing them to commit the transaction.

These protocols help to ensure that all nodes in the system agree on the final outcome of a transaction, even in the presence of failures. This is important for maintaining consistency and fault tolerance in distributed systems.