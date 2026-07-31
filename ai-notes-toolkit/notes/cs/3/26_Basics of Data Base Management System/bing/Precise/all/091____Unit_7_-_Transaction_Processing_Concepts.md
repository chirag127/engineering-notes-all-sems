## Unit 7 - Transaction Processing Concepts

1. **Transaction**: A transaction is a logical unit of work that comprises one or more database operations, such as the modification, insertion, or deletion of data.
2. **ACID Properties**: Transactions must adhere to the ACID properties, which stand for Atomicity, Consistency, Isolation, and Durability. These properties ensure that the database remains in a consistent state even in the event of failures.
3. **Concurrency Control**: Concurrency control is the process of managing simultaneous access to a database by multiple users. This is necessary to prevent conflicts and ensure data integrity.
4. **Locking**: Locking is a common method of concurrency control. It involves placing locks on data items to prevent multiple users from accessing or modifying the same data simultaneously.
5. **Deadlocks**: A deadlock occurs when two or more transactions are waiting for each other to release locks on data items. Deadlocks can be prevented or resolved using various techniques, such as deadlock detection and resolution algorithms.
6. **Commit and Rollback**: A transaction can be committed, meaning that its changes are made permanent in the database, or rolled back, meaning that its changes are undone and the database is restored to its previous state.
7. **Recovery**: Recovery is the process of restoring a database to a consistent state after a failure. This can involve undoing or redoing transactions, depending on the nature of the failure and the recovery technique used.
