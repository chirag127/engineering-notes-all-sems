# Temporal Parameters of Real Time Workload

- A real time workload is a set of tasks or jobs that need to be executed by a real time system within certain time constraints.
- The temporal parameters of a job are the attributes that define its timing requirements and behavior .
- The temporal parameters of a job are:
  - **Release time (r<sub>i</sub>)**: The time when the job becomes available for execution. It may be known exactly or within a range [r<sub>i</sub><sup>-</sup>, r<sub>i</sub><sup>+</sup>] (jitter).
  - **Absolute deadline (d<sub>i</sub>)**: The time by which the job must finish its execution. It may be fixed or variable depending on the system and the job.
  - **Relative deadline (D<sub>i</sub>)**: The maximum time allowed for the job to complete its execution after its release time. It is equal to d<sub>i</sub> - r<sub>i</sub>.
  - **Feasible interval [(r<sub>i</sub>, d<sub>i</sub>)]**: The interval of time during which the job can be executed. It is equal to the relative deadline minus the execution time of the job.
- The temporal parameters of a job determine its priority, schedulability and performance in a real time system .
- A real time system must ensure that all the jobs meet their temporal parameters and constraints, otherwise the system may fail or produce incorrect results .