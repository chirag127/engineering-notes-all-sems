### System Model for Distributed Deadlock Detection

- A distributed system consists of a set of nodes that communicate by message passing.
- Each node has a set of resources that can be requested by processes running on the node or on other nodes.
- A process can request a resource by sending a message to the node that owns the resource.
- A node can grant a resource to a process by sending a message to the process or by placing the resource in a shared buffer.
- A process can release a resource by sending a message to the node that owns the resource or by removing the resource from a shared buffer.
- A process can hold multiple resources at a time and can request additional resources while holding some resources.
- A process can be blocked if it is waiting for a resource that is not available.
- A deadlock occurs when a set of processes are blocked and each process is waiting for a resource that is held by another process in the set.
- A wait-for graph (WFG) is a directed graph that represents the resource requests and grants in the system. Each node in the WFG is a process and each edge is a resource dependency. An edge from process P to process Q means that P is waiting for a resource that is held by Q.
- A cycle in the WFG indicates a deadlock in the system. A deadlock can be detected by finding a cycle in the WFG.
- There are three main approaches to deadlock detection in distributed systems: centralized, hierarchical, and distributed.
- In the centralized approach, there is a designated node that collects the local WFGs from all the nodes and constructs a global WFG. The designated node then searches for a cycle in the global WFG and initiates a recovery action if a deadlock is found.
- In the hierarchical approach, there is a tree structure of nodes that are responsible for deadlock detection. Each node collects the local WFGs from its children and constructs a partial WFG. The root node collects the partial WFGs from its children and constructs a global WFG. The root node then searches for a cycle in the global WFG and initiates a recovery action if a deadlock is found.
- In the distributed approach, there is no designated node or tree structure for deadlock detection. Each node participates in the deadlock detection algorithm by sending and receiving messages. There are two main types of distributed algorithms: path-pushing and edge-chasing.
- In the path-pushing algorithm, each node maintains a set of paths that represent the resource dependencies in the system. A path is a sequence of processes that are waiting for resources. Each node periodically sends its paths to its neighbors and updates its paths based on the received paths. A node detects a deadlock if it receives a path that contains itself.
- In the edge-chasing algorithm, each node initiates a probe message when it is blocked. A probe message is a token that contains the identity of the initiator and the sequence of processes that have forwarded the probe. Each node forwards the probe message to the process that holds the resource that it is waiting for. A node detects a deadlock if it receives a probe message that contains its own identity.