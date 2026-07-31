# Path Pushing Algorithms

- Path pushing algorithms are a class of distributed deadlock detection algorithms that use an explicit global wait-for graph (WFG) to detect cycles  .
- The main idea is to build a global WFG for each site of the distributed system by sending the local WFG to all the neighboring sites .
- The global WFG is updated whenever a new edge is added or deleted in the local WFG .
- A site initiates a deadlock detection by checking its global WFG for cycles. If a cycle is found, it means that a deadlock exists and the site can initiate a recovery action .
- Path pushing algorithms have the advantage of detecting deadlocks quickly and accurately, but they have the disadvantage of requiring a lot of communication and storage overhead .
- An example of a path pushing algorithm is the Chandy-Misra-Haas algorithm .