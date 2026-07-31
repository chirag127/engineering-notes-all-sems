## Unit 3 - Distributed Deadlock Detection

- A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
- Deadlock detection is the process of identifying the existence of a deadlock in a system.
- Distributed deadlock detection is the process of detecting deadlocks in a distributed system, where processes and resources are located on different nodes connected by a network.
- Distributed deadlock detection can be classified into two categories: global and local.
  - Global deadlock detection involves collecting information from all nodes and applying a centralized algorithm to detect deadlocks.
  - Local deadlock detection involves applying a distributed algorithm that uses local information and message passing to detect deadlocks.
- Distributed deadlock detection can also be classified into two approaches: edge-chasing and probe-based.
  - Edge-chasing is a technique that uses control messages (called probes) to trace the dependency graph of processes and resources. A deadlock is detected when a probe returns to its originator or when a cycle is formed in the graph.
  - Probe-based is a technique that uses special messages (called probes) to initiate deadlock detection at some nodes. A probe contains information about the sender, the receiver, and the resources requested by the sender. A deadlock is detected when a probe reaches a node that is waiting for a resource held by the sender or when a probe returns to its originator.