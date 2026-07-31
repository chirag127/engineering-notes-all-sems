### Transaction Control Commands

Transaction control commands are used to manage changes made by DML statements. These commands allow you to control and manage transactions to maintain the integrity of data within SQL statements. Here are the main transaction control commands in SQL:

1. **COMMIT**: This command is used to permanently save any changes made by a transaction to the database. Once a transaction has been committed, it cannot be rolled back.

2. **ROLLBACK**: This command is used to undo any changes made by a transaction. The ROLLBACK command can only be used to undo changes that have not yet been committed.

3. **SAVEPOINT**: This command is used to create a savepoint within a transaction. A savepoint is a point within a transaction to which you can later roll back.

4. **SET TRANSACTION**: This command is used to specify the characteristics of a transaction. For example, you can use the SET TRANSACTION command to specify that a transaction is read-only or read-write.

These commands are essential for maintaining the integrity of data within a database and ensuring that transactions are completed successfully. It is important to understand how to use these commands when working with SQL and databases.