### Edge Chasing Algorithms for Distributed Deadlock Detection

- Edge chasing algorithms are a class of distributed deadlock detection algorithms that use special messages called probes to trace the dependency graph of processes and resources in a distributed system.
- A probe is a triplet (i, j, k) that denotes that the deadlock detection is initiated by process P_i and the message is being sent by the home site of process P_j to the home site of process P_k.
- The probe message follows the edges of the dependency graph from the waiting processes to the blocking processes until either a cycle is detected or all the edges are traversed.
- A cycle in the dependency graph indicates a deadlock, and the processes involved in the cycle are notified to resolve the deadlock.
- Edge chasing algorithms can be classified into two types: the AND model and the OR model, depending on whether a process waits for all or any of its requested resources to be granted.
- The most well-known edge chasing algorithm for the AND model is the Chandy-Misra-Haas algorithm, which works as follows:

  - Each process maintains a wait-for graph that contains the processes and resources that it depends on.
  - When a process P_i initiates a deadlock detection, it sends a probe (i, i, j) to the home site of each process P_j that it is waiting for.
  - When a process P_j receives a probe (i, k, j) from the home site of process P_k, it checks if it is involved in a deadlock with P_i. If yes, it sends a reply to P_i indicating the deadlock. If no, it forwards the probe (i, j, l) to the home site of each process P_l that it is waiting for.
  - When a process P_i receives a reply from P_j indicating a deadlock, it checks if the reply is consistent with its wait-for graph. If yes, it terminates itself or aborts one of its requests to resolve the deadlock. If no, it ignores the reply.

- Edge chasing algorithms for the OR model are more complex and require additional information to be maintained and exchanged by the processes. One example of such an algorithm is the Menasce-Muntz algorithm, which works as follows:

  - Each process maintains a wait-by graph that contains the processes and resources that depend on it.
  - When a process P_i initiates a deadlock detection, it sends a probe (i, i, j) to the home site of each process P_j that it is waiting for, along with its wait-by graph.
  - When a process P_j receives a probe (i, k, j) from the home site of process P_k, along with a wait-by graph G, it checks if it is involved in a deadlock with P_i. If yes, it sends a reply to P_i indicating the deadlock. If no, it updates its wait-by graph with G and forwards the probe (i, j, l) to the home site of each process P_l that it is waiting for, along with its updated wait-by graph.
  - When a process P_i receives a reply from P_j indicating a deadlock, it checks if the reply is consistent with its wait-by graph. If yes, it terminates itself or aborts one of its requests to resolve the deadlock. If no, it ignores the reply.

- Edge chasing algorithms have the advantages of being simple, efficient, and scalable, as they only require local information and minimal communication overhead. However, they also have some drawbacks, such as the possibility of false deadlock detection, the need for unique identifiers for each probe, and the lack of coordination among multiple initiators of deadlock detection.