### Temporal Parameters of Real Time Workload

- Temporal parameters are the time-related attributes of a real time job or task that specify its timing constraints and requirements.
- The temporal parameters of a job are :
  - **Release time (r<sub>i</sub>)**: The earliest time at which a job can start execution. It may be known exactly or within a range [r<sub>i</sub><sup>-</sup>, r<sub>i</sub><sup>+</sup>] (jitter).
  - **Absolute deadline (d<sub>i</sub>)**: The latest time by which a job must finish execution. It may be hard (must be met) or soft (can be missed occasionally).
  - **Relative deadline (D<sub>i</sub>)**: The maximum allowed time between the release time and the absolute deadline of a job. It is equal to d<sub>i</sub> - r<sub>i</sub>.
  - **Feasible interval [(r<sub>i</sub>, d<sub>i</sub>)]**: The time interval in which a job can be feasibly executed. It is equal to the relative deadline minus the execution time of the job.
- Temporal parameters are important for the analysis and specification of real time systems, as they determine the schedulability and performance of the system.
- Temporal parameters can also be used to express real time constraints, which are the temporal properties that must be satisfied by the system. For example, a real time constraint may specify that a job must start within 10 ms after another job finishes.