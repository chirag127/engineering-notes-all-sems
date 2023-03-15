### Concurrency Control

Concurrency control is a database management systems (DBMS) concept that is used to address the problems that occur with a multi-user system . Concurrency control, when applied to a DBMS, is meant to coordinate simultaneous transactions while preserving data integrity of the respective databases.

Some of the reasons for using concurrency control methods in DBMS are:

- To apply isolation through mutual exclusion between conflicting transactions
- To resolve read-write and write-write conflict issues
- To preserve database consistency through constantly preserving execution obstructions
- To improve the performance and throughput of the system by allowing concurrent access

Some of the common concurrency control methods in DBMS are :

- Lock-based protocols: These protocols use locks to prevent multiple transactions from accessing the same data item at the same time. Locks can be shared or exclusive, and can be granted or denied based on the compatibility matrix. Locks can also be applied at different levels of granularity, such as table, page, or record. Lock-based protocols ensure serializability, but may cause problems such as deadlock, starvation, or cascading rollback.
- Timestamp-based protocols: These protocols use timestamps to order the transactions and determine their precedence. Each transaction is assigned a unique timestamp when it enters the system, and each data item has a read timestamp and a write timestamp to record the last transaction that accessed it. Timestamp-based protocols use validation rules to check if a transaction can read or write a data item without violating serializability. Timestamp-based protocols avoid deadlock, but may cause more aborts and waste of resources.
- Validation-based protocols: These protocols divide the execution of a transaction into three phases: read phase, validation phase, and write phase. In the read phase, the transaction reads the data items from the database and stores them in a local buffer. In the validation phase, the transaction checks if it can commit without violating serializability, using some validation tests. In the write phase, the transaction writes the updated data items to the database. Validation-based protocols avoid deadlock and cascading rollback, but may have high overhead and concurrency issues.
- Multiversion protocols: These protocols allow multiple versions of the same data item to coexist in the database, and assign different versions to different transactions based on some criteria. Multiversion protocols can be based on locks, timestamps, or validation, and can improve the concurrency and availability of the system. However, multiversion protocols may require more storage space and maintenance for the versions, and may have complexity and consistency issues.