# Locks for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- Locks are a mechanism used to ensure that only one transaction can access a data item at a time.
- Locks can be shared or exclusive. Shared locks allow multiple transactions to read a data item simultaneously, while exclusive locks allow only one transaction to write to a data item.
- Locks can be acquired and released by transactions as needed.
- Locks are managed by a lock manager, which is responsible for granting, denying, and releasing locks.
- Locks can be implemented using a lock table, which keeps track of which locks are held by which transactions.
- Deadlocks can occur when two or more transactions are waiting for locks held by each other. Deadlock detection and resolution techniques can be used to prevent or resolve deadlocks.
- Two-phase locking is a protocol used to ensure serializability of transactions. In the first phase, a transaction acquires all the locks it needs. In the second phase, the transaction releases all its locks.
- Locks can be used to implement different isolation levels, such as read committed, repeatable read, and serializable.