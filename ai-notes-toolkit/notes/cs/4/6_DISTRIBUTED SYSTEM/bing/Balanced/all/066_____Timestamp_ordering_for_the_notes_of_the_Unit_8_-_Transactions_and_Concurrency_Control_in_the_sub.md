# Timestamp ordering

Timestamp ordering is a technique for ensuring serializability of transactions in a distributed system. It assigns a unique timestamp to each transaction and uses it to order the execution of conflicting operations.

## Lamport timestamps

Lamport timestamps are a type of logical clock that assigns a unique timestamp to each event in a distributed system, based on the causal relationships among events. Lamport timestamps are defined as follows:

- Each node in the system maintains a local counter that is incremented after each event.
- When a node sends a message, it attaches its current counter value to the message.
- When a node receives a message, it updates its counter to be the maximum of its own counter and the counter value in the message, plus one.
- The Lamport timestamp of an event is the counter value assigned to it by the node where it occurs.

Lamport timestamps provide a partial ordering of events, such that if event A causally precedes event B, then the Lamport timestamp of A is less than the Lamport timestamp of B. However, Lamport timestamps do not distinguish between concurrent events, i.e., events that are not causally related.

## Timestamp ordering protocol

The timestamp ordering protocol is a concurrency control protocol that uses Lamport timestamps to order the execution of conflicting operations in a distributed system. The protocol works as follows:

- Each transaction is assigned a unique timestamp when it starts, which is the Lamport timestamp of its first event.
- Each data item has two timestamps: a read timestamp (RTS) and a write timestamp (WTS), which record the timestamps of the last transaction that read or wrote the item, respectively.
- When a transaction T wants to read a data item X, it checks if its timestamp is greater than or equal to the WTS of X. If yes, it can read X and update the RTS of X to be the maximum of the RTS of X and the timestamp of T. If no, it means that T is trying to read a stale value of X, and the transaction is aborted and restarted with a new timestamp.
- When a transaction T wants to write a data item X, it checks if its timestamp is greater than both the RTS and the WTS of X. If yes, it can write X and update the WTS of X to be the timestamp of T. If no, it means that T is trying to overwrite a newer value of X, and the transaction is aborted and restarted with a new timestamp.

The timestamp ordering protocol ensures serializability of transactions, as it prevents any transaction from violating the precedence order of conflicting operations based on their timestamps. However, it may also abort some transactions that are not actually conflicting, due to the lack of precision of Lamport timestamps.