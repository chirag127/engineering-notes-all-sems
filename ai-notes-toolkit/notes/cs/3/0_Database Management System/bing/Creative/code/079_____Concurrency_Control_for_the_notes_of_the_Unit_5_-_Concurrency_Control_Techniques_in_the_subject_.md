### Concurrency Control

Concurrency control is a database management systems (DBMS) concept that is used to address the problems that occur with a multi-user system. Concurrency control, when applied to a DBMS, is meant to coordinate simultaneous transactions while preserving data integrity of the respective databases.

The main objectives of concurrency control are:

- To ensure the **isolation** of transactions, that is, to prevent interference between concurrent transactions.
- To resolve **conflicts** between read-write and write-write operations on the same data item.
- To preserve the **consistency** of the database, that is, to ensure that the execution of concurrent transactions does not violate the integrity constraints of the database.

The main challenges of concurrency control are:

- To deal with the **lost update** problem, that is, when two transactions update the same data item and one of them overwrites the other's update.
- To deal with the **uncommitted dependency** problem, that is, when one transaction reads a data item that has been updated by another transaction but not yet committed.
- To deal with the **inconsistent analysis** problem, that is, when one transaction reads several data items that have been updated by different transactions and gets an inconsistent view of the database.

The main techniques of concurrency control are:

- **Lock-based protocols**, that use locks to grant or deny access to data items by transactions. Locks can be shared or exclusive, and can be acquired or released at different levels of granularity.
- **Timestamp-based protocols**, that use timestamps to order the transactions and determine their precedence. Timestamps can be assigned either at the beginning or at the end of each transaction, and can be used to validate or invalidate the operations of transactions.
- **Validation-based protocols**, that use a validation phase to check whether the transactions can be committed or aborted. Validation can be done either at the end of each transaction or at the end of each operation.
- **Multiversion protocols**, that use multiple versions of data items to allow concurrent read and write operations. Versions can be created either by copying or by logging the old values of data items, and can be accessed by transactions based on their timestamps or validation results.
- **Snapshot isolation**, that uses snapshots of the database to provide a consistent and isolated view of the data to each transaction. Snapshots can be taken either at the beginning or at the end of each transaction, and can be used to detect or prevent write-write conflicts.