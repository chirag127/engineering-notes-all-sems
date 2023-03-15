### Recoverability

- Recoverability is the property of a schedule that ensures that the database state is consistent after a transaction failure or system crash .
- A schedule is recoverable if it does not contain any dirty read, which is when a transaction reads a data item that is written by another uncommitted transaction .
- A schedule is irrecoverable if it contains a dirty read and the transaction that performs the dirty read commits before the transaction that writes the data item commits or aborts .
- A schedule is cascading abort if it contains a dirty read and the transaction that performs the dirty read aborts, causing the transaction that writes the data item to abort as well.
- A schedule is strict if it does not allow any transaction to read or write a data item until the transaction that last wrote the data item commits or aborts.
- A schedule is rigorous if it does not allow any transaction to read or write a data item until the transaction that first wrote the data item commits or aborts.
- Strict and rigorous schedules are recoverable and avoid cascading aborts, but they may reduce concurrency and performance.
- Recoverability is important for online transaction processing (OLTP) systems, which handle a large number of short and concurrent transactions that access and modify the database.
- Recoverability is achieved by using recovery techniques, such as logging, checkpointing, shadow paging, and locking .
- Recovery techniques ensure that the database can be restored to a consistent state after a transaction failure or system crash, by undoing the effects of uncommitted transactions and redoing the effects of committed transactions .