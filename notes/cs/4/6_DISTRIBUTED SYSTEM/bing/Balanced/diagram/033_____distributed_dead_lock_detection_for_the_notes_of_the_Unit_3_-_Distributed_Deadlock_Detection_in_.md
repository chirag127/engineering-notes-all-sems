### Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set, and none of the processes can proceed or release the resources.
- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems.
- Deadlock detection in distributed systems entails addressing two basic issues: detection of existing deadlocks and resolution of detected deadlocks.
- Deadlock detection requires examination of the status of process-resource interactions for presence of cyclic wait.
- There are three main approaches to detect deadlocks in distributed systems:
  - Centralized approach: A single site is designated as the deadlock detector and collects the local wait-for graphs from all the sites to construct a global wait-for graph. The deadlock detector periodically runs an algorithm to check for cycles in the global wait-for graph and initiates the resolution process if a deadlock is found.
  - Hierarchical approach: The sites are organized into a hierarchy of clusters, and each cluster has a coordinator that acts as the deadlock detector for that cluster. The coordinators communicate with each other to construct a global wait-for graph and detect deadlocks.
  - Distributed approach: There is no central or hierarchical authority, and each site participates in the deadlock detection process. The sites exchange messages to probe for cycles in the wait-for graph and report the results to a designated initiator site. The initiator site decides whether a deadlock exists and initiates the resolution process if needed.
- The resolution process involves aborting one or more deadlocked processes to break the cycle and release the resources. The choice of which process to abort depends on several factors, such as the priority, the execution time, the number of resources held, and the cost of rollback.
- Deadlock detection in distributed systems has some advantages and disadvantages compared to deadlock prevention and avoidance:
  - Advantages: It allows more concurrency and flexibility in resource allocation, and it does not require a priori knowledge of the resource requests and availability.
  - Disadvantages: It incurs more overhead in terms of message passing and computation, and it may cause more wastage of resources and time due to rollback and restart of aborted processes.