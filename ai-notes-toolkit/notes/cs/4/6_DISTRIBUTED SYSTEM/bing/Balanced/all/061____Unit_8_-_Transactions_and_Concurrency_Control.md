# Unit 8 - Transactions and Concurrency Control

## Transactions
- A transaction is a logical unit of work that consists of one or more operations on a database, such as reading, writing, inserting, deleting, or modifying data.
- A transaction has four properties, known as ACID: atomicity, consistency, isolation, and durability.
- Atomicity means that either all the operations of a transaction are executed or none of them are. A transaction is indivisible and cannot be split into smaller units.
- Consistency means that a transaction preserves the integrity constraints and business rules of the database. A transaction transforms the database from one consistent state to another.
- Isolation means that a transaction is executed as if it is the only one running on the database. A transaction does not see the intermediate results or effects of other concurrent transactions.
- Durability means that the effects of a transaction are permanent and do not disappear even in the case of system failures. A transaction is recorded in a non-volatile storage medium.

## Concurrency Control
- Concurrency control is the management of simultaneously executing transactions in a shared database.
- Concurrency control ensures that correct results for concurrent operations are generated while getting those results as quickly as possible.
- Concurrency control is important because it helps data remain consistent and avoids conflicts, anomalies, and inconsistencies that may arise from concurrent transactions.
- Concurrency control techniques implement some protocols that can be broadly classified into two categories: lock-based protocols and timestamp-based protocols.
- Lock-based protocols use locks to control the access of transactions to data items. A lock is a mechanism that grants or denies permission to a transaction to read or write a data item. There are different types of locks, such as shared locks, exclusive locks, and intention locks.
- Timestamp-based protocols use timestamps to order the transactions and determine their precedence. A timestamp is a unique identifier that indicates the start time of a transaction. There are different types of timestamps, such as commit timestamps, logical timestamps, and physical timestamps.