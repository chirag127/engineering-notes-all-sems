### Recovery from transaction failures

- Transaction failures are situations where a transaction cannot complete its execution due to various reasons, such as network failures, deadlock, or errors in application logic.
- Transaction failures can compromise the consistency and integrity of the database, as they may leave the database in an intermediate or inconsistent state.
- Recovery from transaction failures is the process of restoring the database to a consistent state after such failures, by undoing or redoing the effects of the failed transactions.
- Recovery from transaction failures is based on the following concepts:
  - Atomicity: A transaction is either executed in its entirety or not at all.
  - Durability: The effects of a committed transaction are permanent and survive any system failure.
  - Logging: A transaction log is a record of all the changes made by a transaction to the database. It contains information such as transaction ID, operation type, data item, old value, and new value.
  - Checkpoints: A checkpoint is a point in time when the database and the transaction log are synchronized, i.e., all the changes made by the committed transactions are written to the database. Checkpoints reduce the amount of work needed for recovery.
- There are two major techniques for recovery from non-catastrophic transaction failures:
  - Deferred update: This technique does not physically update the database on disk until a transaction has reached its commit point. It only records the changes in the transaction log. If a transaction fails before its commit point, no recovery action is needed, as the database is not affected. If a transaction commits, the recovery manager reads the transaction log and applies the changes to the database (redoing).
  - Immediate update: This technique allows the database to be updated on disk before a transaction reaches its commit point. However, it also records the changes in the transaction log. If a transaction fails before its commit point, the recovery manager reads the transaction log and restores the original values of the data items that were modified by the transaction (undoing). If a transaction commits, the recovery manager ensures that all the changes made by the transaction are written to the database (redoing).
- Recovery from catastrophic transaction failures is the process of restoring the database from a backup copy after a system failure that causes the loss of the entire database or a significant part of it.
- Recovery from catastrophic transaction failures is based on the following steps:
  - Restore a previous copy of the database from archival backup.
  - Apply the transaction log to the copy to reconstruct a more current state of the database by redoing the committed transaction operations up to the failure point.
  - Undo the effects of any uncommitted transactions that were in progress at the time of the failure.