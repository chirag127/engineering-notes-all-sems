### Locks

- Locks are a mechanism to control the concurrent access of data items by transactions in a distributed system.
- A lock is a variable associated with a data item that determines whether read/write operations can be performed on that data item by a transaction .
- A lock can have different modes, such as shared (S), exclusive (X), or update (U), depending on the type of operation that the transaction intends to perform on the data item .
- A lock compatibility matrix is used to specify which lock modes are compatible or incompatible with each other, i.e., whether two transactions can hold locks of different modes on the same data item at the same time .
- A lock manager is a component of the distributed system that is responsible for granting, releasing, and enforcing locks on data items .
- A lock manager can be centralized, distributed, or hierarchical, depending on the architecture of the distributed system and the granularity of the data items .
- Locks are used to ensure the serializability and isolation of transactions, i.e., to prevent conflicts and anomalies that may arise due to concurrent execution of transactions  .
- Locks can also affect the performance and availability of the distributed system, as they may cause blocking, deadlock, or reduced concurrency  .
- Locking-based concurrency control protocols are algorithms that specify the rules and procedures for acquiring and releasing locks on data items by transactions .
- Locking-based concurrency control protocols can be classified into two-phase locking (2PL), strict two-phase locking (S2PL), rigorous two-phase locking (R2PL), timestamp ordering (TO), and optimistic concurrency control (OCC), among others  .
- Locking-based concurrency control protocols have different properties and trade-offs in terms of serializability, recoverability, deadlock prevention, deadlock detection, deadlock resolution, concurrency level, and overhead  .