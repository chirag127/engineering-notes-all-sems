# Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- Priority-ceiling protocol is a synchronization technique for preventing deadlock and unbounded priority inversion in real-time systems that share resources among tasks with different priorities.
- In a dynamic priority system, the priorities of the periodic tasks change with time while the resources required by each task remain constant .
- Hence, the priority ceilings of the resources may change with time as well .
- The priority ceiling of a resource is the highest priority of any task that can access that resource .
- The system ceiling is the highest priority ceiling of any resource currently locked by any task .
- A task can lock a resource only if its priority is higher than the system ceiling .
- This ensures that a higher priority task will not be blocked by a lower priority task that holds a resource .
- For dynamic systems, we can use the priority ceiling protocol to control resource accesses provided we update the priority ceiling of each resource and the system ceiling each time task priorities change .
- This can be done by using a table that stores the priority ceilings of each resource for each possible priority level of the tasks .
- For example, consider a system with two tasks T1 (2, 0.9) and T2 (5, 2.3) executed in a deadline driven system as below :

| Time | T1 | T2 | Priority |
|------|----|----|----------|
| 0    | R  |    | 1        |
| 1    | R  |    | 1        |
| 2    |    | R  | 2        |
| 3    |    | R  | 2        |
| 4    | R  |    | 2        |
| 5    | R  |    | 2        |
| 6    |    | R  | 1        |
| 7    |    | R  | 1        |
| 8    | R  |    | 1        |
| 9    | R  |    | 1        |

- Assume that both tasks share a resource X that is initially unlocked. The priority ceiling of X is 1 from time 0 to 4 and becomes 2 from time 4 to 5 and so on .
- The table below shows the priority ceilings of X for each priority level of the tasks :

| Priority | Priority Ceiling of X |
|----------|-----------------------|
| 1        | 1                     |
| 2        | 2                     |

- The priority ceiling protocol works as follows :
  - At time 0, T1 locks X and executes. The system ceiling becomes 1.
  - At time 2, T2 preempts T1 and executes. The system ceiling remains 1.
  - At time 4, T1 preempts T2 and executes. The system ceiling becomes 2.
  - At time 6, T2 preempts T1 and executes. The system ceiling becomes 1.
  - At time 8, T1 preempts T2 and executes. The system ceiling remains 1.
  - At time 10, T1 unlocks X and finishes. The system ceiling becomes 0.
  - At time 11, T2 resumes and finishes.

- The priority ceiling protocol ensures that no deadlock or unbounded priority inversion occurs in the system .