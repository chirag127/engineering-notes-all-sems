### Log Based Recovery in DBMS

- Log based recovery is a technique used in database management systems (DBMS) to recover a database to a consistent state in the event of a failure or crash.
- It involves the use of transaction logs, which are records of all the transactions performed on the database.
- A transaction log contains the following information for each transaction  :
  - Transaction ID: a unique identifier for the transaction
  - Operation: the type of operation performed by the transaction, such as read, write, commit, abort, etc.
  - Data item: the name of the data item affected by the operation
  - Old value: the value of the data item before the operation
  - New value: the value of the data item after the operation
- A log file is maintained in some stable storage device, such as a disk or a tape, so that it can be accessed even if the main memory is lost  .
- The process of storing the logs should be done before the actual changes are made to the database, to ensure that the logs reflect the correct sequence of operations.
- Log based recovery can be classified into two types: undo logging and redo logging.
  - Undo logging: this type of logging records the old values of the data items before the changes are made by the transactions. It is used to undo the effects of the transactions that are not committed at the time of failure, by restoring the old values to the database.
  - Redo logging: this type of logging records the new values of the data items after the changes are made by the transactions. It is used to redo the effects of the transactions that are committed at the time of failure, by applying the new values to the database.
- Log based recovery can also be combined to form undo/redo logging, which records both the old and the new values of the data items. It is used to undo the effects of the uncommitted transactions and redo the effects of the committed transactions at the time of failure.
- Log based recovery can be implemented using various algorithms, such as immediate update, deferred update, checkpointing, fuzzy checkpointing, etc. These algorithms differ in the way they write the logs and the changes to the database, and the way they handle the recovery process.