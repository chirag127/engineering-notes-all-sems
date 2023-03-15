### Rate Monotonic Algorithm

- Rate monotonic algorithm (RMA) is a priority assignment algorithm used in real-time operating systems with a static-priority scheduling class  .
- The static priorities are assigned according to the cycle duration of the job, so a shorter cycle duration results in a higher job priority  .
- RMA is preemptive, meaning that a higher priority job can interrupt a lower priority job at any time.
- RMA is optimal for periodic tasks, meaning that it can always schedule any set of periodic tasks that is feasible (i.e., that can be scheduled by some algorithm) .
- RMA has a simple schedulability test, which is based on the utilization factor of the task set. The utilization factor of a task is the ratio of its execution time to its period. The utilization factor of a task set is the sum of the utilization factors of all the tasks in the set .
- The schedulability test for RMA is:

  - If the utilization factor of the task set is less than or equal to the number of tasks, then the task set is schedulable by RMA .
  - If the utilization factor of the task set is greater than the number of tasks, then the task set may or may not be schedulable by RMA. A more precise test is needed to determine the schedulability .
  - The more precise test is based on the critical utilization factor, which is a function of the number of tasks. The critical utilization factor is the maximum utilization factor that guarantees the schedulability of any task set with that number of tasks .
  - The critical utilization factor for n tasks is given by the formula:

    - U<sub>c</sub>(n) = n(2<sup>1/n</sup> - 1) .
  - The more precise test for RMA is:

    - If the utilization factor of the task set is less than or equal to the critical utilization factor, then the task set is schedulable by RMA .
    - If the utilization factor of the task set is greater than the critical utilization factor, then the task set is not schedulable by RMA .

- RMA has some advantages and disadvantages as a real-time scheduling algorithm:

  - Advantages:

    - It is simple and easy to implement.
    - It is optimal for periodic tasks.
    - It has a low overhead and a fast response time.
    - It can handle aperiodic and sporadic tasks by using slack stealing or polling servers.

  - Disadvantages:

    - It is not optimal for non-periodic tasks.
    - It may waste CPU time if the tasks have different periods and the utilization factor is low.
    - It may cause priority inversion, which is a situation where a low priority task holds a resource that is needed by a high priority task.
    - It may not be suitable for distributed systems or heterogeneous processors.