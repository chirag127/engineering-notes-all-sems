### Concurrency Control

Concurrency control is a database management systems (DBMS) concept that is used to address the problems that occur with a multi-user system . Concurrency control, when applied to a DBMS, is meant to coordinate simultaneous transactions while preserving data integrity of the respective databases.

The main objectives of concurrency control are:

- To apply isolation through mutual exclusion between conflicting transactions
- To resolve read-write and write-write conflict issues
- To preserve database consistency through constantly preserving execution obstructions
- To ensure serializability and recoverability of transactions

The main techniques of concurrency control are :

- Lock-based protocols: These protocols use locks to prevent multiple transactions from accessing the same data item at the same time. Locks can be shared or exclusive, and can be granted or denied by a lock manager. Lock-based protocols ensure serializability, but may cause deadlock or starvation.
- Timestamp-based protocols: These protocols use timestamps to order the transactions and determine their precedence. Timestamps can be assigned either at the start or at the end of a transaction. Timestamp-based protocols ensure serializability and avoid deadlock, but may cause cascading aborts or wasted work.
- Validation-based protocols: These protocols use a validation or certification phase to check whether a transaction can be committed or not. Validation-based protocols ensure serializability and avoid deadlock and cascading aborts, but may cause high overhead or concurrency reduction.
- Multiversion protocols: These protocols use multiple versions of data items to allow concurrent read operations without locking. Multiversion protocols ensure serializability and avoid deadlock and cascading aborts, but may cause storage overhead or version management complexity.
- Optimistic protocols: These protocols assume that conflicts are rare and allow transactions to execute without any locking or validation. Optimistic protocols ensure serializability and avoid deadlock and cascading aborts, but may cause high abort rate or low throughput.