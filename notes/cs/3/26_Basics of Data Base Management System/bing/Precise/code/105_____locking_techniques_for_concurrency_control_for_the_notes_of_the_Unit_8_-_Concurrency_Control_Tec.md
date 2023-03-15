### Locking Techniques for Concurrency Control

Locking is a technique used to ensure that multiple transactions can access shared data concurrently without causing inconsistencies in the data. Here are some key points to remember about locking techniques for concurrency control:

1. **Locks** are used to control access to data items by transactions. A transaction must acquire a lock on a data item before it can access it.

2. **Lock modes** determine the level of access a transaction has to a data item. The two most common lock modes are shared locks and exclusive locks. Shared locks allow multiple transactions to read a data item simultaneously, while exclusive locks allow only one transaction to write to a data item at a time.

3. **Lock compatibility** determines whether two transactions can hold locks on the same data item at the same time. For example, two shared locks are compatible, but an exclusive lock and a shared lock are not.

4. **Lock granularity** refers to the size of the data item being locked. Fine-grained locking, where small data items are locked, can increase concurrency but also increase the overhead of lock management. Coarse-grained locking, where larger data items are locked, can reduce lock management overhead but also reduce concurrency.

5. **Deadlocks** can occur when two or more transactions are waiting for each other to release locks. Deadlock prevention and detection techniques can be used to avoid or resolve deadlocks.

6. **Two-phase locking (2PL)** is a commonly used locking protocol that ensures serializability. In 2PL, a transaction must acquire all its locks before it releases any locks.
