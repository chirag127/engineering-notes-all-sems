### Recovery in Concurrent Systems

Recovery in concurrent systems is the process of restoring the system to a consistent state after a failure, while preserving the effects of the committed transactions and discarding the effects of the aborted transactions. Recovery in concurrent systems is challenging because multiple transactions may be executing at the same time and their operations may be interleaved in the log. Therefore, the recovery system needs to use some techniques to ensure that the recovery is correct and efficient. Some of the techniques are:

- Interaction with concurrency control: The recovery system depends on the concurrency control system that is used to manage the concurrent transactions. For example, if the concurrency control system uses locking, then the recovery system needs to release the locks held by the aborted transactions and restore the data items to their previous values. If the concurrency control system uses timestamps, then the recovery system needs to check the timestamps of the data items and the transactions to determine which updates need to be undone or redone.

- Transaction rollback: The recovery system can rollback a failed transaction by using the log. The system scans the log backward from the point of failure, and for every log record found for the failed transaction, the system restores the data item to its previous value. This process is also called undoing the transaction.

- Checkpoints: Checkpoints are points in time when the system saves a snapshot of the current state of the system to a stable storage. Checkpoints reduce the amount of log records that the system needs to scan during recovery, because the system can start the recovery from the most recent checkpoint instead of the beginning of the log. Checkpoints also help to remove the log records that are no longer needed, because the updates of the committed transactions have been written to the stable storage. Checkpoints can be of different types, such as fuzzy checkpoints, where transactions are allowed to perform updates while the checkpoint is being taken, or consistent checkpoints, where the system ensures that no transaction is in progress during the checkpoint.

- Restart recovery: Restart recovery is the process of recovering the system after a crash. The system constructs two lists: the undo-list and the redo-list. The undo-list contains the transactions that need to be undone, and the redo-list contains the transactions that need to be redone. The system constructs the two lists as follows:

  - Initially, they are both empty.
  - The system scans the log backward, examining each record, until it finds the first <checkpoint> record.
  - For each <start T> record found before the <checkpoint> record, the system adds T to the undo-list.
  - For each <commit T> or <abort T> record found before the <checkpoint> record, the system removes T from the undo-list and adds T to the redo-list.
  - The system scans the log forward from the <checkpoint> record, examining each record.
  - For each <start T> record found after the <checkpoint> record, the system adds T to the undo-list.
  - For each <commit T> record found after the <checkpoint> record, the system removes T from the undo-list and adds T to the redo-list.
  - For each <abort T> record found after the <checkpoint> record, the system removes T from the undo-list.
  - The system performs the undo and redo operations according to the two lists. The system undoes the transactions in the reverse order of their start times, and redoes the transactions in the same order of their commit times. The system uses the log records to perform the undo and redo operations. For each <write T, X, old, new> record, the system restores X to old for undo, and to new for redo. For each <commit T> or <abort T> record, the system writes an <end T> record to the log.