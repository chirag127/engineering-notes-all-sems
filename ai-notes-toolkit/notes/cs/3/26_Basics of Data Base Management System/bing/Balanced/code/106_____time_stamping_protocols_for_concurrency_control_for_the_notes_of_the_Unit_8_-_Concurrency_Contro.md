### Time stamping protocols for concurrency control

- Time stamping protocols are a type of non-locking concurrency control methods that use timestamps to order the transactions and ensure serializability.
- A timestamp is a unique identifier that represents the creation time of a transaction or a data item. It can be based on the system clock or a logical counter.
- The basic idea of time stamping protocols is to assign a timestamp to each transaction when it enters the system, and use the timestamp to determine the precedence and compatibility of conflicting operations.
- There are two main types of time stamping protocols: basic timestamp ordering and optimistic concurrency control.

#### Basic timestamp ordering

- In this protocol, each data item has two timestamps: read timestamp (RTS) and write timestamp (WTS). RTS is the largest timestamp of any transaction that has successfully read the data item, and WTS is the largest timestamp of any transaction that has successfully written the data item.
- When a transaction Ti requests to read or write a data item X, the protocol compares the timestamp of Ti (TS(Ti)) with the timestamps of X (RTS(X) and WTS(X)) and decides whether to grant or reject the request based on the following rules:

  - If Ti requests to read X:
    - If TS(Ti) < WTS(X), then Ti is trying to read a value of X that has been overwritten by a later transaction. The request is rejected and Ti is aborted.
    - If TS(Ti) >= WTS(X), then Ti can read X without violating serializability. The request is granted and RTS(X) is updated to max(RTS(X), TS(Ti)).
  - If Ti requests to write X:
    - If TS(Ti) < RTS(X), then Ti is trying to write a value of X that has been read by a later transaction. The request is rejected and Ti is aborted.
    - If TS(Ti) < WTS(X), then Ti is trying to write a value of X that has been overwritten by a later transaction. The request is rejected and Ti is aborted.
    - If TS(Ti) >= RTS(X) and TS(Ti) >= WTS(X), then Ti can write X without violating serializability. The request is granted and WTS(X) is updated to TS(Ti).

- The basic timestamp ordering protocol ensures that the transactions are executed in the order of their timestamps, which is equivalent to a serial schedule. However, it has some drawbacks, such as:

  - It may cause unnecessary aborts of transactions that do not actually conflict with each other.
  - It may cause starvation of transactions that have low timestamps and are repeatedly aborted by later transactions.
  - It may cause cascading aborts of transactions that depend on the values read or written by aborted transactions.

#### Optimistic concurrency control

- In this protocol, each transaction is divided into three phases: read phase, validation phase, and write phase. The protocol assumes that conflicts among transactions are rare and allows transactions to execute concurrently without locking or checking for conflicts in the read phase. However, before committing, each transaction has to pass the validation phase, where the protocol checks for conflicts and serializability using timestamps.
- In the read phase, a transaction Ti reads the values of data items from the database and stores them in a local buffer. Ti also records the timestamps of the data items in the read set (RS(Ti)) and the write set (WS(Ti)).
- In the validation phase, Ti obtains a unique commit timestamp (CTS(Ti)) and compares it with the timestamps of other transactions that have already committed or are in the validation phase. Ti passes the validation if and only if the following conditions are satisfied for every data item X in RS(Ti) or WS(Ti):

  - Ti is the only transaction that has accessed X in its read phase, or
  - Ti has accessed X in its read phase and no other transaction has written X in its write phase, or
  - Ti has accessed X in its write phase and no other transaction has accessed X in its read or write phase, or
  - Ti has accessed X in its read phase and some other transaction Tj has accessed X in its write phase, but CTS(Ti) < CTS(Tj).

- If Ti passes the validation, it proceeds to the write phase, where it writes the values of the data items in WS(Ti) to the database and commits. If Ti fails the validation, it is aborted and restarted with a new timestamp.
- The optimistic concurrency control protocol ensures that the transactions are executed in a serializable order based