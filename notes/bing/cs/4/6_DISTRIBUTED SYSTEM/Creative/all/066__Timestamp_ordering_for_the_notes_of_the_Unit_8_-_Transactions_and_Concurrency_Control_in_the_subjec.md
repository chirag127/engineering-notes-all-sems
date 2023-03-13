### Timestamp ordering for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- Timestamp ordering is a technique to ensure serializability of transactions in a distributed system by assigning a unique identifier to each transaction based on the logical or physical time of its start.
- Timestamp ordering can be implemented using two approaches: basic timestamp ordering and optimistic timestamp ordering.
- Basic timestamp ordering assigns a timestamp to each transaction when it starts and uses it to order the read and write operations on each data item. If a transaction tries to read or write a data item that has a newer timestamp, it is aborted and restarted with a new timestamp. This ensures that transactions are executed in a chronological order and no conflicts occur.
- Optimistic timestamp ordering assumes that conflicts are rare and allows transactions to execute without any synchronization until they commit. At commit time, each transaction is validated by checking if its read set and write set are consistent with the timestamps of the data items. If a transaction passes the validation, it is assigned a commit timestamp and its write operations are applied to the database. If a transaction fails the validation, it is aborted and restarted with a new timestamp.
- Timestamp ordering has some advantages and disadvantages compared to other concurrency control techniques, such as locking and multiversion concurrency control. Some of the advantages are:
  - Timestamp ordering does not require any locking or deadlock detection, which reduces the overhead and complexity of the system.
  - Timestamp ordering preserves the temporal order of transactions, which is useful for applications that require causality or consistency of events.
  - Timestamp ordering can handle long-running transactions and read-only transactions efficiently, as they do not cause any conflicts or aborts.
- Some of the disadvantages are:
  - Timestamp ordering may cause unnecessary aborts and restarts of transactions, especially if the system is highly concurrent or the timestamps are not synchronized well.
  - Timestamp ordering may not guarantee the isolation level of transactions, as some anomalies such as dirty reads, non-repeatable reads, and phantom reads may still occur.
  - Timestamp ordering may not support some advanced features such as nested transactions, savepoints, or partial rollbacks, as they require more complex timestamp management.

- Here is a mnemonic to remember the basic timestamp ordering protocol:

  - **B**efore **R**eading or **W**riting, **C**heck the **T**imestamps
  - **B**asic **T**imestamp **O**rdering: **B**R**W**C**T**O