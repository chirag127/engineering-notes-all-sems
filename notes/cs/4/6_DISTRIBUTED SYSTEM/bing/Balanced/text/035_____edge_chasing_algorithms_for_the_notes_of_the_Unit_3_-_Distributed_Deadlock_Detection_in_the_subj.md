### Edge Chasing Algorithms for Distributed Deadlock Detection

- Edge chasing algorithms are a class of distributed deadlock detection algorithms that use special messages called probes to trace the dependency graph of processes and resources in a distributed system.
- A probe is a triplet (i, j, k) that denotes that the deadlock detection is initiated by process P_i and the message is being sent by the home site of process P_j to the home site of process P_k.
- The home site of a process is the site where the process is executing.
- A probe message is sent along the edges of the dependency graph, following the wait-for relations between processes.
- If a probe message returns to the initiator process, it means that a cycle exists in the dependency graph and a deadlock has occurred.
- One of the most well-known edge chasing algorithms is the Chandy-Misra-Haas algorithm, which works for the AND request model, where a process can request multiple resources simultaneously and wait for all of them to be granted.
- The Chandy-Misra-Haas algorithm works as follows:

  - Each process maintains a local wait-for graph that contains the processes that it is waiting for and the processes that are waiting for it.
  - When a process P_i initiates a deadlock detection, it sends a probe message (i, i, j) to the home site of each process P_j that it is waiting for.
  - When the home site of a process P_j receives a probe message (i, k, j), it checks if P_j is waiting for any other process. If not, it discards the message. If yes, it forwards the message to the home site of each process P_l that P_j is waiting for, with the probe message (i, j, l).
  - When the home site of the initiator process P_i receives a probe message (i, j, i), it declares a deadlock and initiates a recovery procedure.

- The advantages of edge chasing algorithms are:

  - They are simple and easy to implement.
  - They do not require global knowledge of the system state or a central coordinator.
  - They can detect deadlocks in a finite number of steps.

- The disadvantages of edge chasing algorithms are:

  - They may generate a large number of probe messages, which consume network bandwidth and processing power.
  - They may cause false positives, where a deadlock is detected even though it does not exist, due to the delay or loss of messages in the network.
  - They may not be able to handle dynamic changes in the system, such as process migration or resource relocation.