### Locking Techniques for Concurrency Control

- Concurrency control is the process of managing simultaneous access to shared data in a database system.
- Concurrency control ensures that transactions are executed in a consistent and correct manner, and that the database state remains valid after each transaction.
- Locking is one of the most common concurrency control techniques, which involves using locks to restrict access to data items by different transactions.
- A lock is a mechanism that grants or denies permission to read or write a data item to a transaction.
- A lock manager is a subsystem that manages the allocation and release of locks for transactions.
- There are different types of locks, such as binary locks, shared/exclusive locks, and multiple granularity locks, that provide different levels of concurrency and isolation.
- A locking protocol is a set of rules that governs how transactions acquire and release locks on data items.
- A locking protocol should ensure serializability, which means that the concurrent execution of transactions should produce the same result as some serial execution of the same transactions.
- One of the most widely used locking protocols is the two-phase locking (2PL) protocol, which divides the transaction into two phases: a growing phase and a shrinking phase.
- In the growing phase, a transaction can acquire locks on data items, but cannot release any lock. In the shrinking phase, a transaction can release locks on data items, but cannot acquire any new lock.
- The 2PL protocol ensures serializability, but it may cause deadlocks, which occur when two or more transactions are waiting for each other to release locks on data items.
- To prevent or resolve deadlocks, various techniques can be used, such as deadlock prevention, deadlock detection, deadlock avoidance, and deadlock recovery.
- Another locking protocol is the timestamp ordering (TO) protocol, which assigns a unique timestamp to each transaction, and uses the timestamps to order the access to data items by different transactions.
- The TO protocol ensures serializability and avoids deadlocks, but it may cause aborts, which occur when a transaction is rolled back and restarted due to a conflict with another transaction.
- To reduce the number of aborts, various techniques can be used, such as multi-version concurrency control (MVCC), validation concurrency control (VCC), and optimistic concurrency control (OCC).
- MVCC maintains multiple versions of each data item, and allows transactions to read the most recent committed version of a data item, without locking it.
- VCC validates each transaction before committing it, by checking if it conflicts with any other transaction that has committed in the meantime.
- OCC assumes that conflicts are rare, and allows transactions to execute without locking any data item, but validates them at the end of the execution.