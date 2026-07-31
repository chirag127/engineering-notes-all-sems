# Rate Monotonic Algorithm

- Rate monotonic algorithm (RMA) is a priority assignment algorithm used in real-time operating systems with a static-priority scheduling class .
- The static priorities are assigned according to the cycle duration of the job, so that a shorter cycle duration results in a higher job priority .
- RMA is preemptive, meaning that a higher priority job can interrupt a lower priority job at any time.
- RMA is optimal for periodic tasks, meaning that it can schedule any set of periodic tasks that is feasible, i.e., that can be scheduled by any algorithm .
- RMA has a simple schedulability test, which is based on the utilization factor of the task set, defined as the sum of the ratios of execution time to period for each task .
- The schedulability test states that a set of periodic tasks is schedulable by RMA if the utilization factor is less than or equal to n(2^(1/n) - 1), where n is the number of tasks .
- RMA has some limitations, such as not being suitable for aperiodic or sporadic tasks, not considering deadlines or resource constraints, and not being optimal for multiprocessor systems .