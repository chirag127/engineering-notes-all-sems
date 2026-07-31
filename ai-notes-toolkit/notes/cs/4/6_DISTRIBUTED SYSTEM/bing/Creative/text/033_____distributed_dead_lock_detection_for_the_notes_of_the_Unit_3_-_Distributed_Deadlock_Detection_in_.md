### Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set.
- Deadlocks can occur in distributed systems when distributed transactions or concurrency control are used.
- Deadlock detection is the approach of identifying and resolving existing deadlocks in the system.
- Deadlock detection in distributed systems entails two basic issues:
  - Detection of existing deadlocks
  - Resolution of detected deadlocks
- Deadlock detection requires examination of the status of process-resource interactions for presence of cyclic wait.
- Deadlock detection in distributed systems can be done using three approaches:
  - Centralized approach: A single node is designated as the deadlock detector and collects information from all other nodes to construct a global wait-for graph (WFG) and detect cycles.
  - Hierarchical approach: The nodes are organized into a hierarchy of clusters and each cluster has a coordinator that collects information from its members and communicates with other coordinators to construct a partial WFG and detect cycles.
  - Distributed approach: Each node maintains its own local WFG and exchanges information with other nodes using messages to detect cycles in a distributed manner.
- Some examples of distributed deadlock detection algorithms are:
  - Chandy-Misra-Haas algorithm: A distributed edge-chasing algorithm that uses probe messages to trace the dependency paths in the WFG.
  - Ho-Ramamoorthy algorithm: A distributed algorithm that uses a diffusing computation to initiate and terminate the deadlock detection process.
  - Menasce-Muntz algorithm: A hierarchical algorithm that uses a tree structure to organize the nodes and coordinators and uses a combination of edge-chasing and WFG construction to detect cycles.