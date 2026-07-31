# Unit 7 - Transaction Processing Concepts

- A **transaction** is a logical unit of work that accesses and possibly modifies data in a database.
- A transaction has the following properties :
  - **Atomicity**: A transaction must either complete all of its operations or none of them. If a transaction fails, the database state is restored to the state before the transaction started.
  - **Consistency**: A transaction must preserve the integrity constraints of the database. If the database is consistent before the transaction, it must be consistent after the transaction.
  - **Isolation**: A transaction must not be affected by the concurrent execution of other transactions. Each transaction must execute as if it were the only one in the system.
  - **Durability**: The effects of a successful transaction must be permanent and survive any system failures.
- A **transaction processing system** is a system that supports the execution of transactions on a large database with many concurrent users.
- A transaction processing system has the following components :
  - **Transaction manager**: The component that coordinates the execution of transactions and ensures their ACID properties. It also handles transaction failures and recovery.
  - **Scheduler**: The component that controls the order of execution of operations from different transactions. It also resolves conflicts and ensures serializability of transactions.
  - **Buffer manager**: The component that manages the movement of data between the main memory and the disk. It also implements caching and buffering techniques to improve performance.
  - **Recovery manager**: The component that ensures the durability of transactions and recovers the database from failures. It also implements logging and checkpointing techniques to facilitate recovery.
  - **Lock manager**: The component that implements locking protocols to ensure the isolation of transactions. It also handles deadlock detection and resolution.
  - **Query processor**: The component that parses, optimizes, and executes queries from transactions. It also implements query evaluation and optimization techniques to improve performance.