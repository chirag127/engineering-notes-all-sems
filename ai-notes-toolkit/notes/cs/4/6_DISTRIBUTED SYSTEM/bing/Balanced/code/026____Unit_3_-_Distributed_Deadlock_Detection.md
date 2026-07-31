## Unit 3 - Distributed Deadlock Detection

- A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
- Deadlock detection is the process of finding out whether a deadlock has occurred or not in a system.
- Distributed deadlock detection is the process of detecting deadlocks in a distributed system, where processes and resources may be located on different nodes connected by a network.
- Distributed deadlock detection can be classified into two categories: centralized and distributed.
- Centralized deadlock detection involves a designated node, called the coordinator, that collects global information about the system and runs a deadlock detection algorithm.
- Distributed deadlock detection involves each node running a local deadlock detection algorithm and exchanging messages with other nodes to detect global deadlocks.
- There are different types of distributed deadlock detection algorithms, such as:
  - Path-pushing algorithms, where each node maintains a wait-for graph and sends it to other nodes along a potential deadlock cycle.
  - Edge-chasing algorithms, where each node sends a probe message to the node it is waiting for, and the probe message is forwarded along the wait-for chain until it either reaches the initiator node (deadlock detected) or a node that is not waiting for anyone (deadlock not detected).
  - Diffusion computation algorithms, where each node initiates a computation to detect a deadlock involving itself, and the computation is propagated to other nodes through messages. The computation terminates when either a deadlock is detected or all nodes have been visited.