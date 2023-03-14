 Here is the content in markdown format for the topic - ### path pushing algorithms for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM:

### Path Pushing Algorithms

Path pushing algorithms are distributed deadlock detection algorithms that work by propagating resource allocation information along the dependency graph of the distributed system. Each process keeps track of the resources it has allocated to other processes. When a process requests additional resources, it checks if the granting of the request would create a cycle in the dependency graph (which would indicate a deadlock). If so, the request is denied. Else, the allocation information is propagated to the processes that grant the requested resources.

Advantages:

- Detects distributed deadlocks
- Does not require global system state information

Disadvantages:

- May lead to false positives (incorrectly detecting deadlocks)
- Messages required for propagating allocation information can lead to overhead

Examples:

- Wait-for graph algorithm
- Circular wait algorithm

Applications: Used in distributed resource allocation and transaction management in distributed databases.

Mnemonics:

- Think of path pushing algorithms as propagating "deadlock detection waves" through the system dependency graph.
- The algorithms push resource allocation information along paths in the graph, checking for cycles (deadlocks) along the way.