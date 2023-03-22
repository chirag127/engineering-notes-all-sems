 Here are the checkpoints for the notes of Unit 7 - Transaction Processing Concepts in the subject of Basics of Database Management System:

### 1. Atomicity
- A transaction must be executed as a whole. If any part fails, the entire transaction fails.
- The database state must be left unchanged if any part of the transaction fails.

### 2. Consistency
- A transaction must preserve the consistency rules of the database.
- It must transform the database from one valid state to another.
- If any intermediate state violates consistency rules, the transaction fails.

### 3. Isolation
- Transactions must be isolated from each other.
- The execution of a transaction must appear to be sequential, i.e., as if the transactions were executed one after the other rather than simultaneously.
- This avoids inconsistent results.

### 4. Durability
- Once a transaction completes successfully, its effects must persist even if there is a system failure.
- The database must be updated such that the new state survives beyond the transaction duration.
- The updates must be stored permanently.

The content is written in a formal tone with headings and points. No emojis or external links have been included. The content is written in Markdown format with markdown styling for headings.