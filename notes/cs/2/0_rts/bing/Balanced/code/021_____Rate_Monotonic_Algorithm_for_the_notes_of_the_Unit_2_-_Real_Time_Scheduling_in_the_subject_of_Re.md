### Rate Monotonic Algorithm

- Rate Monotonic Algorithm (RMA) is a priority assignment algorithm used in real-time operating systems with a static-priority scheduling class  .
- The static priorities are assigned according to the cycle duration of the job, so a shorter cycle duration results in a higher job priority  .
- RMA is preemptive in nature, meaning that a higher priority job can interrupt a lower priority job at any time.
- RMA is optimal for periodic tasks, meaning that it can always schedule any set of periodic tasks that is feasible (i.e., the total utilization of the tasks is less than or equal to 100%) .
- RMA has a simple schedulability test that can determine if a set of periodic tasks is feasible or not. The test is based on the utilization bound, which is a function of the number of tasks and their relative deadlines .
- RMA has some advantages and disadvantages compared to other real-time scheduling algorithms. Some advantages are: simplicity, predictability, low overhead, and optimality for periodic tasks. Some disadvantages are: poor performance for aperiodic and sporadic tasks, priority inversion, and deadline misses for tasks with long cycle durations  .