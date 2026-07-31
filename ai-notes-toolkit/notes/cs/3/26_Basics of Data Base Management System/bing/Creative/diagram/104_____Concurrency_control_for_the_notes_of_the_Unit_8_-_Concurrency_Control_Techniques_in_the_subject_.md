# Concurrency control

Concurrency control is a database management systems (DBMS) concept that is used to address the problems that occur with a multi-user system. Concurrency control, when applied to a DBMS, is meant to coordinate simultaneous transactions while preserving data integrity of the respective databases.

## Concurrency control techniques

There are two main types of concurrency control techniques: pessimistic and optimistic.

### Pessimistic concurrency control

Pessimistic concurrency control assumes that conflicts are likely to happen and prevents them by locking the data items that are accessed by a transaction. Locking can be done at different levels of granularity, such as rows, pages, tables, or databases. Locking can also be done in different modes, such as shared, exclusive, or update. Pessimistic concurrency control ensures serializability, which means that the concurrent execution of transactions is equivalent to some serial execution of the same transactions.

Some examples of pessimistic concurrency control techniques are:

- Two-phase locking (2PL): A transaction acquires all the locks it needs before releasing any lock. It has two phases: growing phase, where it acquires locks, and shrinking phase, where it releases locks.
- Timestamp ordering (TO): A transaction is assigned a unique timestamp when it starts, and the data items are also stamped with the timestamp of the last transaction that accessed them. A transaction can read or write a data item only if its timestamp is greater than the data item's timestamp.
- Multiversion concurrency control (MVCC): A transaction can read the previous version of a data item that was committed before the transaction started, and write a new version of the data item that is visible only to itself until it commits.

### Optimistic concurrency control

Optimistic concurrency control assumes that conflicts are rare and allows transactions to execute without locking. However, before committing, a transaction has to validate that it has not violated the data integrity by conflicting with other transactions. If a conflict is detected, the transaction is aborted and restarted. Optimistic concurrency control avoids the overhead of locking and the possibility of deadlock, but it may incur more aborts and restarts.

Some examples of optimistic concurrency control techniques are:

- Validation-based concurrency control: A transaction is divided into three phases: read phase, where it reads data items, validation phase, where it checks for conflicts, and write phase, where it writes data items.
- Timestamp-based concurrency control: A transaction is assigned a unique timestamp when it starts, and the data items are also stamped with the timestamp of the last transaction that read or wrote them. A transaction can commit only if its timestamp is greater than the data item's read and write timestamps.
- Snapshot isolation: A transaction can read the snapshot of the database that was taken when the transaction started, and write to a private workspace that is merged with the database when the transaction commits. A transaction can commit only if no other transaction has modified the same data items that it has written.