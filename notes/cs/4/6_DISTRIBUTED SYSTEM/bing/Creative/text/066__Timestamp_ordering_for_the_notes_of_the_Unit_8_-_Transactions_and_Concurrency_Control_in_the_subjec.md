### Timestamp ordering for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- Timestamp ordering is a technique to ensure serializability of transactions in a distributed system without using locks.
- A distributed system consists of a collection of distinct processes that are spatially separated and communicate with each other by exchanging messages.
- A timestamp is a unique and monotonically increasing value that is assigned to each transaction or event in the system.
- Timestamps can be based on physical clocks, logical clocks, or a combination of both.
- Physical clocks are real devices that measure the passage of time, but they may not be synchronized or accurate across the system.
- Logical clocks are abstract mechanisms that assign timestamps based on the causal ordering of events, such as Lamport timestamps or vector clocks.
- Causal ordering means that if event A could have influenced event B, then the timestamp of A is less than the timestamp of B.
- Timestamp ordering protocols use timestamps to determine the order of execution of transactions or events, and to detect and resolve conflicts.
- A conflict occurs when two transactions try to access the same data item in an incompatible way, such as one reading and one writing.
- Timestamp ordering protocols can be classified into two categories: optimistic and pessimistic.
- Optimistic protocols assume that conflicts are rare and allow transactions to proceed without checking for conflicts until they commit. If a conflict is detected, the transaction with the smaller timestamp is aborted and restarted with the same timestamp.
- Pessimistic protocols check for conflicts before allowing transactions to access data items. If a conflict is detected, the transaction with the smaller timestamp is either aborted and restarted with a new timestamp, or delayed until the conflicting transaction finishes.
- An example of an optimistic protocol is the basic timestamp ordering protocol, which assigns timestamps to transactions when they start, and tags each data item with the timestamps of the last transactions that read or wrote it. It uses the Thomas write rule to ignore some write operations that are overwritten by later transactions.
- An example of a pessimistic protocol is the timestamp ordering with multiversion concurrency control protocol, which assigns timestamps to transactions when they commit, and maintains multiple versions of each data item with their timestamps. It allows transactions to read the latest version of a data item that is older than their timestamp, and to write a new version of a data item if their timestamp is larger than the timestamp of the current version.
- Timestamp ordering protocols can ensure conflict serializability, which means that the execution of transactions is equivalent to some serial order that respects the timestamps.
- Timestamp ordering protocols cannot prevent deadlocks, which occur when two or more transactions wait for each other to release data items. Deadlocks can be detected and resolved by using timeouts, aborts, or waits-for graphs.
- Timestamp ordering protocols can also suffer from starvation, which occurs when a transaction is repeatedly aborted or delayed due to conflicts with other transactions. Starvation can be avoided by using priority queues, aging, or backoff mechanisms.