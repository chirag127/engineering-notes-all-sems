# Unit 4 - Transaction Processing Concept

- A **transaction** is a logical unit of work that accesses and possibly modifies data in a database or a file system .
- A **transaction processing system (TPS)** is a software system that executes transactions and ensures that they are completed correctly and reliably.
- A transaction has four main properties, known as **ACID** :
  - **Atomicity**: A transaction must either be executed in its entirety or not at all. If any part of the transaction fails, the entire transaction is aborted and the database is restored to its previous state.
  - **Consistency**: A transaction must preserve the integrity and validity of the database. It must not violate any integrity constraints or business rules.
  - **Isolation**: A transaction must not interfere with other concurrent transactions. Each transaction must execute as if it is the only one in the system.
  - **Durability**: A transaction must ensure that its effects are permanent and persistent, even in the event of system failures or power outages.
- A transaction can have one of the following outcomes:
  - **Commit**: The transaction is successfully completed and its changes are made permanent in the database.
  - **Rollback**: The transaction is aborted and its changes are undone in the database.
  - **Partial commit**: The transaction is partially completed and some of its changes are made permanent in the database. This is an undesirable outcome that violates atomicity and consistency.
- A transaction can be executed in different modes, depending on the level of isolation and concurrency control required:
  - **Serial**: The transactions are executed one after another, in a sequential order. This mode ensures the highest level of isolation and consistency, but reduces the system throughput and performance.
  - **Parallel**: The transactions are executed simultaneously, in an overlapping or interleaved order. This mode improves the system throughput and performance, but may cause conflicts and inconsistencies among transactions.
  - **Mixed**: The transactions are executed in a combination of serial and parallel modes, depending on the degree of conflict and dependency among transactions. This mode balances the trade-off between isolation and concurrency, but requires more complex algorithms and protocols to manage transactions.