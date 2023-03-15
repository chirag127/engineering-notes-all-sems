# Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- Priority-ceiling protocol is a job task synchronization protocol in a real-time system that prevents deadlocks and unbounded priority inversions.
- There are two variants of the protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP).
- In a dynamic priority system, the priorities of the periodic tasks change with time while the resources required by each task remain constant .
- Hence, the priority ceilings of the resources may change with time .
- The priority ceiling of a resource is the highest priority of any task that may access that resource.
- The system ceiling is the highest priority ceiling of any resource currently locked.
- A task can lock a resource only if its priority is higher than the system ceiling.
- A task that locks a resource inherits the priority ceiling of that resource until it releases it.
- For dynamic systems, we can use the priority ceiling protocol to control resource accesses provided we update the priority ceiling of each resource and the ceiling of the system each time task priorities change .
- This ensures that no task is blocked by a lower priority task and that no circular wait is possible .
- An example of using priority ceiling protocol in a dynamic priority system is given below :

![example](https://benchpartner.com/images/Real-Time-System/Use-of-Priority-Ceiling-Protocol-in-Dynamic-Priority-Systems.png)

- In this example, there are two tasks T1 and T2 with dynamic priorities and two resources X and Y with priority ceilings .
- The priority ceiling of X is 1 from time 0 to 4 and becomes 2 from time 4 to 5 and so on .
- The priority ceiling of Y is 2 from time 0 to 5 and becomes 1 from time 5 to 6 and so on .
- The system ceiling is the maximum of the priority ceilings of the locked resources at any time .
- The table below shows the priority ceilings and the system ceiling at different time intervals :

| Time | Priority ceiling of X | Priority ceiling of Y | System ceiling |
|------|-----------------------|-----------------------|----------------|
| 0-1  | 1                     | 2                     | 0              |
| 1-2  | 1                     | 2                     | 1              |
| 2-3  | 1                     | 2                     | 2              |
| 3-4  | 1                     | 2                     | 1              |
| 4-5  | 2                     | 2                     | 2              |
| 5-6  | 2                     | 1                     | 2              |
| 6-7  | 2                     | 1                     | 1              |
| 7-8  | 2                     | 1                     | 0              |

- The priority ceiling protocol ensures that T1 and T2 can access the resources without deadlock or unbounded priority inversion .
- However, the protocol may cause some blocking of higher priority tasks by lower priority tasks when the priority ceilings change .
- For example, T1 is blocked by T2 from time 4 to 5 when the priority ceiling of X becomes 2 .
- This blocking can be reduced by using the Immediate Ceiling Priority Protocol (ICPP), which assigns the priority ceiling of a resource to a task as soon as it requests the resource, rather than when it locks it.
- This way, T1 would inherit the priority ceiling of X as soon as it requests it at time 4 and would not be blocked by T2.
- The table below shows the priority ceilings and the system ceiling at different time intervals using ICPP:

| Time | Priority ceiling of X | Priority ceiling of Y | System ceiling |
|------|-----------------------|-----------------------|----------------|
| 0-1  | 1                     | 2                     | 0              |
| 1-2  | 1