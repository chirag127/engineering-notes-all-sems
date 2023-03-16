## Unit 8 - Transactions and Concurrency Control

1. **Transactions** are a sequence of database operations that are executed as a single unit of work. The purpose of a transaction is to ensure data consistency and integrity in the face of failures, such as system crashes or power outages.

2. **Concurrency control** is the process of managing simultaneous access to a database by multiple users. The goal of concurrency control is to ensure that transactions are executed in a way that maintains the consistency and integrity of the data.

3. **Locking** is a common concurrency control mechanism used to prevent conflicts between transactions. Locking involves placing locks on data items to prevent other transactions from accessing or modifying them until the lock is released.

4. **Two-phase locking (2PL)** is a locking protocol that ensures serializability. In 2PL, a transaction must acquire all the locks it needs before it can release any locks. This is done in two phases: the growing phase, where the transaction acquires locks, and the shrinking phase, where the transaction releases locks.

5. **Deadlocks** can occur when two or more transactions are waiting for each other to release locks. Deadlock prevention and detection techniques can be used to avoid or resolve deadlocks.

6. **Timestamp ordering** is another concurrency control mechanism that assigns a timestamp to each transaction and uses the timestamps to determine the order in which transactions are executed.

7. **Optimistic concurrency control** is a technique that assumes that conflicts between transactions are rare and allows transactions to execute without acquiring locks. Conflicts are detected at the end of the transaction, and if a conflict is detected, the transaction is rolled back and restarted.

8. **Multiversion concurrency control** is a technique that maintains multiple versions of data items to allow transactions to read data without acquiring locks. Transactions can read the version of the data item that was current at the start of the transaction, even if the data item has been modified by other transactions.