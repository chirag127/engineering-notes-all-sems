### Temporal Parameters of Real Time Workload

- A real time workload is a set of tasks or jobs that need to be executed by a real time system within certain time constraints.
- The temporal parameters of a job are the attributes that define its timing requirements and characteristics .
- The temporal parameters of a job are:
  - **Release time (r<sub>i</sub>)**: The earliest time at which the job can start execution.
  - **Absolute deadline (d<sub>i</sub>)**: The latest time by which the job must finish execution.
  - **Relative deadline (D<sub>i</sub>)**: The maximum time allowed for the job to finish execution after its release time. It is equal to d<sub>i</sub> - r<sub>i</sub>.
  - **Feasible interval ([r<sub>i</sub>, d<sub>i</sub>])**: The time interval in which the job can be feasibly executed. It is equal to [r<sub>i</sub>, r<sub>i</sub> + D<sub>i</sub>].
- The temporal parameters of a job can be specified by the application or the system designer, or they can be derived from the system model or the environment .
- The temporal parameters of a job can be fixed or variable, depending on the nature of the real time system and the workload.
- The temporal parameters of a job can affect the schedulability, performance, and correctness of the real time system .