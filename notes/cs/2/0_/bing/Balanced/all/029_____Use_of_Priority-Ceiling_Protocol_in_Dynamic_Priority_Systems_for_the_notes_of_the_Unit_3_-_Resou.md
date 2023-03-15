# Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- Priority-ceiling protocol is a job task synchronization protocol in a real-time system that prevents deadlocks and unbounded priority inversions.
- There are two variants of the protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP).
- In a dynamic priority system, the priorities of the periodic tasks change with time while the resources required by each task remain constant .
- Hence, the priority ceilings of the resources may change with time .
- The priority ceiling of a resource is the highest priority of any task that can access that resource.
- The system ceiling is the highest priority ceiling of any resource currently locked.
- A task can lock a resource only if its priority is higher than the system ceiling.
- A task that locks a resource inherits the priority ceiling of that resource until it releases it.
- For dynamic systems, we can use the priority ceiling protocol to control resource accesses provided we update the priority ceiling of each resource and the ceiling of the system each time task priorities change .
- This ensures that no task is blocked by a lower priority task and that no deadlock can occur.
- An example of using the priority ceiling protocol in a dynamic priority system is given below :

| Task | Period | Execution Time | Resource |
| --- | --- | --- | --- |
| T1 | 2 | 0.9 | X |
| T2 | 5 | 2.3 | Y |

- The priority of T1 is 1 from time 0 to 4 and becomes 2 from time 4 to 5 and so on.
- The priority of T2 is 2 from time 0 to 5 and becomes 1 from time 5 to 10 and so on.
- The priority ceiling of X is 1 from time 0 to 4 and becomes 2 from time 4 to 5 and so on.
- The priority ceiling of Y is 2 from time 0 to 5 and becomes 1 from time 5 to 10 and so on.
- The system ceiling is 0 initially and changes according to the resource locks and releases.
- The execution of the tasks with the priority ceiling protocol is shown below:

| Time | Task | Resource | System Ceiling |
| --- | --- | --- | --- |
| 0 | T1 starts | - | 0 |
| 0.1 | T1 locks X | X | 1 |
| 0.5 | T2 starts | - | 1 |
| 0.9 | T1 releases X | - | 0 |
| 0.9 | T1 finishes | - | 0 |
| 2 | T1 starts | - | 0 |
| 2.1 | T1 locks X | X | 1 |
| 2.3 | T2 finishes | - | 1 |
| 2.9 | T1 releases X | - | 0 |
| 2.9 | T1 finishes | - | 0 |
| 4 | T1 starts | - | 0 |
| 4.1 | T1 locks X | X | 2 |
| 4.9 | T1 releases X | - | 0 |
| 4.9 | T1 finishes | - | 0 |
| 5 | T2 starts | - | 0 |
| 5.1 | T2 locks Y | Y | 1 |
| 7.4 | T2 releases Y | - | 0 |
| 7.4 | T2 finishes | - | 0 |
| 8 | T1 starts | - | 0 |
| 8.1 | T1 locks X | X | 2 |
| 8.9 | T1 releases X | - | 0 |
| 8.9 | T1 finishes | - | 0 |
| 10 | T2 starts | - | 0 |
| 10.1 | T2 locks Y | Y | 1 |
| 12.4 | T2 releases Y | - | 0 |
| 12.4 | T2 finishes | - | 0 |

- As we can see, the priority ceiling protocol ensures that T1 is not blocked by T2 when it needs X, and that