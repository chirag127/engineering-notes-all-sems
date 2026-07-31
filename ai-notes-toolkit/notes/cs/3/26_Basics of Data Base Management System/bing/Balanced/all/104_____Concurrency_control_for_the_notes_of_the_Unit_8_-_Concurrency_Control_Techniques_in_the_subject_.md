# Concurrency Control

Concurrency control is a database management systems (DBMS) concept that is used to address the problems that occur with a multi-user system. Concurrency control, when applied to a DBMS, is meant to coordinate simultaneous transactions while preserving data integrity of the respective databases.

Some of the problems that concurrency control aims to prevent are:

- Lost update: When two transactions update the same data item and one of them overwrites the other's update.
- Dirty read: When a transaction reads a data item that has been modified by another transaction that has not yet committed or aborted.
- Non-repeatable read: When a transaction reads the same data item twice and gets different values due to another transaction's update.
- Phantom read: When a transaction reads a set of data items that satisfies some condition and gets different results due to another transaction's insertion or deletion of data items that satisfy the same condition.

There are two main types of concurrency control techniques:

- Pessimistic concurrency control: This technique assumes that conflicts are likely to happen and uses locks to prevent them. A lock is a mechanism that grants exclusive access to a data item to a transaction. A transaction must acquire a lock before reading or writing a data item and release it after finishing. There are different types of locks, such as shared locks, exclusive locks, and intention locks, that allow different levels of concurrency.
- Optimistic concurrency control: This technique assumes that conflicts are rare and does not use locks to prevent them. Instead, it uses a validation mechanism to detect and resolve conflicts after they happen. A validation mechanism can be based on timestamps, versions, or validation queries, that allow a transaction to check if its operations are consistent with the current state of the database.

Some of the advantages and disadvantages of these techniques are:

- Pessimistic concurrency control can avoid the overhead of validation and rollback, but it can also cause deadlock, livelock, and reduced concurrency.
- Optimistic concurrency control can avoid the overhead of locking and deadlock, but it can also cause more aborts and retries, and increased complexity.