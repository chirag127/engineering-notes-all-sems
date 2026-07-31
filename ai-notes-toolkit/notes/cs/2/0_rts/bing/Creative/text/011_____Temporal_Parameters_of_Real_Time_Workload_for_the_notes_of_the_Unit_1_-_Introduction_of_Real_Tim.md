### Temporal Parameters of Real Time Workload

- A real time workload is a set of tasks or jobs that need to be executed by a real time system within certain time constraints.
- The temporal parameters of a job are the attributes that define its timing requirements and behavior .
- The temporal parameters of a job are:
  - **Release time (r<sub>i</sub>)**: The earliest time at which the job can start execution. It may be known exactly or within a range [r<sub>i</sub><sup>-</sup>, r<sub>i</sub><sup>+</sup>] (jitter).
  - **Absolute deadline (d<sub>i</sub>)**: The latest time by which the job must finish execution. It may be hard (must be met) or soft (can be missed with some penalty).
  - **Relative deadline (D<sub>i</sub>)**: The maximum time allowed for the job to finish execution after its release time. It is equal to d<sub>i</sub> - r<sub>i</sub>.
  - **Feasible interval [(r<sub>i</sub>, d<sub>i</sub>)]**: The time interval in which the job can be feasibly executed by the system. It is equal to D<sub>i</sub> + jitter.
- The temporal parameters of a job may depend on the arrival pattern of the job, which can be periodic, sporadic, or aperiodic.
- The temporal parameters of a job may also depend on the precedence constraints among the jobs, which specify the order of execution of the jobs.
- The temporal parameters of a job are used to analyze the schedulability and performance of the real time system .