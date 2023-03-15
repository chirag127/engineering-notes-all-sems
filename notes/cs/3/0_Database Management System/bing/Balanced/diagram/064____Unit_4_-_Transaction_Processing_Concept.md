## Unit 4 - Transaction Processing Concept

- A transaction is a logical unit of work that represents a real-world event of interest to a database system.
- A transaction processing system (TPS) is a software system that supports the execution of transactions over a database.
- A transaction has four main properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that a transaction either executes completely or not at all. If a transaction fails, the database is restored to its original state before the transaction started.
- Consistency means that a transaction preserves the integrity constraints and business rules of the database. A transaction does not violate any predefined rules or conditions on the data.
- Isolation means that a transaction does not interfere with other concurrent transactions. Each transaction executes as if it were the only one in the system.
- Durability means that the effects of a successful transaction are permanent and do not get lost due to system failures or crashes.
- A transaction processing system typically consists of three components: a transaction manager, a concurrency control manager, and a recovery manager.
- A transaction manager is responsible for coordinating the execution of transactions and ensuring their ACID properties. It also provides an interface for the application programs to access the database.
- A concurrency control manager is responsible for managing the concurrent access of transactions to the database and preventing conflicts or anomalies. It uses various techniques such as locking, timestamping, or optimistic methods to ensure serializability of transactions.
- A recovery manager is responsible for restoring the database to a consistent state in case of failures or crashes. It uses various techniques such as logging, checkpointing, or shadow paging to undo or redo the effects of transactions.