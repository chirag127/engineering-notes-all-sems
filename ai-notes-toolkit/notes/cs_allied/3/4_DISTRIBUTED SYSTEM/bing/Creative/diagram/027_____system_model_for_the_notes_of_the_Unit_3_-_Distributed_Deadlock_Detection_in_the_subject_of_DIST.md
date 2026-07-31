### System Model for Distributed Deadlock Detection

- A distributed system consists of a set of nodes that communicate by message passing.
- Each node has a set of resources that can be requested by processes running on the same or different nodes.
- A process can request, hold, and release resources according to some protocol.
- A process is blocked if it is waiting for a resource that is held by another process.
- A deadlock is a situation where a set of processes are blocked and none of them can proceed.
- A wait-for graph (WFG) is a directed graph that represents the blocking relationships among processes. A node in the WFG is a process and an edge from P to Q means that P is waiting for a resource held by Q.
- A cycle in the WFG indicates a deadlock.
- A global WFG is a WFG that contains all the processes and resources in the system. A local WFG is a WFG that contains only the processes and resources on a single node.
- A system model for distributed deadlock detection defines how the global WFG is constructed and analyzed to detect deadlocks.
- There are three main approaches to distributed deadlock detection: centralized, hierarchical, and distributed.    

  - Centralized approach: One node is designated as the deadlock detector (DD) and collects the local WFGs from all the other nodes. The DD constructs the global WFG and checks for cycles periodically or on demand.
  - Hierarchical approach: The nodes are organized into a tree structure, where each node is responsible for a subset of nodes. The root node is the DD and collects the local WFGs from its children. The children nodes may also collect the local WFGs from their descendants and send them to the root. The DD constructs the global WFG and checks for cycles periodically or on demand.
  - Distributed approach: Each node maintains a partial view of the global WFG based on the messages it sends and receives. The nodes cooperate to detect cycles using algorithms such as edge chasing, diffusing computation, or probe-based. The cycle detection can be initiated by any node or by a special node.