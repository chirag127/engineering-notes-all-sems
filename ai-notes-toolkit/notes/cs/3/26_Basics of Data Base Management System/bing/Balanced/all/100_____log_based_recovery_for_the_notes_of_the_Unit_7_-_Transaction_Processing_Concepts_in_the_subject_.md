# Log Based Recovery in DBMS

- Log based recovery in DBMS is a technique to restore the database to a consistent state after a failure or crash.
- It uses a log file, which is a sequence of records that store the details of every transaction performed on the database.
- The log file is maintained in a stable storage device, such as a disk or a tape, that can survive a system failure.
- The log file contains the following information for each transaction:
  - Transaction ID: A unique identifier for the transaction.
  - Operation: The type of operation performed by the transaction, such as read, write, commit, or abort.
  - Data Item: The name of the data item affected by the operation.
  - Old Value: The value of the data item before the operation.
  - New Value: The value of the data item after the operation.
- The log file can be used to recover the database in two ways:
  - Undo: This method is used to undo the effects of incomplete or aborted transactions that may have left the database in an inconsistent state. It involves scanning the log file backwards from the end and restoring the old values of the data items that were modified by the transactions.
  - Redo: This method is used to redo the effects of committed transactions that may have not been reflected in the database due to a failure. It involves scanning the log file forwards from the beginning and applying the new values of the data items that were modified by the transactions.
- The log file can also be used to support concurrency control and recovery protocols, such as two-phase locking and two-phase commit, that ensure the atomicity and durability of transactions.