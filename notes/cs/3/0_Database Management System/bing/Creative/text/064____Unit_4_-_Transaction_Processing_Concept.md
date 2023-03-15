## Unit 4 - Transaction Processing Concept

- A **transaction** is a logical unit of work that accesses and possibly modifies data in a database or a file system .
- A **transaction processing system (TPS)** is a software system that executes transactions and ensures that they are performed reliably and consistently.
- A transaction has four main properties, known as **ACID** :
  - **Atomicity**: A transaction must either complete all of its operations or none of them. If any operation fails, the transaction is aborted and the database is restored to its previous state.
  - **Consistency**: A transaction must preserve the integrity and validity of the database. It must not violate any constraints, rules, or triggers defined on the data.
  - **Isolation**: A transaction must not interfere with other concurrent transactions. Each transaction must execute as if it is the only one running on the system.
  - **Durability**: A transaction must ensure that its effects are permanent and persist even in the case of system failures or power outages.
- A transaction can have one of the following outcomes:
  - **Commit**: The transaction successfully completes all of its operations and the changes are made permanent in the database.
  - **Abort**: The transaction fails to complete some or all of its operations and the changes are discarded. The database is restored to its previous state.
  - **Partial commit**: The transaction completes some of its operations but not all of them. This is an undesirable outcome and should be avoided by using atomicity.
- A transaction can be executed in two modes:
  - **Flat**: The transaction is executed as a single unit without any subtransactions or savepoints. The transaction can only commit or abort as a whole.
  - **Nested**: The transaction is divided into subtransactions that can have their own commit or abort points. The subtransactions can also be nested within other subtransactions. The transaction can commit or abort partially depending on the outcome of the subtransactions.
- A transaction can be classified into two types based on the nature of its operations:
  - **Read-only**: The transaction only reads data from the database and does not modify it. It does not need to lock any data or log any changes. It can be executed concurrently with other transactions without any conflicts.
  - **Update**: The transaction reads and writes data to the database. It needs to lock the data it accesses and log the changes it makes. It may conflict with other transactions that access the same data.