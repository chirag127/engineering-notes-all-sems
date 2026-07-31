# Log Based Recovery in DBMS

- Log based recovery in DBMS is a technique used to recover a database to a consistent state in the event of a failure or crash.
- It involves the use of transaction logs, which are records of all the transactions performed on the database.
- A transaction log contains the following information  :
  - The transaction identifier (Tn)
  - The type of operation (read, write, commit, abort, etc.)
  - The data item name and value before and after the operation
  - The timestamp of the operation
- A log file is created for every operation performed on the database and stored in a stable storage device .
- The log file is used to restore the database to a consistent state by applying the undo and redo operations .
- Undo operations are used to roll back the changes made by uncommitted transactions .
- Redo operations are used to reapply the changes made by committed transactions that may not have been reflected in the database due to the failure .
- There are two types of log based recovery techniques :
  - Deferred update technique: In this technique, the changes made by a transaction are not written to the database until the transaction commits. Only the log file is updated during the execution of the transaction. This technique avoids the need for undo operations, but requires redo operations for committed transactions.
  - Immediate update technique: In this technique, the changes made by a transaction are written to the database as soon as they occur, even before the transaction commits. Both the log file and the database are updated during the execution of the transaction. This technique requires both undo and redo operations for uncommitted and committed transactions, respectively.