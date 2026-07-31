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
- For example, consider a system with two tasks T1 (2, 0.9) and T2 (5, 2.3) executed in deadline driven system as below :

| Time | T1 | T2 | Resource X | Resource Y | System Ceiling |
|------|----|----|------------|------------|----------------|
| 0    | 1  | 2  | -          | -          | -              |
| 1    | 1  | 2  | T1         | -          | 1              |
| 2    | 1  | 2  | T1         | -          | 1              |
| 3    | 1  | 2  | T1         | -          | 1              |
| 4    | 2  | 1  | T1         | -          | 2              |
| 5    | 2  | 1  | -          | T2         | 2              |
| 6    | 2  | 1  | -          | T2         | 2              |
| 7    | 2  | 1  | -          | T2         | 2              |
| 8    | 2  | 1  | -          | T2         | 2              |
| 9    | 2  | 1  | -          | -          | -              |

- The priority ceiling of X is 1 from time 0 to 4 and becomes 2 from time 4 to 5 and so on .
- The priority ceiling of Y is 2 from time 0 to 5 and becomes 1 from time 5 to 6 and so on .
- The system ceiling is updated accordingly whenever a resource is locked or released .
- T1 can lock X at time 1 because its priority is higher than the system ceiling .
- T2 can lock Y at time 5 because its priority is higher than the system ceiling .
- T1 cannot lock Y at time 2 because its priority is lower than the system ceiling .
- T2 cannot lock X at time 6 because its priority is lower than the system ceiling .
- Both tasks can complete their execution without blocking or deadlock .