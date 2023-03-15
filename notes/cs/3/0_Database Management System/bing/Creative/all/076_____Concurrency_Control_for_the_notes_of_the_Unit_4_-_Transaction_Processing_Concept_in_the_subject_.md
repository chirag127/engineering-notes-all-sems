# Concurrency Control

Concurrency control is a procedure of managing simultaneous operations on a database without conflicting with each other. It ensures that database transactions are performed concurrently and accurately to produce correct results without violating the data integrity of the database   .

Some of the objectives of concurrency control are:

- To prevent the loss of data due to concurrent updates by different transactions.
- To maintain the consistency and isolation properties of transactions.
- To avoid deadlock and starvation situations among competing transactions.
- To improve the performance and throughput of the database system.

There are two main approaches to concurrency control: **lock-based** and **timestamp-based** protocols .

## Lock-Based Protocols

Lock-based protocols use locks to control the access of transactions to data items. A lock is a mechanism that grants or denies permission to a transaction to read or write a data item. There are two types of locks: **shared** and **exclusive**.

- A shared lock (S-lock) allows a transaction to read a data item, but not to modify it. Multiple transactions can hold S-locks on the same data item concurrently.
- An exclusive lock (X-lock) allows a transaction to read and write a data item, but not to share it with other transactions. Only one transaction can hold an X-lock on a data item at a time.

A lock-based protocol must follow two rules to ensure serializability of transactions:

- **Two-phase locking (2PL)**: A transaction must acquire all the locks it needs before it releases any lock. This means that a transaction goes through two phases: a growing phase, where it acquires locks, and a shrinking phase, where it releases locks.
- **Conflict serializability**: A transaction must not conflict with another transaction that holds a lock on the same data item. This means that a transaction must wait until the conflicting lock is released before it can proceed.

Some of the advantages and disadvantages of lock-based protocols are:

- Advantages:
  - They are simple and easy to implement.
  - They can handle any type of conflict among transactions.
  - They can be combined with other techniques, such as deadlock detection and prevention, to improve concurrency control.
- Disadvantages:
  - They may cause a high degree of blocking and waiting among transactions, which reduces concurrency and performance.
  - They may lead to deadlock situations, where two or more transactions are waiting for each other to release locks.
  - They may cause cascading aborts, where the failure of one transaction causes the rollback of other transactions that depend on its updates.

## Timestamp-Based Protocols

Timestamp-based protocols use timestamps to order the execution of transactions. A timestamp is a unique identifier that reflects the start time of a transaction. Each transaction is assigned a timestamp when it begins, and each data item has two timestamps: a read timestamp (RTS) and a write timestamp (WTS). The RTS records the timestamp of the last transaction that read the data item, and the WTS records the timestamp of the last transaction that wrote the data item.

A timestamp-based protocol must follow two rules to ensure serializability of transactions:

- **Read-write rule**: A transaction T can read a data item X only if T's timestamp is greater than or equal to X's WTS. This means that T can read the latest version of X, and no other transaction can overwrite X after T reads it. If T's timestamp is less than X's WTS, then T is aborted and restarted with a new timestamp.
- **Write-write rule**: A transaction T can write a data item X only if T's timestamp is greater than both X's RTS and X's WTS. This means that T can write a new version of X, and no other transaction can read or write X before T writes it. If T's timestamp is less than or equal to either X's RTS or X's WTS, then T is aborted and restarted with a new timestamp.

Some of the advantages and disadvantages of timestamp-based protocols are:

- Advantages:
  - They do not use locks, so they avoid blocking, waiting, and deadlock situations among transactions.
  - They do not cause cascading aborts, as transactions are aborted before they make any changes to the database.
  - They ensure that transactions are executed in a chronological order, which preserves causality and consistency.
- Disadvantages:
  - They may cause a high rate of aborts and restarts among transactions, which reduces concurrency and performance.
  - They may not handle some types of conflicts, such as read-read and write