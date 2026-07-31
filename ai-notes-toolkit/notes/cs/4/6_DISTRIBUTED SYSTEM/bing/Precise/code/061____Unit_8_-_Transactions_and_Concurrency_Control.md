## Unit 8 - Transactions and Concurrency Control

1. **Transactions** are a sequence of database operations that are treated as a single logical unit of work. They are used to ensure data consistency and integrity in the database.

2. **Concurrency control** is the process of managing simultaneous access to a database by multiple users. It is used to ensure that transactions are executed in a way that maintains the consistency and integrity of the data.

3. **Locking** is a common concurrency control technique that is used to prevent multiple transactions from accessing the same data simultaneously. Locks can be placed on data items to prevent other transactions from accessing them until the lock is released.

4. **Two-phase locking** is a locking protocol that is used to ensure serializability of transactions. It involves two phases: the growing phase, where locks are acquired, and the shrinking phase, where locks are released.

5. **Deadlocks** can occur when two or more transactions are waiting for each other to release locks. Deadlock prevention and detection techniques can be used to avoid or resolve deadlocks.

6. **Timestamp ordering** is another concurrency control technique that assigns a timestamp to each transaction and uses the timestamps to determine the order in which transactions are executed.

7. **Optimistic concurrency control** is a technique that assumes that conflicts between transactions are rare and allows transactions to execute without acquiring locks. Conflicts are detected at the end of the transaction and the transaction is rolled back if a conflict is detected.

8. **Multiversion concurrency control** is a technique that maintains multiple versions of data items to allow transactions to access older versions of data without acquiring locks.