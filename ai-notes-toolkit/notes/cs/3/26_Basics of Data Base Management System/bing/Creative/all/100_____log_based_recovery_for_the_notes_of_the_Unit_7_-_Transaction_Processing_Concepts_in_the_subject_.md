# Log Based Recovery in DBMS

- Log based recovery in DBMS is a technique used to recover a database to a consistent state in the event of a failure or crash.
- It involves the use of transaction logs, which are records of all the transactions performed on the database.
- A transaction log contains the following information  :
  - The transaction identifier (Tn)
  - The type of operation (read, write, delete, etc.)
  - The data item affected by the operation
  - The old value and the new value of the data item
  - The start and the end of the transaction
- For example, a transaction log for a transaction T1 that updates the city of a customer from Chennai to NCR can be written as follows:
  - <T1, Start>
  - <T1, City, 'Chennai', 'NCR'>
  - <T1, Commit>
- The log is maintained in some stable storage device, such as a disk, so that it can be accessed even after a failure   .
- The log is used to restore the database to a consistent state by applying one of the following methods    :
  - Undo: This method undoes the effects of the transactions that were not committed before the failure. It restores the old values of the data items from the log.
  - Redo: This method redoes the effects of the transactions that were committed before the failure. It applies the new values of the data items from the log.
  - Undo/Redo: This method combines both undo and redo methods. It undoes the effects of the transactions that were not committed and redoes the effects of the transactions that were committed before the failure.
- The choice of the recovery method depends on the type of failure and the checkpoint mechanism used by the DBMS    .
- A checkpoint is a point in time when the DBMS writes all the modified pages of the database to the disk and records the information about the active transactions in the log    .
- A checkpoint helps to reduce the amount of work needed for recovery by limiting the scope of the transactions that need to be undone or redone    .
- The following table summarizes the recovery methods and the conditions for applying them    :

| Recovery Method | Condition |
| --------------- | --------- |
| Undo | The transaction has not committed and has not reached the checkpoint |
| Redo | The transaction has committed and has reached the checkpoint |
| Undo/Redo | The transaction has committed but has not reached the checkpoint |

- Log based recovery in DBMS ensures the atomicity and durability properties of transactions    .
- Atomicity means that either all the operations of a transaction are executed or none of them are executed    .
- Durability means that the effects of a committed transaction are permanent and do not get lost due to a failure    .