# Rate Monotonic Algorithm

- Rate Monotonic Algorithm (RMA) is a priority assignment algorithm used in real-time operating systems with a static-priority scheduling class .
- The static priorities are assigned according to the cycle duration of the job, so a shorter cycle duration results in a higher job priority .
- RMA is preemptive in nature, meaning that a higher priority job can interrupt a lower priority job at any time.
- RMA is optimal for periodic tasks, meaning that it can always schedule any set of periodic tasks that is schedulable by any other static-priority algorithm .
- RMA has some advantages and disadvantages compared to other scheduling algorithms, such as:
  - Advantages:
    - Simple and easy to implement .
    - Predictable and deterministic .
    - Low overhead and context switching .
  - Disadvantages:
    - Not suitable for aperiodic or sporadic tasks .
    - Not optimal for tasks with different deadlines and periods .
    - May suffer from priority inversion and blocking .
- RMA has some feasibility tests to check if a given set of tasks can be scheduled by RMA, such as:
  - Utilization test: The total utilization of the tasks must be less than or equal to the number of tasks times the difference between 2 and the inverse of the number of tasks .
  - Response time test: The worst-case response time of each task must be less than or equal to its deadline .
  - Schedulability test: The worst-case response time of the highest priority task must be less than or equal to its period, and the worst-case response time of each lower priority task must be less than or equal to its deadline minus the interference from higher priority tasks .