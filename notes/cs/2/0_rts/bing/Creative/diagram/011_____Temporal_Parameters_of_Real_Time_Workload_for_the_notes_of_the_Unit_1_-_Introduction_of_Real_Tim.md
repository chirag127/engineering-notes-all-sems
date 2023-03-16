### Temporal Parameters of Real Time Workload

- A real time workload is a set of tasks or jobs that need to be executed by a real time system within certain time constraints.
- The temporal parameters of a job are the attributes that define its timing requirements and characteristics .
- The temporal parameters of a job are:
  - **Release time (r<sub>i</sub>)**: The time instant when the job becomes available for execution. It may be known exactly or within a range [r<sub>i</sub><sup>-</sup>, r<sub>i</sub><sup>+</sup>] (jitter).
  - **Absolute deadline (d<sub>i</sub>)**: The time instant by which the job must finish its execution. It may be fixed or variable depending on the system.
  - **Relative deadline (D<sub>i</sub>)**: The maximum amount of time that the job can tolerate between its release time and its completion time. It is equal to d<sub>i</sub> - r<sub>i</sub>.
  - **Feasible interval [(r<sub>i</sub>, d<sub>i</sub>)]**: The interval of time during which the job can be executed. It is equal to the relative deadline minus the execution time of the job.
- The temporal parameters of a job determine its schedulability, which is the ability of the system to meet the deadlines of all the jobs.
- The temporal parameters of a job may depend on the type of the real time system, such as hard, soft, or firm.
- The temporal parameters of a job may also depend on the type of the workload, such as periodic, aperiodic, or sporadic.