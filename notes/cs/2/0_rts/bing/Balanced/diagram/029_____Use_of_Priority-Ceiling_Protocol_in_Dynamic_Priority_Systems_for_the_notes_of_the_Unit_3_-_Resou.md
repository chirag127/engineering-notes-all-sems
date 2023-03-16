### Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- Priority-ceiling protocol is a job task synchronization protocol in a real-time system that prevents deadlocks and unbounded priority inversions.
- There are two variants of the protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP).
- In a dynamic priority system, the priorities of the periodic tasks change with time while the resources required by each task remain constant .
- Hence, the priority ceilings of the resources may change with time .
- The priority ceiling of a resource is the highest priority of any task that can access that resource.
- The system ceiling is the highest priority ceiling of any resource currently locked.
- A task can lock a resource only if its priority is higher than the system ceiling.
- A task that locks a resource inherits the priority ceiling of that resource until it releases it.
- For dynamic systems, we can use the priority ceiling protocol to control resource accesses provided we update the priority ceiling of each resource and the ceiling of the system each time task priorities change .
- This ensures that no task is blocked by a lower priority task and that no circular wait can occur.
- An example of using the priority ceiling protocol in a dynamic priority system is given below :

| Time | Task | Resource | Priority Ceiling | System Ceiling |
|------|------|----------|------------------|----------------|
| 0    | T1   | X        | 1                | 1              |
| 1    | T1   | X        | 1                | 1              |
| 2    | T1   | X        | 1                | 1              |
| 3    | T1   | X        | 1                | 1              |
| 4    | T2   | Y        | 2                | 2              |
| 5    | T2   | Y        | 2                | 2              |
| 6    | T2   | Y        | 2                | 2              |
| 7    | T2   | Y        | 2                | 2              |
| 8    | T1   | X        | 2                | 2              |
| 9    | T1   | X        | 2                | 2              |

- The priority ceiling of X is 1 from time 0 to 4 and becomes 2 from time 4 to 5 and so on.
- The priority ceiling of Y is 2 from time 4 to 9.
- The system ceiling is the maximum of the priority ceilings of the locked resources at any time.
- T1 locks X at time 0 and inherits its priority ceiling of 1.
- T2 locks Y at time 4 and inherits its priority ceiling of 2.
- T1 cannot lock Y at time 5 because its priority is lower than the system ceiling of 2.
- T2 cannot lock X at time 6 because its priority is lower than the system ceiling of 2.
- T1 releases X at time 9 and resumes its original priority of 1.
- T2 releases Y at time 9 and resumes its original priority of 2.