### Transaction Control Commands

- Transaction Control Language (TCL) is a subset of SQL that is used to manage transactions in a database.
- A transaction is a logical unit of work that consists of one or more SQL statements that are executed as a single unit.
- Transactions ensure the consistency and integrity of the database by following the ACID properties: Atomicity, Consistency, Isolation, and Durability.
- The following commands are used to control transactions in SQL  :

  - **COMMIT**: This command is used to make a transaction permanent in the database. It saves the changes made by the transaction and ends the current transaction.
  - **ROLLBACK**: This command is used to undo the changes made by the transaction and restore the database to its previous state. It aborts the current transaction and discards any changes made since the last commit or savepoint.
  - **SAVEPOINT**: This command is used to create points within a transaction in which to rollback. It allows partial rollback of a transaction by specifying a name for a savepoint. Multiple savepoints can be created within a transaction.
  - **SET TRANSACTION**: This command is used to name a transaction or specify its characteristics, such as isolation level, read-only or read-write access, etc. It must be the first statement of a transaction.

- SQL Server operates in the following transaction modes:

  - **Autocommit transactions**: Each individual statement is a transaction. It is committed automatically when it completes successfully or rolled back if it fails.
  - **Explicit transactions**: Each transaction is explicitly started with the `BEGIN TRANSACTION` statement and explicitly ended with a `COMMIT` or `ROLLBACK` statement. The `BEGIN TRANSACTION` statement can also specify a name for the transaction or indicate that it is a distributed transaction.
  - **Implicit transactions**: A transaction is implicitly started when the previous transaction completes, and it is implicitly committed or rolled back when the connection is closed or a `COMMIT` or `ROLLBACK` statement is executed. This mode can be enabled by setting the `IMPLICIT_TRANSACTIONS` option to `ON`.

- Here is an example of using transaction control commands in SQL:

  ```sql
  -- Start an explicit transaction
  BEGIN TRANSACTION UpdateSalary;

  -- Update the salary of an employee
  UPDATE Employees
  SET Salary = Salary * 1.1
  WHERE EmployeeID = 101;

  -- Create a savepoint within the transaction
  SAVEPOINT SalaryUpdated;

  -- Update the bonus of the same employee
  UPDATE Employees
  SET Bonus = Bonus + 1000
  WHERE EmployeeID = 101;

  -- Rollback to the savepoint
  ROLLBACK TRANSACTION SalaryUpdated;

  -- Commit the transaction
  COMMIT TRANSACTION UpdateSalary;
  ```