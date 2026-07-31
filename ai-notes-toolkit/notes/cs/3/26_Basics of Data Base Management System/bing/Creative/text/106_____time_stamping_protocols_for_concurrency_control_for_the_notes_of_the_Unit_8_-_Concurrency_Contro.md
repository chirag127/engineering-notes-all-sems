### Time stamping protocols for concurrency control

- Time stamping protocols are a type of non-locking concurrency control methods that use timestamps to order the transactions and ensure serializability   .
- A timestamp is a unique identifier that represents the creation time of a transaction or a logical counter that increments after each transaction   .
- Each transaction has two timestamps: a start timestamp (TS) that indicates when the transaction started, and a commit timestamp (CT) that indicates when the transaction committed.
- Each data item also has two timestamps: a read timestamp (RT) that indicates the timestamp of the last transaction that read the data item, and a write timestamp (WT) that indicates the timestamp of the last transaction that wrote the data item.
- The basic rules of timestamp ordering protocol are   :
  - If a transaction T wants to read a data item X, it is allowed to do so only if TS(T) >= WT(X), meaning that T started after the last transaction that wrote X. Otherwise, T is aborted and restarted with a new timestamp.
  - If a transaction T wants to write a data item X, it is allowed to do so only if TS(T) >= RT(X) and TS(T) >= WT(X), meaning that T started after the last transaction that read or wrote X. Otherwise, T is aborted and restarted with a new timestamp.
- The advantages of timestamp ordering protocol are   :
  - It avoids deadlock, as no transaction ever waits for another transaction to release a lock.
  - It ensures serializability, as the transactions are executed in the order of their timestamps.
  - It is easy to implement, as no lock manager or deadlock detection is needed.
- The disadvantages of timestamp ordering protocol are   :
  - It may cause starvation, as a transaction may be repeatedly aborted and restarted if it conflicts with other transactions with higher timestamps.
  - It may cause cascading aborts, as an aborted transaction may invalidate the results of other transactions that depend on it.
  - It may not reflect the actual order of events, as the timestamps may not correspond to the real-time occurrence of the transactions.