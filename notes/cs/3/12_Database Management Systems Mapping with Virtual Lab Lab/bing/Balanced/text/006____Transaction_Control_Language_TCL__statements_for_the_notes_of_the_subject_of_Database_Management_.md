## Transaction Control Language(TCL) statements

- Transaction Control Language (TCL) is a type of SQL command that is used to manage transactions in a database.
- Transactions are a way of grouping multiple SQL statements into a single unit of work, so that either all of the statements are executed, or none of them are.
- This helps to ensure the consistency and integrity of the data in the database.
- TCL commands are used to keep track of the modifications that DML statements make.
- TCL also allows you to organise statements into logical transactions.
- The main TCL commands are:
  - **COMMIT**: It is used to save the transactions in the database . It marks the end of a successful transaction.
  - **ROLLBACK**: It is used to restore the database to that state which was last committed . It undoes the changes made by the previous SQL statements in the current transaction.
  - **SAVEPOINT**: It is used to create a point in the transaction where the changes done till that point will be unchanged and all the transactions after that point will be rolled back . It allows you to partially commit or rollback a transaction.
  - **SET TRANSACTION**: It is used to specify the characteristics of the current transaction, such as isolation level, read-only or read-write mode, etc. It must be the first statement in a transaction.