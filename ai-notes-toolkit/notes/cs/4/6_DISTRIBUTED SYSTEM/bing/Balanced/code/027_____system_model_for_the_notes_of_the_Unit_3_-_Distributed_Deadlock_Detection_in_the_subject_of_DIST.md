### System Model for Distributed Deadlock Detection

- A distributed system consists of a set of nodes that communicate by message passing.
- Each node has a set of resources that can be requested by processes running on the node or on other nodes.
- A process can request, use, and release resources according to some protocol.
- A process may hold some resources while waiting for others, resulting in a wait-for graph (WFG) that represents the dependencies among processes and resources.
- A deadlock occurs when there is a cycle in the WFG, meaning that some processes are waiting for resources that are held by other processes in the cycle, and no progress can be made.
- Deadlock detection is the problem of finding cycles in the WFG and resolving them by aborting some processes or preempting some resources.
- There are three main approaches to deadlock detection in distributed systems: centralized, hierarchical, and distributed.
- In the centralized approach, there is a designated node, called the deadlock detector (DD), that collects information about the WFG from all other nodes and performs cycle detection on the global WFG.
- In the hierarchical approach, the nodes are organized into clusters, and each cluster has a local DD that collects information from the nodes in the cluster and performs cycle detection on the local WFG. The local DDs communicate with a global DD that performs cycle detection on the global WFG, which is constructed from the local WFGs.
- In the distributed approach, there is no central or hierarchical authority, and each node participates in the cycle detection algorithm by sending and receiving messages along the edges of the WFG. There are different algorithms for distributed cycle detection, such as edge chasing, diffusing computation, and probe-based.