# Recovery with Concurrent Transactions

- Recovery with concurrent transactions is the process of restoring the database to a consistent state after a failure, while allowing multiple transactions to execute simultaneously.
- Recovery with concurrent transactions can be done in the following four ways:
  - Interaction with concurrency control
  - Transaction rollback
  - Checkpoints
  - Restart recovery

## Interaction with concurrency control

- In this scheme, the recovery scheme depends greatly on the concurrency control scheme that is used.
- For example, if the concurrency control scheme is based on locking, then the recovery scheme must ensure that the locks are released properly after a failure, and that the transactions that were waiting for the locks are notified.
- Similarly, if the concurrency control scheme is based on timestamps, then the recovery scheme must ensure that the timestamps are assigned correctly after a failure, and that the transactions that were aborted due to timestamp conflicts are restarted.

## Transaction rollback

- In this scheme, the recovery scheme uses the log records to undo the effects of the transactions that were not committed before the failure.
- The recovery scheme scans the log records in reverse order, from the most recent to the oldest, and applies the undo operation for each log record that belongs to an uncommitted transaction.
- The undo operation restores the previous value of the data item that was modified by the transaction, and writes a new log record to indicate the undo operation.
- The recovery scheme stops when it reaches the oldest log record, or when it encounters a log record that belongs to a committed transaction.

## Checkpoints

- In this scheme, the recovery scheme periodically performs a checkpoint operation, which is a special log record that marks a point in time when the database is in a consistent state.
- The checkpoint operation flushes all the modified data pages from the buffer to the disk, and writes a checkpoint log record to the log file.
- The checkpoint log record contains the list of transactions that were active at the time of the checkpoint, and the list of transactions that were committed since the last checkpoint.
- The checkpoint operation reduces the amount of work that the recovery scheme has to do after a failure, as it only has to scan the log records from the most recent checkpoint to the end of the log file.

## Restart recovery

- In this scheme, the recovery scheme uses the checkpoint log records to perform the restart recovery after a failure.
- The restart recovery consists of two phases: analysis and redo/undo.
- In the analysis phase, the recovery scheme scans the log records from the most recent checkpoint to the end of the log file, and identifies the transactions that were active, committed, or aborted at the time of the failure.
- In the redo/undo phase, the recovery scheme performs the redo operation for the transactions that were committed, and the undo operation for the transactions that were active or aborted.
- The redo operation re-applies the effects of the transactions that were committed, and writes a new log record to indicate the redo operation.
- The undo operation reverses the effects of the transactions that were active or aborted, and writes a new log record to indicate the undo operation.