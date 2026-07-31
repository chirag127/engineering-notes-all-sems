### Recovery from Transaction Failures

- A transaction failure is an event that causes a transaction to abort or terminate before completing all its operations on the database.
- A transaction failure can be caused by various reasons, such as user errors, system errors, concurrency control violations, deadlock detection, or disk failures.
- To recover from transaction failure, the atomicity and durability of transactions must be maintained. That is, either all the operations of a transaction are executed or none, and the effects of committed transactions are not lost due to failures.
- There are three states of database recovery in DBMS:
  - Consistent state: A state where the database satisfies all the integrity constraints and reflects a correct state of the real world.
  - Inconsistent state: A state where the database violates some integrity constraints or does not reflect a correct state of the real world.
  - Intermediate state: A state where the database is in the process of executing a transaction and has not reached a consistent or inconsistent state yet.
- There are two types of database recovery techniques in DBMS:
  - Deferred update: A technique where the changes made by a transaction are not written to the database until the transaction commits. This ensures that no undo operation is required in case of a failure, but a redo operation may be needed to restore the committed changes.
  - Immediate update: A technique where the changes made by a transaction are written to the database as soon as they occur, even before the transaction commits. This requires both undo and redo operations in case of a failure, to restore the database to a consistent state.
- To implement database recovery techniques, the DBMS uses the following components:
  - Log: A sequential file that records all the updates made by transactions on the database, along with the transaction identifiers, timestamps, and commit or abort flags.
  - Buffer: A memory area that temporarily stores the pages of the database that are being accessed or modified by transactions.
  - Checkpoint: A point in time when the DBMS writes all the modified pages from the buffer to the disk and records a checkpoint entry in the log. This reduces the amount of work needed for recovery in case of a failure.
  - Recovery manager: A module that is responsible for performing the recovery operations, such as undo and redo, based on the information in the log and the buffer.