### Log Based Recovery in DBMS

- Log based recovery is a technique used in DBMS to recover a database to a consistent state in the event of a failure or crash.
- It involves the use of transaction logs, which are records of all the transactions performed on the database.
- A log record contains the following information  :
  - Transaction ID: a unique identifier for each transaction
  - Operation: the type of operation performed by the transaction, such as read, write, commit, or abort
  - Data item: the name of the data item affected by the operation
  - Old value: the value of the data item before the operation
  - New value: the value of the data item after the operation
- A log record can also have a start or end marker to indicate the beginning or the end of a transaction  .
- For example, a log record for a transaction T1 that updates the city of a customer from Chennai to NCR can be written as:

  <T1, Start>
  <T1, City, Chennai, NCR>
  <T1, Commit>

- Log based recovery can be classified into two types  :
  - Undo logging: also known as rollback or backward recovery, it restores the database to its state before the failure by undoing the effects of the transactions that did not commit
  - Redo logging: also known as rollforward or forward recovery, it restores the database to its state after the failure by redoing the effects of the transactions that did commit
- The choice of undo or redo logging depends on the recovery point objective (RPO) and the recovery time objective (RTO) of the database.
  - RPO is the maximum amount of data loss that can be tolerated in the event of a failure
  - RTO is the maximum amount of time that can be taken to restore the database to a consistent state after a failure
- Undo logging requires less RPO but more RTO, while redo logging requires more RPO but less RTO.
- Log based recovery can be implemented in SQL Server using the following steps:
  - Enable the full recovery model for the database, which ensures that all the transactions are logged
  - Perform regular backups of the database and the transaction log
  - In case of a failure, restore the database from the most recent backup
  - Apply the transaction log backups to the restored database, either in undo or redo mode, depending on the RPO and RTO requirements
  - Verify the consistency and integrity of the database