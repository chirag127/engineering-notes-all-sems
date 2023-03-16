### Edge Chasing Algorithms for Distributed Deadlock Detection

- Edge chasing algorithms are a class of distributed deadlock detection algorithms that use special messages called probes to trace the dependency graph of processes and resources in a distributed system.
- A probe is a triplet (i, j, k) that denotes that the deadlock detection is initiated by process P_i and the message is being sent by the home site of process P_j to the home site of process P_k.
- The probe message follows the edges of the dependency graph from the waiting processes to the blocking processes until either a cycle is detected or the probe reaches a process that is not waiting for any resource.
- A cycle in the dependency graph indicates a deadlock, and the processes involved in the cycle are notified by the probe message.
- Edge chasing algorithms can be applied to different request models, such as AND model, OR model, or AND-OR model, depending on the type of requests that processes can make for resources.
- One of the most well-known edge chasing algorithms is the Chandy-Misra-Haas algorithm for the AND model, which is based on the following rules:

  - Rule 1: A process P_i initiates a deadlock detection by sending a probe (i, i, j) to the home site of process P_j, where P_j is the process that P_i is waiting for.
  - Rule 2: A process P_j receives a probe (i, k, j) from the home site of process P_k. If P_j is not waiting for any resource, it discards the probe. Otherwise, it sends the probe (i, j, l) to the home site of process P_l, where P_l is the process that P_j is waiting for.
  - Rule 3: A process P_i receives a probe (i, k, i) from the home site of process P_k. This means that a cycle has been detected and P_i is involved in a deadlock. P_i informs all the processes in the cycle about the deadlock and terminates the deadlock detection.

- Edge chasing algorithms have the advantages of being simple, efficient, and scalable, as they do not require global information or synchronization among the sites. However, they also have some drawbacks, such as:

  - They may generate false positives, i.e., detect deadlocks that do not exist, due to the presence of concurrent requests and releases of resources.
  - They may generate multiple probes for the same deadlock, resulting in redundant messages and computations.
  - They may not terminate if there are orphan messages, i.e., messages that are lost or delayed in the network.