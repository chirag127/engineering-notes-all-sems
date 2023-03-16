### Path Pushing Algorithms for Distributed Deadlock Detection

- Path pushing algorithms detect distributed deadlocks by maintaining an explicit global wait-for graph (WFG) for each site of the distributed system  .
- The global WFG is a directed graph that represents the dependencies among the processes in the system. A node in the graph is a process and an edge from node P to node Q means that P is waiting for a resource held by Q  .
- The basic idea is to build and update the global WFG at each site whenever a deadlock computation is performed. A site initiates a deadlock computation when it detects a local deadlock or receives a deadlock computation request from another site  .
- When a site performs a deadlock computation, it sends its local WFG to all neighboring sites, where a neighboring site is a site that shares an edge with the sender in the global WFG  .
- Each site then merges the received local WFGs with its own local WFG to form a new global WFG. The site then checks for cycles in the new global WFG, which indicate the presence of a distributed deadlock  .
- If a cycle is detected, the site initiates a deadlock resolution procedure, which may involve aborting or preempting some processes in the cycle  .
- The advantages of path pushing algorithms are that they can detect deadlocks quickly and accurately, and they do not require any additional messages for deadlock detection  .
- The disadvantages of path pushing algorithms are that they require a lot of storage space and communication bandwidth to maintain and exchange the global WFGs, and they may generate false cycles due to the inconsistency of the global WFGs  .