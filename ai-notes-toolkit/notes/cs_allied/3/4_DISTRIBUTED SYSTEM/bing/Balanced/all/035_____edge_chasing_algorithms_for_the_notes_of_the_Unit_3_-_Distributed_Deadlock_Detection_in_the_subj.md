# Edge Chasing Algorithms

- Edge chasing algorithms are a class of distributed deadlock detection algorithms that use special messages called probes to trace the dependency graph of processes and resources in a distributed system.
- A probe is a triplet (i, j, k) that denotes that the deadlock detection is initiated by process P_i and the message is being sent by the home site of process P_j to the home site of process P_k.
- The probe message follows the edges of the dependency graph from the waiting processes to the blocking processes until either a cycle is detected or all the edges are traversed.
- A cycle is detected when a probe message returns to the initiator process or when a process receives a probe message with its own identifier in the triplet.
- The most well-known edge chasing algorithm is the Chandy-Misra-Haas algorithm, which works for the AND request model, where a process can request multiple resources simultaneously and wait for all of them to be granted.
- The Chandy-Misra-Haas algorithm works as follows:

  - Each process maintains a wait-for graph that contains the processes and resources that it is waiting for and the processes and resources that are waiting for it.
  - When a process P_i initiates a deadlock detection, it sends a probe message (i, i, j) to the home site of each process P_j that it is waiting for.
  - When a process P_j receives a probe message (i, k, j), it checks if it is involved in a deadlock with P_i. If yes, it sends a reply message to P_i indicating the deadlock. If no, it forwards the probe message (i, j, l) to the home site of each process P_l that it is waiting for.
  - When a process P_i receives a reply message from P_j, it knows that there is a deadlock involving P_i and P_j and possibly other processes. It can then take appropriate actions to resolve the deadlock, such as aborting or preempting some processes or resources.