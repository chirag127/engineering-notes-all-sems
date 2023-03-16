### Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set.
- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems.
- Deadlock detection in distributed systems entails addressing two basic issues: detection of existing deadlocks and resolution of detected deadlocks.
- Deadlock detection requires examination of the status of process-resource interactions for presence of cyclic wait.
- There are three approaches to detect deadlocks in distributed systems:
  - Centralized approach: A single node is designated as the deadlock detector and collects information from all other nodes to construct a global wait-for graph (WFG) and check for cycles.
  - Hierarchical approach: The nodes are organized into a hierarchy of clusters and each cluster has a coordinator that collects information from its members and communicates with other coordinators to construct a partial WFG and check for cycles.
  - Distributed approach: Each node maintains a local WFG and initiates a probe message along the edges of the WFG to detect cycles.
- To resolve the deadlock, one or more processes involved in the deadlock have to be aborted or preempted.
- The criteria for selecting a victim process include: process priority, process age, process state, number of resources held, number of resources requested, etc.