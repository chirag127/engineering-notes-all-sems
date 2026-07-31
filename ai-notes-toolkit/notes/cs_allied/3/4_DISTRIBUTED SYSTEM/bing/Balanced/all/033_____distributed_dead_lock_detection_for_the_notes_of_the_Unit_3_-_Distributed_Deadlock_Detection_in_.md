# Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set.
- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems.
- Deadlock detection in distributed systems entails addressing two basic issues: detection of existing deadlocks and resolution of detected deadlocks.
- Deadlock detection requires examination of the status of process-resource interactions for presence of cyclic wait.
- Deadlock resolution requires aborting one or more deadlocked processes to break the cycle and release the resources.
- There are three approaches to detect deadlocks in distributed systems:
  - Centralized approach: A designated node collects the local wait-for graphs from all the nodes and constructs a global wait-for graph to detect cycles.
  - Distributed approach: A distributed algorithm is used to propagate the deadlock information among the nodes and detect cycles without constructing a global wait-for graph.
  - Hierarchical approach: The nodes are organized into a hierarchy of clusters and each cluster has a coordinator that collects the local wait-for graphs and detects cycles within the cluster. The coordinators communicate with each other to detect global cycles.
- Each approach has its advantages and disadvantages in terms of communication cost, detection latency, accuracy, and scalability.