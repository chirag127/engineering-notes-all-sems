## Unit 4 - Transaction Processing Concept

- A transaction is a logical unit of work that accesses and possibly modifies data in a database or a system  .
- A transaction processing system (TPS) is a system that supports the execution of transactions in a reliable, efficient and secure manner .
- A transaction has four main properties, also known as ACID properties  :
  - Atomicity: A transaction must either complete all its operations or none of them. If any operation fails, the transaction is aborted and the database is restored to its previous consistent state.
  - Consistency: A transaction must preserve the integrity constraints and business rules of the database. The database must remain consistent before and after the transaction.
  - Isolation: A transaction must not interfere with other concurrent transactions. Each transaction must execute as if it is the only one in the system.
  - Durability: A transaction must ensure that the changes it makes to the database are permanent and not lost due to system failures or crashes.
- A transaction can have one of the following states  :
  - Active: The initial state of a transaction, where it is executing its operations.
  - Partially committed: The state of a transaction after it has executed its final operation, but before it has committed.
  - Committed: The state of a transaction after it has successfully completed and made its changes permanent in the database.
  - Failed: The state of a transaction after it has encountered an error or aborted due to some reason.
  - Aborted: The state of a transaction after it has been rolled back and undone its changes to the database.
- A transaction manager is a component of a TPS that is responsible for coordinating the execution of transactions and ensuring their ACID properties  .
- A transaction manager consists of two sub-components :
  - A scheduler: A module that controls the order and concurrency of transactions. It uses various techniques such as locking, timestamping, serialization and multiversioning to prevent conflicts and ensure isolation.
  - A recovery manager: A module that handles the failure and recovery of transactions. It uses various techniques such as logging, checkpointing, shadow paging and undo/redo to ensure atomicity and durability.