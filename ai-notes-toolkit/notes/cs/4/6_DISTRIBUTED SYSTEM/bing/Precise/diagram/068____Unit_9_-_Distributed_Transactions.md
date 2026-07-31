## Unit 9 - Distributed Transactions

1. **Introduction:** A distributed transaction is a transaction that spans multiple systems or databases. It ensures that either all the changes are committed or none of them are, even if the systems are distributed across different locations.

2. **Two-Phase Commit Protocol:** The two-phase commit protocol is a distributed algorithm that coordinates all the processes that participate in a distributed transaction to either commit or abort the transaction. The protocol has two phases: the prepare phase and the commit phase.

3. **Three-Phase Commit Protocol:** The three-phase commit protocol is an extension of the two-phase commit protocol that introduces an additional phase, the pre-commit phase, to make the protocol more resilient to failures.

4. **Global Transaction Identifier:** A global transaction identifier is a unique identifier that is assigned to a distributed transaction. It is used to track the progress of the transaction across all the systems that participate in the transaction.

5. **Transaction Manager:** A transaction manager is a component that coordinates the execution of distributed transactions. It is responsible for managing the communication between the different systems that participate in the transaction and for ensuring that the transaction is executed atomically.

6. **Distributed Deadlocks:** A distributed deadlock is a situation where two or more transactions are waiting for each other to release locks on resources, but none of them can proceed because the locks are held by the other transactions. Distributed deadlocks can be detected and resolved using various algorithms, such as the wait-for graph algorithm.

7. **Distributed Concurrency Control:** Distributed concurrency control is the process of managing concurrent access to data in a distributed system. It ensures that transactions are executed in a way that preserves the consistency of the data, even if the transactions are executed concurrently on different systems.

8. **Conclusion:** Distributed transactions are an important concept in distributed systems, as they allow multiple systems to participate in a single transaction and ensure that the transaction is executed atomically. Various protocols and algorithms, such as the two-phase commit protocol and the wait-for graph algorithm, can be used to manage distributed transactions and ensure their correctness.