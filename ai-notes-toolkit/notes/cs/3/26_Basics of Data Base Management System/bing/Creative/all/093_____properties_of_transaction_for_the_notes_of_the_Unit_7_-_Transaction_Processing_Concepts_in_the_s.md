# Properties of Transaction in DBMS

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction has four main properties, also known as ACID properties, that ensure the reliability and correctness of the database.
- The four properties are:

  - **Atomicity**: This means that a transaction is either executed completely or not at all. If any part of the transaction fails, the entire transaction is aborted and the database is restored to its previous state before the transaction started. This ensures that the database is not left in an inconsistent state due to partial execution of a transaction.   
  - **Consistency**: This means that a transaction must preserve the integrity constraints and business rules of the database. A transaction must not violate any of the conditions that define a consistent state of the database. If a transaction starts with a consistent state of the database, it must end with a consistent state of the database. This ensures that the database is always valid and accurate.    
  - **Isolation**: This means that a transaction must not interfere with other concurrent transactions. A transaction must execute as if it is the only transaction in the system. The intermediate results and effects of a transaction must not be visible to other transactions until the transaction commits. This ensures that the concurrent execution of transactions does not lead to any anomalies or conflicts.     
  - **Durability**: This means that the effects of a committed transaction must be permanent and persistent in the database. The changes made by a transaction must not be lost due to any system failure or error. The database must be able to recover the committed state of the database after any failure. This ensures that the database is reliable and stable.    

- These properties are essential for ensuring the correctness and efficiency of transaction processing in a database management system.