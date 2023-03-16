### Path Pushing Algorithms

Path pushing algorithms are a type of distributed deadlock detection algorithm used in distributed systems. These algorithms work by propagating information about blocked processes along wait-for edges in the system's resource graph.

Here are some key points to remember about path pushing algorithms:

1. In a path pushing algorithm, each process maintains a set of blocked processes that are dependent on it for resources.
2. When a process becomes blocked, it sends a message to all processes that hold resources it is waiting for, informing them of its blocked status.
3. Upon receiving a blocked message, a process adds the blocked process to its set of dependent processes and propagates the message to all processes that hold resources it is waiting for.
4. If a process receives a blocked message for itself, a deadlock has been detected.
5. When a process releases a resource, it sends a message to all processes in its set of dependent processes, informing them that it is no longer blocked.
6. Upon receiving an unblocked message, a process removes the unblocked process from its set of dependent processes and propagates the message to all processes that hold resources it is waiting for.

These are some of the key points to remember about path pushing algorithms for distributed deadlock detection. It is important to understand how these algorithms work in order to effectively detect and resolve deadlocks in distributed systems.