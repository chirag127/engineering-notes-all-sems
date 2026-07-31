### System Model for Distributed Deadlock Detection

- A distributed system consists of a collection of nodes that communicate and cooperate to achieve a common goal.
- A node can be a process, a processor, a computer, or a cluster of computers.
- A node can request, hold, and release resources that are shared among other nodes.
- A resource can be a physical device, a file, a message, a lock, or a token.
- A node can be in one of the following states: running, blocked, or terminated.
- A node is running if it is executing its own instructions and not waiting for any resource.
- A node is blocked if it is waiting for a resource that is held by another node.
- A node is terminated if it has completed its execution or aborted due to an error or a deadlock.
- A deadlock is a situation where a set of nodes are blocked and each node is waiting for a resource that is held by another node in the set.
- A deadlock can be detected by examining the status of the node-resource interactions and looking for a cycle in the wait-for graph.
- A wait-for graph is a directed graph that represents the node-resource interactions in the system.
- A node in the wait-for graph is a process or a processor that requests or holds resources.
- An edge in the wait-for graph is a directed link from a node A to a node B if A is waiting for a resource that is held by B.
- A cycle in the wait-for graph indicates a deadlock in the system.
- There are three main approaches to deadlock detection in distributed systems: centralized, hierarchical, and distributed.
- In the centralized approach, there is a designated node that collects the local wait-for graphs from all the nodes and constructs a global wait-for graph to detect deadlocks.
- In the hierarchical approach, there are multiple nodes that handle a subset of nodes or clusters of nodes and are responsible for deadlock detection within their scope. These nodes can communicate with each other to detect global deadlocks.
- In the distributed approach, there is no designated node and each node participates in deadlock detection by sending and receiving messages to other nodes. There are different algorithms for distributed deadlock detection, such as edge chasing, probe-based, and diffusing computation.