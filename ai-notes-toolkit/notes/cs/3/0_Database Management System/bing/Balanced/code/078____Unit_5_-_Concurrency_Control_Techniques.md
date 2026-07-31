# Unit 5 - Concurrency Control Techniques

Concurrency control techniques are methods to ensure the correctness and consistency of data in a database system when multiple transactions are executed concurrently. Concurrency control techniques can be classified into two categories: pessimistic and optimistic.

## Pessimistic Concurrency Control

Pessimistic concurrency control techniques assume that conflicts and data inconsistencies are likely to occur when concurrent transactions access the same data, and therefore prevent them by locking the data items before accessing them. Pessimistic concurrency control techniques include:

- **Two-phase locking (2PL)**: A transaction acquires all the locks it needs before releasing any lock. 2PL ensures serializability, but may cause deadlocks and reduce concurrency.
- **Timestamp ordering (TO)**: A transaction is assigned a unique timestamp when it starts, and the data items are also stamped with the timestamp of the last transaction that accessed them. A transaction can read or write a data item only if its timestamp is newer than the data item's timestamp. TO ensures serializability and avoids deadlocks, but may cause aborts and reduce concurrency.
- **Validation (or certification)**: A transaction executes without locking any data item, but before committing, it validates whether its read and write sets are consistent with the database state. If not, the transaction is aborted and restarted. Validation ensures serializability and avoids deadlocks, but may cause aborts and reduce concurrency.

## Optimistic Concurrency Control

Optimistic concurrency control techniques assume that conflicts and data inconsistencies are rare when concurrent transactions access the same data, and therefore allow them to execute without locking, but detect and resolve them after the fact. Optimistic concurrency control techniques include:

- **Multiversion concurrency control (MVCC)**: A transaction can read multiple versions of a data item, each with a different timestamp, and write a new version with its own timestamp. A transaction can commit only if its read and write sets do not conflict with other committed transactions. MVCC ensures serializability and avoids deadlocks and aborts, but may increase storage and maintenance costs.
- **Snapshot isolation (SI)**: A transaction can read a consistent snapshot of the database state at the time it started, and write to a separate workspace without affecting other transactions. A transaction can commit only if its write set does not overlap with the write sets of other concurrent transactions. SI ensures snapshot serializability and avoids deadlocks and aborts, but may cause anomalies such as write skew and lost updates.
- **Commitment ordering (CO)**: A transaction can execute without locking any data item, but before committing, it waits for the commit order to be determined by a centralized or distributed coordinator. The commit order is consistent with the precedence graph of the transactions, and ensures serializability and avoids deadlocks and aborts, but may increase communication and coordination costs.