# Centralized Deadlock Detection

- This is a technique used in distributed systems to handle deadlock detection.
- According to this technique, the system maintains one global wait-for graph in a single chosen site, which is named as deadlock-detection coordinator.
- The coordinator collects information about the local wait-for graphs of each site and constructs the global wait-for graph.
- The coordinator periodically runs a deadlock detection algorithm on the global wait-for graph and identifies any cycles that indicate deadlocks.
- The coordinator then informs the involved sites to abort one or more processes to resolve the deadlock.
- The advantages of this technique are simplicity and low communication overhead.
- The disadvantages of this technique are the dependency on a single coordinator, which can be a bottleneck or a single point of failure, and the possibility of false deadlocks due to stale information .