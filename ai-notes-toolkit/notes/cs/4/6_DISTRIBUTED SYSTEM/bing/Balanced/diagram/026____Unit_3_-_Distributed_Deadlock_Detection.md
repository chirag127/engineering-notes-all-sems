## Unit 3 - Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set.
- A distributed deadlock is a deadlock that involves processes and resources located on different nodes of a distributed system.
- Deadlock detection in distributed systems is the approach of identifying and resolving existing deadlocks in the system.
- Deadlock detection in distributed systems entails addressing two basic issues:
  - Detection of existing deadlocks: This requires examining the status of process-resource interactions for the presence of cyclic wait.
  - Resolution of detected deadlocks: This requires aborting one or more deadlocked processes to break the cycle and release the resources.
- There are three main approaches to detect deadlocks in distributed systems:
  - Centralized approach: This involves designating a single node as the deadlock detector, which collects information from all other nodes and constructs a global wait-for graph (WFG) to detect cycles.
  - Hierarchical approach: This involves organizing the nodes into a hierarchy of clusters, where each cluster has a local deadlock detector and a coordinator. The coordinators communicate with each other and construct a global WFG to detect cycles.
  - Distributed approach: This involves using a distributed algorithm, such as edge chasing or probe-based, to detect cycles in the WFG without constructing it explicitly.