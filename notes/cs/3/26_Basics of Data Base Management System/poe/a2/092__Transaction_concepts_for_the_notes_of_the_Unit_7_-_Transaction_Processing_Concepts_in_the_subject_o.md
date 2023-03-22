 Here is the formal content in Markdown format without any emoji or external links on the given topic:

### Transaction concepts

1. Transaction: A transaction is a logical unit of work that contains one or more SQL statements. A transaction starts with its first executable statement and ends with a COMMIT or ROLLBACK statement.
2. ACID properties: Transactions exhibit four key properties:

Atomicity: Either all operations in a transaction succeed or all fail.
Consistency: A transaction never leaves the database in a half-finished state. If a transaction completes successfully, the database moves from one consistent state to another.
Isolation: Transactions execute independently and do not interfere with each other.
Durability: Once a transaction completes successfully, its effects persist even in the event of a system failure.

3. Commits and rollbacks: A COMMIT statement finalizes all changes made by the transaction and releases any locks it holds. A ROLLBACK statement undoes all changes made by the transaction since the last COMMIT and releases any locks the transaction holds.
4. Locks: To maintain isolation, transactions may place locks on database objects like tables to prevent other transactions from modifying them until the transaction completes its work.
5. Schedules: The order in which transactions' individual statements are executed is called a schedule. Correct schedules must ensure that transactions meet ACID properties.
6. Recoverability: A database is recoverable if it can regain a consistent state after a failure, even if some transactions were in progress at the time of the failure. Full recoverability requires that transactions be atomic, consistent, and durable.