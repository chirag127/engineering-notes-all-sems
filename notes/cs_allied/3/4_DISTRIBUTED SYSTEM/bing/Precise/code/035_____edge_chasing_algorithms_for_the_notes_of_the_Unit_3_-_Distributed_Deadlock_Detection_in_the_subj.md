### Edge Chasing Algorithms

Edge chasing algorithms are used for distributed deadlock detection in distributed systems. Here are some key points to remember about edge chasing algorithms:

1. Edge chasing algorithms are based on the concept of a "probe" message, which is sent along the edges of a wait-for graph to detect cycles.
2. A wait-for graph is a directed graph that represents the dependencies between transactions in a distributed system.
3. When a transaction is waiting for a resource held by another transaction, an edge is added from the waiting transaction to the holding transaction.
4. If a cycle is detected in the wait-for graph, it indicates the presence of a deadlock.
5. In edge chasing algorithms, a probe message is sent from a blocked transaction to the transaction holding the resource it is waiting for.
6. The probe message contains information about the blocked transaction and the resource it is waiting for.
7. When a transaction receives a probe message, it checks if it is also waiting for a resource. If it is, it forwards the probe message to the transaction holding the resource it is waiting for.
8. If the probe message returns to the originating transaction, it indicates the presence of a cycle in the wait-for graph and a deadlock is detected.
9. Edge chasing algorithms can be classified into two categories: centralized and distributed.
10. In centralized edge chasing algorithms, a single site is responsible for detecting deadlocks. In distributed edge chasing algorithms, all sites participate in deadlock detection.
