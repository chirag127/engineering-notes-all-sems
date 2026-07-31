### Path Pushing Algorithms

- Path pushing algorithms detect distributed deadlocks by maintaining an explicit global wait-for graph (WFG) at each site of the distributed system .
- The global WFG is constructed by sending the local WFG of each site to all its neighboring sites whenever a deadlock computation is performed .
- The global WFG contains all the edges of the local WFGs and the edges between the sites that are waiting for resources from other sites .
- A site initiates a deadlock computation when it detects a local deadlock or receives a request from another site .
- A site detects a global deadlock if it finds a cycle in its global WFG that includes itself .
- A site can resolve a global deadlock by aborting one of the processes involved in the cycle or sending a message to another site to abort a process .
- Path pushing algorithms have the advantage of reducing the number of messages exchanged for deadlock detection, but they have the disadvantage of increasing the storage and computation overhead at each site .