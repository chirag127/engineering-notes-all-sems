### Concurrency Control

Concurrency control is a database management systems (DBMS) concept that is used to address the problems that occur with a multi-user system . Concurrency control, when applied to a DBMS, is meant to coordinate simultaneous transactions while preserving data integrity of the respective databases.

The main objectives of concurrency control are:

- To apply isolation through mutual exclusion between conflicting transactions
- To resolve read-write and write-write conflict issues
- To preserve database consistency through constantly preserving execution obstructions
- To ensure serializability and recoverability of transactions

The main techniques of concurrency control are :

- Lock-based protocols: These protocols use locks to prevent multiple transactions from accessing the same data item at the same time. Locks can be shared or exclusive, and can be granted or denied by a lock manager. Locks can also be classified into binary, multiple, or tree-structured locks.
- Timestamp-based protocols: These protocols use timestamps to order the transactions and determine their precedence. Timestamps can be either logical or physical, and can be assigned either at the beginning or at the end of a transaction. Timestamps can also be used to implement optimistic or pessimistic concurrency control.
- Validation-based protocols: These protocols use a validation phase to check whether a transaction can be committed or aborted. Validation can be done either before, during, or after the execution phase of a transaction. Validation can also be based on serializability graphs or certification tests.
- Multiversion protocols: These protocols use multiple versions of data items to allow concurrent read operations without locking. Each version of a data item has a read timestamp and a write timestamp, and a transaction can read the latest version that is compatible with its timestamp. Multiversion protocols can also use locks or timestamps to control write operations.