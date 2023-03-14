### Path-pushing algorithms for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- Path-pushing algorithms detect distributed deadlocks by maintaining an explicit global wait-for graph (WFG) for each site of the distributed system .
- A WFG is a directed graph where nodes are processes and there is an edge from node P1 to node P2 if P1 is blocked and is waiting for P2 to release some resource.
- A system is deadlocked if and only if there exists a directed cycle or knot in the WFG.
- The main idea of path-pushing algorithms is to create a global WFG for each site by sending the local WFG to all neighboring sites.
- When a site in this class of algorithms performs a deadlock computation, it sends its local WFG to all neighboring sites.
- Each site then merges the received WFGs with its own WFG and checks for cycles.
- If a cycle is detected, then a deadlock is declared and a recovery action is taken.
- The advantage of path-pushing algorithms is that they can detect deadlocks quickly and accurately.
- The disadvantage of path-pushing algorithms is that they require a lot of communication and storage overhead, as each site has to maintain and exchange the entire WFG.
- An example of a path-pushing algorithm is the Chandy-Misra-Haas algorithm.