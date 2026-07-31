# System Model for Distributed Deadlock Detection

- A distributed system consists of a collection of processes that communicate and share resources over a network.
- A deadlock is a situation where a set of processes are blocked waiting for resources that are held by other processes in the set.
- Distributed deadlock detection is the problem of finding and resolving deadlocks in a distributed system.
- There are three main approaches to distributed deadlock detection: centralized, hierarchical, and distributed.

## Centralized Approach

- In the centralized approach, one node is designated as the deadlock detector and collects information about the resource allocation and requests from all other nodes.
- The deadlock detector constructs a global wait-for graph (WFG) from the local WFGs of each node and checks for cycles in the graph.
- A cycle in the WFG indicates a deadlock and the deadlock detector can initiate a recovery action, such as aborting or preempting one or more processes in the cycle.
- The advantages of the centralized approach are simplicity and efficiency, as only one node needs to perform the deadlock detection algorithm.
- The disadvantages of the centralized approach are the single point of failure and the communication overhead, as the deadlock detector needs to receive and process messages from all other nodes.

## Hierarchical Approach

- In the hierarchical approach, the nodes are organized into a tree structure, where each node is responsible for a subset of nodes or clusters.
- Each node maintains a local WFG for its cluster and periodically sends it to its parent node in the tree.
- The parent node merges the WFGs from its children and sends the merged WFG to its parent, and so on, until the root node receives the global WFG.
- The root node performs the deadlock detection algorithm on the global WFG and notifies the nodes involved in the deadlock.
- The advantages of the hierarchical approach are fault tolerance and scalability, as the system can tolerate the failure of some nodes and can handle a large number of nodes by increasing the levels of the tree.
- The disadvantages of the hierarchical approach are the complexity and the delay, as the deadlock detection algorithm requires multiple steps and messages to reach the root node and the deadlock may persist for a long time before being detected.

## Distributed Approach

- In the distributed approach, each node participates in the deadlock detection algorithm without relying on a central or hierarchical coordinator.
- There are two main techniques for the distributed approach: edge chasing and probe-based.
- Edge chasing is a technique where each node sends a probe message along the edges of the WFG to detect cycles.
- A probe message contains the identity of the sender and the sequence of nodes it has visited.
- If a node receives a probe message that contains its own identity, it means that a cycle has been detected and a deadlock exists.
- Probe-based is a technique where each node periodically initiates a probe message to check the status of its outgoing edges in the WFG.
- A probe message contains the identity of the initiator and a timestamp.
- If a node receives a probe message, it compares the timestamp with its own and replies with either a positive or a negative acknowledgment.
- A positive acknowledgment means that the node is waiting for a resource that is held by another node and a negative acknowledgment means that the node is not waiting for any resource or has acquired the resource since the probe was initiated.
- If the initiator receives a positive acknowledgment from all its outgoing edges, it means that it is involved in a deadlock and can take a recovery action.
- The advantages of the distributed approach are the absence of a single point of failure and the reduced communication overhead, as the nodes only communicate with their neighbors in the WFG.
- The disadvantages of the distributed approach are the possibility of false or phantom deadlocks and the difficulty of coordinating the recovery actions, as the nodes may have inconsistent or incomplete views of the global WFG.