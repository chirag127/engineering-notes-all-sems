### Transaction concepts

- A **transaction** is an action or series of actions that are performed by a single user or application program, which reads or updates the contents of the database.
- A transaction can be defined as a **logical unit of work** on the database.
- A transaction generally represents **any change** in a database.
- Transactions in a database environment have two main purposes:
  - To provide reliable units of work that allow correct recovery from failures and keep a database consistent even in cases of system failure.
  - To provide isolation between programs accessing a database concurrently.
- A transaction has four properties, known as **ACID**:
  - **Atomicity**: The 'all or nothing' property. A transaction is an indivisible entity that is either performed in its entirety or not performed at all.
  - **Consistency**: A transaction must alter the database from one steady-state to another steady state. This means that the database must satisfy all the integrity constraints before and after the transaction.
  - **Isolation**: Transactions must execute in isolation from each other, as if they were executed serially. This means that the intermediate results of a transaction are not visible to other transactions, and vice versa.
  - **Durability**: The effects of a committed transaction must persist in the database even in the event of system failures. This means that the changes made by a transaction are permanent and cannot be undone.