# Edge Chasing Algorithms for Distributed Deadlock Detection

- Edge chasing algorithms are a class of distributed deadlock detection algorithms that use special messages called probes to trace the dependency graph of processes and resources in a distributed system.
- A probe is a triplet (i, j, k) that denotes that the deadlock detection is initiated by process P_i and the message is being sent by the home site of process P_j to the home site of process P_k.
- The home site of a process is the site where the process is executing.
- A probe message is sent along the edges of the wait-for graph, which represents the requests and waits of processes for resources in the system.
- If a probe message returns to the initiator process, it means that a cycle exists in the wait-for graph and a deadlock has occurred.
- One of the most well-known edge chasing algorithms is the Chandy-Misra-Haas algorithm, which works for the AND request model, where a process can request multiple resources simultaneously and wait for all of them to be granted before proceeding.
- The Chandy-Misra-Haas algorithm works as follows:

  - Each process maintains a local wait-for graph that contains only the nodes and edges relevant to the process.
  - When a process P_i requests a resource R_k from another process P_j, it sends a request message to P_j and adds an edge (P_i, R_k) to its local wait-for graph.
  - When a process P_j receives a request message from another process P_i for a resource R_k that it holds, it checks if it is waiting for any other resource. If not, it grants the resource to P_i and removes the edge (P_j, R_k) from its local wait-for graph. If yes, it adds an edge (R_k, P_i) to its local wait-for graph and sends a probe message (i, j, i) to P_i, indicating that P_j is waiting for a resource that P_i holds.
  - When a process P_i receives a probe message (i, j, k) from another process P_j, it checks if k is equal to i. If yes, it means that a cycle has been detected and P_i initiates the deadlock resolution. If no, it checks if it is waiting for any other resource. If not, it discards the probe message. If yes, it forwards the probe message (i, j, k) to all the processes that hold the resources that P_i is waiting for.
  - When a process P_i receives a grant message from another process P_j for a resource R_k that it requested, it removes the edge (P_i, R_k) from its local wait-for graph and checks if it has received all the resources that it requested. If yes, it proceeds with its execution and releases the resources when done. If no, it continues to wait for the remaining resources.

- The advantages of edge chasing algorithms are that they are simple, efficient, and scalable, as they only involve local information and minimal communication overhead.
- The disadvantages of edge chasing algorithms are that they may generate false positives, as they do not consider the global state of the system, and that they may cause unnecessary delays, as they do not allow partial grants of resources.