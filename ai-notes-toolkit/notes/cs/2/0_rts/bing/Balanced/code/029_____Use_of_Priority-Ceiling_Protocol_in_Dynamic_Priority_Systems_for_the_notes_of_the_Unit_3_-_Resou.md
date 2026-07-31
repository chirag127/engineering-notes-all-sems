### Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- Priority-ceiling protocol is a job task synchronization protocol in a real-time system that prevents deadlocks and unbounded priority inversions.
- There are two variants of the protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP).
- In a dynamic priority system, the priorities of the periodic tasks change with time while the resources required by each task remain constant .
- Hence, the priority ceilings of the resources may change with time. The priority ceiling of a resource is the highest priority of any task that can access that resource.
- For dynamic systems, we can use the priority ceiling protocol to control resource accesses provided we update the priority ceiling of each resource and the ceiling of the system each time task priorities change .
- The ceiling of the system is the highest priority ceiling of all the resources currently locked.
- A task can lock a resource only if its priority is higher than the ceiling of the system. Otherwise, it has to wait until the resource is released.
- This ensures that a task can be blocked by at most one lower priority task, and that task can be blocked by at most one lower priority task, and so on.
- This reduces the blocking time and improves the schedulability of the system.
- An example of using the priority ceiling protocol in a dynamic priority system is given below :

- Consider a system with two tasks Tasks T1 (2, 0.9), T2 (5, 2.3) executed in deadline driven system as below.

| Time | Task | Resource |
| --- | --- | --- |
| 0 | T1 | X |
| 0.9 | T1 | - |
| 1 | T2 | Y |
| 2 | T1 | X |
| 2.9 | T1 | - |
| 3 | T2 | Y |
| 4 | T1 | X |
| 4.9 | T1 | - |
| 5 | T2 | Y |
| 6 | T1 | X |
| 6.9 | T1 | - |
| 7 | T2 | Y |
| 8 | T1 | X |
| 8.9 | T1 | - |
| 9 | T2 | Y |

- The priority ceiling of X is 1 from time 0 to 4 and becomes 2 from time 4 to 5 and so on.
- The priority ceiling of Y is 2 from time 1 to 5 and becomes 1 from time 5 to 9 and so on.
- The ceiling of the system is the maximum of the priority ceilings of X and Y at any time.
- Using the priority ceiling protocol, the tasks can access the resources as follows:

| Time | Task | Resource | Ceiling |
| --- | --- | --- | --- |
| 0 | T1 | X | 1 |
| 0.9 | T1 | - | 0 |
| 1 | T2 | Y | 2 |
| 2 | T1 | X | 2 |
| 2.9 | T1 | - | 2 |
| 3 | T2 | Y | 2 |
| 4 | T1 | X | 2 |
| 4.9 | T1 | - | 2 |
| 5 | T2 | Y | 2 |
| 6 | T1 | X | 2 |
| 6.9 | T1 | - | 2 |
| 7 | T2 | Y | 2 |
| 8 | T1 | X | 2 |
| 8.9 | T1 | - | 2 |
| 9 | T2 | Y | 2 |

- Note that no task is blocked by a lower priority task, and the system is schedulable.