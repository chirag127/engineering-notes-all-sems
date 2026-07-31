### Edge Chasing Algorithms for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

In the field of distributed systems, deadlock detection is a crucial component to ensure the system operates effectively. Edge chasing algorithms are one approach to detecting deadlocks in a distributed system. Here are some important points to understand about edge chasing algorithms:

- Edge chasing algorithms rely on a graph representation of the distributed system, where nodes represent processes and edges represent resource requests.
- In edge chasing algorithms, each process maintains a wait-for graph which stores the resources it is waiting for and the processes it is waiting on.
- When a process requests a resource that is currently held by another process, it sends a probe message to the process holding the resource.
- If the holding process is also waiting for resources, it forwards the probe message to the processes it is waiting on.
- This process of forwarding the probe message along the edges of the wait-for graph continues until either a process is found that is not waiting for any resources, or a cycle is detected in the wait-for graph.
- If a cycle is detected, it indicates a deadlock has occurred, and the processes involved in the cycle can be identified and dealt with accordingly.
- Edge chasing algorithms have advantages over other deadlock detection algorithms, such as reduced message overhead and the ability to detect deadlocks in a distributed system without requiring a centralized coordinator.

It is important to understand edge chasing algorithms and their role in distributed deadlock detection to ensure the smooth operation of distributed systems.