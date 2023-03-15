### Recovery from Transaction Failures

1. **Transaction failure** can occur due to various reasons such as hardware failure, software failure, or power failure.
2. **Recovery** is the process of restoring the database to a consistent state after a transaction failure.
3. **Atomicity** property of a transaction ensures that either all the changes made by a transaction are committed to the database or none at all.
4. **Write-ahead logging** is a common technique used for recovery where changes are first recorded in a log before being applied to the database.
5. **Checkpoints** are used to periodically write all changes from the log to the database to reduce the recovery time.
6. **Undo** and **Redo** operations are used to recover from transaction failures. Undo operation is used to roll back changes made by an uncommitted transaction, while Redo operation is used to reapply changes made by a committed transaction.
7. **Two-phase locking** is a concurrency control technique that ensures the consistency of the database by acquiring locks on data items before accessing them.
8. **Deadlocks** can occur when two or more transactions are waiting for each other to release locks. Deadlock detection and resolution techniques are used to handle deadlocks.
