# Rate Monotonic Algorithm

- Rate monotonic algorithm (RMA) is a static priority scheduling algorithm for real-time systems .
- It assigns priorities to tasks based on their periods or cycle durations, such that shorter period tasks have higher priorities .
- It is a preemptive algorithm, meaning that a higher priority task can interrupt a lower priority task that is currently executing.
- It is optimal for a set of periodic, independent and deterministic tasks, meaning that it can always meet the deadlines of all tasks if they exist .
- It has a schedulability test that can determine if a given set of tasks can be scheduled by RMA or not .
- The schedulability test is based on the utilization factor of the tasks, which is the ratio of their execution time to their period .
- The utilization factor of a set of tasks must be less than or equal to a certain bound, which depends on the number of tasks, for RMA to be feasible .
- The bound is given by the formula: U <= n*(2^(1/n) - 1), where n is the number of tasks .
- If the utilization factor exceeds the bound, RMA may still be able to schedule the tasks, but it is not guaranteed .
- In that case, a more precise schedulability test can be used, which checks the worst-case response time of each task against its deadline .
- The worst-case response time of a task is the maximum time it takes to complete its execution, considering the interference from higher priority tasks .
- The worst-case response time can be calculated iteratively using the formula: R_i = C_i + sum(j=1 to i-1) ceil(R_i/T_j) * C_j, where C_i is the execution time of task i, T_j is the period of task j, and R_i is the response time of task i .
- The task set is schedulable by RMA if and only if R_i <= D_i for all tasks, where D_i is the deadline of task i .
- RMA has some advantages and disadvantages as a real-time scheduling algorithm.
- Some advantages are: simplicity, optimality for periodic tasks, low overhead, and predictability.
- Some disadvantages are: poor resource utilization, inability to handle aperiodic or sporadic tasks, priority inversion, and deadline misses for tasks with long periods.