### System Model for Distributed Deadlock Detection

- A distributed system consists of a set of nodes that communicate by message passing.
- Each node has a set of resources that can be requested by processes running on the node or on other nodes.
- A process can request a resource by sending a message to the node that owns the resource.
- A node can grant a resource to a process by sending a message to the process or by placing the resource in a shared buffer.
- A process can release a resource by sending a message to the node that owns the resource or by removing the resource from a shared buffer.
- A process can hold multiple resources at a time and can request additional resources while holding some resources.
- A process can wait for a resource that is currently held by another process.
- A deadlock occurs when a set of processes are waiting for resources that are held by other processes in the set, and no process can proceed until some other process releases a resource.
- A wait-for graph (WFG) is a directed graph that represents the waiting relationships among processes and resources in the system.
- A node in the WFG is either a process or a resource, and an edge from a node A to a node B means that A is waiting for B.
- A cycle in the WFG indicates the presence of a deadlock in the system.