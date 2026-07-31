## Transaction Control Language(TCL) statements 

Transaction Control Language(TCL) statements are used to manage transactions in a database. They are responsible for controlling the changes made to the data in a database and ensuring that they are consistent and reliable. Here are some important TCL statements that you should know:

1. **COMMIT** - This statement is used to commit a transaction and make all changes made during the transaction permanent. Once a transaction has been committed, it cannot be undone.

2. **ROLLBACK** - This statement is used to undo any changes made during a transaction and roll back to the last committed state. It is typically used when an error occurs during a transaction.

3. **SAVEPOINT** - This statement is used to create a savepoint within a transaction. A savepoint allows you to roll back to a specific point within a transaction instead of rolling back the entire transaction.

4. **ROLLBACK TO SAVEPOINT** - This statement is used to roll back to a specific savepoint within a transaction.

5. **SET TRANSACTION** - This statement is used to set the transaction isolation level and other transaction properties. It can be used to control the behavior of concurrent transactions.

6. **BEGIN TRANSACTION** - This statement is used to start a new transaction. It is typically used in conjunction with other TCL statements to control the behavior of the transaction.

7. **COMMIT WORK** - This statement is used to commit a transaction and make all changes made during the transaction permanent. It is equivalent to the COMMIT statement.

8. **ROLLBACK WORK** - This statement is used to undo any changes made during a transaction and roll back to the last committed state. It is equivalent to the ROLLBACK statement.

TCL statements are an important part of database management systems and are used to ensure the consistency and reliability of the data in a database. It is important to understand how they work and how to use them effectively to manage transactions in a database.