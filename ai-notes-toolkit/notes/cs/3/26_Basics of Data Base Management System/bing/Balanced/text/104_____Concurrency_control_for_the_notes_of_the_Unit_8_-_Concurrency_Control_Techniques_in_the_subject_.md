### Concurrency control

Concurrency control is a procedure of managing simultaneous operations on a database without conflicting with each other. It ensures that database transactions are performed concurrently and accurately to produce correct results without violating the data integrity of the database   .

Concurrency control techniques can be classified into two categories: lock-based protocols and timestamp-based protocols.

#### Lock-based protocols

Lock-based protocols use locks to prevent multiple transactions from accessing the same data item at the same time. A lock is a mechanism that grants or denies access to a data item based on its state. There are two types of locks: shared locks and exclusive locks.

- A shared lock (S-lock) allows a transaction to read a data item, but not to modify it. Multiple transactions can hold shared locks on the same data item concurrently.
- An exclusive lock (X-lock) allows a transaction to read and modify a data item, but not to share it with other transactions. Only one transaction can hold an exclusive lock on a data item at a time.

A transaction must acquire the appropriate lock before accessing a data item, and release the lock after finishing the access. A lock manager is responsible for granting, denying, and releasing locks according to some rules. Some of the common lock-based protocols are:

- Two-phase locking (2PL): A transaction must acquire all the locks it needs before releasing any lock. This ensures that the transaction is serializable, meaning that its effect is equivalent to executing it alone in some order. However, 2PL may cause deadlocks, where two or more transactions are waiting for each other to release locks.
- Strict two-phase locking (Strict 2PL): A transaction must hold all its exclusive locks until it commits or aborts. This ensures that the transaction is recoverable, meaning that its changes are not overwritten by another transaction before it commits. Strict 2PL also prevents cascading aborts, where one transaction aborts and causes other transactions to abort as well.
- Conservative two-phase locking (Conservative 2PL): A transaction must acquire all the locks it needs before it starts execution. This ensures that the transaction is deadlock-free, meaning that it does not wait for any lock during its execution. However, conservative 2PL may cause low concurrency, where some transactions are delayed or rejected unnecessarily.

#### Timestamp-based protocols

Timestamp-based protocols use timestamps to order the transactions and determine their precedence. A timestamp is a unique identifier that reflects the start time of a transaction. Each transaction is assigned a timestamp when it begins, and each data item has two timestamps: read timestamp (RTS) and write timestamp (WTS).

- The read timestamp (RTS) of a data item is the largest timestamp of any transaction that has successfully read the data item.
- The write timestamp (WTS) of a data item is the largest timestamp of any transaction that has successfully written the data item.

A transaction must compare its timestamp with the timestamps of the data item before accessing it, and follow some rules to ensure serializability and recoverability. Some of the common timestamp-based protocols are:

- Basic timestamp ordering (BTO): A transaction can read a data item if its timestamp is greater than or equal to the WTS of the data item. A transaction can write a data item if its timestamp is greater than both the RTS and the WTS of the data item. If a transaction violates any of these rules, it is aborted and restarted with a new timestamp. BTO ensures serializability, but not recoverability or freedom from cascading aborts.
- Thomas' write rule (TWR): A transaction can read a data item if its timestamp is greater than or equal to the WTS of the data item. A transaction can write a data item if its timestamp is greater than the WTS of the data item, and the write is not ignored. A write is ignored if the timestamp of the transaction is less than or equal to the RTS of the data item, meaning that the write is outdated and has no effect. TWR ensures serializability and recoverability, but not freedom from cascading aborts.
- Multiversion timestamp ordering (MVTO): A transaction can read the latest version of a data item that has a WTS less than or equal to the timestamp of the transaction. A transaction can write a new version of a data item if its timestamp is greater than the WTS of the current version of the data item. Each version of a data item has its own RTS and WTS. MVTO ensures serializability, recoverability, and freedom from cascading aborts. However, MV