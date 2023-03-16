# Centralized Deadlock Detection

- Centralized deadlock detection is a technique used in distributed systems to handle deadlock detection by maintaining a global wait-for graph in a single chosen site, called the deadlock-detection coordinator.
- The coordinator collects information about the local wait-for graphs of each site and constructs the global wait-for graph by merging them.
- The coordinator periodically runs a cycle detection algorithm on the global wait-for graph to detect deadlocks.
- If a deadlock is detected, the coordinator selects a victim process to abort and sends a message to the corresponding site to terminate the process.
- The advantages of centralized deadlock detection are simplicity, low communication overhead, and easy implementation.
- The disadvantages of centralized deadlock detection are single point of failure, scalability issues, and lack of autonomy.