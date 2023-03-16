## Unit 8 - Transactions and Concurrency Control

1. **Transaction** - A transaction is a logical unit of work that comprises one or more database operations, such as retrieval, insertion, deletion, or updating of data. A transaction must be atomic, consistent, isolated, and durable (ACID).
2. **Concurrency Control** - Concurrency control is the process of managing simultaneous operations on a database without having them interfere with one another. It ensures that transactions are executed in a safe and consistent manner while maintaining transaction isolation.
3. **Locking** - Locking is a mechanism used to prevent multiple transactions from accessing the same data concurrently. Locks can be shared or exclusive, and can be applied at different levels of granularity, such as at the row, page, or table level.
4. **Two-Phase Locking (2PL)** - Two-phase locking is a concurrency control method that guarantees serializability. It is divided into two phases: the growing phase, where locks are acquired, and the shrinking phase, where locks are released.
5. **Deadlocks** - A deadlock occurs when two or more transactions are waiting for each other to release locks. Deadlock prevention and detection are two methods used to handle deadlocks.
6. **Timestamp Ordering** - Timestamp ordering is a concurrency control method that assigns a timestamp to each transaction and uses these timestamps to determine the order in which transactions are executed.
7. **Optimistic Concurrency Control** - Optimistic concurrency control is a concurrency control method that assumes that conflicts between transactions are rare and allows transactions to execute without acquiring locks. Conflicts are detected at commit time, and transactions are rolled back and restarted if necessary.
