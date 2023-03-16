# Path Pushing Algorithms

Path pushing algorithms are a type of distributed deadlock detection algorithm used in distributed systems. These algorithms are used to detect deadlocks in a distributed system by maintaining a wait-for graph at each site in the system.

Here are some key points to remember about path pushing algorithms:

1. In a path pushing algorithm, each site maintains a local wait-for graph that represents the dependencies between transactions at that site.
2. When a transaction at a site is blocked, the site sends a probe message to the site that holds the resource the transaction is waiting for.
3. The probe message contains the blocked transaction's identifier and the identifier of the transaction that is holding the resource.
4. When a site receives a probe message, it adds an edge to its local wait-for graph representing the dependency between the two transactions.
5. If the site detects a cycle in its local wait-for graph, it initiates a global deadlock detection procedure to determine if a deadlock exists in the system.
6. If a deadlock is detected, one of the transactions involved in the deadlock is aborted to resolve the deadlock.
