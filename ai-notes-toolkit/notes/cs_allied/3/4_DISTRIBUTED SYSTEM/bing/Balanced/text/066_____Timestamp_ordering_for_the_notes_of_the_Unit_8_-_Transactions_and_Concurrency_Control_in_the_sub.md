### Timestamp ordering

- Timestamp ordering is a technique for ensuring serializability of transactions in a distributed system.
- A timestamp is a unique identifier assigned to each transaction that reflects its start time or priority.
- Timestamp ordering enforces a partial order on the transactions based on their timestamps, such that conflicting operations are executed in timestamp order.
- Timestamp ordering can be implemented in two ways: basic timestamp ordering and optimistic timestamp ordering.

#### Basic timestamp ordering

- Basic timestamp ordering assigns a timestamp to each transaction when it starts, and uses these timestamps to order the conflicting operations.
- Each data item has two timestamp fields: read timestamp (RTS) and write timestamp (WTS), which record the largest timestamp of any transaction that has read or written the item, respectively.
- A transaction can read an item if its timestamp is greater than or equal to the item's WTS, and can write an item if its timestamp is greater than both the item's RTS and WTS.
- If a transaction cannot read or write an item, it is aborted and restarted with a new timestamp.
- Basic timestamp ordering ensures serializability, but it may cause unnecessary aborts and restarts, and it does not guarantee freedom from deadlock.

#### Optimistic timestamp ordering

- Optimistic timestamp ordering is a variation of basic timestamp ordering that allows transactions to execute optimistically without checking timestamps, and validates them at commit time.
- Each transaction is divided into three phases: read phase, validation phase, and write phase.
- In the read phase, the transaction reads the data items from the database and stores them in a private workspace, without checking timestamps or locking the items.
- In the validation phase, the transaction checks if its operations are serializable with respect to the other transactions that have committed or are validating.
- In the write phase, the transaction writes its updates to the database, if it passes the validation.
- Optimistic timestamp ordering reduces the number of aborts and restarts, and avoids deadlock, but it may increase the overhead of validation and write phases, and it may not be suitable for high-conflict workloads.