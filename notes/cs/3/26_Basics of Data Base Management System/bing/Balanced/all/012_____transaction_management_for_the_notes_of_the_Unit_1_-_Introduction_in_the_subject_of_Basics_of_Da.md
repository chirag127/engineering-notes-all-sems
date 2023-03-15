# Transaction Management

Transaction management is a logical unit of processing in a DBMS which entails one or more database access operations. It is a transaction is a program unit whose execution may or may not change the contents of a database. Not managing concurrent access may create issues like hardware failure and system crashes.

## Transaction States

There are various database transaction states as follows:

- Active state - this is the state in which the transaction is being executed. It involves reading and writing operations on the database.
- Partially committed state - this is the state in which the transaction has executed its final statement, but the changes are not yet permanent in the database.
- Committed state - this is the state in which the transaction has completed successfully and the changes are permanent in the database.
- Failed state - this is the state in which the transaction has encountered an error or an abort command and cannot continue execution.
- Aborted state - this is the state in which the transaction has been rolled back and the database is restored to its previous state before the transaction started.

## Transaction Properties

A transaction must satisfy four properties, known as ACID properties, to ensure data integrity and consistency :

- Atomicity - this means that the transaction is either executed in its entirety or not executed at all. If any part of the transaction fails, the whole transaction is aborted and the database is left unchanged.
- Consistency - this means that the transaction must preserve the integrity constraints and business rules of the database. The database must remain in a consistent state before and after the transaction.
- Isolation - this means that the transaction must not interfere with other concurrent transactions. The intermediate results of the transaction must not be visible to other transactions until the transaction is committed.
- Durability - this means that the changes made by the transaction must persist even in the event of system failures or power outages. The committed data must be stored in a non-volatile memory.

## Transaction Management Techniques

There are various techniques used by the DBMS to manage transactions and ensure ACID properties, such as:

- Locking - this is a mechanism that prevents concurrent access to the same data item by different transactions. A transaction must acquire a lock on a data item before reading or writing it, and release the lock after finishing the operation. There are different types of locks, such as shared locks, exclusive locks, and deadlock prevention and detection methods.
- Timestamping - this is a mechanism that assigns a unique timestamp to each transaction and each data item. The timestamp indicates the order of execution of the transactions and the data items. A transaction can read or write a data item only if its timestamp is compatible with the timestamp of the data item, otherwise it is aborted or delayed.
- Logging - this is a mechanism that records the changes made by the transactions in a log file. The log file contains information such as the transaction id, the data item, the old value, and the new value. The log file is used to recover the database in case of system failures or transaction aborts. There are different types of logging, such as undo logging, redo logging, and undo/redo logging.
- Checkpointing - this is a mechanism that periodically writes the contents of the main memory to the disk. This reduces the amount of data that needs to be recovered in case of system failures or transaction aborts. A checkpoint is a point in time when the database is in a consistent state and all the transactions have either committed or aborted.