# Rate Monotonic Algorithm

- Rate monotonic algorithm (RMA) is a priority assignment algorithm used in real-time operating systems with a static-priority scheduling class  .
- The static priorities are assigned according to the cycle duration of the job, so a shorter cycle duration results in a higher job priority  .
- RMA is preemptive in nature, meaning that a higher priority job can interrupt a lower priority job at any time.
- RMA is optimal for a set of periodic and independent jobs, meaning that it can always meet the deadlines of all the jobs if there exists a feasible schedule  .
- RMA has a simple and efficient implementation, as it only requires the knowledge of the cycle duration of each job and the current time .
- RMA has some limitations, such as:
  - It does not consider the actual execution time of the jobs, only the worst-case scenario .
  - It does not handle aperiodic or sporadic jobs well, as they may have unpredictable arrival times and deadlines .
  - It does not account for resource sharing or synchronization among the jobs, which may cause blocking or deadlock .
  - It does not guarantee the schedulability of all the jobs, even if the total utilization of the system is less than 100% .
- RMA has some schedulability tests, such as:
  - The necessary condition: The total utilization of the system must be less than or equal to the number of jobs .
  - The sufficient condition: The total utilization of the system must be less than or equal to a certain bound that depends on the number of jobs .
  - The exact condition: The system is schedulable if and only if there exists a feasible schedule that meets all the deadlines .