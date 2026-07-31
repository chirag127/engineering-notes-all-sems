# Time Stamping Protocols for Concurrency Control

- Time stamping protocols are a type of non-locking concurrency control methods that use timestamps to order the transactions and ensure serializability.
- A timestamp is a unique identifier that represents the creation time of a transaction or a data item. It can be either the system time or a logical counter.
- The basic idea of time stamping protocols is to assign a timestamp to each transaction when it enters the system, and use the timestamps to determine the precedence and compatibility of conflicting operations.
- There are two types of time stamping protocols: optimistic and pessimistic.

## Optimistic Time Stamping Protocols

- Optimistic time stamping protocols assume that conflicts are rare and allow transactions to execute without any checks until they are ready to commit.
- At commit time, each transaction is validated to ensure that it does not violate the serializability order based on the timestamps.
- If a transaction passes the validation, it is committed and its effects are made permanent. If a transaction fails the validation, it is aborted and restarted with a new timestamp.
- There are different ways to perform the validation, such as Thomas' write rule, basic timestamp ordering, and multiversion timestamp ordering.

## Pessimistic Time Stamp Ordering Protocols

- Pessimistic time stamp ordering protocols assume that conflicts are frequent and check the compatibility of each operation before it is executed.
- Each data item has two timestamps: read timestamp (RTS) and write timestamp (WTS), which record the latest time when the item was read or written, respectively.
- Each transaction has a timestamp (TS) that is assigned when it enters the system and remains unchanged throughout its execution.
- Before a transaction can read or write a data item, it has to compare its timestamp with the timestamps of the data item and follow some rules to ensure serializability.
- The rules are:

  - A transaction T can read a data item X if TS(T) >= WTS(X), meaning that T is not reading an obsolete value of X. If the condition is true, T performs the read and sets RTS(X) to max(RTS(X), TS(T)).
  - A transaction T can write a data item X if TS(T) > WTS(X) and TS(T) > RTS(X), meaning that T is not overwriting a newer value of X or violating a previous read of X. If the condition is true, T performs the write and sets WTS(X) to TS(T).
  - If either condition is false, T is rejected and aborted.

- Pessimistic time stamp ordering protocols guarantee conflict serializability, but may cause unnecessary aborts and reduce concurrency.