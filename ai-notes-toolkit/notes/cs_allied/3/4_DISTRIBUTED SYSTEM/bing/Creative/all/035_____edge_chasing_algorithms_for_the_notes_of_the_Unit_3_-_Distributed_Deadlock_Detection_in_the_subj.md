# Edge Chasing Algorithms

- Edge chasing algorithms are a class of distributed deadlock detection algorithms that use special messages called probes to detect cycles in the wait-for graph of processes.
- A probe is a triplet (i, j, k) that denotes that the deadlock detection is initiated by process P_i and the message is sent by the home site of process P_j to the home site of process P_k.
- The home site of a process is the site where the process is located and where its local wait-for graph is maintained.
- The probe message contains the information about the initiator of the deadlock detection and the path of the probe in the global wait-for graph.
- The algorithm works as follows:
  - When a process P_i initiates a deadlock detection, it sends a probe (i, i, j) to the home site of each process P_j that it is waiting for.
  - When the home site of a process P_j receives a probe (i, k, j), it checks if P_j is waiting for any other process. If not, it discards the probe. If yes, it appends P_j to the probe and forwards it to the home site of each process P_l that P_j is waiting for, as (i, j, l).
  - When the home site of a process P_i receives a probe (i, k, i), it means that a cycle involving P_i has been detected and a deadlock exists. It informs P_i about the deadlock and the processes involved in the cycle.
  - The algorithm terminates when either a deadlock is detected or all the probes are discarded.
- An example of edge chasing algorithm is the Chandy-Misra-Haas algorithm, which is designed for the AND request model, where a process waits for all the resources it requests before proceeding.
- The advantages of edge chasing algorithms are that they are simple, efficient, and scalable. They do not require global synchronization or centralized control. They only involve the processes and sites that are potentially deadlocked.
- The disadvantages of edge chasing algorithms are that they may generate a large number of probe messages, which can increase the network traffic and delay the deadlock detection. They also require each site to maintain the local wait-for graph of its processes, which can be costly in terms of memory and update overhead.