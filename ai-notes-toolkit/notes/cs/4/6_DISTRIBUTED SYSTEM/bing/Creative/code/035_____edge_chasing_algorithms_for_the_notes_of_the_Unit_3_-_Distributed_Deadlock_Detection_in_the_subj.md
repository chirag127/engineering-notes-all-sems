### Edge Chasing Algorithms for Distributed Deadlock Detection

- Edge chasing algorithms are a class of distributed deadlock detection algorithms that use special messages called probes to trace the dependency graph of processes and resources in a distributed system.
- A probe is a triplet (i, j, k) that denotes that the deadlock detection is initiated by process Pi, and the message is sent by the home site of process Pj to the home site of process Pk.
- The home site of a process is the site where the process is executing, and it is responsible for sending and receiving probes on behalf of the process.
- The algorithm works as follows:
  - When a process Pi initiates a deadlock detection, it sends a probe (i, i, j) to the home site of process Pj, where Pj is the process that Pi is waiting for.
  - When the home site of process Pj receives a probe (i, j, k), it checks if Pj is waiting for any other process Pk. If yes, it forwards the probe (i, j, k) to the home site of process Pk. If no, it discards the probe.
  - When the home site of process Pk receives a probe (i, j, k), it checks if Pk is the same as Pi. If yes, it means that a cycle has been detected, and a deadlock exists. It informs Pi about the deadlock. If no, it repeats the previous step.
  - The algorithm terminates when either a deadlock is detected or all the probes are discarded.
- The algorithm is also known as Chandy-Misra-Haas's algorithm for the AND request model, where a process can request multiple resources simultaneously and wait for all of them to be granted.
- The algorithm has the following properties:
  - It is a distributed algorithm, meaning that it does not require a central coordinator or a global state of the system.
  - It is an edge-chasing algorithm, meaning that it follows the edges of the dependency graph from the waiting nodes to the blocking nodes.
  - It is a probe-based algorithm, meaning that it uses special messages to detect cycles in the dependency graph.
  - It is a local algorithm, meaning that it only involves the sites that are part of the cycle.
  - It is a demand-driven algorithm, meaning that it is initiated only when a process suspects a deadlock.