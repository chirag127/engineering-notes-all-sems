# Unit 3 - Distributed Deadlock Detection

### Edge Chasing Algorithms

- Edge chasing algorithms are used for distributed deadlock detection in distributed systems.
- These algorithms work by sending probe messages along the wait-for graph edges to detect cycles.
- If a cycle is detected, it indicates the presence of a deadlock.
- One example of an edge chasing algorithm is the Chandy-Misra-Haas algorithm.
- In this algorithm, a probe message is sent from a blocked process to the process holding the resource it is waiting for.
- The probe message contains the ID of the blocked process and the ID of the resource it is waiting for.
- When a process receives a probe message, it checks if it is also blocked and waiting for a resource.
- If it is, it forwards the probe message to the process holding the resource it is waiting for.
- If the probe message returns to the original blocked process, a cycle has been detected and a deadlock is present.
- The algorithm can then take appropriate action to resolve the deadlock, such as aborting one of the processes involved in the cycle.
