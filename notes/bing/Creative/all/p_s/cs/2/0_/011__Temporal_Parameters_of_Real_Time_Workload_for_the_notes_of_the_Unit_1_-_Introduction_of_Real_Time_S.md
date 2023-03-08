### Temporal Parameters of Real Time Workload

- A real time workload is a set of tasks or jobs that need to be executed by a real time system within certain time constraints.
- The temporal parameters of a real time workload describe the timing characteristics of each task or job, such as when it is released, when it must finish, and how long it can execute.
- The temporal parameters of a job are  :
  - Release time (r<sub>i</sub>): The time when the job becomes available for execution. It may be known exactly or within a range [r<sub>i</sub><sup>-</sup>, r<sub>i</sub><sup>+</sup>] (jitter).
  - Absolute deadline (d<sub>i</sub>): The time by which the job must finish its execution. It may be hard (must be met) or soft (can be missed with some penalty).
  - Relative deadline (D<sub>i</sub>): The time interval between the release time and the absolute deadline of the job. It is usually constant for periodic tasks.
  - Feasible interval [r<sub>i</sub>, d<sub>i</sub>]: The time interval during which the job can be executed by the system.
- The temporal parameters of a workload are:
  - Number of tasks or jobs in the system (n): The total number of tasks or jobs that need to be executed by the system.
  - Utilization factor (U): The ratio of the total execution time of all tasks or jobs to the total available time of the system. It indicates how busy the system is.
  - Density factor (D): The ratio of the total execution time of all tasks or jobs to the total feasible interval of the system. It indicates how tight the deadlines are.
- The temporal parameters of a real time workload are important for the analysis and specification of the system requirements, as well as for the design and verification of the system behavior . They help to determine the feasibility, schedulability, and performance of the system.

Some possible mnemonics and learning tricks for the topic are:

- To remember the temporal parameters of a job, use the acronym **RADD** (Release time, Absolute deadline, Relative deadline, Duration).
- To remember the temporal parameters of a workload, use the acronym **NUD** (Number of tasks, Utilization factor, Density factor).
- To remember the difference between utilization and density factors, use the phrase **"Utilization is busy, density is tight"**.