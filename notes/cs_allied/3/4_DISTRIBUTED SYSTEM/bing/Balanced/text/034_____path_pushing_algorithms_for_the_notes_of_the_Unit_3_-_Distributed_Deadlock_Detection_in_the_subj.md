### Path Pushing Algorithms

- Path pushing algorithms detect distributed deadlocks by maintaining an explicit global wait-for graph (WFG) at each site of the distributed system .
- The global WFG is constructed by sending the local WFG of each site to all its neighboring sites whenever a deadlock computation is performed .
- The neighboring sites are those that share a common resource or process in the WFG.
- The global WFG is updated whenever a new edge is added or deleted in the local WFG due to a request or a release of a resource.
- The global WFG contains all the edges of the local WFGs and may also contain some false edges that do not exist in the actual WFG of the system.
- A false edge is an edge that represents a dependency that has already been resolved but has not been reflected in the global WFG yet.
- A site can detect a deadlock by checking if there is a cycle in its global WFG that involves one of its local processes .
- If a cycle is detected, the site can initiate a recovery action by sending a message to the processes involved in the cycle.
- The advantages of path pushing algorithms are that they are simple, efficient, and scalable.
- The disadvantages of path pushing algorithms are that they require a lot of communication and storage overhead, and they may detect false deadlocks due to false edges.