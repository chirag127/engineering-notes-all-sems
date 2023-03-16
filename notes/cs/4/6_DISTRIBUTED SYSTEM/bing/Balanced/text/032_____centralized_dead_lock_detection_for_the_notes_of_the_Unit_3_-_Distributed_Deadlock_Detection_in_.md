### Centralized Deadlock Detection

- This is a technique used in distributed systems to handle deadlock detection.
- According to this approach, the system maintains one **global wait-for graph** in a single chosen site, which is named as **deadlock-detection coordinator**.
- The coordinator collects information about the **local wait-for graphs** of each site and constructs the global wait-for graph.
- The coordinator periodically runs a **cycle detection algorithm** on the global wait-for graph to detect deadlocks.
- If a deadlock is detected, the coordinator selects a victim process and sends an **abort message** to the site where the process is located.
- The advantages of this approach are:
  - It is simple and easy to implement.
  - It reduces the communication overhead and the number of messages exchanged.
- The disadvantages of this approach are:
  - It introduces a single point of failure and a performance bottleneck at the coordinator.
  - It requires the coordinator to have a global view of the system, which may not be feasible or accurate in some cases.
  - It may detect false or phantom deadlocks due to the delay in propagating the information to the coordinator.