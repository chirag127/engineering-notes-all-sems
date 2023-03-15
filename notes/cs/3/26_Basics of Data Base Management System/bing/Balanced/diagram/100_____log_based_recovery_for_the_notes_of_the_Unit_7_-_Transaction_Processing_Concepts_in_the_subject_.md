### Log Based Recovery in DBMS

- Log based recovery is a technique used in database management systems (DBMS) to recover a database to a consistent state in the event of a failure or crash.
- It involves the use of transaction logs, which are records of all the transactions performed on the database.
- A log file will be created for every operation performed on the database at that point.
- A log record contains the following information:
  - Transaction ID: A unique identifier for each transaction.
  - Operation: The type of operation performed by the transaction, such as read, write, commit, or abort.
  - Data Item: The name of the data item affected by the operation.
  - Old Value: The value of the data item before the operation.
  - New Value: The value of the data item after the operation.
- Log records are stored in a stable storage device, such as a disk or a tape, that can survive system failures.
- Log records are used to recover the database by applying two techniques:
  - Undo: This technique restores the old value of a data item that was modified by an uncommitted transaction.
  - Redo: This technique restores the new value of a data item that was modified by a committed transaction.
- Log based recovery can be classified into two types:
  - Deferred Update: This type of recovery delays the actual update of the database until the transaction commits. It only requires redo operations to recover the database.
  - Immediate Update: This type of recovery allows the update of the database before the transaction commits. It requires both undo and redo operations to recover the database.