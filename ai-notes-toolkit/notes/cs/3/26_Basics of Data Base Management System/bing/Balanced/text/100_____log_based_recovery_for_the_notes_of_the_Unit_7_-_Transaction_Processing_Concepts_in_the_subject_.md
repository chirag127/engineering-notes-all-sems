### Log Based Recovery in DBMS

- Log based recovery is a technique used in DBMS to recover a database to a consistent state in the event of a failure or crash.
- It involves the use of transaction logs, which are records of all the transactions performed on the database.
- A log record contains the following information  :
  - Transaction ID: a unique identifier for each transaction
  - Operation: the type of operation performed by the transaction, such as read, write, commit, abort, etc.
  - Data item: the name of the data item affected by the operation
  - Old value: the value of the data item before the operation
  - New value: the value of the data item after the operation
- A log record is written to a stable storage device before the actual operation is performed on the database. This is called write-ahead logging (WAL) principle.
- A log record is also written when a transaction starts or ends  . For example, <T1, Start> indicates that transaction T1 has started, and <T1, Commit> indicates that transaction T1 has committed.
- Log based recovery can be classified into two types:
  - Undo logging: this type of logging ensures that all the changes made by an uncommitted transaction are undone in case of a failure. It uses the old values stored in the log records to restore the database to its previous state.
  - Redo logging: this type of logging ensures that all the changes made by a committed transaction are redone in case of a failure. It uses the new values stored in the log records to reapply the operations on the database.
- Log based recovery can also use a combination of undo and redo logging, depending on the type of failure and the state of the transactions.
- Log based recovery requires the use of checkpoints, which are points in time when the database and the log are synchronized. A checkpoint record is written to the log to indicate that all the transactions before the checkpoint have committed and their changes have been written to the database. Checkpoints reduce the amount of work required for recovery by limiting the number of log records that need to be scanned.