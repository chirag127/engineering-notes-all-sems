### Temporal Parameters of Real Time Workload

- Temporal parameters are the time-related attributes of a real time job or task that define its timing constraints and requirements.
- The temporal parameters of a job are :
  - Release time (r<sub>i</sub>): The earliest time at which a job can start execution. It may be known exactly or within a range [r<sub>-</sub>, r<sub>+</sub>] (jitter).
  - Absolute deadline (d<sub>i</sub>): The latest time by which a job must finish execution. It may be hard (must be met) or soft (can be missed occasionally).
  - Relative deadline (D<sub>i</sub>): The maximum time allowed for a job to finish execution after its release time. It is equal to d<sub>i</sub> - r<sub>i</sub>.
  - Feasible interval [(r<sub>i</sub>, d<sub>i</sub>]: The time interval in which a job can be feasibly executed. It is equal to D<sub>i</sub>.
- The temporal parameters of a job can be specified by a real time constraint, which is a logical expression that relates temporal properties with an explicit reference to time. For example, a real time constraint may specify that a job must start 5 ms after another job finishes.
- The temporal parameters of a job can be used to analyze and verify the schedulability and performance of a real time system, which is the ability of the system to meet the timing constraints of all the jobs. For example, a schedulability test can check if the feasible intervals of all the jobs are compatible with the available resources and the scheduling algorithm.