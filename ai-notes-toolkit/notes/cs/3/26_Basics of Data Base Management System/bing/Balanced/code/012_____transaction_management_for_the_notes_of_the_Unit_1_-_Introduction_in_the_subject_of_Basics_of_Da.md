### Transaction Management

Transaction management is a logical unit of processing in a DBMS which entails one or more database access operations. It is a transaction is a program unit whose execution may or may not change the contents of a database. Not managing concurrent access may create issues like hardware failure and system crashes.

A transaction symbolizes a unit of work, performed within a database management system (or similar system) against a database, that is treated in a coherent and reliable way independent of other transactions. A transaction generally represents any change in a database.

Some of the topics covered in this unit are:

- Transaction states
- Transaction properties
- Transaction log
- Concurrency control
- Locking mechanisms
- Deadlocks
- Serializability
- Recovery techniques

#### Transaction States

There are various database transaction states as follows:

- Active state - this is the state in which the transaction is being executed and database modifications are being made.
- Partially committed state - this is the state in which the transaction has executed its final statement but the changes are not yet permanent in the database.
- Committed state - this is the state in which the transaction has completed successfully and the changes are permanent in the database.
- Failed state - this is the state in which the transaction has encountered an error and cannot continue execution.
- Aborted state - this is the state in which the transaction has been rolled back and the database is restored to its previous state before the transaction started.

#### Transaction Properties

A transaction must satisfy four properties, known as ACID properties, to ensure data integrity and consistency:

- Atomicity - this means that either all the operations in a transaction are executed or none of them are. A transaction is an indivisible unit of work.
- Consistency - this means that a transaction must preserve the consistency rules of the database, such as referential integrity, domain constraints, etc. A transaction must not leave the database in an inconsistent state.
- Isolation - this means that a transaction must not interfere with other concurrent transactions. A transaction must execute as if it is the only one in the system.
- Durability - this means that the changes made by a transaction must persist even in the event of system failures. A transaction must not lose its effects due to power outages, crashes, etc.

#### Transaction Log

Every SQL Server database has a transaction log that records all transactions and the database modifications made by each transaction. The transaction log is a critical component of the database. If there is a system failure, you will need that log to bring your database back to a consistent state.

The transaction log contains the following information:

- The start and end of each transaction
- The names of the data items that are accessed and modified by each transaction
- The old and new values of the data items that are updated by each transaction
- The commit or rollback operations of each transaction

The transaction log is used for two main purposes:

- Recovery - the transaction log is used to undo the effects of incomplete transactions and redo the effects of committed transactions in case of a system failure. This ensures that the ACID properties of transactions are maintained.
- Auditing - the transaction log is used to track the history of transactions and the changes they made to the database. This can help in detecting unauthorized access, fraud, or errors.

#### Concurrency Control

Concurrency control is the process of managing simultaneous access to the database by multiple transactions. Concurrency control is necessary to ensure the isolation and consistency properties of transactions. Without concurrency control, concurrent transactions may cause the following problems:

- Lost update - this occurs when two transactions update the same data item and one of them overwrites the changes of the other without knowing it.
- Dirty read - this occurs when one transaction reads a data item that has been modified by another transaction but not yet committed. The read value may be incorrect or inconsistent.
- Unrepeatable read - this occurs when one transaction reads the same data item twice and gets different values because another transaction has updated it in between.
- Phantom read - this occurs when one transaction reads a set of data items that satisfy some condition and another transaction inserts or deletes some data items that affect the condition. The read set may change unexpectedly.

There are various techniques for concurrency control, such as:

- Locking - this is the most common technique, which involves granting exclusive or shared access to data items based on the operations performed by transactions. Locking can prevent lost updates, dirty reads, and unrepeatable reads, but may cause deadlocks or reduced concurrency.
- Timestamping - this is a technique that assigns a unique timestamp