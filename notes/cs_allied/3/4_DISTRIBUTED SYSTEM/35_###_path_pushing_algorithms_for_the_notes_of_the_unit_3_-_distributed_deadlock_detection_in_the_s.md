### path pushing algorithms for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

Path pushing algorithms are a type of decentralized algorithm used for deadlock detection in distributed systems. The basic idea behind path pushing algorithms is to have each node in the system periodically push a message along a path through the network, and if a cycle is detected, a deadlock is declared.

There are two main types of path pushing algorithms:
1. Depth-first search (DFS) based algorithms: nodes perform a DFS traversal of the network and push messages along the path.
2. Breadth-first search (BFS) based algorithms: nodes perform a BFS traversal of the network and push messages along the path.

Both DFS-based and BFS-based path pushing algorithms have advantages and disadvantages. DFS-based algorithms are typically faster, but can miss some deadlocks, while BFS-based algorithms are slower but more comprehensive.

In summary, path pushing algorithms are a type of decentralized algorithm used for deadlock detection in distributed systems, and can be based on either a depth-first search (DFS) or a breadth-first search (BFS) traversal of the network.
