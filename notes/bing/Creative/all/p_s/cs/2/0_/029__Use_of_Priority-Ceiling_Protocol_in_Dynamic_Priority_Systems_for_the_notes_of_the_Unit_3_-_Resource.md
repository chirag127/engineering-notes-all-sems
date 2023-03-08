### Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- In a dynamic priority system, the priorities of the periodic tasks change with time while the resources required by each task remain constant. Hence, the priority ceilings of the resources may change with time.
- The priority ceiling of a resource is the highest priority of any task that can access that resource. The system ceiling is the highest priority ceiling of any resource that is currently in use.
- The priority ceiling protocol (PCP) is a job task synchronization protocol in a real-time system that prevents deadlock, priority inversion, and unbounded blocking.
- The PCP works as follows:
  - Each resource is assigned a static priority ceiling equal to the highest priority of any task that can access it.
  - A task can access a resource only if its priority is higher than the system ceiling.
  - When a task accesses a resource, it inherits the priority ceiling of that resource and the system ceiling is updated accordingly.
  - When a task releases a resource, it restores its original priority and the system ceiling is updated accordingly.
- For dynamic systems, we can use the PCP to control resource accesses provided we update the priority ceiling of each resource and the system ceiling each time task priorities change.
- An example of using the PCP in a dynamic system is shown below:

| Task | Period | Execution Time | Resource |
|------|--------|----------------|----------|
| T1   | 2      | 0.9            | X        |
| T2   | 5      | 2.3            | X, Y     |

- The priority of each task is inversely proportional to its deadline, which is equal to its period. Therefore, the priority of T1 is higher than the priority of T2 at the beginning of each period.
- The priority ceiling of X is 1 from time 0 to 4 and becomes 2 from time 4 to 5 and so on. The priority ceiling of Y is 2. The system ceiling is the maximum of the priority ceilings of the resources in use.
- The execution of the tasks and the resource accesses are shown in the following figure:

```
Time: 0  1  2  3  4  5  6  7  8  9
T1  : X  X  X  X  X  X  X  X  X  X
T2  :    Y  Y  Y  Y  Y  Y  Y  Y  Y
PCX : 1  1  1  1  2  2  2  2  1  1
PCY : 2  2  2  2  2  2  2  2  2  2
SC  : 0  1  2  2  2  2  2  2  2  2
```

- At time 0, T1 starts and accesses X. The priority ceiling of X is 1 and the system ceiling is 0. T1 inherits the priority ceiling of X and the system ceiling becomes 1.
- At time 1, T2 starts and tries to access Y. The priority ceiling of Y is 2 and the system ceiling is 1. T2 can access Y since its priority is higher than the system ceiling. T2 inherits the priority ceiling of Y and the system ceiling becomes 2.
- At time 2, T1 tries to access X again. The priority ceiling of X is 1 and the system ceiling is 2. T1 cannot access X since its priority is lower than the system ceiling. T1 is blocked by T2.
- At time 4, T2 releases Y. The priority of T2 changes to 2 since its deadline is 5. The priority ceiling of X also changes to 2 since T2 can access it. T2 restores its original priority and the system ceiling becomes 2.
- At time 5, T2 releases X. T2 restores its original priority and the system ceiling becomes 0. T1 resumes and accesses X. The priority ceiling of X is 2 and the system ceiling is 0. T1 inherits the priority ceiling of X and the system ceiling becomes 2.
- At time 6, T2 starts a new period and tries to access Y. The priority ceiling of Y is

Some possible mnemonics and learning tricks for the topic are:

- PCP: Priority Ceiling Protocol. Remember that PCP prevents PIP (Priority Inversion Problem) and PDP (Priority Deadlock Problem).
- The priority ceiling of a resource is the highest priority of any task that can access it. Remember that the ceiling is the highest point in a room and the highest priority task can reach it.
- A task can access a resource only if its priority is higher than the system ceiling. Remember that the system ceiling is like a barrier that blocks lower priority tasks from accessing resources.
- When a task accesses a resource, it inherits the priority ceiling of that resource and the system ceiling is updated accordingly. Remember that the task gets a boost in priority and the system ceiling rises with it.
- When a task releases a resource, it restores its original priority and the system ceiling is updated accordingly. Remember that the task goes back to its normal priority and the system ceiling falls with it.