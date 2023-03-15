# Properties of Transaction in DBMS

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction has four main properties, also known as ACID properties, that ensure the reliability and correctness of the database.
- The ACID properties are:

  - **Atomicity**: This means that a transaction is either executed completely or not at all. If any part of the transaction fails, the entire transaction is aborted and the database is restored to its previous state.
  - **Consistency**: This means that a transaction must preserve the integrity and validity of the database. A transaction must obey the predefined rules and constraints of the database, such as primary keys, foreign keys, triggers, etc. A transaction must not leave the database in an inconsistent state.
  - **Isolation**: This means that a transaction must not interfere with other concurrent transactions. A transaction must execute as if it is the only transaction in the system. The intermediate results of a transaction must not be visible to other transactions until the transaction is committed or aborted.
  - **Durability**: This means that the effects of a committed transaction must be permanent and persistent in the database. The changes made by a transaction must not be lost due to system failures, power outages, crashes, etc. The database must ensure the recovery of the committed transactions in case of any failure.

- These properties are essential for maintaining the accuracy and consistency of the data in a database. They also help in preventing data loss, corruption, and anomalies.