# Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set.
- Deadlocks can occur in distributed systems when distributed transactions or concurrency control are used.
- Deadlock detection is the approach of handling deadlocks by identifying and resolving them after they occur.
- Deadlock detection in distributed systems entails two basic issues:
  - Detection of existing deadlocks by examining the status of process-resource interactions for the presence of cyclic wait.
  - Resolution of detected deadlocks by aborting one or more deadlocked processes.
- Deadlock detection in distributed systems can be done by three approaches:
  - Centralized approach: A single node is designated as the deadlock detector and collects information from all other nodes about their resource requests and allocations.
  - Distributed approach: Each node maintains its own local wait-for graph and periodically exchanges information with other nodes to construct a global wait-for graph.
  - Hierarchical approach: The nodes are organized into a hierarchy of clusters and each cluster has a coordinator that acts as the deadlock detector for the cluster.
- Each approach has its own advantages and disadvantages in terms of communication overhead, accuracy, scalability, and fault tolerance.