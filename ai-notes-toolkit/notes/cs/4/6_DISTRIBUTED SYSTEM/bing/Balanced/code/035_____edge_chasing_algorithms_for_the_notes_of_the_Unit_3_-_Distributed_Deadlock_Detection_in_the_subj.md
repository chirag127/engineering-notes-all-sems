### Edge Chasing Algorithms for Distributed Deadlock Detection

- Edge chasing algorithms are a class of distributed deadlock detection algorithms that use special messages called probes to trace the dependency graph of processes and resources in a distributed system.
- A probe is a triplet (i, j, k) that denotes that the deadlock detection is initiated by process P_i and the message is being sent by the home site of process P_j to the home site of process P_k.
- The probe message follows the edges of the dependency graph from the waiting processes to the blocking processes until either a cycle is detected or all the edges are traversed.
- A cycle is detected when a probe message returns to the initiator process or when a process receives a probe message with its own identifier in the triplet.
- Edge chasing algorithms can be applied to different request models, such as AND model, OR model, or general model, depending on the type of requests that processes can make for resources.
- One of the most well-known edge chasing algorithms is the Chandy-Misra-Haas algorithm for the AND model, which assumes that a process can request multiple resources simultaneously and must acquire all of them to proceed.
- The Chandy-Misra-Haas algorithm works as follows:

  - Each process maintains a wait-for graph that records its dependency on other processes.
  - When a process P_i initiates a deadlock detection, it sends a probe message (i, i, j) to the home site of each process P_j that it is waiting for.
  - When a process P_j receives a probe message (i, k, j), it checks if it is dependent on any other process. If not, it discards the message. If yes, it does the following:
    - If j = i, then a cycle is detected and P_j informs P_i of the deadlock.
    - If j != i and P_j has not participated in the deadlock detection initiated by P_i before, then P_j records i in its local state and sends a probe message (i, j, l) to the home site of each process P_l that it is waiting for.
    - If j != i and P_j has participated in the deadlock detection initiated by P_i before, then P_j discards the message.
  - When a process P_i receives a deadlock notification from another process, it informs all the processes that are dependent on it to abort and releases all the resources that it holds.

- The advantages of edge chasing algorithms are that they are simple, efficient, and scalable. They do not require global information or synchronization among processes or sites. They only generate probe messages when a deadlock is suspected and they terminate the detection when a cycle is found or when all the edges are traversed.
- The disadvantages of edge chasing algorithms are that they may generate false positives, meaning that they may detect a cycle that does not correspond to a real deadlock. This can happen when the dependency graph changes dynamically due to resource releases or process terminations. They may also generate duplicate probe messages if multiple processes initiate the deadlock detection concurrently.