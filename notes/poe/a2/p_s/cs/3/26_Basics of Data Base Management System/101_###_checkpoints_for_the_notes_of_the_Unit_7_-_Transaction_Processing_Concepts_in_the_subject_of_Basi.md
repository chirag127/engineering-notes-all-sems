 Here are the checkpoints for the notes of Unit 7 - Transaction Processing Concepts in the subject of Basics of Data Base Management System:

### 1. Transactions
- A transaction is a logical unit of work that accesses and possibly modifies the contents of a database.
- Transactions execute as a single unit, either fully completing or fully aborting.
- Atomicity property: Either all steps of a transaction are executed or none are.
- Consistency property: A transaction moves the database from one consistent state to another.
- Isolation property: Transactions execute independently and concurrently without interference.
- Durability property: Once a transaction commits, its effects persist even if there is a system failure.

### 2. Transaction Processing
- Transaction processing ensures that the database remains in a consistent state despite system failures or concurrent transactions.
- The main steps in transaction processing are:
1. Begin transaction
2. Read/write data
3. Commit transaction (make changes permanent) or abort transaction (roll back to initial state)

### 3. Concurrency Control
- Concurrency control allows multiple transactions to execute simultaneously while maintaining database consistency.
- Two common approaches:
1. Locking: Prevent access to data that is locked by another transaction. Can lead to deadlocks.
2. Optimistic concurrency control: Transactions work on the assumption that there will be no conflicts, then check for conflicts before committing and resolving any conflicts that are detected.

### 4. Recovery Manager
- The recovery manager is responsible for undoing the partial effects of aborted transactions and recovering from system failures.
- Uses log records and rollback segments to restore the database to a consistent state in the event of a failure or transaction abort.

[Other points and diagrams can be added here as needed.]