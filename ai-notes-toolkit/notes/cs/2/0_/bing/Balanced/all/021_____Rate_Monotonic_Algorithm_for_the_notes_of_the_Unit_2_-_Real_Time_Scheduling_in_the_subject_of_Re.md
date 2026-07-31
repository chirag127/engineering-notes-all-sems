# Rate Monotonic Algorithm

- Rate monotonic algorithm (RMA) is a priority assignment algorithm used in real-time operating systems with a static-priority scheduling class  .
- The static priorities are assigned according to the cycle duration of the job, so a shorter cycle duration results in a higher job priority  .
- RMA is preemptive in nature, meaning that a higher priority job can interrupt a lower priority job at any time.
- RMA is optimal for periodic tasks, meaning that it can always schedule any set of periodic tasks that is feasible (i.e., that can be scheduled by some algorithm)  .
- RMA has a simple schedulability test that can determine if a set of periodic tasks is feasible or not. The test is based on the utilization factor of the tasks, which is the ratio of the execution time to the period of each task  .
- The schedulability test for RMA is:

  - For n tasks, the utilization factor of each task is Ui = Ci / Ti, where Ci is the execution time and Ti is the period of task i.
  - The total utilization factor of the system is U = sum of Ui for i = 1 to n.
  - The system is schedulable by RMA if U <= n * (2^(1/n) - 1), which is the utilization bound for RMA  .

- RMA has some advantages and disadvantages as a real-time scheduling algorithm. Some of them are:

  - Advantages:
    - Simple and easy to implement.
    - Optimal for periodic tasks.
    - Low overhead and predictable behavior.
    - Suitable for hard real-time systems that require guaranteed deadlines  .
  - Disadvantages:
    - Not optimal for aperiodic or sporadic tasks.
    - Not suitable for systems with dynamic priorities or varying execution times.
    - May cause priority inversion, which is a situation where a low priority task holds a shared resource that a high priority task needs, and the high priority task is blocked by a medium priority task that does not need the resource  .