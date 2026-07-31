# Transaction Control Language (TCL) Statements

- Transaction Control Language (TCL) is a type of SQL command that is used to manage transactions in a database  .
- Transactions are a way of grouping multiple SQL statements into a single unit of work, so that either all of the statements are executed, or none of them are .
- TCL allows you to organise statements into logical transactions, keep track of the modifications that DML statements make, and save or undo the changes to the database  .
- The main TCL commands are:
  - **COMMIT**: It is used to save the transactions in the database and end the current transaction  . After the commit is performed, the database state is changed from one to another consistent state.
  - **ROLLBACK**: It is used to restore the database to the last committed state or to a specified savepoint  . It undoes the changes made by the DML statements in the current transaction.
  - **BEGIN**: It is used to start a new transaction explicitly  . It is optional in some database systems, as a transaction can be implicitly started by a DML statement.
  - **SAVEPOINT**: It is used to create a named point in the transaction that can be used as a reference for rollback  . It allows you to partially undo the changes made by the DML statements in the current transaction.
- An example of using TCL commands is:

```sql
-- Start a new transaction
BEGIN;
-- Insert a new record into the employee table
INSERT INTO employee (id, name, salary) VALUES (101, 'Alice', 5000);
-- Create a savepoint named SP1
SAVEPOINT SP1;
-- Update the salary of Alice
UPDATE employee SET salary = 6000 WHERE id = 101;
-- Rollback to the savepoint SP1
ROLLBACK TO SP1;
-- Commit the transaction
COMMIT;
```

- In this example, the insert statement is executed and saved to the database, but the update statement is undone by the rollback to the savepoint SP1. The final state of the database is consistent with the commit statement.