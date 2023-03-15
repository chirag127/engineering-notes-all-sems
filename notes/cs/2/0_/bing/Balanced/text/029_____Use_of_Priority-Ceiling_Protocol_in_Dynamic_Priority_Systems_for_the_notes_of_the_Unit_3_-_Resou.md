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

- Task T1 requires resource X for 0.3 time units and task T2 requires resource Y for 0.5 time units.

- The priority of T1 is higher than T2 from time 0 to 4 and lower than T2 from time 4 to 5.

- The priority ceiling of X is 1 from time 0 to 4 and becomes 2 from time 4 to 5 and so on.

- The priority ceiling of Y is 2 from time 0 to 5 and becomes 1 from time 5 to 6 and so on.

- The ceiling of the system is the maximum of the priority ceilings of X and Y.

- The execution of the tasks using the priority ceiling protocol is shown below:

| Time | T1 | T2 | X | Y | System Ceiling |
|------|----|----|---|---|----------------|
| 0    | 1  | 2  | 1 | 2 | 2              |
| 1    | 1  | 2  | 1 | 2 | 2              |
| 2    | 1  | 2  | 1 | 2 | 2              |
| 3    | 1  | 2  | 1 | 2 | 2              |
| 4    | 2  | 1  | 2 | 2 | 2              |
| 5    | 2  | 1  | 2 | 1 | 2              |
| 6    | 1  | 2  | 1 | 1 | 1              |
| 7    | 1  | 2  | 1 | 1 | 1              |

- At time 0, T1 starts executing and locks X. The system ceiling is 2, which is the priority ceiling of Y.

- At time 1, T2 starts executing and locks Y. The system ceiling remains 2.

- At time 2, T1 finishes using X and releases it. The system ceiling remains 2.

- At time 3, T1 finishes its execution and T2 continues.

- At time 4, the priorities of T1 and T2 change. T1 becomes lower priority and T2 becomes higher priority. The priority ceiling of X also changes to 2.

- At time 5, T2 finishes using Y and releases it. The system ceiling becomes 2, which is the priority ceiling of X. The priority ceiling of Y also changes to 1.

- At time 6, T2 finishes its execution and T1 resumes. The system ceiling becomes 1, which is the priority ceiling of Y.

- At time 7, T1 finishes its execution and the system is idle.