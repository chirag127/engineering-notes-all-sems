### Timestamp ordering

- Timestamp ordering is a technique for ensuring serializability of transactions in a distributed system.
- A transaction is a sequence of operations that must be executed atomically, i.e., either all or none of them are performed.
- Serializability means that the concurrent execution of transactions produces the same result as some sequential execution of them.
- Timestamp ordering assigns a unique timestamp to each transaction when it starts, and uses these timestamps to order the operations of different transactions.
- The timestamp of a transaction reflects its logical start time, not the physical time on the node where it executes.
- Timestamp ordering can be implemented using logical clocks, such as Lamport timestamps, or physical clocks, such as synchronized clocks.
- Logical clocks are based on the causal ordering of events in the system, i.e., if event A happens before event B, then the timestamp of A is less than the timestamp of B.
- Physical clocks are based on the real time of the nodes, and require some synchronization mechanism to ensure that they do not drift too much.
- Timestamp ordering can be applied to different granularities of data, such as records, pages, or objects.
- Timestamp ordering can be enforced by different protocols, such as basic timestamp ordering, optimistic timestamp ordering, or multiversion timestamp ordering.
- Basic timestamp ordering checks the timestamps of transactions before reading or writing data, and aborts any transaction that violates the order.
- Optimistic timestamp ordering allows transactions to execute without checking timestamps, but validates them at the end and aborts any transaction that conflicts with the order.
- Multiversion timestamp ordering maintains multiple versions of data, and assigns timestamps to each version. Transactions can read the latest version that is compatible with their timestamp, and write new versions with their timestamp.