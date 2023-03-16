## Unit 9 - Distributed Transactions

1. **Introduction:** A distributed transaction is a transaction that spans multiple systems, typically databases, and ensures that all changes are committed or rolled back across all systems.

2. **Two-Phase Commit Protocol:** The two-phase commit protocol is a distributed algorithm used to coordinate the commit or rollback of a distributed transaction. The first phase, called the prepare phase, involves each participating system voting on whether to commit or abort the transaction. The second phase, called the commit phase, involves the coordinator sending a commit or abort message to all participants based on the outcome of the vote.

3. **Three-Phase Commit Protocol:** The three-phase commit protocol is an extension of the two-phase commit protocol that adds an additional phase, called the pre-commit phase, to reduce the risk of blocking in the event of a coordinator failure.

4. **Global Transaction Identifier:** A global transaction identifier is a unique identifier assigned to a distributed transaction by the coordinator. It is used to track the progress of the transaction across all participating systems.

5. **Distributed Deadlocks:** Distributed deadlocks can occur when multiple transactions are waiting for resources held by other transactions in a distributed system. Deadlock detection and resolution techniques, such as timeouts and deadlock detection algorithms, can be used to prevent or resolve distributed deadlocks.

6. **Distributed Concurrency Control:** Distributed concurrency control mechanisms, such as distributed locking and distributed timestamp ordering, can be used to ensure the consistency and isolation of distributed transactions.

7. **Recovery:** Recovery mechanisms, such as write-ahead logging and checkpointing, can be used to ensure the durability of distributed transactions in the event of a system failure.

8. **Summary:** Distributed transactions provide a mechanism for ensuring the consistency and durability of changes made to multiple systems in a distributed environment. The two-phase and three-phase commit protocols are commonly used to coordinate the commit or rollback of distributed transactions. Distributed concurrency control and recovery mechanisms are also important for ensuring the correctness and durability of distributed transactions.