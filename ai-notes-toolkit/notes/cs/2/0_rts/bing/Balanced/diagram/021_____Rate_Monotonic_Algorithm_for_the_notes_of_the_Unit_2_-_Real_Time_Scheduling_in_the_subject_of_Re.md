### Rate Monotonic Algorithm

- Rate Monotonic Algorithm (RMA) is a priority assignment algorithm used in real-time operating systems with a static-priority scheduling class  .
- The static priorities are assigned according to the cycle duration of the job, so a shorter cycle duration results in a higher job priority  .
- RMA is preemptive in nature, meaning that a higher priority job can interrupt a lower priority job at any time.
- RMA is optimal for a set of periodic and independent jobs, meaning that it can always meet the deadlines of all the jobs if there exists any feasible schedule  .
- RMA has a simple and efficient implementation, as it only requires the knowledge of the cycle durations of the jobs and does not need any dynamic information such as deadlines or execution times .
- RMA has some limitations, such as:
  - It does not consider the actual execution times of the jobs, which may lead to underutilization of the processor .
  - It does not handle aperiodic or sporadic jobs, which may have unpredictable arrival times or deadlines .
  - It does not guarantee the schedulability of all feasible sets of jobs, as it may fail to meet the deadlines of some jobs even if the processor utilization is less than 100% .
- RMA has a sufficient and necessary schedulability test, which is based on the utilization bound of the processor  . The utilization bound is given by:

  U = n * (2^(1/n) - 1)

  where n is the number of jobs and U is the maximum utilization that can be achieved by RMA.

  The test states that a set of jobs is schedulable by RMA if and only if the total utilization of the jobs is less than or equal to U  .

- RMA can be illustrated by the following example:

  Suppose there are three periodic and independent jobs, J1, J2, and J3, with the following parameters:

  | Job | Cycle Duration | Execution Time | Priority |
  | --- | -------------- | -------------- | -------- |
  | J1  | 20             | 5              | 3        |
  | J2  | 10             | 2              | 2        |
  | J3  | 5              | 1              | 1        |

  The priorities are assigned according to the cycle durations, so J3 has the highest priority and J1 has the lowest priority.

  The utilization bound for n = 3 is:

  U = 3 * (2^(1/3) - 1) = 0.7798

  The total utilization of the jobs is:

  U = 5/20 + 2/10 + 1/5 = 0.65

  Since U < 0.7798, the set of jobs is schedulable by RMA.

  The following diagram shows the schedule of the jobs by RMA:

  ```
  Time: 0   5   10  15  20  25  30  35  40  45  50
  J3  : |---|---|---|---|---|---|---|---|---|---|---|
  J2  : |   |   |---|   |   |---|   |   |---|   |   |
  J1  : |   |   |   |   |---|   |   |   |   |   |---|
  ```

  As can be seen, all the jobs meet their deadlines and no job is interrupted by a lower priority job.