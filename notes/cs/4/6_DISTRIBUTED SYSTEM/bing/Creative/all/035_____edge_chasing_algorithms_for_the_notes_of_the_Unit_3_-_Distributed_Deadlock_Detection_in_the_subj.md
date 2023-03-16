# Edge Chasing Algorithms for Distributed Deadlock Detection

- Edge chasing algorithms are a class of distributed deadlock detection algorithms that use special messages called probes to trace the dependency graph of processes and resources in a distributed system  .
- A probe is a triplet (i, j, k) that denotes that the deadlock detection is initiated by process P_i and the message is being sent by the home site of process P_j to the home site of process P_k .
- The probe message follows the edges of the dependency graph from the waiting processes to the blocking processes until either a cycle is detected or all the edges are traversed  .
- A cycle is detected when a probe message returns to the initiator process or when a process receives a probe message with its own identifier in the triplet  .
- If a cycle is detected, then a deadlock exists and the processes involved in the cycle are notified to resolve the deadlock  .
- If no cycle is detected, then no deadlock exists and the probe messages are discarded  .
- Edge chasing algorithms are also known as Chandy-Misra-Haas's algorithms, as they were proposed by K. Mani Chandy, Jayadev Misra, and Laura M. Haas in 1983  .
- Edge chasing algorithms can be applied to different request models, such as AND model, OR model, and AND-OR model, depending on the type of resource requests made by the processes .
- Edge chasing algorithms have some advantages and disadvantages over other classes of distributed deadlock detection algorithms, such as path-pushing, diffusion computation, and global state detection .
- Some advantages are:
  - Edge chasing algorithms are simple and easy to implement.
  - Edge chasing algorithms do not require the maintenance of global or local wait-for graphs .
  - Edge chasing algorithms can detect deadlocks in a distributed system without a central coordinator or a leader process .
- Some disadvantages are:
  - Edge chasing algorithms may generate a large number of probe messages, which can increase the network traffic and the message overhead .
  - Edge chasing algorithms may detect false deadlocks, which are cycles that do not involve all the processes in the system .
  - Edge chasing algorithms may not detect some deadlocks, which are cycles that involve processes that are not reachable by the probe messages .