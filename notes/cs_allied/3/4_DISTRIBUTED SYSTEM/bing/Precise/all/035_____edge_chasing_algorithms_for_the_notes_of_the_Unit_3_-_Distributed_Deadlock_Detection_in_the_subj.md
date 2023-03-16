# Edge Chasing Algorithms

Edge chasing algorithms are used for distributed deadlock detection in distributed systems. These algorithms are also known as path-pushing algorithms. The basic idea behind edge chasing algorithms is to detect cycles in the wait-for graph of the distributed system.

Here are some key points to remember about edge chasing algorithms:

1. Edge chasing algorithms work by sending probe messages along the edges of the wait-for graph.
2. When a process receives a probe message, it checks if it is waiting for any other process. If it is, it forwards the probe message to the process it is waiting for.
3. If a process receives a probe message that it has already seen, it means that a cycle has been detected in the wait-for graph, indicating a deadlock.
4. Edge chasing algorithms can be classified into two types: diffusing computation and edge chasing.
5. In diffusing computation, the probe messages are sent along the edges of the wait-for graph in a breadth-first manner.
6. In edge chasing, the probe messages are sent along the edges of the wait-for graph in a depth-first manner.
