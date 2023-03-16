### Edge Chasing Algorithms for Distributed Deadlock Detection

- Edge chasing algorithms are a class of distributed deadlock detection algorithms that use special messages called probes to trace the dependency graph of processes and resources in a distributed system.
- A probe is a triplet (i, j, k) that denotes that the deadlock detection is initiated by process P_i and the message is being sent by the home site of process P_j to the home site of process P_k.
- The probe message follows the edges of the dependency graph from the waiting processes to the blocking processes until either a cycle is detected or all the edges are traversed.
- A cycle in the dependency graph indicates a deadlock, and the processes involved in the cycle are notified to resolve the deadlock.
- Edge chasing algorithms can be classified into two types: the AND model and the OR model, depending on whether a process waits for all or any of its requested resources to be granted.
- The most well-known edge chasing algorithm for the AND model is the Chandy-Misra-Haas algorithm, which has the following steps:

  - Each process maintains a wait-for graph that contains the processes and resources that it is waiting for and the processes and resources that are waiting for it.
  - When a process P_i requests a resource R_k that is held by another process P_j, it sends a probe message (i, i, j) to the home site of P_j.
  - When a process P_j receives a probe message (i, l, j), it checks if it is involved in a deadlock with P_i. If yes, it sends a message to P_i to inform it of the deadlock. If no, it forwards the probe message (i, j, k) to the home site of each process P_k that holds a resource that P_j is waiting for.
  - When a process P_k receives a probe message (i, j, k), it checks if it is involved in a deadlock with P_i. If yes, it sends a message to P_i to inform it of the deadlock. If no, it discards the probe message.

- The advantages of edge chasing algorithms are that they are simple, efficient, and decentralized. They do not require global information or synchronization among the processes or sites.
- The disadvantages of edge chasing algorithms are that they may generate a large number of probe messages, especially in the presence of multiple initiators or concurrent requests. They may also incur false positives, meaning that they may detect a deadlock that does not exist due to the delay or loss of messages.