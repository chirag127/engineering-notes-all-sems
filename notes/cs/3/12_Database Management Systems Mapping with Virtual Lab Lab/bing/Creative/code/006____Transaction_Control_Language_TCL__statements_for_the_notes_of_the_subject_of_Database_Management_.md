# Transaction Control Language(TCL) statements for the notes of the subject of Database Management Systems Mapping with Virtual Lab Lab

- Transaction Control Language (TCL) is a language that manages transactions within the database. Transactions are a sequence of operations that are performed as a single logical unit of work.
- TCL commands are used to execute the changes made by the Data Manipulation Language (DML) statements, such as INSERT, UPDATE, and DELETE.
- TCL commands also allow the statements to be grouped together into logical transactions, which can be committed or rolled back as a whole.
- The main TCL commands are:
  - COMMIT: It saves all the changes made by the transaction to the database and ends the transaction.
  - ROLLBACK: It undoes all the changes made by the transaction and restores the database to its previous state before the transaction started.
  - SAVEPOINT: It creates a named point in the transaction that can be used to roll back to a specific state within the transaction.
  - SET TRANSACTION: It sets the properties of the transaction, such as isolation level, read-only or read-write mode, etc.
- Some examples of TCL commands are:

  - COMMIT;
    - This command commits the current transaction and saves all the changes to the database.
  - ROLLBACK;
    - This command rolls back the current transaction and discards all the changes made by it.
  - SAVEPOINT sp1;
    - This command creates a savepoint named sp1 in the current transaction.
  - ROLLBACK TO sp1;
    - This command rolls back the current transaction to the savepoint sp1 and undoes all the changes made after it.
  - SET TRANSACTION READ ONLY;
    - This command sets the current transaction to read-only mode, which means it can only query the database and not modify it.