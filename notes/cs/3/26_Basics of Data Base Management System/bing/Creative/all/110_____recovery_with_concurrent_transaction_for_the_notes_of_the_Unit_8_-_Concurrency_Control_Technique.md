# Recovery with Concurrent Transaction

Recovery with concurrent transaction is the process of restoring the database to a consistent state after a failure that involves multiple transactions. Recovery with concurrent transaction is important to ensure the ACID properties of transactions, especially atomicity and durability.

Recovery with concurrent transaction can be done in the following four ways:

- Interaction with concurrency control: In this scheme, the recovery scheme depends greatly on the concurrency control scheme that is used. For example, if strict two-phase locking is used, then no transaction can commit until all its locks are released. This ensures that no transaction can be affected by the rollback of another transaction. If timestamp ordering is used, then no transaction can read or write a data item that has been written by a younger transaction. This ensures that no transaction can be affected by the abort of another transaction.
- Transaction rollback: In this scheme, the recovery system can undo the effects of a transaction by using the log records. For example, if a transaction T writes a new value V to a data item X, then the log record will contain the old value W of X. The recovery system can use this log record to restore X to W and undo the write operation of T. Transaction rollback can be done for a single transaction or for a group of transactions that are dependent on each other.
- Checkpoints: In this scheme, the recovery system periodically performs a checkpoint operation, which is a special log record that marks a point in time when the database is in a consistent state. A checkpoint operation involves the following steps  :

  - The DBMS stops accepting new transactions and waits for the active transactions to finish their current operations.
  - The DBMS forces all the modified buffers in the main memory to be written to the disk.
  - The DBMS writes a checkpoint record to the log file and forces the log file to be written to the disk.
  - The DBMS resumes accepting new transactions.

  A checkpoint operation reduces the amount of work that the recovery system has to do in case of a failure. The recovery system only has to consider the transactions that were active after the last checkpoint.
- Restart recovery: In this scheme, the recovery system uses the log records and the checkpoint records to restore the database to a consistent state after a failure. Restart recovery involves the following steps  :

  - The recovery system scans the log file backwards from the end until it reaches the most recent checkpoint record. This is called the analysis phase, where the recovery system identifies the transactions that were active, committed, or aborted at the time of the failure.
  - The recovery system scans the log file forwards from the most recent checkpoint record until the end. This is called the redo phase, where the recovery system redoes all the operations of the committed transactions to ensure that their effects are reflected in the database.
  - The recovery system scans the log file backwards from the end until the most recent checkpoint record. This is called the undo phase, where the recovery system undoes all the operations of the active or aborted transactions to ensure that their effects are removed from the database.

  Restart recovery ensures that the database is restored to the most recent consistent state before the failure.