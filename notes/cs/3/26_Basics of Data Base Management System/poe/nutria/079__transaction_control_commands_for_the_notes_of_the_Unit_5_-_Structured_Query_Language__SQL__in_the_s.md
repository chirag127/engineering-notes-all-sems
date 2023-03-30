
### Transaction Control Commands

1. **COMMIT**: A COMMIT statement is used to save the changes made by a transaction to the database. It is used to end a transaction and make permanent changes visible to other users.

2. **ROLLBACK**: A ROLLBACK statement is used to undo the changes made by a transaction. It is used to restore the database to its previous state before the transaction was executed.

3. **SAVEPOINT**: A SAVEPOINT statement is used to create a point in a transaction to which you can later roll back. This allows you to undo part of a transaction without rolling back the entire transaction.

4. **SET TRANSACTION**: A SET TRANSACTION statement is used to specify the characteristics of the current transaction. It can be used to set the transaction isolation level, the transaction name, and the transaction read-only status.