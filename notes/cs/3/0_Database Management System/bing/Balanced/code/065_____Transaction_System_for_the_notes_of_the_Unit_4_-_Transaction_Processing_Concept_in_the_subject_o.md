### Transaction System for the notes of the Unit 4 - Transaction Processing Concept in the subject of Database Management System

- A transaction system is a database system that supports the execution of transactions, which are units of work that must be performed atomically and consistently.
- A transaction system ensures that the database remains in a consistent state after each transaction, even in the presence of failures or concurrent access.
- A transaction system provides the following properties, also known as ACID properties:
  - Atomicity: A transaction is either executed completely or not at all. If a transaction fails, the database is restored to its original state before the transaction started.
  - Consistency: A transaction preserves the integrity constraints and business rules of the database. The database is always in a valid state before and after a transaction.
  - Isolation: A transaction is executed as if it were the only one running in the system. The intermediate results of a transaction are not visible to other transactions, and vice versa.
  - Durability: The effects of a committed transaction are permanent and cannot be lost due to failures or power outages.
- A transaction system implements various mechanisms to achieve these properties, such as:
  - Concurrency control: A technique to coordinate the access of multiple transactions to the same data, and to prevent conflicts or anomalies that may arise from concurrent execution.
  - Recovery management: A technique to restore the database to a consistent state after a failure, by undoing or redoing the operations of transactions that were affected by the failure.
  - Logging: A technique to record the changes made by transactions to the database, and to support the recovery process in case of failures.
  - Locking: A technique to grant exclusive or shared access to data items to transactions, and to prevent unauthorized or conflicting access by other transactions.
  - Timestamping: A technique to assign a logical order to transactions based on their start or commit times, and to ensure that transactions are executed in a serializable manner.
  - Deadlock detection and resolution: A technique to identify and resolve situations where two or more transactions are waiting for each other to release a lock, and to prevent the system from being blocked.