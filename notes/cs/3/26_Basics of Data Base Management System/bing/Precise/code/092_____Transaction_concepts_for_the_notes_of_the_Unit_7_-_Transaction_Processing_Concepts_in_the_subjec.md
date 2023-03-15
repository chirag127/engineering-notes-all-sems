### Transaction concepts for the notes of the Unit 7 - Transaction Processing Concepts in the subject of Basics of Data Base Management System

A transaction is a logical unit of work that contains one or more SQL statements. A transaction is an atomic unit. The effects of all the SQL statements in a transaction can be either all committed (applied to the database) or all rolled back (undone from the database).

- **ACID Properties**: A transaction has four properties, known as the ACID properties: Atomicity, Consistency, Isolation, and Durability.
  - **Atomicity**: A transaction is atomic, meaning that it is treated as a single, indivisible unit of work. Either all the changes made during the transaction are committed to the database, or none of them are.
  - **Consistency**: A transaction must ensure that the database remains in a consistent state. This means that any data written to the database must be valid according to all defined rules, including constraints, cascades, and triggers.
  - **Isolation**: Transactions must be isolated from one another, meaning that the intermediate state of one transaction cannot be visible to other transactions. This ensures that the results of a transaction are not affected by other transactions running concurrently.
  - **Durability**: Once a transaction has been committed, its changes to the database must be permanent, even in the event of a system failure.

- **Commit and Rollback**: A transaction can be committed, meaning that all the changes made during the transaction are saved to the database, or it can be rolled back, meaning that all the changes are undone and the database is returned to its state before the transaction began.

- **Transaction States**: A transaction can be in one of several states: active, partially committed, failed, or aborted. An active transaction is one that is currently in progress. A partially committed transaction is one that has completed its final statement, but has not yet been committed or rolled back. A failed transaction is one that has been rolled back due to an error. An aborted transaction is one that has been rolled back by the user or the system.

- **Concurrency Control**: Concurrency control is the process of managing simultaneous access to the database by multiple transactions. This is necessary to ensure that the transactions do not interfere with one another and that the database remains in a consistent state. There are several methods for achieving concurrency control, including locking, timestamp ordering, and optimistic concurrency control.

- **Deadlocks**: A deadlock is a situation where two or more transactions are waiting for each other to release locks on resources, and none of them can proceed. Deadlocks can be prevented or resolved using various techniques, including deadlock detection and resolution, timeout-based schemes, and deadlock avoidance.

These are some of the key concepts related to transactions in the context of database management systems. Understanding these concepts is essential for effectively managing and maintaining the integrity of data in a database.