## Transaction Control Language(TCL) statements

Transaction Control Language (TCL) is a type of SQL command that is used to manage transactions in a database. Transactions are a way of grouping multiple SQL statements into a single unit of work, so that either all of the statements are executed, or none of them are. This helps to ensure the consistency and integrity of the data in the database.

TCL commands are used to keep track of the modifications that DML statements (such as INSERT, DELETE, and UPDATE) make. TCL allows the statements to be grouped together into logical transactions.

The main TCL commands are:

- **COMMIT**: It is used to save the transactions in the database. It marks the end of a successful transaction and makes the changes permanent .
- **ROLLBACK**: It is used to restore the database to that state which was last committed. It undoes the changes made by the transaction and cancels its effects .
- **SAVEPOINT**: It is used to create a point in the transaction where the changes done till that point will be unchanged and all the transactions after that point will be rolled back. It allows partial rollback of a transaction .
- **SET TRANSACTION**: It is used to specify the characteristics of the current transaction, such as isolation level, read-only or read-write mode, etc.

Here is an example of using TCL commands in SQL:

```sql
-- Begin a transaction
BEGIN;

-- Insert a record into the employee table
INSERT INTO employee (id, name, salary) VALUES (101, 'Alice', 5000);

-- Create a savepoint
SAVEPOINT sp1;

-- Update the salary of Alice
UPDATE employee SET salary = 6000 WHERE id = 101;

-- Rollback to the savepoint
ROLLBACK TO sp1;

-- Commit the transaction
COMMIT;
```

In this example, the transaction begins with the BEGIN command and ends with the COMMIT command. The INSERT statement is executed and saved in the database. The UPDATE statement is executed but not saved, because it is rolled back to the savepoint sp1. The savepoint sp1 preserves the state of the database after the INSERT statement. The final result is that the employee table has one record with id 101, name Alice, and salary 5000.