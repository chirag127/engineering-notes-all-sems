### Recovery with Concurrent Transactions

Recovery with concurrent transactions is the process of restoring the database to a consistent state after a failure, while ensuring the ACID properties of the transactions. Recovery with concurrent transactions can be done in the following four ways:

- **Interaction with concurrency control**: In this scheme, the recovery scheme depends greatly on the concurrency control scheme that is used. For example, if strict two-phase locking is used, then no transaction can commit until all its locks are released, and no transaction can read a value that is updated by an uncommitted transaction. This ensures that the log records of a transaction are written before its commit record, and that the undo and redo operations are performed in the correct order.
- **Transaction rollback**: In this scheme, a transaction that fails or aborts is rolled back by undoing its effects on the database. This is done by using the log records of the transaction, which contain the old and new values of the data items that it updated. The undo operation restores the old values of the data items, and the redo operation restores the new values of the data items. The rollback can be done in two ways: backward recovery and forward recovery. In backward recovery, the undo operations are performed in the reverse order of the transaction, starting from the last log record. In forward recovery, the redo operations are performed in the same order of the transaction, starting from the first log record.
- **Checkpoints**: In this scheme, a checkpoint is a point in time when the database is in a consistent state, and all the log records of the committed transactions are written to the disk. A checkpoint is performed periodically by the DBMS to reduce the amount of work that needs to be done during recovery. A checkpoint involves the following steps: 
  - The DBMS writes a <START CKPT> record to the log, listing the active transactions at that point.
  - The DBMS forces all the log records in the buffer to the disk.
  - The DBMS forces all the modified data pages in the buffer to the disk.
  - The DBMS writes an <END CKPT> record to the log.
- **Restart recovery**: In this scheme, the DBMS uses the checkpoints and the log records to recover the database after a failure. The restart recovery involves the following steps:
  - The DBMS scans the log backward from the end until it finds the most recent <START CKPT> record. It identifies the active transactions at that point, and adds them to a list of transactions to be undone.
  - The DBMS scans the log forward from the most recent <START CKPT> record until the end. For each log record, it performs the following actions:
    - If the log record is a <COMMIT T> record, where T is a transaction, then it removes T from the list of transactions to be undone, and adds T to a list of transactions to be redone.
    - If the log record is an <UPDATE T, X, old, new> record, where T is a transaction, X is a data item, old is the old value of X, and new is the new value of X, then it performs the following actions:
      - If T is in the list of transactions to be undone, then it performs an undo operation by restoring the old value of X in the database, and writing an <UNDO T, X, old, new> record to the log.
      - If T is in the list of transactions to be redone, then it performs a redo operation by restoring the new value of X in the database, and writing a <REDO T, X, old, new> record to the log.
  - The DBMS forces all the log records and the modified data pages to the disk.
  - The DBMS scans the log forward from the end, and for each transaction T in the list of transactions to be undone, it writes an <ABORT T> record to the log.