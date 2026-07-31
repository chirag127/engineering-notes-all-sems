### Log Based Recovery

Log based recovery is a technique used in transaction processing systems to ensure the atomicity and durability of transactions. It is a part of the recovery subsystem of a database management system.

Here are some key points to remember about log based recovery:

1. A log is a sequence of records that describes all the changes made to the database.
2. Each log record contains information about a single operation of a transaction, such as the old value and the new value of the data item being modified.
3. The log is stored on a stable storage device, such as a hard disk, to ensure that it is not lost in the event of a system failure.
4. In the event of a system failure, the recovery subsystem uses the log to undo the changes made by incomplete transactions and to redo the changes made by committed transactions.
5. There are two main types of log based recovery: undo logging and redo logging.
6. Undo logging, also known as rollback logging, is used to undo the changes made by incomplete transactions.
7. Redo logging, also known as rollforward logging, is used to redo the changes made by committed transactions.
8. Some systems use a combination of undo and redo logging, known as undo/redo logging, to provide more flexibility in the recovery process.
