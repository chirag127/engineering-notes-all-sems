### Log Based Recovery

Log based recovery is a technique used in database management systems to recover from failures and ensure the consistency and durability of transactions. Here are some key points to remember about log based recovery:

1. A log is a sequence of records that records all changes made to the database.
2. Each log record contains information about the transaction that made the change, the data item that was changed, and the before and after values of the data item.
3. The log is stored on stable storage, such as a disk, to ensure that it is not lost in the event of a failure.
4. In the event of a failure, the log is used to undo any changes made by incomplete transactions and redo any changes made by committed transactions.
5. There are two main types of log based recovery: undo logging and redo logging.
6. Undo logging, also known as write-ahead logging, records changes to the database before they are made. In the event of a failure, the log is used to undo any changes made by incomplete transactions.
7. Redo logging, on the other hand, records changes to the database after they are made. In the event of a failure, the log is used to redo any changes made by committed transactions.
8. Both undo and redo logging can be combined to create a more robust recovery mechanism.
