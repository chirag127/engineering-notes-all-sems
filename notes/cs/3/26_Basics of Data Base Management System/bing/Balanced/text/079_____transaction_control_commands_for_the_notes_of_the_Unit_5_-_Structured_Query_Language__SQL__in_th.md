### Transaction Control Commands

- Transaction Control Language (TCL) is a subset of SQL that is used to manage transactions in a database.
- A transaction is a logical unit of work that consists of one or more SQL statements that are executed as a single unit.
- A transaction has the following properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the statements in a transaction are executed successfully or none of them are executed at all.
- Consistency means that a transaction preserves the integrity of the database and does not violate any constraints or rules.
- Isolation means that a transaction is not affected by the concurrent execution of other transactions and does not interfere with them.
- Durability means that the effects of a transaction are permanent and persist even in the event of a system failure or power outage.
- The following commands are used to control transactions in SQL:
  - **COMMIT**: This command is used to make a transaction permanent in the database. It saves the changes made by the transaction and ends the current transaction.
  - **ROLLBACK**: This command is used to undo the changes made by the transaction and restore the database to its previous state before the transaction started. It aborts the current transaction and discards any changes made by it.
  - **SAVEPOINT**: This command is used to create points within a transaction that can be used to roll back to a specific state in case of an error or failure. It allows partial undo of a transaction.
  - **SET TRANSACTION**: This command is used to specify the characteristics of a transaction, such as its isolation level, name, or read-only status. It must be executed before any other SQL statement in the transaction.