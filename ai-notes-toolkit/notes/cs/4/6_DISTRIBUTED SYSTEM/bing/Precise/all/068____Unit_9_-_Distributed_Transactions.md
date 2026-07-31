## Unit 9 - Distributed Transactions

1. **Introduction**: A distributed transaction is a transaction that spans multiple systems, typically across a network. It ensures that either all the changes are committed or none of them are, even if some of the systems fail.

2. **Two-Phase Commit Protocol**: The two-phase commit protocol is a distributed algorithm that coordinates all the processes that participate in a distributed transaction to either commit or abort the transaction. The first phase is the voting phase, where the coordinator sends a prepare message to all participants and waits for their votes. The second phase is the commit phase, where the coordinator decides whether to commit or abort the transaction based on the votes received.

3. **Three-Phase Commit Protocol**: The three-phase commit protocol is an extension of the two-phase commit protocol that introduces a new phase, the pre-commit phase, to make the protocol more resilient to failures. In the pre-commit phase, the coordinator sends a pre-commit message to all participants and waits for their acknowledgments before proceeding to the commit phase.

4. **Global Transaction Identifier**: A global transaction identifier is a unique identifier assigned to a distributed transaction by the coordinator. It is used to track the progress of the transaction and to recover from failures.

5. **Recovery**: Recovery in distributed transactions involves restoring the system to a consistent state after a failure. This can be achieved through techniques such as write-ahead logging and checkpointing.

6. **Concurrency Control**: Concurrency control in distributed transactions involves ensuring that transactions do not interfere with each other and that the system remains in a consistent state. This can be achieved through techniques such as locking and timestamp ordering.

7. **Challenges**: Distributed transactions present several challenges, such as ensuring atomicity and durability across multiple systems, handling network and system failures, and managing concurrency and consistency.

8. **Conclusion**: Distributed transactions are an important concept in distributed systems, allowing for consistent and reliable data management across multiple systems. Despite the challenges, various techniques and protocols have been developed to ensure the correctness and efficiency of distributed transactions.