# Transaction Control Commands

- Transaction Control Language (TCL) is a subset of SQL that is used to manage transactions in a database.
- A transaction is a logical unit of work that consists of one or more SQL statements that are executed as a single unit.
- Transactions ensure the consistency and integrity of the database by following the ACID properties: Atomicity, Consistency, Isolation, and Durability.
- The following commands are used to control transactions in SQL:

  - **COMMIT**: This command is used to make a transaction permanent in a database. It saves the changes made by the transaction and ends the current transaction.
  - **ROLLBACK**: This command is used to undo the changes made by the transaction and restore the database to its previous state. It aborts the current transaction and discards any changes made since the last commit or savepoint.
  - **SAVEPOINT**: This command is used to create points within a transaction in which to rollback. It allows partial rollback of a transaction by specifying a name for a savepoint. Multiple savepoints can be created within a transaction.
  - **SET TRANSACTION**: This command is used to specify the characteristics of the current transaction, such as isolation level, read-only or read-write access, and name.

- SQL Server operates in the following transaction modes:

  - **Autocommit transactions**: Each individual statement is a transaction. The changes made by the statement are committed or rolled back automatically depending on whether the statement succeeds or fails.
  - **Explicit transactions**: Each transaction is explicitly started with the `BEGIN TRANSACTION` statement and explicitly ended with a `COMMIT` or `ROLLBACK` statement. The changes made by the transaction are not permanent until a `COMMIT` statement is executed.
  - **Implicit transactions**: A new transaction is implicitly started when the previous transaction is completed. The `SET IMPLICIT_TRANSACTIONS ON` statement enables this mode. The changes made by the transaction are not permanent until a `COMMIT` statement is executed.

- Examples of transaction control commands in SQL:

  - To start an explicit transaction and commit it:

    ```sql
    BEGIN TRANSACTION;
    -- SQL statements
    COMMIT TRANSACTION;
    ```

  - To start an explicit transaction and rollback it:

    ```sql
    BEGIN TRANSACTION;
    -- SQL statements
    ROLLBACK TRANSACTION;
    ```

  - To create a savepoint within a transaction and rollback to it:

    ```sql
    BEGIN TRANSACTION;
    -- SQL statements
    SAVEPOINT savepoint_name;
    -- SQL statements
    ROLLBACK TRANSACTION savepoint_name;
    -- SQL statements
    COMMIT TRANSACTION;
    ```

  - To set the isolation level of a transaction to serializable:

    ```sql
    SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
    BEGIN TRANSACTION;
    -- SQL statements
    COMMIT TRANSACTION;
    ```