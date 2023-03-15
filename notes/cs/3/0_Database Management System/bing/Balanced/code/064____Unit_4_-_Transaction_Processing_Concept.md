## Unit 4 - Transaction Processing Concept

- A transaction is a logical unit of work that accesses and possibly modifies data in a database or a system .
- A transaction processing system (TPS) is a system that supports the execution of transactions in a reliable, efficient and secure manner.
- A transaction has four main properties, also known as ACID properties :
  - Atomicity: A transaction must either complete all its operations or none of them. If a transaction fails, it must be rolled back to its initial state.
  - Consistency: A transaction must preserve the integrity and validity of the data. It must not violate any constraints or rules defined on the data.
  - Isolation: A transaction must not interfere with other concurrent transactions. Each transaction must execute as if it is the only one in the system.
  - Durability: A transaction must ensure that its effects are permanent and not lost due to system failures or crashes.
- A transaction can have one of the following states :
  - Active: The initial state of a transaction, where it is executing its operations.
  - Partially committed: The state of a transaction after it has executed its final operation, but before it has committed.
  - Committed: The state of a transaction after it has successfully completed and its effects are recorded in the database or the system.
  - Failed: The state of a transaction after it has encountered an error or aborted due to some reason.
  - Aborted: The state of a transaction after it has been rolled back and its effects are undone.
- A transaction manager is a component of a TPS that is responsible for coordinating and controlling the execution of transactions. It performs the following functions:
  - Scheduling: It decides the order and timing of transactions to be executed.
  - Logging: It records the history and status of transactions in a log file for recovery purposes.
  - Concurrency control: It ensures that concurrent transactions do not conflict with each other and maintain isolation.
  - Recovery: It restores the system to a consistent state in case of failures or crashes.