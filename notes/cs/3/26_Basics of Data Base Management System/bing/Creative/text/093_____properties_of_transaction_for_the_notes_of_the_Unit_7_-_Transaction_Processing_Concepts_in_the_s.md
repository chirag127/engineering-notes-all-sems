### Properties of Transaction for the Notes of the Unit 7 - Transaction Processing Concepts in the Subject of Basics of Data Base Management System

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database. A transaction has a beginning and an end.
- A transaction must satisfy the ACID properties, which are Atomicity, Consistency, Isolation, and Durability. 
- Atomicity means that a transaction is either completed in its entirety or not executed at all. If a transaction fails, the database is restored to its original state before the transaction started.  
- Consistency means that a transaction must preserve the integrity constraints of the database. A transaction can only bring the database from one valid state to another valid state.  
- Isolation means that a transaction must not interfere with other concurrent transactions. Each transaction should execute as if it is the only transaction in the system.  
- Durability means that the effects of a committed transaction are permanent and persist even in the case of system failures. The database must not lose any data due to power outages, crashes, or errors.  
- A transaction can be in one of the following states: active, partially committed, committed, failed, or aborted. 
- Active is the initial state of a transaction when it is executed. 
- Partially committed is the state of a transaction after it has executed its final statement, but before it has committed. 
- Committed is the state of a transaction after it has successfully completed and made its changes permanent in the database. 
- Failed is the state of a transaction when it cannot continue due to some error or violation of integrity constraints. 
- Aborted is the state of a transaction when it has been rolled back and the database is restored to its state before the transaction started. 
- A schedule is a sequence of operations from a set of concurrent transactions. 
- A schedule is serial if it executes the transactions one after another, without interleaving their operations. 
- A schedule is serializable if it is equivalent to some serial schedule, meaning that it produces the same final state of the database as the serial schedule. 
- A schedule is recoverable if it ensures that a transaction can only commit after all the transactions whose changes it has read have committed. 
- A schedule is cascadeless if it ensures that a transaction can only read the changes made by a committed transaction. 
- A schedule is strict if it ensures that a transaction can only read and write the data items that have not been accessed by any other transaction. 
- A schedule is conflict-serializable if it can be transformed into a serial schedule by swapping the order of non-conflicting operations. 
- A schedule is view-serializable if it is equivalent to a serial schedule in terms of the read and write operations on each data item. 
- A transaction management system is responsible for ensuring the ACID properties of transactions, by using various techniques such as locking, timestamping, logging, recovery, and concurrency control.  

: https://www.educba.com/transaction-property-in-dbms/
: https://www.guru99.com/dbms-transaction-management.html
: https://byjus.com/gate/transaction-in-dbms-notes/
: https://www.javatpoint.com/dbms-transaction-property
: https://www.w3schools.in/dbms/transaction
: https://www.geeksforgeeks.org/acid-properties-in-dbms/