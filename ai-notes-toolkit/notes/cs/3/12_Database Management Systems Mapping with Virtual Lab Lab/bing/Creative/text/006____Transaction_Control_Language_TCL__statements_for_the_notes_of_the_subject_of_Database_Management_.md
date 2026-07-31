## Transaction Control Language(TCL) statements for the notes of the subject of Database Management Systems Mapping with Virtual Lab Lab

- Transaction Control Language (TCL) is a language that manages transactions within the database. Transactions are logical units of work that consist of one or more SQL statements that are executed as a whole  .
- TCL commands are used to control the changes made by the Data Manipulation Language (DML) statements, such as INSERT, UPDATE, and DELETE   .
- TCL commands also allow the statements to be grouped together into logical transactions, which can be committed or rolled back as a unit .
- The main TCL commands are:
  - COMMIT: This command saves all the changes made by the DML statements in the database and ends the current transaction   .
  - ROLLBACK: This command undoes all the changes made by the DML statements in the current transaction and restores the database to its previous state before the transaction started   .
  - SAVEPOINT: This command creates a named point in the current transaction that can be used to roll back to a specific state within the transaction .
  - SET TRANSACTION: This command sets the properties of the current transaction, such as isolation level, read-only or read-write mode, and transaction name.
- TCL commands help to maintain the consistency and integrity of the database and ensure that the transactions follow the ACID properties, which are:
  - Atomicity: A transaction is either completed in its entirety or not at all .
  - Consistency: A transaction transforms the database from one consistent state to another consistent state .
  - Isolation: A transaction is executed independently of other concurrent transactions and does not interfere with them .
  - Durability: The effects of a committed transaction are permanent and do not get lost due to system failures .
- TCL commands can be used in SQL queries or in stored procedures, triggers, and functions.
- TCL commands can be executed automatically by the database system or manually by the user.
- Examples of TCL commands are:

  - COMMIT: `COMMIT;`
  - ROLLBACK: `ROLLBACK;`
  - SAVEPOINT: `SAVEPOINT sp1;`
  - ROLLBACK TO SAVEPOINT: `ROLLBACK TO sp1;`
  - SET TRANSACTION: `SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;`