### Transaction Control Commands

Transaction control commands are used to manage changes made by DML statements. These commands allow statements to be grouped together into logical transactions. The following are the transaction control commands in SQL:

1. **COMMIT**: This command is used to save the changes made by a transaction permanently to the database. Once a transaction is committed, the changes cannot be undone.

2. **ROLLBACK**: This command is used to undo the changes made by a transaction. It restores the data to its state before the transaction began.

3. **SAVEPOINT**: This command is used to create a savepoint within a transaction. A savepoint allows you to roll back to a specific point within a transaction, rather than rolling back the entire transaction.

4. **SET TRANSACTION**: This command is used to specify the characteristics of a transaction. It can be used to set the isolation level, the read-only or read-write access mode, and the diagnostic size.

These commands are essential for maintaining the integrity and consistency of the data in a database. They allow you to group related changes together and ensure that either all changes are made or none are made, preventing partial updates that could leave the database in an inconsistent state.