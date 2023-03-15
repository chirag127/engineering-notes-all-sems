### Transaction concepts

A transaction is a logical unit of work that accesses and possibly modifies the data in a database. A transaction has the following properties :

- **Atomicity**: A transaction is either completed in its entirety or not at all. If any error occurs during the execution of a transaction, the database is restored to its original state before the transaction began.
- **Consistency**: A transaction must preserve the integrity constraints of the database. A transaction can only bring the database from one consistent state to another consistent state.
- **Isolation**: A transaction must not interfere with other concurrent transactions. The intermediate results of a transaction are not visible to other transactions until the transaction is committed.
- **Durability**: The effects of a committed transaction are permanent and must not be lost due to system failures.

A transaction can be executed using a simple pattern like the following:

1. Begin the transaction.
2. Execute a set of data manipulations and/or queries.
3. If no error occurs, then commit the transaction.
4. If an error occurs, then roll back the transaction.

A transaction can be controlled by using the following commands:

- **BEGIN TRANSACTION**: This command marks the beginning of a transaction.
- **COMMIT**: This command saves the changes made by the transaction and ends the transaction.
- **ROLLBACK**: This command discards the changes made by the transaction and restores the database to its previous state before the transaction began.

Some examples of transactions in a database are:

- Transferring money from one account to another account in a banking system.
- Booking a flight ticket and a hotel room in a travel system.
- Updating the inventory and the sales records in a retail system.