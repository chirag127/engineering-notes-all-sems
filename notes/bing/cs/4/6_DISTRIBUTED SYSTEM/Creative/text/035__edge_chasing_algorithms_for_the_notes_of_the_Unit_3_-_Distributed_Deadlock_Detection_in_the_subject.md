### Edge Chasing Algorithms for Distributed Deadlock Detection

- Edge chasing algorithms are a class of distributed deadlock detection algorithms that use special messages called probes to trace the dependency graph of processes and resources in a distributed system.
- A probe is a triplet (i, j, k) that denotes that the deadlock detection is initiated by process P_i and the message is being sent by the home site of process P_j to the home site of process P_k.
- The probe message follows the edges of the dependency graph from the waiting processes to the blocking processes until either a cycle is detected or the probe reaches a process that is not waiting for any resource.
- A cycle is detected when a probe message returns to the initiator process or to a process that has already received the same probe message.
- Edge chasing algorithms can be classified into two types: the AND model and the OR model, depending on whether a process can request multiple resources simultaneously or not.
- The AND model assumes that a process can request multiple resources at the same time and it must acquire all of them before proceeding. The OR model assumes that a process can request one resource at a time and it can proceed with any of them.
- The most well-known edge chasing algorithm for the AND model is the Chandy-Misra-Haas algorithm, which is based on the following rules:

  - Rule 1: A process P_i initiates a deadlock detection by sending a probe message (i, i, j) to the home site of process P_j, where P_j is the process that holds the resource that P_i is waiting for.
  - Rule 2: When the home site of process P_j receives a probe message (i, k, j), it forwards the message to P_j. If P_j is not waiting for any resource, it discards the message. Otherwise, it sends a probe message (i, j, l) to the home site of process P_l, where P_l is the process that holds the resource that P_j is waiting for.
  - Rule 3: When a process P_i receives a probe message (i, k, i), it detects a deadlock and initiates a recovery procedure. When a process P_j receives a probe message (i, k, j) that it has already received before, it discards the message.

- The most well-known edge chasing algorithm for the OR model is the Huang algorithm, which is based on the following rules:

  - Rule 1: A process P_i initiates a deadlock detection by sending a probe message (i, i, j) to the home site of process P_j, where P_j is one of the processes that holds a resource that P_i is waiting for.
  - Rule 2: When the home site of process P_j receives a probe message (i, k, j), it forwards the message to P_j. If P_j is not waiting for any resource, it discards the message. Otherwise, it sends a probe message (i, j, l) to the home site of process P_l, where P_l is one of the processes that holds a resource that P_j is waiting for.
  - Rule 3: When a process P_i receives a probe message (i, k, i), it detects a deadlock and initiates a recovery procedure. When a process P_j receives a probe message (i, k, j) that it has already received before, it discards the message. Additionally, when a process P_j receives a probe message (i, k, j) that has a different value of k than the previous probe message from the same initiator, it discards the previous probe message and forwards the new one.

- Edge chasing algorithms have the advantages of being simple, efficient, and scalable, as they only require local information and communication. However, they also have some drawbacks, such as the possibility of false deadlock detection, the need for unique identifiers for probe messages, and the overhead of maintaining and forwarding probe messages.