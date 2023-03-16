### Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems

- Aperiodic jobs are jobs that have no fixed arrival or execution pattern, and have soft deadlines or no deadlines at all.
- Sporadic jobs are jobs that have a minimum inter-arrival time between successive jobs, and have hard or firm deadlines.
- Priority driven systems are systems that assign priorities to jobs based on some criteria, and schedule the highest priority job at any given time.
- Clock driven systems are systems that schedule jobs based on a pre-defined table that specifies the start and end times of each job in each cycle.

- The main challenge of scheduling aperiodic and sporadic jobs in priority driven systems is to balance the responsiveness of aperiodic jobs and the schedulability of periodic and sporadic jobs.
- The main challenge of scheduling aperiodic and sporadic jobs in clock driven systems is to accommodate the variability of aperiodic jobs and the unpredictability of sporadic jobs.

- Some of the algorithms for scheduling aperiodic and sporadic jobs in priority driven systems are:

  - Background scheduling: aperiodic jobs are executed only when no periodic or sporadic jobs are ready, and have the lowest priority in the system. This algorithm guarantees the schedulability of periodic and sporadic jobs, but may result in poor response times for aperiodic jobs.
  - Polling server: a periodic task with a fixed period and execution time is created to serve aperiodic jobs. The server has a priority higher than some periodic tasks, and can preempt them to execute aperiodic jobs. This algorithm improves the responsiveness of aperiodic jobs, but may cause deadline misses for periodic tasks with lower priority than the server.
  - Deferrable server: similar to the polling server, but the server can defer its execution if no aperiodic jobs are ready, and use its unused capacity later in the same period. This algorithm reduces the interference of the server on periodic tasks, but may still cause deadline misses for periodic tasks with lower priority than the server.
  - Sporadic server: similar to the deferrable server, but the server has a minimum inter-arrival time between successive executions, and can replenish its capacity after each execution. This algorithm allows the server to handle sporadic jobs as well as aperiodic jobs, but may still cause deadline misses for periodic tasks with lower priority than the server.
  - Slack stealing: aperiodic jobs are executed by stealing the slack time of periodic and sporadic jobs, where slack time is the difference between the worst-case execution time and the actual execution time of a job. This algorithm maximizes the utilization of the system, and can complete aperiodic jobs early, but requires the knowledge of the slack time of all jobs in the system.

- Some of the algorithms for scheduling aperiodic and sporadic jobs in clock driven systems are:

  - Spare capacity scheduling: aperiodic jobs are executed in the spare slots of the schedule table, where spare slots are the intervals that are not allocated to any periodic or sporadic jobs. This algorithm guarantees the schedulability of periodic and sporadic jobs, but may result in poor response times for aperiodic jobs if the spare capacity is low.
  - Dynamic adjustment of the schedule table: the schedule table is modified at run time to accommodate aperiodic and sporadic jobs, by shifting or swapping the slots of periodic jobs. This algorithm improves the responsiveness of aperiodic and sporadic jobs, but may cause deadline misses for periodic jobs if the modifications are not feasible or safe.
  - Hybrid scheduling: a combination of clock driven and priority driven scheduling, where aperiodic and sporadic jobs are handled by a priority driven algorithm, and periodic jobs are handled by a clock driven algorithm. This algorithm allows the flexibility of priority driven scheduling and the predictability of clock driven scheduling, but may require complex coordination and synchronization between the two algorithms.