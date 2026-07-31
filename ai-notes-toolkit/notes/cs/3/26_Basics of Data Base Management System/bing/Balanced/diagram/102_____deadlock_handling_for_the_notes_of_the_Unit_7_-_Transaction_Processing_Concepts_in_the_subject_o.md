### Deadlock Handling

- A deadlock is a situation where two or more transactions are waiting for each other to release a lock on a resource, and none of them can proceed.
- Deadlocks can reduce the concurrency and performance of a transaction processing system, and may cause transactions to abort and roll back.
- There are three main methods for handling deadlocks: prevention, avoidance, and detection and resolution.

#### Prevention
- Deadlock prevention is a technique that ensures that deadlocks never occur in the system by imposing some constraints on how transactions can acquire and release locks.
- Some of the common prevention methods are:
  - Timestamp ordering: transactions are assigned a unique timestamp when they start, and they can only request locks on resources in the order of their timestamps. This prevents cyclic waiting among transactions.
  - No waiting: transactions are not allowed to wait for a lock on a resource. If a transaction requests a lock and it is not available, the transaction is aborted and restarted later with a new timestamp.
  - No preemption: transactions are not allowed to release a lock on a resource until they commit or abort. This prevents a transaction from holding a lock and waiting for another lock that is held by another transaction.

#### Avoidance
- Deadlock avoidance is a technique that allows the system to grant a lock request only if it is safe to do so, i.e., if granting the lock will not lead to a deadlock in the future.
- One of the common avoidance methods is:
  - Wait-for graph: the system maintains a graph of transactions and resources, where an edge from a transaction to a resource means that the transaction holds a lock on the resource, and an edge from a resource to a transaction means that the transaction is waiting for a lock on the resource. The system grants a lock request only if it does not create a cycle in the graph, which indicates a deadlock.

#### Detection and Resolution
- Deadlock detection and resolution is a technique that allows the system to periodically check for deadlocks in the system, and resolve them by aborting one or more transactions involved in the deadlock.
- Some of the common detection and resolution methods are:
  - Timeout: the system sets a maximum time limit for a transaction to wait for a lock on a resource. If the limit is exceeded, the transaction is aborted and restarted later with a new timestamp.
  - Deadlock detection algorithm: the system runs an algorithm that scans the wait-for graph for cycles, and identifies the transactions involved in the deadlock. The system then chooses one or more transactions to abort and release their locks, based on some criteria such as the age, priority, or number of locks held by the transactions.