### Path Pushing Algorithms

Path pushing algorithms are a class of algorithms used in distributed deadlock detection. These algorithms work by propagating information about blocked processes along wait-for edges in the resource graph. The basic idea is to push information about blocked processes along the wait-for edges until a cycle is detected, indicating a deadlock.

Here are some key points to remember about path pushing algorithms:

1. Path pushing algorithms are used in distributed deadlock detection.
2. These algorithms work by propagating information about blocked processes along wait-for edges in the resource graph.
3. The basic idea is to push information about blocked processes along the wait-for edges until a cycle is detected, indicating a deadlock.
4. Path pushing algorithms can be classified into two categories: edge-chasing algorithms and diffusing computation algorithms.
5. Edge-chasing algorithms work by sending probe messages along wait-for edges to detect cycles in the resource graph.
6. Diffusing computation algorithms work by initiating a distributed computation to detect cycles in the resource graph.
