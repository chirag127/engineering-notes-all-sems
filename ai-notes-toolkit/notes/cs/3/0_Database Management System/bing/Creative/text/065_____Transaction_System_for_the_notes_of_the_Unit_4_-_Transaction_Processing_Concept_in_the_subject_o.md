### Transaction System for the notes of the Unit 4 - Transaction Processing Concept in the subject of Database Management System

- A transaction system is a database system that supports the execution of transactions, which are units of work that must be performed atomically and consistently.
- A transaction system ensures that the database remains in a consistent state after each transaction, and that concurrent transactions do not interfere with each other.
- A transaction system provides the following properties, also known as ACID properties:
  - Atomicity: A transaction is either executed completely or not at all. If a transaction fails, the database is restored to its original state before the transaction started.
  - Consistency: A transaction preserves the integrity constraints and business rules of the database. The database is always in a valid state before and after a transaction.
  - Isolation: A transaction is executed as if it were the only one running in the system. The intermediate results of a transaction are not visible to other transactions, and vice versa.
  - Durability: The effects of a committed transaction are permanent and cannot be lost due to system failures or power outages.
- A transaction system implements various mechanisms to achieve these properties, such as:
  - Locking: A technique that prevents concurrent transactions from accessing or modifying the same data item. A transaction must acquire a lock on a data item before reading or writing it, and release the lock after finishing the operation. Locks can be shared or exclusive, depending on the type of operation.
  - Logging: A technique that records the changes made by transactions to the database in a persistent storage device, such as a disk. A log contains information about the transaction id, the data item, the old value, and the new value. Logs are used to undo or redo transactions in case of failures or rollbacks.
  - Recovery: A technique that restores the database to a consistent state after a failure or a rollback. Recovery uses the logs to undo the effects of incomplete or aborted transactions, and to redo the effects of committed transactions that may have been lost due to failures.
  - Concurrency control: A technique that coordinates the execution of concurrent transactions to ensure isolation and consistency. Concurrency control uses locking, timestamps, or other methods to determine the order and validity of transactions. Concurrency control also detects and resolves conflicts and deadlocks among transactions.