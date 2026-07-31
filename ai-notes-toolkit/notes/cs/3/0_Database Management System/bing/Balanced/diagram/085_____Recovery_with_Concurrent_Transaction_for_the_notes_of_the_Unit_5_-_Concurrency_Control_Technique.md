Recovery with Concurrent Transactions

- Recovery is the process of restoring the database to a consistent state after a failure or an abort.
- Concurrent transactions are transactions that execute simultaneously and access the same data items in the database.
- Recovery with concurrent transactions can be done in the following four ways:
  - Interaction with concurrency control
  - Transaction rollback
  - Checkpoints
  - Restart recovery

Interaction with concurrency control

- In this scheme, the recovery scheme depends greatly on the concurrency control scheme that is used.
- For example, if locking is used for concurrency control, then the recovery scheme must ensure that the locks are released after a transaction commits or aborts.
- Similarly, if timestamp ordering is used for concurrency control, then the recovery scheme must ensure that the timestamps are updated after a transaction commits or aborts.

Transaction rollback

- In this scheme, the recovery scheme uses the log records to undo the effects of an aborted transaction.
- The log records contain the information about the operations performed by the transactions, such as read, write, commit, and abort.
- The recovery scheme scans the log records in reverse order and restores the old values of the data items that were modified by the aborted transaction.
- This process is called undoing or rolling back the transaction.

Checkpoints

- In this scheme, the recovery scheme periodically performs a checkpoint operation, which records the current state of the database and the transactions in the log.
- A checkpoint operation consists of the following steps:
  - Write all modified buffer blocks to disk.
  - Write a <checkpoint> record to the log and flush it to disk.
  - Write all active transactions to the log and flush it to disk.
- A checkpoint operation reduces the amount of work that needs to be done during restart recovery, as it ensures that all the transactions that committed before the checkpoint are already reflected in the database.

Restart recovery

- In this scheme, the recovery scheme uses the log records to restore the database to a consistent state after a system failure.
- The recovery scheme scans the log records from the most recent checkpoint to the end of the log and performs the following actions:
  - For each <commit T> record, do nothing, as the transaction T has already committed and its effects are in the database.
  - For each <abort T> record, undo the transaction T by restoring the old values of the data items that were modified by T, using the log records.
  - For each transaction T that has neither a <commit T> nor an <abort T> record, undo the transaction T by restoring the old values of the data items that were modified by T, using the log records.
- This process is called redoing or rolling forward the transactions.