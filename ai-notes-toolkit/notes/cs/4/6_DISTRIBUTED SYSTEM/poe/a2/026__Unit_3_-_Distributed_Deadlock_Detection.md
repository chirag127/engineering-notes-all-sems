 Here is the content in Markdown format with formal tone and without emojis/external links as specified:

## Unit 3 - Distributed Deadlock Detection

1. Deadlocks in distributed systems: When multiple processes are accessing resources across a distributed system, deadlocks can occur due to cyclic dependencies between processes and resources. For example, Process 1 waits for Resource 2 which is held by Process 3 which is waiting for Resource 1 held by Process 1.
2. Directed graph model: The deadlock situation can be represented using a directed graph where vertices represent processes and resources and edges represent dependencies. A cycle in the graph indicates a deadlock.
3. Centralized deadlock detection: A centralized coordinator tracks resource allocation and can detect deadlocks by checking for cycles in the dependency graph. However, this can become a bottleneck in scalable distributed systems.
4. Distributed deadlock detection: Each process maintains partial information about resource allocation and dependencies. They can exchange messages to collaboratively detect deadlocks in a distributed fashion. Some approaches are:
- Edge chasing: Processes exchange information about edges in the dependency graph and check for cycles.
- Incidence matrix: Each process maintains a row of an incidence matrix capturing resource allocation. The matrix can be combined to detect cycles.
- Wait-for graph: Each process maintains a local wait-for graph and the graphs are merged to check for cycles.

The above content summarizes key concepts and approaches related to distributed deadlock detection. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.