### Recovery from Transaction Failures

- A transaction failure is an event that causes a transaction to abort or terminate before completing all its operations on the database.
- A transaction failure can be caused by various reasons, such as user errors, system errors, concurrency control violations, or hardware failures.
- To recover from transaction failures, the database management system (DBMS) must ensure the atomicity and durability of transactions, which are two of the ACID properties of transactions.
- Atomicity means that either all the operations of a transaction are executed or none. Durability means that the effects of a committed transaction are permanent and not lost due to any failure.
- There are three main techniques for recovery from transaction failures in DBMS: logging, checkpointing, and shadow paging.

#### Logging

- Logging is a technique that records the changes made by transactions to the database in a separate file called the log or the journal.
- The log contains information such as the transaction id, the operation performed, the old value and the new value of the data item, and the commit or abort status of the transaction.
- The log is used to undo or redo the operations of transactions in case of a failure, depending on whether the transaction was committed or aborted before the failure.
- There are two types of logging: undo logging and redo logging.
- Undo logging is a technique that uses the log to undo the effects of uncommitted transactions after a failure. It restores the old values of the data items that were modified by the uncommitted transactions.
- Redo logging is a technique that uses the log to redo the effects of committed transactions after a failure. It applies the new values of the data items that were modified by the committed transactions.
- A combination of undo and redo logging is also possible, which is called undo/redo logging.

#### Checkpointing

- Checkpointing is a technique that periodically writes the contents of the main memory buffers to the disk, and records a special entry called the checkpoint in the log.
- The checkpoint entry indicates the point in time when the DBMS was in a consistent state, and all the transactions before the checkpoint were committed and their effects were written to the disk.
- The checkpointing technique reduces the amount of work that the DBMS has to do for recovery after a failure, as it only has to consider the transactions that occurred after the checkpoint.
- There are two types of checkpointing: fuzzy checkpointing and synchronous checkpointing.
- Fuzzy checkpointing is a technique that allows the DBMS to continue processing transactions while performing the checkpointing operation. It does not require the DBMS to flush all the buffers to the disk at once, but rather in batches.
- Synchronous checkpointing is a technique that requires the DBMS to stop processing transactions while performing the checkpointing operation. It ensures that all the buffers are flushed to the disk at once, and no transaction is active during the checkpoint.

#### Shadow Paging

- Shadow paging is a technique that uses a separate file or page table to keep track of the changes made by transactions to the database.
- The shadow page table contains the addresses of the original pages of the database, which are not modified by the transactions. The current page table contains the addresses of the modified pages of the database, which are stored in a different location on the disk.
- The shadow page table is never updated by the transactions, but only by the DBMS when a transaction commits. The current page table is updated by the transactions as they modify the database.
- The shadow paging technique does not require logging or checkpointing, as it can recover from a failure by simply discarding the current page table and using the shadow page table to access the database.
- However, the shadow paging technique has some disadvantages, such as the overhead of maintaining two page tables, the difficulty of handling concurrent transactions, and the waste of disk space due to the duplication of pages.