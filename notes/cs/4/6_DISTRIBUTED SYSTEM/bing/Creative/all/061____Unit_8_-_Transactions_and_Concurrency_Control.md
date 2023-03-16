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
- Concurrency control also keeps each transaction isolated as it is executed which helps data remain consistent even after the transaction ends especially in multi-user systems.
- Concurrency control can be implemented using various techniques, such as locking, timestamping, validation, and multiversioning.
- Locking is a technique where a transaction acquires a lock on a data item before reading or writing it, and releases the lock after finishing the operation.
- Timestamping is a technique where a transaction is assigned a unique timestamp when it starts, and the order of conflicting operations is determined by the timestamps.
- Validation is a technique where a transaction is executed without any locks, but is validated before committing to ensure that it does not violate any consistency rules.
- Multiversioning is a technique where a transaction operates on a snapshot of the database taken at a certain point in time, and the changes are merged with the current database state after committing.