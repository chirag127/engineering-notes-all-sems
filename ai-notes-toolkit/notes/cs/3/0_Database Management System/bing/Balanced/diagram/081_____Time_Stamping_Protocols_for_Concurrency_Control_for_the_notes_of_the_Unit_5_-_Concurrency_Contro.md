### Time Stamping Protocols for Concurrency Control

- Time stamping protocols are a type of concurrency control methods that do not use locks to ensure serializability of transactions.
- Time stamping protocols assign a unique timestamp to each transaction when it is created. The timestamp can be either the system time or a logical counter.
- Time stamping protocols use the timestamps to order the transactions and determine their precedence. A transaction with an earlier timestamp has a higher priority than a transaction with a later timestamp.
- Time stamping protocols ensure that any conflicting read and write operations are executed in timestamp order. A conflict occurs when two transactions access the same data item and at least one of them is a write operation.
- Time stamping protocols can be classified into two types: basic timestamp ordering and timestamp ordering with Thomas' write rule.
- Basic timestamp ordering protocol checks the timestamps of transactions before allowing them to read or write data items. It uses two timestamp values for each data item: read timestamp (RTS) and write timestamp (WTS). RTS is the largest timestamp of any transaction that has successfully read the data item. WTS is the largest timestamp of any transaction that has successfully written the data item.
- Basic timestamp ordering protocol enforces the following rules:
  - A transaction T can read a data item X only if T's timestamp is greater than or equal to the WTS of X. This ensures that T does not read a stale value of X that was overwritten by a later transaction.
  - A transaction T can write a data item X only if T's timestamp is greater than both the RTS and the WTS of X. This ensures that T does not overwrite a more recent value of X that was read or written by a later transaction.
  - If a transaction T violates any of the above rules, it is aborted and restarted with a new timestamp.
- Timestamp ordering with Thomas' write rule is a variation of the basic timestamp ordering protocol that allows some write operations to be ignored without affecting serializability. It uses the same timestamp values and read rule as the basic protocol, but modifies the write rule as follows:
  - A transaction T can write a data item X only if T's timestamp is greater than the WTS of X. This ensures that T does not overwrite a more recent value of X that was written by a later transaction.
  - If T's timestamp is less than or equal to the RTS of X, then T's write operation is ignored. This means that T's write operation does not affect any later transaction that has already read X.
  - If T's timestamp is greater than the RTS of X but less than the WTS of X, then T is aborted and restarted with a new timestamp.
- Timestamp ordering with Thomas' write rule can improve the performance of the system by reducing the number of aborts and restarts. However, it may also result in some transactions writing less data than they intended.