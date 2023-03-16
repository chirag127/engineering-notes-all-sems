### Centralized Deadlock Detection

Centralized deadlock detection is a method used in distributed systems to detect deadlocks. In this approach, a single designated site, called the coordinator, is responsible for detecting deadlocks in the system. The following are the key points to note about centralized deadlock detection:

1. The coordinator maintains global wait-for graph (WFG) of the system. Each site sends information about its local wait-for graph to the coordinator, which then constructs the global WFG.

2. The coordinator periodically runs a cycle detection algorithm on the global WFG to check for the presence of deadlocks.

3. If a deadlock is detected, the coordinator initiates a recovery procedure to resolve the deadlock. This may involve aborting one or more processes involved in the deadlock.

4. Centralized deadlock detection has the advantage of being simple to implement and understand. However, it has several disadvantages, including the potential for the coordinator to become a single point of failure and a bottleneck in the system.

5. To mitigate the disadvantages of centralized deadlock detection, several variations of the approach have been proposed, including hierarchical and distributed deadlock detection algorithms.
