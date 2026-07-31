 Here is the content in markdown format without any emojis or external links and in formal tone:

### Transaction Control Commands

1. COMMIT - Finalizes all changes made by the current transaction. Releases any locks currently held by the transaction.
2. ROLLBACK - Undoes all changes made in the current transaction. Releases any locks currently held by the transaction.
3. SAVEPOINT identifier - Establishes a savepoint within the current transaction. The savepoint can be rolled back to later, undoing all changes made after the savepoint.
4. ROLLBACK TO SAVEPOINT identifier - Rolls back a transaction to the specified savepoint. All changes made after the savepoint are undone, but changes made before the savepoint remain pending.

The transaction control commands allow you to group SQL statements into transactions. A transaction is a unit of work that is guaranteed to be atomic, consistent, isolated, and durable (ACID). This allows you to logically group related changes to data and either commit all of the changes at once or rollback the entire transaction if an error occurs.

The notes are written in points and in a formal tone without any emojis or external links as per the given instructions. Let me know if you would like me to modify or expand the content in any way.