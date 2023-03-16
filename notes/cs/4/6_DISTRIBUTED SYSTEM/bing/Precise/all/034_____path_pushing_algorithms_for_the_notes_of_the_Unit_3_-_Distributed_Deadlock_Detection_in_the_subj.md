# Path Pushing Algorithms

Path pushing algorithms are a type of distributed deadlock detection algorithm used in distributed systems. These algorithms work by propagating information about wait-for relationships between processes throughout the system. Here are some key points to remember about path pushing algorithms:

1. Path pushing algorithms work by having each process maintain a wait-for graph that represents the wait-for relationships between processes in the system.
2. When a process is blocked and waiting for a resource held by another process, it sends a message to that process to update its wait-for graph.
3. When a process receives a wait-for graph update message, it updates its own wait-for graph and propagates the update to other processes in the system.
4. If a cycle is detected in the wait-for graph, it indicates the presence of a deadlock. The system can then take appropriate action to resolve the deadlock.
5. Path pushing algorithms can be classified into two categories: edge-chasing algorithms and diffusing computation algorithms.
6. Edge-chasing algorithms work by having each process send a probe message along the edges of the wait-for graph to detect cycles.
7. Diffusing computation algorithms work by having each process initiate a computation to detect cycles in the wait-for graph.

These are some of the key points to remember about path pushing algorithms for distributed deadlock detection. They are an important concept in the study of distributed systems and are covered in Unit 3 - Distributed Deadlock Detection of the subject DISTRIBUTED SYSTEM.