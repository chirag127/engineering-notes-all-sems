### Log Based Recovery in DBMS

- Log based recovery in DBMS is a technique used to recover a database to a consistent state in the event of a failure or crash.
- It involves the use of transaction logs, which are records of all the transactions performed on the database.
- A log record contains the following information  :
  - Transaction ID: A unique identifier for each transaction.
  - Operation: The type of operation performed by the transaction, such as read, write, commit, or abort.
  - Data Item: The name of the data item affected by the operation.
  - Old Value: The value of the data item before the operation.
  - New Value: The value of the data item after the operation.
- A log record can also have a start or end marker to indicate the beginning or the end of a transaction  .
- For example, a log record for a transaction T1 that updates the city of a customer from Chennai to NCR can be written as:

  `<T1, Start>`  
  `<T1, City, Chennai, NCR>`  
  `<T1, Commit>`

- Log based recovery in DBMS can be classified into two types  :
  - Undo Logging: This type of logging ensures that the database is restored to its state before the failure by undoing the effects of the transactions that did not commit.
  - Redo Logging: This type of logging ensures that the database is restored to its state after the failure by redoing the effects of the transactions that did commit.
- The choice of logging type depends on the recovery algorithm used by the DBMS, such as immediate update, deferred update, checkpointing, or shadow paging  .
- Log based recovery in DBMS provides the following advantages  :
  - It preserves the ACID properties of transactions, such as atomicity, consistency, isolation, and durability.
  - It minimizes the data loss and inconsistency caused by failures or crashes.
  - It reduces the need for frequent backups and restores of the database.
  - It improves the performance and availability of the database.