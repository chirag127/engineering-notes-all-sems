### Locks for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- Locks are a mechanism used to ensure that only one transaction can access a data item at a time.
- Locks can be either shared or exclusive. Shared locks allow multiple transactions to read a data item simultaneously, while exclusive locks allow only one transaction to write to a data item.
- Locks are acquired and released by the transaction manager, which is responsible for ensuring that the locking protocol is followed.
- Locks can be implemented at different levels of granularity, such as at the row, page, or table level.
- Deadlocks can occur when two or more transactions are waiting for each other to release locks. Deadlock detection and resolution techniques are used to prevent and resolve deadlocks.
- Two-phase locking (2PL) is a commonly used locking protocol that ensures serializability. In 2PL, a transaction must acquire all the locks it needs before it can release any locks.
- Locks are an important part of concurrency control in distributed systems, as they help ensure that transactions can be executed concurrently without interfering with each other.
