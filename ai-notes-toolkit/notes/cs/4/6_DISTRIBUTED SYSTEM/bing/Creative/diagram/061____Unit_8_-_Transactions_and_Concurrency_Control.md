## Unit 8 - Transactions and Concurrency Control

A transaction is a logical unit of work that consists of a sequence of database operations, such as queries, updates, inserts, or deletes. A transaction has the following properties:

- Atomicity: A transaction is either executed in its entirety or not at all. If a transaction fails, the database is restored to its state before the transaction started.
- Consistency: A transaction preserves the consistency of the database, meaning that it does not violate any integrity constraints or business rules.
- Isolation: A transaction is executed as if it were the only one running on the database, meaning that it does not interfere with or see the effects of other concurrent transactions.
- Durability: The effects of a transaction are permanent, meaning that they persist even if the system crashes or power fails.

Concurrency control is the process of managing the simultaneous execution of transactions on a shared database, such that the transactions do not conflict with each other and the database remains consistent. Concurrency control techniques can be classified into two categories:

- Locking-based: A locking-based technique uses locks to prevent transactions from accessing or modifying data that is being used by another transaction. A lock is a mechanism that grants exclusive or shared access to a data item or a set of data items. There are different types of locks, such as binary locks, shared/exclusive locks, or multiple granularity locks. Locking-based techniques can also use timestamps or validation rules to avoid deadlock or starvation situations.
- Non-locking-based: A non-locking-based technique does not use locks, but instead relies on other mechanisms, such as timestamps, version numbers, or optimistic validation, to ensure serializability of transactions. Serializability is the property that the concurrent execution of transactions is equivalent to some serial execution of the same transactions. Non-locking-based techniques can also use multiversion concurrency control or snapshot isolation to allow more concurrency and reduce conflicts.