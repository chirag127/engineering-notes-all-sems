### Recovery from Transaction Failures

- A transaction failure is an event that causes a transaction to abort or terminate before completing all its operations.
- A transaction failure can be caused by various reasons, such as system crash, power failure, user error, deadlock, concurrency control violation, or integrity constraint violation.
- To recover from transaction failure, the atomicity and durability of transactions must be maintained. That is, either all the operations of a transaction are executed or none, and the effects of committed transactions are not lost due to failures.
- There are three states of database recovery in DBMS:
  - Consistent state: A state where the database satisfies all the integrity constraints and reflects a correct state of the real world.
  - Inconsistent state: A state where the database violates some integrity constraints or does not reflect a correct state of the real world.
  - Intermediate state: A state where the database is in the process of executing a transaction and has not reached a consistent or inconsistent state yet.
- There are two types of database recovery techniques in DBMS:
  - Deferred update: A technique where the changes made by a transaction are not written to the database until the transaction commits. This ensures that no undo operation is required in case of a failure, but a redo operation may be needed to restore the committed changes.
  - Immediate update: A technique where the changes made by a transaction are written to the database as soon as they occur, even before the transaction commits. This requires both undo and redo operations in case of a failure, to restore the database to a consistent state.
- To perform database recovery, the DBMS uses a recovery manager, which is a component that maintains a log of all the transactions and their operations. The log contains information such as transaction id, operation type, data item, old value, new value, commit record, and abort record.
- The recovery manager uses the log to perform the following steps:
  - Analysis: The recovery manager scans the log backward from the end and identifies the transactions that were active, committed, or aborted at the time of the failure.
  - Redo: The recovery manager scans the log forward from the beginning and reapplies all the operations of the committed transactions to ensure that their effects are reflected in the database.
  - Undo: The recovery manager scans the log backward from the end and reverses all the operations of the active or aborted transactions to ensure that their effects are removed from the database.