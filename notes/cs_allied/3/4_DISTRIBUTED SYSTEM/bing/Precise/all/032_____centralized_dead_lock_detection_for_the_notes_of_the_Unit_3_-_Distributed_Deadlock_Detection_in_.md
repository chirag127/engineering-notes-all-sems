# Centralized Deadlock Detection

Centralized deadlock detection is a method for detecting deadlocks in a distributed system. In this approach, a single designated node, called the coordinator, is responsible for detecting deadlocks. The following are the key points to note about centralized deadlock detection:

1. The coordinator maintains a global wait-for graph (WFG) that represents the dependencies between transactions in the system.
2. Each node in the system periodically sends information about its local wait-for graph to the coordinator.
3. The coordinator merges the local wait-for graphs to construct the global wait-for graph.
4. The coordinator then checks the global wait-for graph for cycles. If a cycle is detected, it indicates the presence of a deadlock.
5. The coordinator can then initiate a recovery procedure to resolve the deadlock, such as aborting one or more transactions involved in the deadlock.

Centralized deadlock detection has the advantage of being relatively simple to implement and understand. However, it has some drawbacks, such as the potential for the coordinator to become a bottleneck and the need for all nodes to periodically send information to the coordinator, which can generate a significant amount of network traffic. Additionally, if the coordinator fails, the entire deadlock detection mechanism is disrupted.
