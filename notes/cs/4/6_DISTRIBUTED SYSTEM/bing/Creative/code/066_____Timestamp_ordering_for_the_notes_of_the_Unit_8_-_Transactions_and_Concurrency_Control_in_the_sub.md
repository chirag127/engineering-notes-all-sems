### Timestamp ordering for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- Timestamp ordering is a technique to ensure serializability of transactions in a distributed system.
- A transaction is a sequence of operations that must be executed atomically, i.e., either all or none of them are performed.
- Serializability is the property that the concurrent execution of transactions produces the same result as some sequential execution of them.
- Timestamp ordering assigns a unique timestamp to each transaction when it starts, and uses these timestamps to order the operations of different transactions.
- A timestamp is a logical or physical value that represents the occurrence time of an event or a message in the system.
- Logical timestamps are based on the causal relationships among events, such as Lamport timestamps , which use a logical time function that increments a counter for each event and synchronizes it with other nodes when messages are sent or received.
- Physical timestamps are based on the real time of the system clocks, such as wall-clock time or GPS time, which require clock synchronization among nodes to ensure accuracy and consistency.
- Timestamp ordering can be applied to different levels of granularity, such as transactions, operations, objects, or pages, depending on the system design and requirements.
- Timestamp ordering can be implemented in different ways, such as optimistic, pessimistic, or multiversion, depending on the system assumptions and trade-offs.
- Optimistic timestamp ordering assumes that conflicts among transactions are rare, and allows transactions to execute without checking timestamps until they commit, at which point they are validated and aborted if they violate serializability.
- Pessimistic timestamp ordering assumes that conflicts among transactions are frequent, and checks timestamps before each operation, and rejects the operation if it violates serializability.
- Multiversion timestamp ordering maintains multiple versions of each object, and assigns a timestamp to each version, and allows transactions to access the most recent version that is compatible with their timestamp, thus avoiding conflicts and aborts.