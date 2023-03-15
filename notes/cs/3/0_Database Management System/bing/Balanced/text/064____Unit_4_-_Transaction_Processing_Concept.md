## Unit 4 - Transaction Processing Concept

- A transaction is a logical unit of work that accesses and possibly modifies data in a database or a system.
- A transaction processing system (TPS) is a system that supports the execution of transactions in a reliable, efficient and secure manner.
- A transaction has four main properties, also known as ACID properties:
  - Atomicity: A transaction is either executed completely or not at all. If a transaction fails, all the changes made by it are rolled back.
  - Consistency: A transaction preserves the consistency of the database or the system by ensuring that it satisfies all the integrity constraints and business rules.
  - Isolation: A transaction is executed in isolation from other concurrent transactions, meaning that it does not interfere with or see the intermediate results of other transactions.
  - Durability: A transaction ensures that the changes made by it are permanent and will not be lost due to system failures or errors.
- A transaction can have one of the following states:
  - Active: The initial state of a transaction when it starts execution.
  - Partially committed: The state of a transaction when it has executed its final statement but has not yet committed.
  - Committed: The state of a transaction when it has successfully completed and its changes are made permanent.
  - Failed: The state of a transaction when it encounters an error or aborts due to some reason.
  - Aborted: The state of a transaction when it has been rolled back and its changes are undone.
- A transaction manager is a component of a TPS that is responsible for coordinating the execution of transactions and ensuring their ACID properties. It performs the following functions:
  - Scheduling: It decides the order and timing of transactions to be executed.
  - Logging: It records the history of transactions and their changes in a log file for recovery purposes.
  - Concurrency control: It controls the concurrent execution of transactions and prevents conflicts and inconsistencies.
  - Recovery: It restores the database or the system to a consistent state in case of failures or errors.