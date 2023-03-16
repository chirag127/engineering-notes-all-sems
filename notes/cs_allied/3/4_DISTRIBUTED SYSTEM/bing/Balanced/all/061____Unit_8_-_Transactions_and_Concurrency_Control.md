## Unit 8 - Transactions and Concurrency Control

- A transaction is a logical unit of work that consists of a sequence of database operations, such as queries, updates, inserts, or deletes.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
  - Atomicity means that either all the operations of a transaction are executed or none of them are.
  - Consistency means that a transaction preserves the integrity constraints of the database.
  - Isolation means that a transaction does not interfere with other concurrent transactions.
  - Durability means that the effects of a committed transaction are permanent and survive any system failures.
- Concurrency control is the process of managing simultaneous access to shared data by multiple transactions, while ensuring data consistency and preventing conflicts.
- Concurrency control techniques can be classified into two categories: pessimistic and optimistic.
  - Pessimistic concurrency control assumes that conflicts are likely to occur and prevents them by locking the data items accessed by a transaction until it commits or aborts.
  - Optimistic concurrency control assumes that conflicts are rare and detects them by validating the read and write sets of a transaction before committing it.
- Some common concurrency control protocols are:
  - Two-phase locking (2PL): a transaction acquires all the locks it needs before releasing any of them. 2PL ensures serializability, but may cause deadlocks or starvation.
  - Timestamp ordering (TO): a transaction is assigned a unique timestamp when it starts, and the order of conflicting operations is determined by their timestamps. TO ensures serializability, but may cause cascading aborts or excessive restarts.
  - Validation (or optimistic) concurrency control (VCC): a transaction executes without locking any data items, and validates its read and write sets at commit time. VCC ensures serializability, but may cause high abort rates or wasted resources.
  - Multiversion concurrency control (MVCC): a transaction operates on a snapshot of the database taken at its start time, and writes to a new version of the data items. MVCC ensures serializability and avoids locking, but may cause storage overhead or garbage collection issues.