## Unit 8 - Transactions and Concurrency Control

1. **Transactions** are a sequence of database operations that are executed as a single unit of work. The purpose of a transaction is to ensure data consistency in the face of concurrent access and failures.
2. **Concurrency control** is the process of managing simultaneous access to a database by multiple users while maintaining data consistency and integrity.
3. **Locking** is a common concurrency control mechanism that restricts access to data while it is being modified by a transaction. Locks can be shared or exclusive, and can be applied at different levels of granularity, such as row-level or table-level.
4. **Deadlocks** can occur when two or more transactions are waiting for each other to release locks. Deadlock detection and resolution techniques are used to prevent or resolve deadlocks.
5. **Isolation levels** determine the degree to which transactions are isolated from each other. Common isolation levels include read uncommitted, read committed, repeatable read, and serializable.
6. **Two-phase locking (2PL)** is a concurrency control protocol that uses locks to ensure serializability. In the first phase, a transaction acquires all the locks it needs. In the second phase, it releases all the locks.
7. **Timestamp ordering** is a concurrency control protocol that assigns a timestamp to each transaction and uses the timestamps to determine the order in which transactions are allowed to execute.
8. **Optimistic concurrency control (OCC)** is a concurrency control protocol that assumes that conflicts between transactions are rare and allows transactions to execute without acquiring locks. Conflicts are detected at commit time and the transaction is rolled back if a conflict is detected.