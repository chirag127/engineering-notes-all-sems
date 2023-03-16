# Path Pushing Algorithms for Distributed Deadlock Detection

- Path pushing algorithms detect distributed deadlocks by maintaining an explicit global wait-for graph (WFG) at each site of the distributed system .
- The global WFG is a directed graph that represents the dependencies among the processes in the system. A node in the graph is a process and an edge from node P to node Q means that P is waiting for a resource held by Q.
- The basic idea is to build and update the global WFG at each site whenever a deadlock computation is performed. A site initiates a deadlock computation when it detects a local deadlock or receives a request from another site.
- When a site performs a deadlock computation, it sends its local WFG to all neighboring sites, where a neighboring site is a site that shares a common edge with the sender in the global WFG.
- Each site that receives a local WFG merges it with its own local WFG to form a new global WFG and sends the updated global WFG to its neighbors.
- This process continues until all sites have the same global WFG, which reflects the current state of the system.
- A site can detect a distributed deadlock by checking if there is a cycle in the global WFG that involves one of its local processes.
- The advantages of path pushing algorithms are that they can detect deadlocks quickly and accurately, and they do not require any additional messages for deadlock detection.
- The disadvantages of path pushing algorithms are that they require a lot of storage space and communication bandwidth to maintain and exchange the global WFG, and they may cause false deadlock detection due to the delay and inconsistency of the global WFG.