### Path Pushing Algorithms

Path pushing algorithms are used to detect and resolve deadlocks in distributed systems. These algorithms are designed to detect cycles in a distributed system and break the deadlock by releasing resources. Path pushing algorithms work by pushing the deadlock detection message along a path in the system until a cycle is detected.

There are two types of path pushing algorithms:

1. Chandy-Misra-Haas (CMH) Algorithm:
   - This algorithm is based on the principle of "wait-for" graph.
   - It uses a message called a probe to detect cycles in the system.
   - The probe message is sent along a path in the system until it reaches a process that is waiting for a resource held by the process that initiated the probe.
   - Once a deadlock cycle is detected, the algorithm releases the resources held by the processes in the cycle, allowing them to continue their computation.

2. Distributed Edge Chasing (DEC) Algorithm:
   - This algorithm is based on the idea of edge chasing, where a message is sent along an edge in the system to detect cycles.
   - The algorithm uses a message called a inquiry to detect cycles.
   - The inquiry message is sent along a path in the system until it reaches a process that is waiting for a resource held by the process that initiated the inquiry.
   - If the process has the requested resource, it sends a reply message back along the path to the initiating process.
   - If the process does not have the requested resource, it sends an inquiry message along the edge it is waiting on.
   - When a deadlock cycle is detected, the algorithm releases the resources held by the processes in the cycle, allowing them to continue their computation.

Both of these path pushing algorithms are effective in detecting and resolving deadlocks in distributed systems. However, the DEC algorithm is more efficient than the CMH algorithm in terms of message complexity and response time. Therefore, the DEC algorithm is preferred over the CMH algorithm in most cases.