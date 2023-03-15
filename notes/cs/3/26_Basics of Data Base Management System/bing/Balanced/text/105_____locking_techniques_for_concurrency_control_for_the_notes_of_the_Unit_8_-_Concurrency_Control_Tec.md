### Locking Techniques for Concurrency Control

Concurrency control is the process of managing concurrent access to a shared database by multiple transactions. Concurrency control ensures that the transactions are executed in a way that preserves the consistency and integrity of the database.

One of the most common concurrency control techniques is locking. Locking is an operation that grants a transaction permission to read or write a data item. A lock manager is a subsystem that manages the acquisition and release of locks by transactions.

There are different types of locks, such as:

- Binary locks: These locks have only two states, locked or unlocked. A transaction can either lock a data item for exclusive access or leave it unlocked for shared access.
- Shared and exclusive locks: These locks allow multiple transactions to read the same data item concurrently, but only one transaction can write to it. A transaction can acquire a shared lock (S-lock) to read a data item or an exclusive lock (X-lock) to write to it. A data item can have multiple S-locks but only one X-lock at a time.
- Read and write locks: These locks are similar to shared and exclusive locks, but they are more fine-grained. A transaction can acquire a read lock (R-lock) to read a data item or a write lock (W-lock) to write to it. A data item can have multiple R-locks but only one W-lock at a time. A W-lock is compatible with an R-lock, but not with another W-lock.
- Intention locks: These locks are used to indicate the intention of a transaction to acquire a lock on a lower level of granularity. For example, a transaction can acquire an intention shared lock (IS-lock) on a table to indicate that it will acquire S-locks on some rows of the table. An intention exclusive lock (IX-lock) indicates that the transaction will acquire X-locks on some rows of the table. An intention lock is compatible with another intention lock, but not with a data lock.
- Certify locks: These locks are used in multi-version concurrency control techniques, where each transaction works on a local version of the data item and commits the changes to the global version only after certifying that no conflicts exist. A transaction can acquire a certify lock (C-lock) on a data item to indicate that it has completed its updates on the local version and is ready to commit. A C-lock is compatible with an R-lock, but not with another C-lock or a W-lock.

Locking techniques can be classified into two categories based on the timing of lock acquisition and release:

- Strict two-phase locking (2PL): In this technique, a transaction follows two phases: a growing phase and a shrinking phase. In the growing phase, the transaction can acquire locks but cannot release them. In the shrinking phase, the transaction can release locks but cannot acquire new ones. This technique ensures serializability, which means that the concurrent execution of transactions is equivalent to some serial execution of the same transactions.
- Non-strict two-phase locking: In this technique, a transaction can release locks before committing, but it cannot acquire new locks after releasing any lock. This technique allows more concurrency than strict 2PL, but it may not ensure serializability. However, it ensures recoverability, which means that the effects of a transaction are not visible to other transactions until it commits.