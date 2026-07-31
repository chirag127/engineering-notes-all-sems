### Centralized Deadlock Detection

Centralized deadlock detection is a method used in distributed systems to detect deadlocks. In this method, a single designated site, called the coordinator, is responsible for detecting deadlocks. The coordinator maintains global wait-for graph (WFG) and periodically runs a cycle detection algorithm to detect deadlocks.

The following are the key points to note about centralized deadlock detection:

1. The coordinator site is responsible for maintaining the global wait-for graph (WFG) and running the cycle detection algorithm.
2. The other sites in the distributed system send information about their local wait-for graphs to the coordinator.
3. The coordinator merges the local wait-for graphs to form the global wait-for graph.
4. The coordinator runs a cycle detection algorithm on the global wait-for graph to detect deadlocks.
5. If a deadlock is detected, the coordinator initiates a recovery procedure to resolve the deadlock.
6. Centralized deadlock detection has the advantage of simplicity, but it can be a bottleneck and a single point of failure.
