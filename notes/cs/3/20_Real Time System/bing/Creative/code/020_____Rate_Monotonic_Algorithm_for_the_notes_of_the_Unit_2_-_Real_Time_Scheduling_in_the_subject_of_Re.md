### Rate Monotonic Algorithm

- Rate monotonic algorithm (RMA) is a priority assignment algorithm used in real-time operating systems with a static-priority scheduling class   .
- The static priorities are assigned according to the cycle duration of the task, so that a shorter cycle duration results in a higher task priority   .
- It is a preemptive algorithm, meaning that a higher priority task can interrupt a lower priority task at any time .
- It is optimal for periodic tasks, meaning that it can schedule any set of periodic tasks that is feasible, i.e., that can meet all deadlines all the time  .
- It has a simple schedulability test, based on the utilization factor of the task set, which is the sum of the ratios of execution time to period for each task  .
- The schedulability test is sufficient but not necessary, meaning that it can reject some task sets that are actually schedulable  .
- It can also be extended to handle aperiodic and sporadic tasks, by using slack stealing or server mechanisms .