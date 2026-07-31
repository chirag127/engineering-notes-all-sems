### Recovery from Transaction Failures

1. **Transaction failure** can occur due to various reasons such as hardware failure, software failure, power failure, or network failure.
2. **Recovery** is the process of restoring the database to a consistent state after a transaction failure.
3. **Atomicity** property of a transaction ensures that either all the changes made by a transaction are committed to the database or none at all.
4. **Write-ahead logging** is a common technique used for recovery where changes are first recorded in a log before being applied to the database.
5. **Checkpoints** are used to periodically write the log and database changes to disk to reduce the amount of work needed for recovery.
6. **Undo** and **Redo** operations are used to rollback or reapply changes to the database during recovery.
7. **Two-phase locking** is used to ensure that transactions do not interfere with each other during recovery.
