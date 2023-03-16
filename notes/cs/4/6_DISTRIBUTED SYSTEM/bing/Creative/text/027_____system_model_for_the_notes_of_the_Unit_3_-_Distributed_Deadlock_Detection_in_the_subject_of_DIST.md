### System Model for Distributed Deadlock Detection

- A distributed system consists of a set of nodes that communicate by message passing.
- Each node has a set of resources that can be requested by processes running on the node or on other nodes.
- A process can request a resource by sending a message to the node that owns the resource.
- A node can grant a resource to a process by sending a message to the process or by placing the resource in a shared buffer.
- A process can release a resource by sending a message to the node that owns the resource or by removing the resource from a shared buffer.
- A process can hold multiple resources at a time and can request additional resources while holding some resources.
- A process can wait for a resource if the resource is not available or if the node that owns the resource is busy or unreachable.
- A deadlock occurs when a set of processes are waiting for resources that are held by other processes in the set, and none of the processes can proceed or release any resources.
- A distributed deadlock detection algorithm is a method to detect and resolve deadlocks in a distributed system.
- A distributed deadlock detection algorithm can be classified into three categories: centralized, hierarchical, and distributed.
- A centralized deadlock detection algorithm assigns a single node as the deadlock detector, which collects information from all other nodes and constructs a global wait-for graph to detect cycles.
- A hierarchical deadlock detection algorithm divides the nodes into clusters, and assigns a node in each cluster as the cluster controller, which collects information from the nodes in the cluster and constructs a local wait-for graph. The cluster controllers communicate with each other to construct a global wait-for graph and detect cycles.
- A distributed deadlock detection algorithm does not assign any node as the deadlock detector, but instead relies on the cooperation of all nodes to exchange information and detect cycles. A distributed deadlock detection algorithm can use either edge chasing or probe-based techniques.
- Edge chasing is a technique where a node initiates a deadlock detection by sending a probe message along the edges of the wait-for graph, and the probe message returns to the initiator if a cycle is detected.
- Probe-based is a technique where a node periodically sends a probe message to all its neighbors, and the probe message collects information about the resources and processes along the way, and returns to the initiator with the information. The initiator then analyzes the information to detect cycles.