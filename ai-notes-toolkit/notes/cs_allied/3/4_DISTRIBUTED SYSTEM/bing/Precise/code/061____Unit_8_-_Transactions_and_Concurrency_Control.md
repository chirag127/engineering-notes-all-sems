## Unit 8 - Transactions and Concurrency Control

1. **Transactions** are a sequence of database operations that are executed as a single unit of work. The purpose of a transaction is to ensure data consistency in the face of concurrent access and failures.

2. **Concurrency control** is the process of managing simultaneous access to a database by multiple users. It ensures that transactions are executed in a way that maintains the consistency and integrity of the data.

3. **Locking** is a common method used for concurrency control. It involves placing locks on data items to prevent multiple transactions from accessing the same data simultaneously.

4. **Two-phase locking** is a locking protocol that ensures serializability of transactions. It involves two phases: the growing phase, where locks are acquired, and the shrinking phase, where locks are released.

5. **Deadlocks** can occur when two or more transactions are waiting for each other to release locks. Deadlock prevention and detection techniques can be used to avoid or resolve deadlocks.

6. **Timestamp ordering** is another method used for concurrency control. It assigns a timestamp to each transaction and ensures that conflicting operations are executed in timestamp order.

7. **Optimistic concurrency control** is a method that assumes that conflicts between transactions are rare. Transactions are allowed to execute without acquiring locks, and conflicts are detected and resolved at commit time.

8. **Multiversion concurrency control** is a method that maintains multiple versions of data items. Transactions can read older versions of data items, allowing for increased concurrency.