```markdown
### Transaction Control Commands

- Transaction Control Language (TCL) is a subset of SQL that is used to manage transactions in a database.
- A transaction is a logical unit of work that consists of one or more SQL statements that are executed as a single unit.
- Transactions ensure the consistency and integrity of the database by following the ACID properties: Atomicity, Consistency, Isolation, and Durability.
- The following commands are used to control transactions in SQL:

  - **COMMIT**: This command is used to make a transaction permanent in the database. It saves the changes made by the transaction and ends the current transaction.  
  - **ROLLBACK**: This command is used to undo the changes made by the transaction and restore the database to its previous state. It aborts the current transaction and ends it.  
  - **SAVEPOINT**: This command is used to create points within a transaction that can be used to roll back to a specific state. It allows partial rollback of a transaction.  
  - **SET TRANSACTION**: This command is used to specify the characteristics of the current transaction, such as isolation level, read-only or read-write access, and name. 

- SQL Server operates in the following transaction modes: 

  - **Autocommit transactions**: Each individual statement is a transaction. It is committed or rolled back automatically depending on whether it succeeds or fails.
  - **Explicit transactions**: Each transaction is explicitly started with the `BEGIN TRANSACTION` statement and explicitly ended with a `COMMIT` or `ROLLBACK` statement. 
  - **Implicit transactions**: A new transaction is implicitly started after the previous transaction is committed or rolled back. The `SET IMPLICIT_TRANSACTIONS ON` statement enables this mode.

- Example of using transaction control commands in SQL:

  ```sql
  -- Start an explicit transaction
  BEGIN TRANSACTION;

  -- Insert a new record into the Customers table
  INSERT INTO Customers (CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country)
  VALUES (92, 'Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway');

  -- Create a savepoint within the transaction
  SAVEPOINT SP1;

  -- Update the record with CustomerID = 92
  UPDATE Customers
  SET ContactName = 'Tommy B. Erichsen'
  WHERE CustomerID = 92;

  -- Roll back to the savepoint
  ROLLBACK TO SP1;

  -- Commit the transaction
  COMMIT;
  ```
```