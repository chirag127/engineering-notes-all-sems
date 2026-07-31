### Log Based Recovery

Log based recovery is a technique used in database management systems to recover from failures and ensure the consistency and durability of transactions. It is a part of the transaction processing concept in database management systems.

Here are some key points to note about log based recovery:

1. Log based recovery uses a log file to record all changes made to the database during transactions. This log file is stored on a stable storage device, separate from the database itself.

2. In the event of a failure, the log file is used to recover the database to a consistent state. This is done by undoing or redoing the changes recorded in the log file, depending on the type of failure that occurred.

3. There are two main types of log based recovery: undo logging and redo logging. Undo logging is used to undo changes made by transactions that were not committed before the failure occurred. Redo logging is used to redo changes made by transactions that were committed before the failure occurred.

4. Log based recovery is an important part of ensuring the ACID properties of transactions. The ACID properties are Atomicity, Consistency, Isolation, and Durability. Log based recovery helps to ensure the consistency and durability of transactions.

5. Log based recovery is not the only technique used to recover from failures in database management systems. Other techniques include checkpointing and shadow paging.
