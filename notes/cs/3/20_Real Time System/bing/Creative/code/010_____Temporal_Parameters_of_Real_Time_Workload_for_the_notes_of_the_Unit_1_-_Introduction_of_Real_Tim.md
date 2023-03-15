### Temporal Parameters of Real Time Workload

- A real time workload is a set of tasks or jobs that need to be executed by a real time system within certain time constraints.
- The temporal parameters of a job are the attributes that define its timing requirements and characteristics .
- The temporal parameters of a job are:
  - **Release time (r<sub>i</sub>)**: The time instant when the job becomes available for execution. It may be known exactly or within a range [r<sub>i</sub><sup>-</sup>, r<sub>i</sub><sup>+</sup>] (jitter).
  - **Absolute deadline (d<sub>i</sub>)**: The time instant by which the job must finish its execution. It may be fixed or variable depending on the system.
  - **Relative deadline (D<sub>i</sub>)**: The time interval between the release time and the absolute deadline of the job. It may be equal to or less than the job's execution time.
  - **Feasible interval ([r<sub>i</sub>, d<sub>i</sub>])**: The time interval in which the job can be feasibly executed by the system. It depends on the system's scheduling policy and resource availability.
- The temporal parameters of a job determine its urgency, priority, and schedulability in a real time system .
- A real time system must ensure that all the jobs in the workload meet their temporal parameters, otherwise the system may fail to deliver the expected functionality and quality of service .