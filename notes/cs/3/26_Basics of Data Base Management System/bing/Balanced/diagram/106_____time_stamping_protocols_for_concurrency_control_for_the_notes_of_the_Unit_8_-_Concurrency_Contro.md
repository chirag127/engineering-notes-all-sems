### Time stamping protocols for concurrency control

- Time stamping protocols are a type of non-locking concurrency control methods that use timestamps to order the transactions and ensure serializability.
- A timestamp is a unique identifier that represents the creation time of a transaction or a data item. It can be either system time or logical counter.
- The basic idea of time stamping protocols is to assign a timestamp to each transaction when it enters the system, and use the timestamp to determine the precedence and compatibility of conflicting operations.
- There are two main types of time stamping protocols: basic timestamp ordering and optimistic concurrency control.

#### Basic timestamp ordering

- In basic timestamp ordering, each data item has two timestamps: read timestamp (RTS) and write timestamp (WTS). RTS is the largest timestamp of any transaction that has successfully read the data item, and WTS is the largest timestamp of any transaction that has successfully written the data item.
- When a transaction Ti tries to read or write a data item Q, the protocol checks the timestamps of Ti and Q, and decides whether to allow or reject the operation based on the following rules:

  - If Ti tries to read Q:
    - If TS(Ti) < WTS(Q), then the read is rejected, because Q has been modified by a newer transaction after Ti started. This is called a read-write conflict, and Ti is aborted and restarted with a new timestamp.
    - If TS(Ti) >= WTS(Q), then the read is allowed, and RTS(Q) is updated to max(RTS(Q), TS(Ti)), because Ti is the latest transaction that has read Q.
  - If Ti tries to write Q:
    - If TS(Ti) < RTS(Q), then the write is rejected, because Q has been read by a newer transaction after Ti started. This is called a write-read conflict, and Ti is aborted and restarted with a new timestamp.
    - If TS(Ti) < WTS(Q), then the write is rejected, because Q has been modified by a newer transaction after Ti started. This is called a write-write conflict, and Ti is aborted and restarted with a new timestamp.
    - If TS(Ti) >= RTS(Q) and TS(Ti) >= WTS(Q), then the write is allowed, and WTS(Q) is updated to TS(Ti), because Ti is the latest transaction that has modified Q.

- The basic timestamp ordering protocol ensures that the transactions are executed in timestamp order, and thus preserves serializability. However, it has some drawbacks, such as:

  - It may cause unnecessary aborts of transactions that do not actually conflict with each other, such as when Ti reads Q and then Tj writes Q, and TS(Ti) < TS(Tj). This is called the Thomas write rule, and it can be relaxed by allowing Tj to overwrite Q if TS(Tj) > RTS(Q).
  - It may cause cascading aborts of transactions that depend on aborted transactions, such as when Ti writes Q and then Tj reads Q, and TS(Ti) < TS(Tj), and then Ti is aborted. This can be prevented by using strict timestamp ordering, which requires that a transaction can only commit after all its write operations are executed.

#### Optimistic concurrency control

- Optimistic concurrency control (OCC) is another type of timestamp ordering protocol that assumes that conflicts are rare and delays the validation of transactions until they are ready to commit.
- In OCC, each transaction goes through three phases: read phase, validation phase, and write phase.
- In the read phase, the transaction reads the data items from the database and stores them in a local buffer, without checking or updating any timestamps. The transaction also records its start timestamp (TS(Ti)) when it enters the system.
- In the validation phase, the transaction checks whether it has any conflicts with other transactions that have committed since its start timestamp. The transaction records its end timestamp (TE(Ti)) when it finishes the read phase, and compares it with the commit timestamps (TC(Tj)) of other transactions. The validation rules are:

  - If Ti reads Q and Tj writes Q, and TS(Ti) < TC(Tj) < TE(Ti), then Ti is aborted, because Q has been modified by a committed transaction during Ti's read phase. This is a read-write conflict.
  - If Ti writes Q and Tj reads or writes Q, and TS(Ti) < TC(Tj), then Ti is aborted, because Q has been accessed by a committed transaction before Ti's validation phase. This is a write-read or write-write