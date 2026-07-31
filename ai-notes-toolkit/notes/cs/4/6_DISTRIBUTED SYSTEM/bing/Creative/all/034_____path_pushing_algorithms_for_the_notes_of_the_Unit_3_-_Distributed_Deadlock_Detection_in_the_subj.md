# Path Pushing Algorithms

- Path pushing algorithms are a class of distributed deadlock detection algorithms that use an explicit global wait-for graph (WFG) to detect cycles  .
- A WFG is a directed graph that represents the dependencies among processes in a distributed system. A node in the WFG is a process and an edge from node P to node Q means that P is waiting for a resource held by Q  .
- The basic idea of path pushing algorithms is to build a global WFG for each site of the distributed system. A site is a logical unit that contains one or more processes  .
- In this class of algorithms, at each site, whenever a deadlock computation is performed, it sends its local WFG to all the neighboring sites. A neighboring site is a site that has an edge to or from the current site in the global WFG  .
- Each site maintains a local WFG that contains the nodes and edges of the processes at that site, as well as the nodes and edges of the processes at the neighboring sites that are reachable from the current site  .
- Each site also maintains a path matrix that records the paths from the processes at the current site to the processes at the neighboring sites. A path is a sequence of nodes and edges in the WFG that represents a dependency chain  .
- When a site receives a local WFG from a neighboring site, it updates its own local WFG and path matrix by adding or deleting nodes and edges, and by merging or splitting paths. It also sends its updated local WFG to all its neighboring sites  .
- A site detects a deadlock when it finds a cycle in its local WFG. A cycle is a path that starts and ends at the same node. A cycle indicates that there is a circular dependency among the processes in the cycle, and thus they are deadlocked  .
- A site initiates a deadlock resolution when it detects a deadlock. It sends a message to all the processes in the cycle, asking them to release their resources or abort. It also informs the neighboring sites about the deadlock resolution  .
- Path pushing algorithms have the advantage of being simple and efficient, as they only require local information and communication. They also have the disadvantage of being prone to false deadlocks, as they may detect cycles that do not exist in the global WFG  .

: https://www.javatpoint.com/deadlock-detection-in-distributed-systems
: https://www.geeksforgeeks.org/deadlock-handling-strategies-in-distributed-system/
: https://www.cs.uic.edu/~ajayk/Chapter10.pdf