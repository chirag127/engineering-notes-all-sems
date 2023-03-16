# Timestamp ordering

- Timestamp ordering is a technique for ensuring serializability of transactions in a distributed system.
- A transaction is a sequence of operations that must be executed atomically, i.e., either all or none of them are performed.
- Serializability is the property that the concurrent execution of transactions produces the same result as some sequential execution of them.
- Timestamp ordering assigns a unique timestamp to each transaction when it starts, and uses these timestamps to order the operations of different transactions.
- The timestamp of a transaction reflects its logical start time, not the physical time on the node where it executes.
- Timestamp ordering can be implemented using logical clocks, such as Lamport timestamps, which are monotonically increasing counters that are updated based on the causal dependencies among events in the system.
- Lamport timestamps have the property that if event A causally precedes event B, then the timestamp of A is less than the timestamp of B.
- Timestamp ordering can be applied to different levels of granularity, such as read and write operations, data items, or database pages.
- Timestamp ordering can be enforced by different protocols, such as basic timestamp ordering, optimistic timestamp ordering, or multiversion timestamp ordering.
- Basic timestamp ordering requires that a transaction's read or write operation on a data item is executed only if its timestamp is greater than the timestamp of the last write operation on that data item, otherwise the transaction is aborted and restarted with a new timestamp.
- Optimistic timestamp ordering allows a transaction to execute optimistically without checking timestamps, but validates its operations at commit time using timestamps, and aborts and restarts the transaction if any conflict is detected.
- Multiversion timestamp ordering maintains multiple versions of each data item, each with a timestamp of the transaction that created it, and allows a transaction to read the latest version of a data item that has a timestamp less than or equal to its own timestamp, and to write a new version of a data item with its own timestamp.