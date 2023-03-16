## Unit 9 - Distributed Transactions

1. **Introduction:** A distributed transaction is a transaction that spans multiple systems or databases. It ensures that either all the changes are committed or none of them are, even if the systems are distributed across different locations.

2. **Two-Phase Commit Protocol:** The two-phase commit protocol is a distributed algorithm that coordinates all the processes that participate in a distributed transaction to either commit or abort the transaction. The first phase is the voting phase, where the coordinator sends a prepare message to all participants and waits for their votes. The second phase is the commit phase, where the coordinator decides whether to commit or abort the transaction based on the votes received.

3. **Three-Phase Commit Protocol:** The three-phase commit protocol is an extension of the two-phase commit protocol that introduces a new phase called the pre-commit phase. This phase is used to avoid blocking in case of a coordinator failure.

4. **Global Transaction Identifier:** A global transaction identifier is a unique identifier assigned to a distributed transaction. It is used to track the progress of the transaction across all the participating systems.

5. **Recovery:** Recovery in distributed transactions involves restoring the system to a consistent state after a failure. This can be achieved using techniques such as write-ahead logging and checkpointing.

6. **Concurrency Control:** Concurrency control in distributed transactions involves managing the simultaneous execution of transactions in a way that ensures the consistency of the data. This can be achieved using techniques such as locking and timestamp ordering.

7. **Challenges:** Distributed transactions present several challenges, such as the need for a reliable communication infrastructure, the possibility of network partitions, and the need for efficient concurrency control and recovery mechanisms.