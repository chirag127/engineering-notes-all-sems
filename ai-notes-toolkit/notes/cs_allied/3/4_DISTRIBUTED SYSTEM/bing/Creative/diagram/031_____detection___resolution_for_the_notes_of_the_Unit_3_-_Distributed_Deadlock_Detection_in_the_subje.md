### Detection and Resolution of Distributed Deadlocks

- A distributed deadlock is a situation where a set of processes in a distributed system are waiting for resources held by other processes in the same set, and none of them can proceed.
- Distributed deadlock detection is the process of identifying the existence of a distributed deadlock in the system.
- Distributed deadlock resolution is the process of breaking the deadlock by aborting one or more processes involved in the deadlock.
- There are different techniques for distributed deadlock detection and resolution, based on various strategies such as:
  - Centralized approach: A single designated node (coordinator) is responsible for maintaining the global wait-for graph (WFG) and detecting cycles in it. The coordinator can also initiate the resolution by choosing a victim process to abort. This approach is simple and efficient, but it has a single point of failure and a high communication overhead.
  - Distributed approach: Each node maintains a local WFG and exchanges messages with other nodes to detect cycles. There are different algorithms for this approach, such as:
    - Path-pushing algorithm: Each node periodically sends its local WFG to its neighbors, and each node merges the received WFGs with its own. A cycle is detected when a node receives a WFG that contains a path from itself to itself.
    - Edge-chasing algorithm: Each node periodically initiates a probe message that traverses the WFG along the edges. A cycle is detected when a node receives a probe message that originated from itself.
    - Diffusing computation algorithm: Each node initiates a diffusing computation when it requests a resource and waits for it. A diffusing computation consists of a set of nodes that are involved in the request and a set of messages that are exchanged among them. A cycle is detected when a node receives a message that indicates that all its children in the diffusing computation are blocked.
  - Hierarchical approach: The nodes are organized into a hierarchy of clusters, and each cluster has a coordinator that maintains a local WFG and detects cycles within the cluster. The coordinators also communicate with each other to detect cycles across clusters. This approach reduces the communication overhead and the single point of failure, but it increases the complexity and the detection latency.
- The resolution of distributed deadlocks can be based on various criteria, such as:
  - Process priority: The process with the lowest priority is aborted.
  - Resource utilization: The process that holds the most resources is aborted.
  - Process age: The process that has been running for the longest time is aborted.
  - Process progress: The process that has made the least progress is aborted.
  - Process dependency: The process that has the most dependents is aborted.