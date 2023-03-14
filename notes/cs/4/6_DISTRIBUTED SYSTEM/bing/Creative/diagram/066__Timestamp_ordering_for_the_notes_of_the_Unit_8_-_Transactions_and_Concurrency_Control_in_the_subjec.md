Timestamp ordering is a technique for ensuring the serializability of transactions in a distributed system. It assigns a unique timestamp to each transaction and uses it to determine the order of execution and the validity of read and write operations. There are different variants of timestamp ordering, such as basic timestamp ordering, optimistic timestamp ordering, and multiversion timestamp ordering. Here is a diagram of the basic timestamp ordering protocol, using ASCII characters:

### Timestamp ordering for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

```
+----------------+----------------+----------------+
| Transaction T1 | Transaction T2 | Transaction T3 |
+----------------+----------------+----------------+
| TS(T1) = 10    | TS(T2) = 20    | TS(T3) = 30    |
+----------------+----------------+----------------+
| Read(X)        |                |                |
|                | Write(X)       |                |
|                |                | Read(X)        |
| Write(Y)       |                |                |
|                | Read(Y)        |                |
|                |                | Write(Y)       |
+----------------+----------------+----------------+
| R-TS(X) = 10   | W-TS(X) = 20   | R-TS(X) = 30   |
+----------------+----------------+----------------+
| W-TS(Y) = 10   | R-TS(Y) = 20   | W-TS(Y) = 30   |
+----------------+----------------+----------------+
```

The diagram shows three transactions with their timestamps and operations on two data items, X and Y. Each data item has two timestamps, R-TS and W-TS, which record the last transaction that read or wrote to it. The protocol checks these timestamps for every operation and aborts the transaction if it violates the timestamp order. For example, T1 can read X and write Y without any problem, but T2 cannot write X because its timestamp is less than R-TS(X), which means T1 has already read X. Similarly, T3 cannot read X because its timestamp is greater than W-TS(X), which means T2 has already written X. The protocol ensures that the execution schedule is equivalent to a serial schedule where T1 < T2 < T3.