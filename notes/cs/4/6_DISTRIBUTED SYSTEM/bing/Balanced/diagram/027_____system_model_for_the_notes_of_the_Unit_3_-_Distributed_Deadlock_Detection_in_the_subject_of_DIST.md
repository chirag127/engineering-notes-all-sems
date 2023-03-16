### System Model for Distributed Deadlock Detection

- A distributed system consists of a set of nodes that communicate by message passing.
- Each node has a set of resources that can be requested by processes running on the same or different nodes.
- A process can request, hold, and release resources according to some protocol.
- A process is blocked if it is waiting for a resource that is held by another process.
- A deadlock is a situation where a set of processes are blocked and none of them can proceed.
- A wait-for graph (WFG) is a directed graph that represents the blocking relationships among processes. A node in the WFG is a process and an edge from P to Q means that P is waiting for a resource held by Q.
- A cycle in the WFG indicates a deadlock.
- Distributed deadlock detection is the problem of finding cycles in the WFG of a distributed system.
- There are three main approaches to distributed deadlock detection: centralized, hierarchical, and distributed.
- In the centralized approach, there is a designated node (called the coordinator) that collects the local WFGs from all the nodes and constructs the global WFG. The coordinator then runs a cycle detection algorithm on the global WFG and informs the nodes about the deadlocks.
- In the hierarchical approach, the nodes are organized into clusters and each cluster has a leader that acts as a coordinator for the cluster. The leaders communicate with each other to construct a global WFG and detect cycles.
- In the distributed approach, there is no coordinator and each node participates in the deadlock detection process. The nodes exchange messages (called probes) that contain information about the WFG. A cycle is detected when a probe returns to its originator.