### Locks for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- Locks are a mechanism used to ensure that transactions are executed in a way that maintains the consistency and integrity of the data in a database.
- Locks are used to prevent multiple transactions from accessing the same data simultaneously, which could result in conflicts and inconsistencies.
- There are two main types of locks: shared locks and exclusive locks.
- Shared locks allow multiple transactions to read the same data simultaneously, but prevent any transaction from modifying the data.
- Exclusive locks allow a single transaction to both read and modify the data, but prevent any other transaction from accessing the data.
- Locks can be applied at different levels of granularity, such as at the row level, page level, or table level.
- The lock manager is responsible for managing locks and ensuring that transactions acquire the appropriate locks before accessing data.
- Deadlocks can occur when two or more transactions are waiting for each other to release locks. Deadlock detection and resolution techniques are used to detect and resolve deadlocks.
- Locks are an essential component of concurrency control in distributed systems, ensuring that transactions are executed in a way that maintains the consistency and integrity of the data.