### Centralized Deadlock Detection

- This is a technique used in distributed systems to handle deadlock detection.
- According to this technique, the system maintains one **global wait-for graph** in a single chosen site, which is named as **deadlock-detection coordinator**.
- The global wait-for graph is a directed graph that represents the waiting relationships among processes and resources in the system.
- Each site in the system periodically sends its local wait-for graph to the coordinator, which then merges them to form the global wait-for graph .
- The coordinator periodically runs a **cycle detection algorithm** on the global wait-for graph to check for the existence of deadlocks .
- If a deadlock is detected, the coordinator selects one or more processes to abort and sends a message to the corresponding sites to terminate them .
- The advantages of this technique are:
  - It is simple and easy to implement.
  - It reduces the communication overhead and the frequency of deadlock detection as compared to the distributed approach.
- The disadvantages of this technique are:
  - It introduces a single point of failure and a performance bottleneck in the coordinator.
  - It may not reflect the current state of the system accurately due to the delays in sending and receiving the local wait-for graphs.
  - It may detect false or phantom deadlocks due to the inconsistency of the global wait-for graph.