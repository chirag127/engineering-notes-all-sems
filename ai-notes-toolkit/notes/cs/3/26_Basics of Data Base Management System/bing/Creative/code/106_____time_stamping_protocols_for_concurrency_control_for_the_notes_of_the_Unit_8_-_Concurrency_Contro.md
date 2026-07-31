### Time stamping protocols for concurrency control

- Time stamping protocols are a type of non-locking concurrency control methods that use either system time or logical counters as timestamps to order the transactions and ensure serializability   .
- Timestamps are assigned to each transaction when it is created, and to each read or write operation when it is issued   .
- The timestamps determine the precedence order of the transactions, and any conflicting read and write operations are executed according to the timestamp order   .
- There are two types of timestamp ordering protocols: basic timestamp ordering and optimistic timestamp ordering   .
- Basic timestamp ordering protocol uses two timestamps for each data item: read timestamp (RTS) and write timestamp (WTS), which record the latest time when the item was read or written, respectively   .
- Basic timestamp ordering protocol enforces two rules: read-write rule and write-write rule   .
- Read-write rule: If a transaction T1 tries to read a data item X that was last written by a transaction T2, and the timestamp of T1 is smaller than the timestamp of T2, then T1 is aborted and restarted with a new timestamp, because T1 is trying to read a value of X that is not yet valid   .
- Write-write rule: If a transaction T1 tries to write a data item X that was last written by a transaction T2, and the timestamp of T1 is smaller than the timestamp of T2, then T1 is aborted and restarted with a new timestamp, because T1 is trying to overwrite a newer value of X that was already written by T2   .
- Optimistic timestamp ordering protocol assumes that conflicts among transactions are rare and allows transactions to execute without any checks until they are ready to commit   .
- Optimistic timestamp ordering protocol uses three phases for each transaction: read phase, validation phase, and write phase   .
- Read phase: The transaction reads the data items from the database and stores them in a local buffer. It also records the timestamps of the data items in another buffer called read set   .
- Validation phase: The transaction checks whether it has any conflicts with other transactions that have committed in the meantime. It uses another buffer called write set to store the data items that it intends to write to the database   .
- Write phase: If the transaction passes the validation phase, it writes the data items from the write set to the database. Otherwise, it is aborted and restarted with a new timestamp   .
- The validation phase uses three tests to detect conflicts: write-write test, read-write test, and write-read test   .
- Write-write test: If a transaction T1 tries to write a data item X that was already written by another transaction T2 that committed after T1 started, then T1 is aborted, because T1 is trying to overwrite a newer value of X that was already committed by T2   .
- Read-write test: If a transaction T1 tries to write a data item X that was already read by another transaction T2 that committed after T1 started, then T1 is aborted, because T1 is trying to change a value of X that was already seen by T2   .
- Write-read test: If a transaction T1 tries to read a data item X that was already written by another transaction T2 that committed after T1