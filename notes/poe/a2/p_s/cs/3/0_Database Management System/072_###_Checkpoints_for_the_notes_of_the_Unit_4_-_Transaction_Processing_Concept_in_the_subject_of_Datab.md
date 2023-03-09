 Here are the checkpoints for the notes of Unit 4 - Transaction Processing Concept in Database Management System:

### 1. Concept of Transaction
- A transaction is a logical unit of work that is atomic, consistent, isolated and durable (ACID)
- It is a sequence of database operations that transforms the database from one consistent state to another
- Either all operations of a transaction are executed successfully or none
- If any operation fails, the entire transaction is rolled back (undo operation) to restore the original state

### 2. Transaction States
- A transaction goes through different states - active, partially committed, committed, failed, aborted
- A transaction starts in active state, moves to partially committed state after commit operation, committed state after log record write, failed state if error occurs, aborted state if rolled back

### 3. Transaction Management
- Transaction management ensures that database transactions are executed reliably
- It consists of concurrency control, recovery management and scheduling
- Concurrency control - maintains data consistency while multiple transactions access database concurrently
- Recovery management - ensures that committed transactions are not undone and aborted transactions are rolled back in case of failure
- Scheduling - determines the order in which transactions are processed by DBMS

[You can include additional points, diagrams, examples, etc. here as per the instructions]