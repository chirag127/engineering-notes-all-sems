# Concurrency Control

Concurrency control is a database management systems (DBMS) concept that is used to address the problems that occur with a multi-user system. Concurrency control, when applied to a DBMS, is meant to coordinate simultaneous transactions while preserving data integrity of the respective databases.

The main objectives of concurrency control are:

- To ensure the **isolation** of transactions, that is, to prevent interference or conflicts between concurrent transactions.
- To resolve **read-write** and **write-write** conflicts, that is, to handle situations where one transaction reads or writes data that is concurrently modified by another transaction.
- To preserve **database consistency**, that is, to ensure that the database state remains valid after the execution of concurrent transactions.

Some of the benefits of concurrency control are:

- It improves the **throughput** of the system, that is, the number of transactions that can be completed in a given time.
- It reduces the **waiting time** of the transactions, that is, the time that a transaction spends in a ready state before getting the system resources to execute.
- It enhances the **availability** of the data, that is, the degree to which the data can be accessed by the transactions.

Some of the challenges of concurrency control are:

- It introduces **overhead** to the system, that is, the extra work or resources that are required to implement concurrency control mechanisms.
- It may cause **deadlocks**, that is, situations where two or more transactions are waiting for each other to release the resources they hold.
- It may affect the **serializability** of the transactions, that is, the equivalence of the concurrent execution of transactions to some serial execution.

There are two main types of concurrency control methods in DBMS:

- **Lock-based** protocols, which use locks to grant or deny access to data items by the transactions. A lock is a mechanism that allows a transaction to claim exclusive or shared control over a data item. Lock-based protocols can be classified into binary, shared/exclusive, and multiple granularity locking protocols.
- **Timestamp-based** protocols, which use timestamps to order the transactions and determine their validity. A timestamp is a unique identifier that reflects the relative starting time of a transaction. Timestamp-based protocols can be classified into basic, Thomas's write rule, and multiversion timestamp ordering protocols.

Other types of concurrency control methods in DBMS include:

- **Validation-based** protocols, which use a validation phase to check the consistency of the transactions before committing them. A validation phase is a process that verifies whether a transaction has violated any concurrency control rules or not. Validation-based protocols can be classified into basic, optimistic, and pessimistic protocols.
- **Snapshot** protocols, which use snapshots or versions of the data to allow concurrent read operations without locking. A snapshot or a version is a copy of the data at a certain point in time. Snapshot protocols can be classified into snapshot isolation, multiversion concurrency control, and snapshot serializability protocols.