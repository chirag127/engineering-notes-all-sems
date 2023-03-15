### Transaction Control Commands

Transaction control commands are used to manage the changes made by SQL statements in a database. A transaction is a logical unit of work that consists of one or more SQL statements that are executed as a whole. Transactions ensure the consistency and integrity of the data in the database by following the ACID properties: atomicity, consistency, isolation, and durability.

The main transaction control commands in SQL are:

- **COMMIT**: This command is used to make the changes made by a transaction permanent in the database. It ends the current transaction and saves the work done. It also releases any locks held by the transaction on the data.
- **ROLLBACK**: This command is used to undo the changes made by a transaction and restore the database to its previous state. It ends the current transaction and discards the work done. It also releases any locks held by the transaction on the data.
- **SAVEPOINT**: This command is used to create points within a transaction that can be used to roll back to a specific state in case of an error or failure. A savepoint is a name given to a point in the transaction. Multiple savepoints can be created within a transaction. To roll back to a savepoint, the ROLLBACK TO SAVEPOINT command is used.
- **SET TRANSACTION**: This command is used to specify the characteristics of the current transaction, such as its isolation level, read-only or read-write mode, and name. It must be the first statement of a transaction and can only be executed once per transaction.

Some examples of transaction control commands are:

```sql
-- Start a transaction
BEGIN TRANSACTION;

-- Insert a record into a table
INSERT INTO customers (id, name, email) VALUES (1, 'Alice', 'alice@example.com');

-- Create a savepoint
SAVEPOINT sp1;

-- Update a record in the table
UPDATE customers SET email = 'alice@gmail.com' WHERE id = 1;

-- Roll back to the savepoint
ROLLBACK TO SAVEPOINT sp1;

-- Commit the transaction
COMMIT;
```

```sql
-- Start a transaction with a name and isolation level
SET TRANSACTION NAME 'tran1' ISOLATION LEVEL SERIALIZABLE;

-- Delete a record from a table
DELETE FROM customers WHERE id = 1;

-- Roll back the transaction
ROLLBACK;
```