### Log Based Recovery in DBMS

- Log based recovery is a technique used in database management systems (DBMS) to recover a database to a consistent state in the event of a failure or crash.
- It involves the use of transaction logs, which are records of all the transactions performed on the database.
- A log record contains the following information  :
  - Transaction ID: A unique identifier for each transaction.
  - Operation: The type of operation performed by the transaction, such as read, write, commit, or abort.
  - Data item: The name of the data item affected by the operation.
  - Old value: The value of the data item before the operation.
  - New value: The value of the data item after the operation.
- A log file is maintained in a stable storage device, such as a disk or a tape, that is not affected by the failure  .
- The log file is updated before the actual changes are made to the database, to ensure that the log reflects the latest state of the database  .
- The log file is used to recover the database in two scenarios  :
  - Undo: If a transaction is aborted or fails before committing, then the log file is used to undo the changes made by the transaction and restore the database to its previous state. This is done by applying the inverse operations of the transaction in the reverse order of the log records.
  - Redo: If a transaction is committed but the changes are not reflected in the database due to a failure, then the log file is used to redo the changes made by the transaction and bring the database to its committed state. This is done by applying the same operations of the transaction in the same order of the log records.
- Log based recovery ensures the atomicity and durability properties of transactions, which are essential for maintaining the consistency and integrity of the database.