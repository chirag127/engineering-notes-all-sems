### Rate Monotonic Algorithm for the notes of the Unit 2 - Real Time Scheduling in the subject of Real Time System

- Rate Monotonic Algorithm (RMA) is a priority assignment algorithm used in real-time operating systems with a static-priority scheduling class   .
- The static priorities are assigned according to the cycle duration of the task, so that a shorter cycle duration results in a higher task priority   .
- RMA is preemptive in nature, meaning that a higher priority task can interrupt a lower priority task at any time .
- RMA is optimal for periodic tasks, meaning that it can schedule any set of periodic tasks that is feasible, i.e., that can be scheduled by any other algorithm  .
- RMA has a simple schedulability test, which is based on the utilization factor of the task set, defined as the sum of the ratios of execution time to period for each task  .
- The schedulability test states that a task set is schedulable by RMA if its utilization factor is less than or equal to n(2^(1/n) - 1), where n is the number of tasks  .
- RMA has some advantages, such as easy implementation, low overhead, and guaranteed performance for feasible task sets .
- RMA also has some disadvantages, such as poor resource utilization, inability to handle aperiodic or sporadic tasks, and priority inversion problem .