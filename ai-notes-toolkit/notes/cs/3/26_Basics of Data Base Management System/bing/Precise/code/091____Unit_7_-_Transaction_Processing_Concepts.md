## Unit 7 - Transaction Processing Concepts

1. **Transaction**: A transaction is a logical unit of work that comprises one or more database operations, such as the retrieval or update of data.

2. **ACID Properties**: Transactions have four key properties, known as the ACID properties: Atomicity, Consistency, Isolation, and Durability.

    - **Atomicity**: This property ensures that either all the operations in a transaction are completed or none of them are. If a transaction fails at any point, all changes made during the transaction are rolled back to their previous state.

    - **Consistency**: This property ensures that the database remains in a consistent state before and after the transaction. Any transaction that would violate the consistency rules of the database is not allowed.

    - **Isolation**: This property ensures that each transaction is executed in isolation from other transactions. This means that the intermediate state of a transaction is not visible to other transactions.

    - **Durability**: This property ensures that once a transaction is committed, its changes to the database are permanent and will survive any subsequent failures.

3. **Concurrency Control**: Concurrency control is the process of managing simultaneous access to the database by multiple transactions. This is necessary to ensure the isolation property of transactions.

4. **Locking**: Locking is a common method used for concurrency control. It involves placing locks on the data items that a transaction wants to access. There are two types of locks: shared locks and exclusive locks.

5. **Deadlocks**: A deadlock occurs when two or more transactions are waiting for each other to release locks. Deadlock prevention and detection are important aspects of concurrency control.

6. **Commit and Rollback**: A transaction can be committed, which means that its changes to the database are made permanent. Alternatively, a transaction can be rolled back, which means that its changes are undone and the database is restored to its previous state.

7. **Transaction Log**: A transaction log is a record of all changes made to the database as part of a transaction. It is used to ensure the durability property of transactions and to recover the database in the event of a failure.

8. **Two-Phase Commit**: The two-phase commit protocol is a method used to ensure that a distributed transaction is either committed on all participating databases or rolled back on all of them. It involves a coordinator and participants and consists of two phases: the prepare phase and the commit phase.