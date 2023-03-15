### Recovery with Concurrent Transactions in DBMS

Recovery with concurrent transactions is the process of restoring the database to a consistent state after a failure that involves two or more transactions. The main challenges of recovery with concurrent transactions are:

- How to deal with the interleaving of logs from different transactions.
- How to ensure that the atomicity and durability properties of transactions are preserved.
- How to minimize the amount of work that needs to be redone or undone during recovery.

There are four main techniques for recovery with concurrent transactions:

- Interaction with concurrency control: This technique relies on the concurrency control scheme that is used to prevent or resolve conflicts among concurrent transactions. For example, if locking is used, then the recovery system can use the lock table to identify the transactions that were active at the time of failure and roll them back. If timestamp ordering is used, then the recovery system can use the timestamps to determine the order of operations and undo or redo them accordingly.
- Transaction rollback: This technique allows a transaction to abort and undo its effects in case of a failure or a conflict. The recovery system can use the log records to undo the operations of a transaction in the reverse order of their execution. The undo operation restores the previous value of a data item that was modified by the transaction. The recovery system also deletes the log records of the aborted transaction to free up space.
- Checkpoints: This technique reduces the amount of work that needs to be done during recovery by periodically saving the state of the database and the transactions. A checkpoint is a special log record that marks a point in time when the database is consistent and all the transactions have either committed or aborted. The recovery system can use the checkpoint to determine the starting point of recovery and ignore the log records before the checkpoint. The recovery system only needs to redo the operations of the committed transactions and undo the operations of the active transactions after the checkpoint.
- Restart recovery: This technique handles the case when the system crashes during the recovery process. The recovery system can use a restart record to indicate the beginning of a recovery process. The restart record contains information about the transactions that were active, committed, or aborted at the time of the crash. The recovery system can use the restart record to resume the recovery process from where it left off.
