## Transaction Control Language(TCL) statements

- Transaction Control Language (TCL) is a type of SQL command that is used to manage transactions in a database.
- Transactions are a way of grouping multiple SQL statements into a single unit of work, so that either all of the statements are executed, or none of them are.
- This helps to ensure the consistency and integrity of the data in the database.
- The main TCL commands are:
  - **COMMIT**: It is used to save the changes made by the transactions in the database  .
  - **ROLLBACK**: It is used to undo the changes made by the transactions in the database  . It can restore the database to the last committed state or to a specified savepoint.
  - **SAVEPOINT**: It is used to create a point in the transaction where the changes can be rolled back to  . It allows partial rollback of a transaction.
  - **SET TRANSACTION**: It is used to specify the characteristics of the current transaction, such as isolation level, read-only or read-write mode, etc.
- TCL commands can be used with DML statements (INSERT, UPDATE, DELETE) to control the changes made to the data in the database.
- An example of using TCL commands is:

```sql
-- Begin a transaction
BEGIN TRANSACTION;

-- Insert a record into the table
INSERT INTO student (id, name, age) VALUES (101, 'Alice', 20);

-- Create a savepoint
SAVEPOINT sp1;

-- Update the record
UPDATE student SET age = 21 WHERE id = 101;

-- Rollback to the savepoint
ROLLBACK TO sp1;

-- Commit the transaction
COMMIT;
```

- In this example, the transaction begins with the BEGIN TRANSACTION statement. Then, a record is inserted into the student table. A savepoint named sp1 is created after the insertion. Then, the record is updated with a new age value. However, the update is rolled back to the savepoint sp1, which means the insertion is still valid but the update is not. Finally, the transaction is committed with the COMMIT statement, which saves the insertion in the database.