### Edge Chasing Algorithms for Distributed Deadlock Detection

- Edge chasing algorithms are a class of distributed deadlock detection algorithms that use special messages called probes to trace the dependency graph of processes and resources in a distributed system.
- A probe is a triplet (i, j, k) that denotes that the deadlock detection is initiated by process P_i and the message is being sent by the home site of process P_j to the home site of process P_k.
- The probe message follows the edges of the dependency graph from the initiator to the blocked processes and back to the initiator, forming a cycle if a deadlock exists.
- The most common edge chasing algorithm is the Chandy-Misra-Haas algorithm, which works for the AND request model, where a process can request multiple resources simultaneously and wait for all of them to be granted.
- The Chandy-Misra-Haas algorithm works as follows:

  - Each process maintains a wait-for graph (WFG) that contains the processes and resources that it is waiting for or holding.
  - When a process P_i initiates a deadlock detection, it sends a probe (i, i, j) to the home site of each process P_j that it is waiting for in its WFG.
  - When a process P_j receives a probe (i, k, j) from the home site of process P_k, it does the following:
    - If P_j is not waiting for any other process, it discards the probe.
    - If P_j is the initiator P_i, it detects a deadlock and terminates the detection.
    - If P_j is waiting for some other processes, it adds the edge (k, j) to its WFG and sends a probe (i, j, l) to the home site of each process P_l that it is waiting for in its WFG.
  - The algorithm terminates when either a deadlock is detected or all the probes are discarded.

- The advantages of edge chasing algorithms are:

  - They are simple and efficient, requiring only O(n) messages per detection, where n is the number of processes in the system.
  - They do not require global knowledge of the system state or a central coordinator.
  - They can detect deadlocks involving multiple resources and cycles of arbitrary length.

- The disadvantages of edge chasing algorithms are:

  - They may generate false positives, detecting cycles that do not correspond to actual deadlocks, due to the asynchronous nature of the system and the possibility of message delays or losses.
  - They may generate false negatives, missing some deadlocks, due to the concurrent initiation of multiple detections or the concurrent execution of requests and releases.
  - They may incur high communication overhead, especially in systems with high resource contention and frequent deadlock detection.