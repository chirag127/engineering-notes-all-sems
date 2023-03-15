### Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- Priority-ceiling protocol is a job task synchronization protocol in a real-time system that prevents deadlocks and unbounded priority inversions.
- There are two variants of the protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP).
- In a dynamic priority system, the priorities of the periodic tasks change with time while the resources required by each task remain constant .
- Hence, the priority ceilings of the resources may change with time .
- The priority ceiling of a resource is the highest priority of any task that can access that resource.
- The system ceiling is the highest priority ceiling of any resource currently locked.
- A task can lock a resource only if its priority is higher than the system ceiling.
- A task that locks a resource inherits the priority ceiling of that resource until it releases it.
- For dynamic systems, we can use the priority ceiling protocol to control resource accesses provided we update the priority ceiling of each resource and the system ceiling each time task priorities change .
- This ensures that no task is blocked by a lower priority task and that no deadlock can occur.
- An example of a dynamic system with two tasks T1 (2, 0.9) and T2 (5, 2.3) executed in deadline driven system with one resource X is shown below :

| Time | T1 | T2 | X | Priority ceiling of X | System ceiling |
|------|----|----|---|-----------------------|----------------|
| 0    | 1  | 2  | - | 1                     | -              |
| 1    | 1  | 2  | 1 | 1                     | 1              |
| 2    | 1  | 2  | 1 | 1                     | 1              |
| 3    | 1  | 2  | 1 | 1                     | 1              |
| 4    | 2  | 1  | 1 | 2                     | 2              |
| 5    | 2  | 1  | 2 | 2                     | 2              |
| 6    | 2  | 1  | 2 | 2                     | 2              |
| 7    | 2  | 1  | 2 | 2                     | 2              |
| 8    | 2  | 1  | - | 2                     | -              |
| 9    | 2  | 1  | - | 2                     | -              |
| 10   | -  | 1  | - | 2                     | -              |

- The priority ceiling of X is 1 from time 0 to 4 and becomes 2 from time 4 to 5 and so on .
- T1 locks X at time 1 and inherits its priority ceiling of 1 .
- T2 cannot lock X until T1 releases it at time 8 .
- T2 locks X at time 5 and inherits its priority ceiling of 2 .
- T1 cannot lock X until T2 releases it at time 8 .
- Both tasks complete their execution before their deadlines .