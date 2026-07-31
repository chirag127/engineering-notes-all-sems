# Temporal Parameters of Real Time Workload

- A real time workload is a set of jobs that need to be executed by a real time system within certain time constraints.
- A job is a unit of work that requires processor time and other resources to complete.
- A job can be periodic, aperiodic, or sporadic, depending on its arrival pattern and frequency.
- A job can be characterized by its temporal parameters, which describe its timing requirements and constraints.
- The temporal parameters of a job are:

  - Release time (r_i): the earliest time at which the job can start execution.
  - Absolute deadline (d_i): the latest time by which the job must finish execution.
  - Relative deadline (D_i): the maximum time allowed for the job to complete after its release time.
  - Feasible interval [(r_i, d_i)]: the time interval in which the job can be feasibly executed.
  - Execution time (e_i): the actual time required by the job to complete on the processor.
  - Laxity (l_i): the amount of time left for the job to complete before its deadline, given by l_i = d_i - e_i - t, where t is the current time.

- The temporal parameters of a job can be used to determine its priority, schedulability, and performance in a real time system.