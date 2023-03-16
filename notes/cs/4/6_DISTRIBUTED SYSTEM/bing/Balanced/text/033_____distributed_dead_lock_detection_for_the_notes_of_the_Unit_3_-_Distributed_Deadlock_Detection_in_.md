### Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set.
- Deadlocks can occur in distributed systems when distributed transactions or concurrency control are used.
- Deadlock detection is the approach of identifying and resolving existing deadlocks in the system.
- Deadlock detection in distributed systems entails two basic issues:
  - Detection of existing deadlocks by examining the status of process-resource interactions for presence of cyclic wait.
  - Resolution of detected deadlocks by aborting one or more deadlocked processes.
- Deadlock detection in distributed systems can be done by using one of the following methods:
  - Centralized approach: A single node is designated as the deadlock detector and collects information from all other nodes about their resource requests and allocations. The deadlock detector constructs a global wait-for graph (WFG) and checks for cycles in it. If a cycle is found, the deadlock detector selects a victim process and sends a message to abort it.
  - Distributed approach: Each node maintains a local wait-for graph (WFG) and periodically sends it to a neighboring node. The neighboring node merges the received WFG with its own and forwards it to another node. This process continues until a node receives its own WFG back. The node then checks for cycles in the merged WFG and if found, selects a victim process and sends a message to abort it.
  - Hierarchical approach: The nodes are organized into a hierarchy of clusters. Each cluster has a coordinator node that collects information from its members and constructs a local WFG. The coordinators periodically exchange their WFGs with their parent or child coordinators and merge them. The root coordinator checks for cycles in the global WFG and if found, selects a victim process and sends a message to abort it.