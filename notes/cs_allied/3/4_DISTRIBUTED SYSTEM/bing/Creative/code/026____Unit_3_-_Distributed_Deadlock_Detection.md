## Unit 3 - Distributed Deadlock Detection

- A deadlock is a condition where a set of processes request resources that are held by other processes in the set.
- Deadlocks can be handled by three strategies: deadlock prevention, deadlock avoidance, and deadlock detection.
- Deadlock prevention and avoidance are impractical in distributed systems, because they require global knowledge and coordination of the system state.
- Deadlock detection is the best approach to handle deadlocks in distributed systems.
- Deadlock detection entails two basic issues: detection of existing deadlocks and resolution of detected deadlocks.
- Detection of existing deadlocks requires examination of the status of process-resource interactions for presence of cyclic wait.
- Resolution of detected deadlocks requires aborting one or more deadlocked processes to break the cycle.
- There are three approaches to detect deadlocks in distributed systems: centralized, hierarchical, and distributed.
- Centralized approach: one node is designated as the deadlock detector and collects the local wait-for graphs from all the nodes to construct a global wait-for graph and check for cycles .
- Hierarchical approach: the nodes are organized into a tree structure and each node collects the local wait-for graphs from its children and sends them to its parent, until the root node constructs a global wait-for graph and checks for cycles.
- Distributed approach: each node maintains its own local wait-for graph and initiates a probe message to detect cycles in the system, using algorithms such as edge chasing, diffusing computation, or echo.
- Each approach has its own advantages and disadvantages in terms of communication cost, detection latency, and fault tolerance.