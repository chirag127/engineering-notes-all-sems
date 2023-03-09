 Here is the content in markdown format for the given topic:

### Case Study of Oracle for the notes of the Unit 5 - Concurrency Control Techniques in the subject of Database Management System

Oracle uses the following concurrency control techniques:

1. Locking: Oracle uses row-level locking and table-level locking to prevent dirty reads and inconsistent reads.
- Row-level locking: When a transaction updates a row, it obtains an exclusive lock on that row. This prevents other transactions from reading or updating the same row.
- Table-level locking: When a transaction performs bulk operations like dropping a table, it obtains an exclusive lock on the entire table. This prevents other transactions from performing any operations on the table.

2. Multi-version concurrency control (MVCC): Oracle uses a variation of MVCC called SNAPSHOT ISOLATION. It provides read consistency without requiring read locks. Each transaction sees a consistent snapshot of the database as of the time the transaction started.

Advantages:
- Allows high concurrency as it avoids read locks.
- Provides isolation between reads and writes.

Disadvantages:
- Requires additional storage to maintain multiple versions of data.
- Complex to implement.

3. Serializability: Oracle guarantees serializable execution of transactions using a technique called conflict resolution. If two transactions conflict, Oracle rolls back one of the transactions to resolve the conflict and maintain serializability.

Applications:
- Used in banking systems to process multiple transactions concurrently while maintaining consistency.
- Used in airline reservation systems to book multiple seats concurrently.

[Diagrams and examples can be added here to illustrate the concepts]