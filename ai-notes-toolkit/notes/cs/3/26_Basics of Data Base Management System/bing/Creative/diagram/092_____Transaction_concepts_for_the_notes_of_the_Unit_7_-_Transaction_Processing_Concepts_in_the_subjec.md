### Transaction concepts

A transaction is a logical unit of work that accesses and possibly modifies the data in a database. Transactions are executed by users or applications to perform some tasks on the database. Transactions have the following characteristics :

- A transaction is a **single unit of logic** or work, sometimes made up of multiple operations.
- A transaction is **indivisible**, meaning that it either executes all or none of its operations.
- A transaction is **independent** of other transactions, meaning that it does not interfere with or depend on the concurrent execution of other transactions.
- A transaction is **coherent and reliable**, meaning that it preserves the consistency and integrity of the database.

Transactions in a database environment have two main purposes:

- To provide a mechanism to **recover** from failures and errors, by restoring the database to a consistent state before the failure.
- To provide a mechanism to **isolate** the effects of concurrent transactions, by ensuring that each transaction sees a consistent view of the database.

Transactions are usually issued to the database system in a language like SQL wrapped in a transaction, using a pattern similar to the following:

1. Begin the transaction.
2. Execute a set of data manipulations and/or queries.
3. If no error occurs, then commit the transaction.
4. If an error occurs, then roll back the transaction.

To ensure the reliability and correctness of transactions, database systems follow the **ACID** properties, which are:

- **Atomicity**: The 'all or nothing' property. A transaction is an indivisible entity that is either performed in its entirety or not performed at all.
- **Consistency**: A transaction must alter the database from one steady-state to another steady state. This means that a transaction must not violate any integrity constraints or rules defined on the database.
- **Isolation**: Transactions must execute in isolation from each other, meaning that they do not see the intermediate or uncommitted results of other transactions. This ensures that the concurrent execution of transactions does not lead to inconsistency or anomalies in the database.
- **Durability**: The 'once and for all' property. A transaction that has been committed must remain so, even in the event of system failures or crashes. This means that the effects of a committed transaction must be permanently recorded in the database.

These are the basic concepts of transactions in database systems. Transactions are essential for ensuring the reliability, consistency, and correctness of data in a database. Transactions also enable concurrent access and manipulation of data by multiple users or applications without compromising the integrity of the database.