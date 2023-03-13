### Locks

- Locks are a mechanism to ensure serializability and consistency of transactions in a distributed system.
- Locks prevent concurrent transactions from accessing or modifying the same data item in a conflicting way.
- Locks can be classified into two types: shared locks and exclusive locks.
- Shared locks allow multiple transactions to read the same data item, but not to modify it. Exclusive locks allow only one transaction to read or modify the data item, and block any other transactions from accessing it.
- Locks can be acquired and released by transactions according to a locking protocol, which defines the rules and order of locking and unlocking operations.
- A common locking protocol is two-phase locking (2PL), which requires that a transaction acquires all the locks it needs before releasing any lock, and releases all the locks it holds after it commits or aborts.
- 2PL ensures serializability, but it may cause deadlocks, which occur when two or more transactions are waiting for each other to release locks.
- Deadlocks can be detected and resolved by using a deadlock detection algorithm, which periodically checks for cycles in the wait-for graph of transactions and locks, and aborts one or more transactions to break the cycle.
- Deadlocks can also be prevented or avoided by using a deadlock prevention or avoidance algorithm, which imposes some constraints on the locking protocol or the order of lock requests, such as timestamp ordering, wound-wait, or wait-die.
- Locks can be implemented in different granularities, such as record-level, page-level, file-level, or table-level, depending on the size of the data item to be locked. Finer-grained locks allow more concurrency, but incur more overhead. Coarser-grained locks reduce the overhead, but may cause more conflicts and blocking.