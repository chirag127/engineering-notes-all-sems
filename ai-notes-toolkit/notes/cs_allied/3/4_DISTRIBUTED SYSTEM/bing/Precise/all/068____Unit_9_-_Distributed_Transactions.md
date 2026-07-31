## Unit 9 - Distributed Transactions

1. **Introduction:** A distributed transaction is a transaction that spans multiple systems, typically databases, and ensures that all changes are committed or rolled back together.

2. **Two-Phase Commit Protocol:** The two-phase commit protocol is a distributed algorithm used to coordinate the commit or rollback of a distributed transaction. The first phase involves the coordinator sending a prepare message to all participants, and the participants responding with a vote to either commit or abort. In the second phase, the coordinator sends a commit or abort message to all participants based on the votes received.

3. **Three-Phase Commit Protocol:** The three-phase commit protocol is an extension of the two-phase commit protocol that adds an additional phase to ensure that all participants are ready to commit before the final commit message is sent. This additional phase helps to avoid blocking in the case of a coordinator failure.

4. **Global Transaction Identifier:** A global transaction identifier is a unique identifier assigned to a distributed transaction to track its progress across multiple systems.

5. **Distributed Deadlocks:** Distributed deadlocks can occur when multiple transactions are waiting for resources held by other transactions in a distributed system. Deadlock detection and resolution techniques must be used to prevent or resolve these deadlocks.

6. **Distributed Concurrency Control:** Distributed concurrency control is the process of managing concurrent access to data in a distributed system. Common techniques include two-phase locking and timestamp ordering.

7. **Recovery:** Recovery in a distributed system involves restoring the system to a consistent state after a failure. This can involve rolling back or committing transactions based on the state of the system at the time of the failure.

8. **Conclusion:** Distributed transactions are an important concept in distributed systems, allowing for coordinated changes across multiple systems. Various protocols and techniques are used to ensure the consistency and correctness of these transactions.