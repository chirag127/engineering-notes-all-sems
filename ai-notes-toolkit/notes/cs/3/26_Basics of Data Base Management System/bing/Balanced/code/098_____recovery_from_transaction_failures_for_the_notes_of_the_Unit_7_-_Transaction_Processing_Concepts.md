### Recovery from transaction failures in DBMS

- A transaction failure is an event that causes a transaction to abort or terminate before it can commit its changes to the database.
- A transaction failure can be caused by various reasons, such as system errors, user errors, concurrency conflicts, or integrity violations.
- A transaction failure can affect the consistency and integrity of the database, as it may leave the database in an inconsistent state or violate some constraints or rules.
- To recover from a transaction failure, the DBMS must ensure that the effects of the failed transaction are undone or rolled back, and that the database is restored to a consistent state.
- There are mainly two types of recovery techniques used in DBMS: rollback/undo recovery and compensation/redo recovery.
- Rollback/undo recovery technique is based on the principle of backing out or undoing the effects of a transaction that has not completed successfully due to a system failure or error.
- Rollback/undo recovery technique requires the DBMS to keep a log of all the operations performed by each transaction, along with the old and new values of the data items affected by the operations.
- Rollback/undo recovery technique uses the log to undo the operations of the failed transaction in the reverse order, restoring the old values of the data items and releasing any locks held by the transaction.
- Compensation/redo recovery technique is based on the principle of repeating or redoing the effects of a transaction that has committed successfully but whose changes have not been written to the disk due to a system failure or error.
- Compensation/redo recovery technique requires the DBMS to keep a log of all the operations performed by each transaction, along with the new values of the data items affected by the operations.
- Compensation/redo recovery technique uses the log to redo the operations of the committed transaction in the same order, applying the new values of the data items and acquiring any locks needed by the transaction.
- In a partitioned database environment, where the database is distributed across multiple servers or partitions, a transaction failure can affect more than one partition.
- In this case, the DBMS must perform crash recovery on the failed partition, and transaction recovery on the other partitions involved in the transaction.
- Crash recovery is the process of restarting the database manager on the failed partition and restoring the database to a consistent state.
- Transaction recovery is the process of ensuring the atomicity and durability of the transactions that were executing on the other partitions when the failure occurred.
- Transaction recovery can involve either rollback/undo or compensation/redo techniques, depending on the state of the transaction at the time of the failure.
- If the transaction was not committed, the DBMS must roll back the transaction on all the partitions.
- If the transaction was committed, the DBMS must redo the transaction on the failed partition and ensure that the changes are written to the disk.