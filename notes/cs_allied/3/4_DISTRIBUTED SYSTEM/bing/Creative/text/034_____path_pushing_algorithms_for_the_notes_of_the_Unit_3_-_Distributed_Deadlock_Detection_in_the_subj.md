### Path Pushing Algorithms for Distributed Deadlock Detection

- Path pushing algorithms detect distributed deadlocks by maintaining an explicit global wait-for graph (WFG) at each site of the distributed system  .
- The global WFG is a directed graph that represents the dependencies among the processes in the system. A node in the graph is a process and an edge from node P to node Q means that P is waiting for a resource held by Q  .
- The basic idea is to build and update the global WFG at each site whenever a process requests, releases, or blocks on a resource. The global WFG is also exchanged among the neighboring sites periodically or on demand  .
- A site can initiate a deadlock detection by traversing its local copy of the global WFG and checking for cycles. A cycle in the global WFG indicates a deadlock among the processes involved in the cycle  .
- The advantages of path pushing algorithms are that they can detect deadlocks quickly and accurately, and they do not require any additional messages for deadlock detection  .
- The disadvantages of path pushing algorithms are that they require a lot of storage space and communication bandwidth to maintain and exchange the global WFG, and they may incur high overhead for updating the global WFG frequently  .