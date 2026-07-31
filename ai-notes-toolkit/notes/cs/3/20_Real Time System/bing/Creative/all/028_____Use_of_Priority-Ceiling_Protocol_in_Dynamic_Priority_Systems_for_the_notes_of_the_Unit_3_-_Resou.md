# Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- Priority-ceiling protocol is a synchronization technique for preventing deadlock and unbounded priority inversion in real-time systems that share resources among tasks with different priorities.
- In a dynamic priority system, the priorities of the periodic tasks change with time while the resources required by each task remain constant .
- Hence, the priority ceilings of the resources may change with time as well .
- The priority ceiling of a resource is the highest priority of any task that can access that resource .
- The system ceiling is the highest priority ceiling of any resource currently locked by any task .
- A task can lock a resource only if its priority is higher than the system ceiling .
- This ensures that a higher priority task will not be blocked by a lower priority task that holds a resource .
- For dynamic systems, we can use the priority ceiling protocol to control resource accesses provided we update the priority ceiling of each resource and the system ceiling each time task priorities change .
- This can be done by using a table that stores the priority ceiling of each resource for each possible priority level of the tasks .
- For example, consider a system with two tasks T1 (2, 0.9) and T2 (5, 2.3) executed in a deadline driven system as below :

| Time | T1 | T2 | Priority |
|------|----|----|----------|
| 0    | 1  | 2  | T1 > T2  |
| 1    | 1  | 2  | T1 > T2  |
| 2    | 1  | 2  | T1 > T2  |
| 3    | 1  | 2  | T1 > T2  |
| 4    | 2  | 1  | T2 > T1  |
| 5    | 2  | 1  | T2 > T1  |
| 6    | 2  | 1  | T2 > T1  |
| 7    | 2  | 1  | T2 > T1  |

- Suppose both tasks need to access a shared resource X. The priority ceiling of X is 1 from time 0 to 4 and becomes 2 from time 4 to 5 and so on .
- The table for the priority ceiling of X is as follows:

| Priority | Ceiling |
|----------|---------|
| 1        | 2       |
| 2        | 1       |

- The system ceiling is initially 0 and changes according to the resource locking and unlocking by the tasks .
- If T1 locks X at time 0, the system ceiling becomes 2 and T2 cannot lock X until T1 releases it .
- If T2 locks X at time 4, the system ceiling becomes 1 and T1 cannot lock X until T2 releases it .
- This way, the priority ceiling protocol prevents deadlock and priority inversion in dynamic priority systems .