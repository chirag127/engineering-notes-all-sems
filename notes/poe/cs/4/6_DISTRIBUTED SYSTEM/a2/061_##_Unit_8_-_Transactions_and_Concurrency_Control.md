 Here is the content in markdown format for Unit 8 - Transactions and Concurrency Control:

## Unit 8 - Transactions and Concurrency Control

Transactions and concurrency control are crucial concepts in database management systems to ensure data integrity and consistency.

### Transactions

- A transaction is a logical unit of work that contains one or more SQL statements.
- A transaction must satisfy the ACID properties:
- Atomicity: Either all statements succeed or all fail.
- Consistency: Data is consistent before and after transaction.
- Isolation: Transactions are isolated from each other.
- Durability: Changes are permanent after commit.
- Types:
- Short transactions: Simple queries, inserts, updates, deletes.
- Long transactions: Complex operations, multiple statements.

#### Commit and Rollback

- Commit: Successful transaction changes are applied permanently to the database.
- Rollback: If any error occurs, all changes are undone, restoring original state.

#### Isolation Levels (prevent lost updates)

- Read uncommitted: Allows dirty reads.
- Read committed: Reads only committed data (solves dirty reads).
- Repeatable read: Reads same data for entire transaction (solves non-repeatable reads).
- Serializable: Strict isolation but low concurrency.

### Concurrency Control

- Ensures correct execution of transactions when running concurrently.
- Problems: Lost updates, uncommitted dependency, inconsistent analysis.
- Methods: Locking, timestamp ordering, optimistic concurrency control.
- Locking: Exclusive lock - only one transaction can access data. Prevent lost updates but low concurrency.
- Timestamp ordering: Transactions get timestamp and access data if timestamp is less than data timestamp.
- Optimistic concurrency control: Transactions assume no conflicts and validate at commit. If data changed, roll back and retry. Higher concurrency but chance of rollbacks.

[Additional details and diagrams can be added here to supplement the points and make the content more comprehensible.]