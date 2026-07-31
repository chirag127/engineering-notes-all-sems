### Log Based Recovery in DBMS

- Log based recovery is a technique used in database management systems (DBMS) to recover a database to a consistent state in the event of a failure or crash.
- It involves the use of transaction logs, which are records of all the transactions performed on the database.
- A log record contains the following information  :
  - Transaction ID: A unique identifier for each transaction.
  - Operation: The type of operation performed by the transaction, such as read, write, commit, or abort.
  - Data Item: The name of the data item affected by the operation.
  - Old Value: The value of the data item before the operation.
  - New Value: The value of the data item after the operation.
- A log file is maintained in some stable storage device, such as a disk or a tape, so that it can be accessed even if the main memory is lost  .
- A log file is updated before the actual changes are made to the database, following the write-ahead logging (WAL) protocol  .
- Log based recovery can be classified into two types    :
  - Undo logging: This type of logging records the old values of the data items before they are modified by the transactions. It is used to undo the effects of the transactions that are not committed at the time of failure. It follows the undo-no-redo rule, which means that only the uncommitted transactions are rolled back and the committed transactions are not redone.
  - Redo logging: This type of logging records the new values of the data items after they are modified by the transactions. It is used to redo the effects of the transactions that are committed but not reflected in the database at the time of failure. It follows the no-undo-redo rule, which means that only the committed transactions are redone and the uncommitted transactions are not rolled back.