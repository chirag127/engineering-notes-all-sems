### Centralized deadlock detection approach in distributed database

- This is a technique used in distributed database systems to handle deadlock detection.
- According to this approach, the system maintains one global wait-for graph in a single chosen site, which is named as the deadlock-detection coordinator.
- The coordinator collects information about the local wait-for graphs of each site and constructs the global wait-for graph.
- The coordinator periodically runs a cycle detection algorithm on the global wait-for graph to detect deadlocks.
- If a deadlock is detected, the coordinator selects a victim process and sends an abort message to the site where the process is located.
- The advantages of this approach are:
  - It is simple and easy to implement.
  - It reduces the communication overhead as only one site is responsible for deadlock detection.
  - It avoids false or phantom deadlocks as the global wait-for graph is consistent.
- The disadvantages of this approach are:
  - It introduces a single point of failure as the coordinator site may crash or become unreachable.
  - It creates a bottleneck as the coordinator site may be overloaded with deadlock detection requests.
  - It may not be scalable as the size of the global wait-for graph may grow with the number of sites and processes.
- A possible mnemonic to remember this approach is: **C**oordinator **C**ollects **C**ycles and **C**hooses **C**andidates to **C**ancel.
- A possible learning trick to understand this approach is to draw a diagram of the global wait-for graph and the local wait-for graphs of each site, and trace the steps of the cycle detection algorithm and the victim selection algorithm.
- An example of a global wait-for graph and a local wait-for graph is shown below:

```
Global wait-for graph:

P1 -> P2 -> P3 -> P4 -> P1 (deadlock cycle)

Local wait-for graph at site 1:

P1 -> P2

Local wait-for graph at site 2:

P2 -> P3

Local wait-for graph at site 3:

P3 -> P4

Local wait-for graph at site 4:

P4 -> P1
```