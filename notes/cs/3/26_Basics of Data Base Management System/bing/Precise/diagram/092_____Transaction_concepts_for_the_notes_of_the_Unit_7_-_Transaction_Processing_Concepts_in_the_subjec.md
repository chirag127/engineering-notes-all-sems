### Transaction concepts for the notes of the Unit 7 - Transaction Processing Concepts in the subject of Basics of Data Base Management System

A transaction is a logical unit of work that contains one or more SQL statements. A transaction is an atomic unit. The effects of all the SQL statements in a transaction can be either all committed (applied to the database) or all rolled back (undone from the database).

- **ACID Properties**: A transaction has four properties, known as the ACID properties: Atomicity, Consistency, Isolation, and Durability.
    - **Atomicity**: A transaction is an atomic unit of work; either all of its data modifications are performed or none of them is performed.
    - **Consistency**: When completed, a transaction must leave all data in a consistent state. In a relational database, all rules must be applied to the transaction's modifications to maintain all data integrity.
    - **Isolation**: Modifications made by concurrent transactions must be isolated from the modifications made by any other concurrent transactions. A transaction either sees data in the state it was in before another concurrent transaction modified it, or it sees the data after the second transaction has completed, but it does not see an intermediate state.
    - **Durability**: After a transaction has completed, its effects are permanently in place in the system. The modifications persist even in the event of a system failure.
- **Commit and Rollback**: A transaction ends when it is committed or rolled back, either explicitly with a COMMIT or ROLLBACK statement or implicitly when a DDL statement is issued.
    - **Commit**: A COMMIT statement ends the current transaction and makes all changes performed in the transaction permanent.
    - **Rollback**: A ROLLBACK statement undoes all the changes performed in the current transaction.
- **Savepoints**: A savepoint is a point in a transaction to which you can later roll back. Use the SAVEPOINT statement to create a savepoint within a transaction.
- **Locking**: Locking is a mechanism to prevent destructive interaction between transactions accessing the same resource. There are different levels of locking, including row-level locking, page-level locking, and table-level locking.
- **Deadlocks**: A deadlock occurs when two or more transactions are waiting for each other to release locks. Most database management systems have deadlock detection and resolution mechanisms to handle deadlocks.