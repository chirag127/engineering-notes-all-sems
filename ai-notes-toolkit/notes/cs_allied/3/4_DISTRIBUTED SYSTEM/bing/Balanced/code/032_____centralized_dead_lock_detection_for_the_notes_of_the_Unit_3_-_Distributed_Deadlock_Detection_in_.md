### Centralized Deadlock Detection

- This is a technique used in distributed systems to handle deadlock detection.
- According to this approach, the system maintains one **Global wait-for graph** in a single chosen site, which is named as **deadlock-detection coordinator**.
- The coordinator collects information about the local wait-for graphs of all the sites and constructs the global wait-for graph.
- The coordinator periodically runs a deadlock detection algorithm on the global wait-for graph to identify any cycles.
- If a cycle is detected, the coordinator selects one or more processes to abort and sends a message to the corresponding sites to terminate them.
- The advantages of this approach are:
  - It is simple and easy to implement.
  - It reduces the communication overhead and the complexity of the algorithm.
- The disadvantages of this approach are:
  - It introduces a single point of failure and a performance bottleneck in the system.
  - It requires the coordinator to have a global view of the system, which may not be feasible or accurate in a dynamic and asynchronous environment.
  - It may detect false or phantom deadlocks due to the delay in propagating the information to the coordinator.