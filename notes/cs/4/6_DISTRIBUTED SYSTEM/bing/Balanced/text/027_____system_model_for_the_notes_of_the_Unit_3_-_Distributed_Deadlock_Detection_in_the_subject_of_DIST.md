### System Model for Distributed Deadlock Detection

- A distributed system consists of a collection of nodes that communicate and cooperate to achieve a common goal.
- A node can be a process, a processor, a computer, or a cluster of computers.
- A node can request, hold, and release resources that are shared among the nodes.
- A resource can be a physical device, a logical entity, or a message.
- A node can be in one of the following states: active, waiting, or blocked.
- An active node is executing its own instructions and does not need any resource.
- A waiting node is waiting for a resource that is currently held by another node.
- A blocked node is waiting for a resource that is not currently available in the system.
- A deadlock is a situation where a set of nodes are blocked and none of them can proceed.
- A deadlock can be detected by examining the wait-for graph (WFG) of the system, which is a directed graph that represents the resource requests and holds among the nodes.
- A node in the WFG corresponds to a node in the system, and an edge from node A to node B means that node A is waiting for a resource held by node B.
- A deadlock exists in the system if and only if the WFG contains a cycle.
- There are three main approaches to deadlock detection in distributed systems: centralized, hierarchical, and distributed.
- In the centralized approach, there is a designated node, called the coordinator, that is responsible for collecting the local WFGs from all the nodes and constructing the global WFG. The coordinator periodically checks the global WFG for cycles and initiates deadlock resolution if needed.
- In the hierarchical approach, the system is divided into clusters of nodes, and each cluster has a local coordinator that collects the local WFGs from the nodes in the cluster and constructs the cluster WFG. The cluster coordinators communicate with a global coordinator that collects the cluster WFGs and constructs the global WFG. The global coordinator periodically checks the global WFG for cycles and initiates deadlock resolution if needed.
- In the distributed approach, there is no coordinator, and each node participates in the deadlock detection algorithm. The nodes exchange messages to construct and check the global WFG in a distributed manner. There are different algorithms for distributed deadlock detection, such as edge chasing, diffusing computation, and probe-based algorithms.