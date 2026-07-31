### Transaction Control Commands

Transaction control commands are used to manage the changes made by SQL statements in a database. A transaction is a logical unit of work that consists of one or more SQL statements that are executed as a whole. Transactions ensure the consistency and integrity of the data in a database by following the ACID properties: atomicity, consistency, isolation, and durability.

The main transaction control commands in SQL are:

- **COMMIT**: This command is used to make the changes made by a transaction permanent in the database. It ends the current transaction and saves the work done. It also releases any locks held by the transaction on the data.
- **ROLLBACK**: This command is used to undo the changes made by a transaction and restore the database to its previous state. It ends the current transaction and discards the work done. It also releases any locks held by the transaction on the data.
- **SAVEPOINT**: This command is used to create points within a transaction where the changes can be rolled back to without affecting the entire transaction. It allows partial undo of the work done by a transaction. It does not end the current transaction or release any locks.
- **SET TRANSACTION**: This command is used to specify the characteristics of the current transaction, such as its isolation level, name, or read-only status. It must be the first statement of a transaction and can only be executed once per transaction.

Some examples of transaction control commands are:

```sql
-- Start a transaction
BEGIN TRANSACTION;

-- Insert a record into a table
INSERT INTO customers (id, name, email) VALUES (1, 'Alice', 'alice@example.com');

-- Create a savepoint
SAVEPOINT sp1;

-- Update the record
UPDATE customers SET email = 'alice@gmail.com' WHERE id = 1;

-- Rollback to the savepoint
ROLLBACK TO sp1;

-- Commit the transaction
COMMIT;
```

```sql
-- Start a transaction with a name and isolation level
SET TRANSACTION NAME 'tran1' ISOLATION LEVEL SERIALIZABLE;

-- Delete a record from a table
DELETE FROM customers WHERE id = 1;

-- Rollback the transaction
ROLLBACK tran1;
```