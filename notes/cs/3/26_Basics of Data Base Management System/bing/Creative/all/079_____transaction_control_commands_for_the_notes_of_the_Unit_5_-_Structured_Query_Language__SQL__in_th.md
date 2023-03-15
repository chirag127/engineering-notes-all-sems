# Transaction Control Commands

- Transaction control commands are used to manage the changes made by SQL statements in a database.
- A transaction is a logical unit of work that consists of one or more SQL statements that are executed as a single unit.
- A transaction has the following properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the statements in a transaction are executed successfully or none of them are executed at all.
- Consistency means that the database remains in a valid state before and after a transaction.
- Isolation means that the changes made by one transaction are not visible to other transactions until the transaction is committed.
- Durability means that the changes made by a committed transaction are permanent and not lost due to system failures.
- The following commands are used to control transactions in SQL:
  - **COMMIT** - This command is used to make a transaction permanent in a database. It saves the changes made by the transaction and ends the current transaction.
  - **ROLLBACK** - This command is used to undo the changes made by a transaction. It restores the database to its previous state before the transaction started and ends the current transaction.
  - **SAVEPOINT** - This command is used to create points within a transaction to which the transaction can be rolled back partially. It allows dividing a transaction into smaller subtransactions.
  - **SET TRANSACTION** - This command is used to specify the characteristics of a transaction, such as its isolation level, name, or read-only status.
- SQL Server operates in the following transaction modes:
  - **Autocommit transactions** - Each individual statement is a transaction. It is committed automatically when it completes successfully or rolled back automatically when it fails.
  - **Explicit transactions** - Each transaction is explicitly started with the **BEGIN TRANSACTION** statement and explicitly ended with a **COMMIT** or **ROLLBACK** statement.
  - **Implicit transactions** - A transaction is implicitly started when the first SQL statement is executed after the **SET IMPLICIT_TRANSACTIONS ON** statement. It is ended with a **COMMIT** or **ROLLBACK** statement or when another **SET IMPLICIT_TRANSACTIONS ON** statement is executed.
- A transaction can be explicitly executed as a distributed transaction by using **BEGIN DISTRIBUTED TRANSACTION**. A distributed transaction involves multiple servers or databases that are coordinated by the Microsoft Distributed Transaction Coordinator (MS DTC).