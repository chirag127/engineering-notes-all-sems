### Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set.
- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems.
- Deadlock detection in distributed systems entails addressing two basic issues: detection of existing deadlocks and resolution of detected deadlocks.
- Deadlock detection requires examination of the status of process-resource interactions for presence of cyclic wait.
- There are three approaches to detect deadlocks in distributed systems:
  - Centralized approach: A single site is designated as the deadlock detector and collects global wait-for graph (WFG) from local WFGs at other sites. The deadlock detector periodically checks the global WFG for cycles and initiates recovery actions if needed.
  - Hierarchical approach: The sites are organized into a hierarchy of clusters. Each cluster has a coordinator that collects local WFGs from its members and constructs a cluster WFG. The coordinators communicate with each other to form a global WFG and detect cycles.
  - Distributed approach: There is no central or hierarchical authority. Each site maintains its own local WFG and participates in a distributed algorithm to detect cycles. One such algorithm is edge chasing, which involves sending probe messages along the edges of the WFG until a cycle is found or the probe is discarded.
- To resolve the deadlock, one or more deadlocked processes have to be aborted and their resources have to be released. The selection of the victim process can be based on criteria such as priority, age, number of resources, etc. The aborted process can be restarted later with some rollback mechanism.