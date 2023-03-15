### Concurrency Control

Concurrency control is a procedure of managing simultaneous operations on a database without conflicting with each other. It ensures that database transactions are performed concurrently and accurately to produce correct results without violating the data integrity of the database   .

Some of the objectives of concurrency control are:

- To prevent the loss of data due to concurrent updates by different transactions.
- To maintain the consistency and isolation properties of transactions.
- To avoid deadlock and starvation situations among competing transactions.
- To improve the performance and throughput of the database system.

There are two main approaches to concurrency control: **lock-based** and **timestamp-based** protocols .

#### Lock-Based Protocols

Lock-based protocols use locks to control the access of transactions to data items. A lock is a mechanism that grants or denies permission to a transaction to read or write a data item. There are two types of locks: **shared** and **exclusive**.

- A shared lock (S-lock) allows a transaction to read a data item, but not to modify it. Multiple transactions can hold S-locks on the same data item concurrently.
- An exclusive lock (X-lock) allows a transaction to read and write a data item, but not to share it with other transactions. Only one transaction can hold an X-lock on a data item at a time.

A transaction must acquire the appropriate lock on a data item before accessing it, and release the lock after finishing the access. A transaction can also lock a set of data items, such as a table or a page, to reduce the overhead of locking individual items. This is called **granularity** of locking.

The main challenge of lock-based protocols is to ensure that the locking and unlocking operations do not cause any conflicts or deadlocks among transactions. A conflict occurs when two transactions try to access the same data item with incompatible locks, such as an S-lock and an X-lock. A deadlock occurs when two or more transactions are waiting for each other to release locks on data items that they need.

To prevent conflicts and deadlocks, lock-based protocols must follow some rules, such as:

- **Two-phase locking (2PL)**: A transaction must acquire all the locks it needs before releasing any lock. This ensures that a transaction holds the locks for the duration of its execution, and does not interfere with other transactions that need the same data items. 2PL can be divided into two phases: **growing** and **shrinking**. In the growing phase, a transaction can only acquire locks, and in the shrinking phase, it can only release locks.
- **Conservative 2PL**: A transaction must acquire all the locks it needs before starting its execution. This ensures that a transaction does not block or get blocked by other transactions, but it may cause a transaction to wait unnecessarily for locks that are not available.
- **Strict 2PL**: A transaction must hold all the X-locks it acquires until it commits or aborts. This ensures that a transaction does not write any data item that may be read by another transaction before it commits, and thus preserves the serializability of transactions.
- **Rigorous 2PL**: A transaction must hold all the locks (S-locks and X-locks) it acquires until it commits or aborts. This ensures that a transaction does not read or write any data item that may be modified by another transaction before it commits, and thus preserves the strict serializability of transactions.

#### Timestamp-Based Protocols

Timestamp-based protocols use timestamps to order the execution of transactions and to detect conflicts. A timestamp is a unique identifier that represents the logical start time of a transaction. Timestamps can be assigned by a global clock, a logical counter, or a random number generator.

A transaction must have a timestamp before accessing any data item. A data item also has two timestamps: **read timestamp (RTS)** and **write timestamp (WTS)**. RTS is the largest timestamp of any transaction that has read the data item, and WTS is the largest timestamp of any transaction that has written the data item.

A transaction can read or write a data item only if its timestamp is compatible with the RTS and WTS of the data item. Otherwise, the transaction is aborted and restarted with a new timestamp. The compatibility rules are:

- To read a data item, the transaction's timestamp must be greater than or equal to the WTS of the data item. This ensures that a transaction does not read a stale value that has been overwritten by a later transaction.
- To write a data item, the