# Transaction Concepts

A transaction is a logical unit of work that accesses and possibly modifies the data in a database. A transaction has the following properties :

- **Atomicity**: A transaction is either performed in its entirety or not performed at all. If any error occurs during the execution of a transaction, the database is restored to its original state as if the transaction never happened.
- **Consistency**: A transaction must preserve the integrity constraints and business rules of the database. A transaction can only bring the database from one consistent state to another consistent state.
- **Isolation**: A transaction must not interfere with other concurrent transactions. The intermediate results of a transaction are not visible to other transactions until the transaction is committed.
- **Durability**: The effects of a committed transaction are permanent and must not be lost due to system failures or power outages.

A transaction can be executed using a simple pattern like the following:

1. Begin the transaction.
2. Execute a set of data manipulations and/or queries.
3. If no error occurs, then commit the transaction.
4. If an error occurs, then roll back the transaction.

A transaction can be classified into different types based on its characteristics, such as:

- **Read-only transaction**: A transaction that only reads data from the database and does not modify it.
- **Read-write transaction**: A transaction that reads and writes data to the database.
- **Flat transaction**: A transaction that has a single entry and exit point and does not contain any nested transactions.
- **Nested transaction**: A transaction that contains one or more sub-transactions within it, each with its own commit and rollback operations.
- **Distributed transaction**: A transaction that spans multiple database systems or network nodes and requires coordination among them.