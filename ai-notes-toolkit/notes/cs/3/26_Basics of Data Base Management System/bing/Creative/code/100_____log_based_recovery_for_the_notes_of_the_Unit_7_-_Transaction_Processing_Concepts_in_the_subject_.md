### Log Based Recovery in DBMS

Log based recovery is a technique used in database management systems (DBMS) to recover a database to a consistent state in the event of a failure or crash. It involves the use of transaction logs, which are records of all the transactions performed on the database.

Some key points about log based recovery are:

- A log is a sequence of records that is maintained in a stable storage device to note down all the changes made by transactions in a sequential manner.
- A log record contains the transaction id, the operation, the data item, and the old and new values of the data item.
- A log record can also indicate the start, commit, or abort of a transaction.
- A log record is written to the stable storage before the actual change is made to the database. This is called the write-ahead logging (WAL) protocol.
- The log can be used to undo or redo the effects of transactions in case of a failure.
- There are two types of log based recovery methods: deferred update and immediate update.
- In deferred update, no changes are made to the database until the transaction commits. Only the log records are written before the commit. After the commit, the log records are used to update the database.
- In immediate update, changes are made to the database as soon as the transaction executes. The log records are also written before the changes. In case of a failure, the log records are used to undo or redo the changes depending on whether the transaction has committed or not.
- Log based recovery ensures the atomicity and durability properties of transactions.