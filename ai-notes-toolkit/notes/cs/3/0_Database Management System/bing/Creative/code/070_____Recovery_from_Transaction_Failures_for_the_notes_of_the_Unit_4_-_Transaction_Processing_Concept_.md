### Recovery from Transaction Failures

- A transaction failure is an event that causes a transaction to abort or terminate before completing all its operations on the database.
- A transaction failure can be caused by various reasons, such as user errors, system errors, concurrency control violations, or hardware failures.
- To recover from transaction failure, the atomicity and durability of transactions as a whole must be maintained. That is, either all the operations are executed or none, and the effects of committed transactions are not lost due to failures.
- There are three states of database recovery in DBMS:
  - Consistent state: A state where the database satisfies all the integrity constraints and reflects a correct state of the real world.
  - Inconsistent state: A state where the database violates some integrity constraints or does not reflect a correct state of the real world.
  - Intermediate state: A state where the database is in the process of executing a transaction and has not reached a consistent or inconsistent state yet.
- There are two types of database recovery techniques in DBMS:
  - Deferred update: A technique where the changes made by a transaction are not written to the database until the transaction commits. This ensures that no undo operation is required in case of a failure, but a redo operation may be needed to restore the committed changes.
  - Immediate update: A technique where the changes made by a transaction are written to the database as soon as they occur, even before the transaction commits. This requires both undo and redo operations in case of a failure, to restore the database to a consistent state.
- To perform database recovery, the DBMS needs to keep track of the states and actions of all the transactions, which can be done by using the following:
  - Transaction log: A file that records all the updates and operations performed by the transactions on the database, along with the transaction identifiers, timestamps, and commit or abort flags.
  - Checkpoints: A point in time where the DBMS writes all the modified pages from the buffer to the disk and records a checkpoint entry in the log. This reduces the amount of work needed for recovery in case of a failure.
  - Backup: A copy of the database that is periodically taken and stored on a secondary storage device. This can be used to restore the database in case of a catastrophic failure that damages the primary storage device.