Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of concurrency control for the notes of the unit 8 - concurrency control techniques in the subject of basics of data base management system.

### Concurrency control

- Concurrency control is the process of managing simultaneous operations on a database without affecting data integrity and consistency.
- Concurrency control ensures that transactions are executed in a correct and consistent manner, and that concurrent transactions do not interfere with each other.
- Concurrency control is necessary to prevent problems such as lost updates, dirty reads, unrepeatable reads, and phantom reads, which can occur when multiple transactions access and modify the same data concurrently.
- Concurrency control can be implemented using various techniques, such as locking, timestamping, validation, and multiversion concurrency control.

#### Locking

- Locking is a technique that uses locks to control the access of transactions to data items in a database.
- A lock is a mechanism that grants or denies permission to a transaction to read or write a data item.
- There are two types of locks: shared locks and exclusive locks.
- A shared lock allows a transaction to read a data item, but not to modify it. Multiple transactions can hold shared locks on the same data item concurrently.
- An exclusive lock allows a transaction to read and write a data item, but not to share it with other transactions. Only one transaction can hold an exclusive lock on a data item at a time.
- A transaction must acquire a lock on a data item before accessing it, and release the lock after finishing the access.
- A transaction can lock a data item at different levels of granularity, such as record level, page level, file level, or table level. The level of granularity affects the performance and concurrency of the system.
- A locking protocol is a set of rules that governs how transactions acquire and release locks. A locking protocol must ensure serializability, which means that the concurrent execution of transactions is equivalent to some serial execution of the same transactions.
- A common locking protocol is two-phase locking (2PL), which requires that a transaction acquires all the locks it needs before releasing any lock, and releases all the locks it holds after acquiring the last lock. 2PL ensures serializability, but may cause deadlocks, which occur when two or more transactions are waiting for each other to release locks.
- Deadlocks can be prevented or resolved using various methods, such as deadlock prevention, deadlock detection, deadlock avoidance, or deadlock recovery.

#### Timestamping

- Timestamping is a technique that uses timestamps to order the execution of transactions and to determine their conflicts.
- A timestamp is a unique identifier that represents the logical start time of a transaction. Timestamps can be generated using a logical counter or a system clock.
- A transaction is assigned a timestamp when it starts, and each data item in the database has two timestamps: a read timestamp (RTS) and a write timestamp (WTS). RTS is the largest timestamp of any transaction that has read the data item, and WTS is the largest timestamp of any transaction that has written the data item.
- A timestamp-based protocol is a set of rules that governs how transactions access data items based on their timestamps. A timestamp-based protocol must ensure serializability and avoid cascading aborts, which occur when a transaction aborts and causes other transactions that have read its data to abort as well.
- A common timestamp-based protocol is basic timestamp ordering (BTO), which uses the following rules:

  - A transaction T can read a data item X if T's timestamp is greater than or equal to X's WTS. Otherwise, T is rejected and aborted, as it is trying to read an obsolete value of X.
  - A transaction T can write a data item X if T's timestamp is greater than both X's RTS and X's WTS. Otherwise, T is rejected and aborted, as it is trying to write an inconsistent value of X.
  - If a transaction T can read or write a data item X, then X's RTS or WTS is updated to T's timestamp, respectively.

- BTO ensures serializability and avoids cascading aborts, but may cause starvation, which occurs when a transaction is repeatedly aborted and restarted due to conflicts with other transactions.

#### Validation

- Validation is a technique that uses a validation phase to check the conflicts of transactions before committing them to the database.
- A validation phase is a period of time during which a transaction is validated, that is, checked for conflicts with other transactions that have already committed or are being validated.
- A validation protocol is a set of rules that governs how transactions are validated and committed. A validation protocol must ensure serializability and avoid cascading abort