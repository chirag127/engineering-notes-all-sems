## Unit 8 - Transactions and Concurrency Control

1. **Transactions** are a sequence of database operations that are treated as a single logical unit of work. They are used to ensure data consistency and integrity in the database.

2. **Concurrency control** is the process of managing simultaneous access to a database by multiple users. It is used to ensure that transactions are executed in a way that maintains the consistency and integrity of the data.

3. **Locking** is a common concurrency control technique that is used to prevent multiple transactions from accessing the same data at the same time. When a transaction wants to access a piece of data, it must first acquire a lock on that data. If another transaction already holds a lock on the data, the requesting transaction must wait until the lock is released.

4. **Deadlocks** can occur when two or more transactions are waiting for each other to release locks. Deadlock prevention and detection techniques are used to avoid or resolve deadlocks.

5. **Isolation levels** determine the degree to which one transaction is isolated from the effects of other transactions. Higher isolation levels provide stronger guarantees of consistency, but can reduce concurrency and performance.

6. **Two-phase locking (2PL)** is a concurrency control protocol that uses locking to ensure serializability of transactions. In the first phase, a transaction acquires all the locks it needs. In the second phase, it releases all the locks.

7. **Timestamp ordering (TO)** is a concurrency control protocol that assigns a timestamp to each transaction and uses the timestamps to determine the order in which transactions are allowed to execute.

8. **Optimistic concurrency control (OCC)** is a concurrency control protocol that assumes that conflicts between transactions are rare and allows transactions to execute without acquiring locks. Conflicts are detected at commit time, and if a conflict is detected, one of the conflicting transactions is rolled back and must be retried.

9. **Multi-version concurrency control (MVCC)** is a concurrency control protocol that allows multiple versions of the same data to exist at the same time. Transactions can read a consistent snapshot of the database without acquiring locks, which can improve concurrency and performance.