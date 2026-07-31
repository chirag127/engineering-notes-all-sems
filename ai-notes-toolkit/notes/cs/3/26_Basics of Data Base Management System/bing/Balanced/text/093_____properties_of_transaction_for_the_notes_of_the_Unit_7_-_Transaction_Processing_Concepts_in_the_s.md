### Properties of Transaction for the Notes of the Unit 7 - Transaction Processing Concepts in the Subject of Basics of Data Base Management System

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction has four main properties, collectively known as ACID, that ensure the reliability and correctness of the database operations.
- The four properties are:

  - **Atomicity**: This means that a transaction is either executed completely or not at all. If any part of the transaction fails, the entire transaction is aborted and the database is restored to its previous state before the transaction started.
  - **Consistency**: This means that a transaction must preserve the integrity constraints and business rules of the database. A transaction cannot leave the database in an inconsistent state, such as violating a primary key or a foreign key constraint.
  - **Isolation**: This means that a transaction must not interfere with other concurrent transactions. Each transaction must execute as if it is the only transaction in the system. The intermediate results of a transaction are not visible to other transactions until the transaction commits.
  - **Durability**: This means that the effects of a committed transaction are permanent and persist even in the case of system failures. The database system must ensure that the committed data is not lost or corrupted by using recovery techniques such as logging and checkpointing.