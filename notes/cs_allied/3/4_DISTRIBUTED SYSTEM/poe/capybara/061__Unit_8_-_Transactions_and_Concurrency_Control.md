## Unit 8 - Transactions and Concurrency Control

Transactions and concurrency control are critical aspects of database management systems. A database transaction is a sequence of operations that is executed as a single unit of work. Concurrency control is the process of managing access to shared resources in a multi-user environment to ensure data consistency and integrity.

### Transactions

1. A transaction is a logical unit of work that must be completed as a single, indivisible unit.
2. Transactions have four properties: atomicity, consistency, isolation, and durability (ACID).
3. Atomicity ensures that a transaction is executed as a single unit of work. If any part of the transaction fails, the entire transaction is rolled back, and the database is returned to its previous state.
4. Consistency ensures that a transaction brings the database from one consistent state to another. The database must meet all integrity constraints before and after the transaction.
5. Isolation ensures that multiple transactions can access the same data concurrently without interfering with each other.
6. Durability ensures that once a transaction is committed, the changes made to the database persist, even if there is a system failure.

### Concurrency Control

1. Concurrency control is the process of managing access to shared resources in a multi-user environment.
2. One of the primary challenges of concurrency control is preventing concurrent transactions from interfering with each other and producing inconsistent results.
3. Locking is a common technique used to manage concurrency control. Locks prevent other transactions from accessing the same data while a transaction is in progress.
4. Two-phase locking is a common locking protocol that ensures serializability by holding all locks until the end of the transaction.
5. Optimistic concurrency control is an alternative technique that allows multiple transactions to access the same data simultaneously. It assumes that conflicts between transactions are rare and resolves them when they occur.
6. Deadlocks can occur when two or more transactions are waiting for each other to release locks. To prevent deadlocks, a timeout mechanism is often used to release locks held by inactive transactions.

Overall, transactions and concurrency control are essential for maintaining the consistency and integrity of a database in a multi-user environment. Understanding these concepts is critical for effective database management.