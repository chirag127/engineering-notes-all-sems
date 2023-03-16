### Edge Chasing Algorithms

Edge chasing algorithms are used for distributed deadlock detection in distributed systems. Here are some key points to note about edge chasing algorithms:

1. Edge chasing algorithms are based on the concept of sending probe messages to detect cycles in the wait-for graph.
2. A probe message contains information about the initiator of the probe, the current transaction, and the blocked transaction.
3. When a transaction receives a probe message, it checks if it is waiting for any other transaction. If it is, it forwards the probe message to the transaction it is waiting for.
4. If a transaction receives a probe message that it has already seen, it means that a cycle has been detected and a deadlock exists.
5. Once a deadlock is detected, a resolution mechanism is used to break the deadlock, such as aborting one of the transactions involved in the deadlock.
6. Edge chasing algorithms can be classified into two categories: centralized and distributed.
7. In centralized edge chasing algorithms, a single site is responsible for detecting deadlocks, while in distributed edge chasing algorithms, all sites participate in the deadlock detection process.
