# Transaction Concepts

A transaction is a logical unit of work that accesses and possibly modifies the data in a database. Transactions are executed by users or applications to perform some tasks on the database. Transactions have the following characteristics:

- A transaction is a **single unit of logic** or work, that is either performed in its entirety or not at all .
- A transaction is **independent** of other transactions, meaning that its execution does not interfere with or depend on the execution of other transactions.
- A transaction is **coherent and reliable**, meaning that it preserves the consistency and integrity of the database .
- A transaction can be **committed** or **aborted**. Committing a transaction means that the changes made by the transaction are permanently saved in the database. Aborting a transaction means that the changes made by the transaction are discarded and the database is restored to its previous state .

A transaction can be executed using a language like SQL wrapped in a transaction, using a pattern similar to the following:

1. Begin the transaction.
2. Execute a set of data manipulations and/or queries.
3. If no error occurs, then commit the transaction.
4. If an error occurs, then roll back the transaction.

A transaction must satisfy the **ACID** properties, which are as follows:

- **Atomicity**: The 'all or nothing' property. A transaction is an indivisible entity that is either performed in its entirety or not at all. If any part of the transaction fails, the whole transaction is aborted and the database is left unchanged.
- **Consistency**: A transaction must alter the database from one steady-state to another steady state. This means that the transaction must obey the rules and constraints defined by the database schema, such as data types, primary keys, foreign keys, etc. The transaction must not leave the database in an inconsistent or invalid state.
- **Isolation**: Transactions must appear to execute in isolation from each other, meaning that the concurrent execution of multiple transactions does not affect their outcomes. Each transaction must operate on a consistent snapshot of the database, as if no other transactions were running at the same time.
- **Durability**: The changes made by a committed transaction must persist in the database, even in the event of system failures, power outages, crashes, etc. The database system must ensure that the committed data is safely stored and can be recovered when needed.

These properties are essential for ensuring the correctness and reliability of transactions and the database system.