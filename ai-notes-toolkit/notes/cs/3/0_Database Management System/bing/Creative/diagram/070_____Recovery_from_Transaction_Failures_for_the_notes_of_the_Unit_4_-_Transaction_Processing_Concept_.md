### Recovery from Transaction Failures

- A transaction failure is an event that causes a transaction to abort or terminate before completing all its operations on the database.
- Transaction failures can be caused by various reasons, such as logical errors, concurrency control violations, system crashes, or disk failures.
- To recover from transaction failures, the atomicity and durability properties of transactions must be ensured. That is, either all the effects of a transaction are reflected in the database, or none of them are.
- There are three states of database recovery in DBMS:
  - Consistent state: A state where the database satisfies all the integrity constraints and no transaction is in progress.
  - Inconsistent state: A state where the database may violate some integrity constraints due to an incomplete transaction.
  - Intermediate state: A state between the consistent and inconsistent states, where some operations of a transaction have been executed but not all.
- There are two main types of recovery techniques in DBMS:
  - Undo recovery technique: This technique is based on the principle of undoing or rolling back the effects of an aborted transaction. It uses a log file to keep track of the actions performed by each transaction, such as read, write, commit, or abort. The log file also records the old and new values of the data items modified by each transaction. To undo a transaction, the log file is scanned backwards and the old values of the data items are restored to the database.
  - Redo recovery technique: This technique is based on the principle of redoing or repeating the effects of a committed transaction. It also uses a log file to record the actions and values of each transaction. To redo a transaction, the log file is scanned forward and the new values of the data items are applied to the database.
- Depending on the type of failure, a combination of undo and redo techniques may be required to restore the database to a consistent state. For example, in case of a system crash, the transactions that were in progress at the time of the crash need to be undone, while the transactions that were committed before the crash need to be redone. This is known as undo/redo recovery technique.
- In a partitioned database environment, where the database is distributed across multiple servers, recovery from transaction failures may involve multiple servers that participated in the transaction. There are two types of recovery in this case:
  - Crash recovery: This occurs on the server where the failure occurred. The server is restarted and the log file is used to undo or redo the transactions as needed.
  - Coordination recovery: This occurs on the other servers that were involved in the transaction. The servers communicate with each other to determine the status of the transaction and decide whether to commit or abort it. This may require a two-phase commit protocol to ensure atomicity.