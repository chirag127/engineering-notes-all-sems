# Unit 8 - Transactions and Concurrency Control

## Transactions
- A transaction is a logical unit of work that consists of a sequence of operations on a database.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the operations of a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction does not interfere with other concurrent transactions.
- Durability means that the effects of a committed transaction are permanent and survive any system failures.

## Concurrency Control
- Concurrency control is the management of simultaneously executing transactions in a shared database.
- Concurrency control ensures that correct results for concurrent operations are generated while getting those results as quickly as possible.
- Concurrency control also prevents data inconsistency and ensures serializability, which is the equivalence of concurrent execution to some serial execution of the transactions.
- Concurrency control techniques implement some protocols that can be broadly classified into two categories: lock-based protocols and timestamp-based protocols.
- Lock-based protocols use locks to control the access of transactions to data items. A lock is a mechanism that grants or denies permission to read or write a data item. There are different types of locks, such as binary locks, shared/exclusive locks, and multiple granularity locks.
- Timestamp-based protocols use timestamps to order the transactions and determine their precedence. A timestamp is a unique identifier that indicates the time at which a transaction started. There are two types of timestamps: commit timestamps and logical timestamps.