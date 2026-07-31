# Time Stamping Protocols for Concurrency Control

- Time stamping protocols are a type of non-locking concurrency control methods that use timestamps to order the transactions and ensure serializability   .
- A timestamp is a unique identifier that represents the creation time of a transaction or a data item. It can be either the system time or a logical counter  .
- The main idea of time stamping protocols is to assign a timestamp to each transaction when it enters the system, and use the timestamp to determine the precedence and compatibility of the transactions   .
- There are two types of time stamping protocols: basic timestamp ordering and timestamp ordering with Thomas' write rule   .

## Basic Timestamp Ordering

- In basic timestamp ordering, each data item has two timestamps: read timestamp (RTS) and write timestamp (WTS). RTS is the largest timestamp of any transaction that has successfully read the data item, and WTS is the largest timestamp of any transaction that has successfully written the data item   .
- The protocol works as follows   :
  - If a transaction T wants to read a data item X, it checks the WTS of X. If the WTS of X is larger than the timestamp of T, it means that some other transaction has modified X after T started, so T is aborted and restarted with a new timestamp. Otherwise, T is allowed to read X and the RTS of X is updated to the maximum of the RTS of X and the timestamp of T.
  - If a transaction T wants to write a data item X, it checks both the RTS and WTS of X. If either the RTS or WTS of X is larger than the timestamp of T, it means that some other transaction has read or written X after T started, so T is aborted and restarted with a new timestamp. Otherwise, T is allowed to write X and the WTS of X is updated to the timestamp of T.
- The basic timestamp ordering protocol ensures that the transactions are executed in a conflict-serializable order that is consistent with their timestamps. However, it may cause unnecessary aborts and restarts of transactions that do not actually conflict with each other   .

## Timestamp Ordering with Thomas' Write Rule

- Timestamp ordering with Thomas' write rule is a variation of basic timestamp ordering that avoids some unnecessary aborts and restarts by applying a write rule   .
- The write rule states that if a transaction T wants to write a data item X, and the WTS of X is larger than the timestamp of T, then T's write operation can be ignored, because it will be overwritten by a later transaction anyway   .
- The protocol works as follows   :
  - If a transaction T wants to read a data item X, it checks the WTS of X. If the WTS of X is larger than the timestamp of T, it means that some other transaction has modified X after T started, so T is aborted and restarted with a new timestamp. Otherwise, T is allowed to read X and the RTS of X is updated to the maximum of the RTS of X and the timestamp of T.
  - If a transaction T wants to write a data item X, it checks both the RTS and WTS of X. If the RTS of X is larger than the timestamp of T, it means that some other transaction has read X after T started, so T is aborted and restarted with a new timestamp. If the WTS of X is larger than the timestamp of T, it means that some other transaction has written X after T started, so T's write operation is ignored. Otherwise, T is allowed to write X and the WTS of X is updated to the timestamp of T.
- The timestamp ordering with Thomas' write rule protocol ensures that the transactions are executed in a view-serializable order that is consistent with their timestamps. It also reduces the number of