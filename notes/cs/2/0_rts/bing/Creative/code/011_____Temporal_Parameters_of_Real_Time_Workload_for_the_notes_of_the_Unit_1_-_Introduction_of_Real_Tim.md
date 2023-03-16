### Temporal Parameters of Real Time Workload

- A real time workload is a set of tasks or jobs that need to be executed by a real time system within certain time constraints.
- The temporal parameters of a real time workload describe the timing characteristics of each task or job, such as when it is released, when it must finish, and how long it can execute.
- The temporal parameters of a job are :
  - Release time (r_i): the time when the job becomes available for execution.
  - Absolute deadline (d_i): the time by which the job must finish its execution.
  - Relative deadline (D_i): the maximum amount of time the job can execute after its release time.
  - Feasible interval [(r_i, d_i)]: the interval of time in which the job can be feasibly executed.
- The temporal parameters of a task are:
  - Period (T_i): the time interval between two consecutive releases of the same task.
  - Utilization (U_i): the ratio of the execution time of the task to its period.
  - Phase (φ_i): the time difference between the release time of the first job of the task and the start of the system.
- The temporal parameters of a real time workload can be used to analyze the schedulability and performance of the system, and to design appropriate scheduling algorithms and policies.