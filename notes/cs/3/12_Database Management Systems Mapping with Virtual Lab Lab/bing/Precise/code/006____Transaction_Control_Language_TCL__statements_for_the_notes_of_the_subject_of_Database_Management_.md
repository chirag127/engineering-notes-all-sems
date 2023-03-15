## Transaction Control Language(TCL) statements for the notes of the subject of Database Management Systems Mapping with Virtual Lab Lab

Transaction Control Language (TCL) is a subset of SQL (Structured Query Language) that is used to manage transactions in a database. A transaction is a logical unit of work that contains one or more SQL statements. TCL statements are used to control and manage transactions to ensure the consistency and integrity of data in a database.

The main TCL statements are:

1. **COMMIT**: This statement is used to permanently save any changes made by the transaction to the database. Once a transaction is committed, the changes made by the transaction become permanent and cannot be undone.

2. **ROLLBACK**: This statement is used to undo any changes made by the transaction to the database. If a transaction is rolled back, all changes made by the transaction are undone and the database is restored to its state before the transaction began.

3. **SAVEPOINT**: This statement is used to create a savepoint within a transaction. A savepoint is a point within a transaction to which you can roll back. If a transaction is rolled back to a savepoint, all changes made after the savepoint are undone, but changes made before the savepoint are retained.

These statements are used to ensure the consistency and integrity of data in a database by allowing the user to control transactions and make changes to the database in a controlled manner. They are an essential part of any database management system and are commonly used in conjunction with other SQL statements to manage data in a database.