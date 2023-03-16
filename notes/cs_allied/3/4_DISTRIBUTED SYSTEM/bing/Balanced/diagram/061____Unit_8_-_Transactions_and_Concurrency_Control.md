## Unit 8 - Transactions and Concurrency Control

A transaction is a logical unit of work that consists of a sequence of database operations, such as insertions, deletions, updates, and queries. A transaction has the following properties:

- Atomicity: A transaction is either executed in its entirety or not at all. If a transaction fails, the database is restored to its state before the transaction started.
- Consistency: A transaction preserves the consistency of the database, meaning that it does not violate any integrity constraints or business rules.
- Isolation: A transaction is executed as if it is the only one running on the database, meaning that it does not interfere with or see the effects of other concurrent transactions.
- Durability: The effects of a transaction are permanent, meaning that they persist even if the system fails or restarts.

Concurrency control is the process of managing the simultaneous execution of transactions on a shared database, such that the transactions do not conflict with each other and the database remains consistent. Concurrency control techniques can be classified into two categories:

- Locking-based: A locking protocol is a set of rules that determines when a transaction can acquire or release a lock on a data item. A lock is a mechanism that grants exclusive or shared access to a data item to a transaction. Locking protocols can prevent concurrency problems such as lost updates, uncommitted data, and inconsistent reads, but they may also cause deadlock, where two or more transactions are waiting for each other to release locks.
- Timestamp-based: A timestamp is a unique identifier that indicates the order of transactions. A timestamp-based protocol is a set of rules that determines whether a transaction can read or write a data item based on its timestamp and the timestamps of other transactions that have accessed the same data item. Timestamp-based protocols can prevent concurrency problems such as lost updates, uncommitted data, and inconsistent reads, but they may also cause aborts, where a transaction is rolled back because it has violated the timestamp order.