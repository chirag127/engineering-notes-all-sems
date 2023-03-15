### Log-Based Recovery

Log-based recovery is a technique used in transaction processing systems to ensure the durability and consistency of data in the event of a system failure. This is achieved by maintaining a log of all changes made to the database, which can be used to recover the database to a consistent state in the event of a failure.

Here are some key points to remember about log-based recovery:

1. The log is a sequential record of all changes made to the database, including the old and new values of the data, as well as the transaction that made the change.
2. The log is stored on a stable storage device, such as a hard disk, to ensure that it is not lost in the event of a system failure.
3. In the event of a system failure, the log is used to recover the database to a consistent state by undoing or redoing transactions as necessary.
4. There are two main approaches to log-based recovery: undo logging and redo logging.
5. Undo logging involves recording enough information in the log to undo any changes made by a transaction in the event of a failure.
6. Redo logging involves recording enough information in the log to redo any changes made by a transaction in the event of a failure.
7. Both undo and redo logging can be used in combination to provide more flexible and efficient recovery.
