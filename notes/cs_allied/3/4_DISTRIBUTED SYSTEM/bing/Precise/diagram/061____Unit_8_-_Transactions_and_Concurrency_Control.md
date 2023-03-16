## Unit 8 - Transactions and Concurrency Control

1. **Transactions** are a sequence of database operations that are executed as a single unit of work. The purpose of a transaction is to ensure data consistency in the face of concurrent access and failures.

2. **Concurrency control** is the process of managing simultaneous access to a database by multiple users. It ensures that transactions are executed in a manner that maintains the consistency and integrity of the database.

3. **Locking** is a common concurrency control mechanism used to prevent conflicts between transactions. It involves placing locks on data items to prevent other transactions from accessing or modifying them until the lock is released.

4. **Two-phase locking (2PL)** is a locking protocol that ensures serializability. It involves two phases: the growing phase, where locks are acquired, and the shrinking phase, where locks are released.

5. **Deadlocks** can occur when two or more transactions are waiting for each other to release locks. Deadlock prevention and detection techniques can be used to avoid or resolve deadlocks.

6. **Timestamp ordering** is another concurrency control mechanism that assigns a timestamp to each transaction and uses the timestamps to determine the order in which transactions are executed.

7. **Optimistic concurrency control** is a technique that assumes conflicts between transactions are rare and allows transactions to execute without acquiring locks. Conflicts are detected at commit time and the transaction is rolled back if a conflict is detected.

8. **Multiversion concurrency control** is a technique that maintains multiple versions of data items to allow transactions to read data without acquiring locks. It uses timestamps or other mechanisms to determine which version of a data item a transaction should read.