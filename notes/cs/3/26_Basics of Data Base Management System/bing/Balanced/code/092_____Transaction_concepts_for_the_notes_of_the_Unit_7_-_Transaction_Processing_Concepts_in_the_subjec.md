### Transaction concepts

A transaction is a logical unit of work that accesses and possibly modifies the data in a database. Transactions are executed by users or applications to perform some tasks on the database. Transactions have the following characteristics:

- A transaction is a **single unit of logic** or work, that is either performed in its entirety or not at all .
- A transaction is **independent** of other transactions, meaning that its execution does not interfere with or depend on other transactions.
- A transaction is **coherent** and **reliable**, meaning that it preserves the consistency and integrity of the database.
- A transaction can be **committed** or **rolled back**, meaning that its effects are either made permanent or undone in the database .

Transactions in a database environment have two main purposes:

- To provide a **correct and consistent** view of the data to each user or application, regardless of concurrent access or system failures.
- To provide a **mechanism** for recovering from failures and maintaining the database in a consistent state.

Transactions are governed by the **ACID** properties, which are:

- **Atomicity**: The 'all or nothing' property. A transaction is an indivisible entity that is either performed in its entirety or not at all. If any part of the transaction fails, the whole transaction is aborted and the database is restored to its previous state.
- **Consistency**: A transaction must alter the database from one steady-state to another steady state. This means that the transaction must obey all the integrity constraints and business rules of the database, and not leave the database in an inconsistent or invalid state.
- **Isolation**: Transactions are executed in isolation from each other, meaning that their intermediate results are not visible to other transactions. This ensures that concurrent transactions do not interfere with each other and produce incorrect results.
- **Durability**: The 'once and for all' property. Once a transaction is committed, its effects are permanent and cannot be lost, even in the event of a system failure or power outage. The database system must ensure that the committed data is written to a non-volatile storage and can be recovered if needed.