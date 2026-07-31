## Unit 9 - Distributed Transactions

1. **Introduction:** A distributed transaction is a transaction that spans multiple systems or databases. It ensures that either all the changes are committed or none of them are, even if the systems are distributed across different locations.

2. **Two-Phase Commit Protocol:** The two-phase commit protocol is a distributed algorithm that coordinates all the processes that participate in a distributed transaction to either commit or abort the transaction. The first phase is the voting phase, where the coordinator sends a prepare message to all participants and waits for their votes. The second phase is the commit phase, where the coordinator decides whether to commit or abort the transaction based on the votes received.

3. **Three-Phase Commit Protocol:** The three-phase commit protocol is an extension of the two-phase commit protocol that introduces a new phase called the pre-commit phase. This phase is used to avoid blocking in case of a coordinator failure.

4. **Global Transaction Identifier:** A global transaction identifier is a unique identifier assigned to a distributed transaction. It is used to track the progress of the transaction across all the participating systems.

5. **Recovery:** Recovery in distributed transactions involves restoring the system to a consistent state after a failure. This can be achieved through techniques such as write-ahead logging and checkpointing.

6. **Concurrency Control:** Concurrency control in distributed transactions involves managing concurrent access to shared data. This can be achieved through techniques such as locking, timestamp ordering, and optimistic concurrency control.

7. **Challenges:** Distributed transactions present several challenges such as network latency, network partitioning, and node failures. These challenges need to be addressed to ensure the correctness and reliability of the distributed transaction system.

8. **Conclusion:** Distributed transactions are an important concept in distributed systems. They provide a mechanism to ensure the consistency and reliability of data across multiple systems. However, they also present several challenges that need to be addressed to ensure their correct and efficient operation.