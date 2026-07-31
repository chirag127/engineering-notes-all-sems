# System Model for Distributed Deadlock Detection

- A distributed system consists of a collection of nodes that communicate and cooperate to achieve a common goal.
- A node can be a process, a processor, a computer, or a cluster of computers.
- A node can request, hold, and release resources that are shared among other nodes.
- A resource can be a physical device, a file, a message, a lock, or any other entity that can be accessed by a node.
- A node can be in one of the following states: running, blocked, or aborted.
- A node is running if it is executing its instructions and not waiting for any resource.
- A node is blocked if it is waiting for a resource that is held by another node.
- A node is aborted if it is terminated due to a failure or a deadlock resolution.
- A deadlock is a situation where a set of nodes are blocked and each node in the set is waiting for a resource that is held by another node in the set.
- A deadlock can be detected by examining the wait-for graph (WFG) of the system, which is a directed graph that represents the resource requests and holds of the nodes.
- A node in the WFG corresponds to a node in the system, and an edge from node A to node B indicates that node A is waiting for a resource that is held by node B.
- A deadlock exists in the system if and only if the WFG contains a cycle.
- There are three main approaches to deadlock detection in distributed systems: centralized, hierarchical, and distributed.
- In the centralized approach, there is a designated node called the deadlock detector (DD) that is responsible for collecting the local WFGs from all the nodes and constructing the global WFG of the system. The DD periodically checks the global WFG for cycles and initiates deadlock resolution if a deadlock is found.
- In the hierarchical approach, the system is divided into clusters of nodes, and each cluster has a local DD that handles the deadlock detection within the cluster. The local DDs communicate with a global DD that handles the deadlock detection across the clusters. The global DD periodically requests the local WFGs from the local DDs and constructs the global WFG of the system. The global DD checks the global WFG for cycles and initiates deadlock resolution if a deadlock is found.
- In the distributed approach, there is no central or global DD, and each node participates in the deadlock detection process. The nodes exchange messages to construct and check the global WFG of the system. There are different algorithms for distributed deadlock detection, such as edge chasing, diffusing computation, and probe-based algorithms. These algorithms differ in the way they propagate and process the information about the resource requests and holds of the nodes.