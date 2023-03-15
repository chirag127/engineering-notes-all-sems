### Temporal Parameters of Real Time Workload

- Temporal parameters are the time-related attributes of a real time job or task that specify its timing constraints and requirements.
- The temporal parameters of a job are :
  - Release time (r<sub>i</sub>): The earliest time at which a job can start execution. It may be known exactly or within a range [r<sub>-</sub>, r<sub>+</sub>] (jitter).
  - Absolute deadline (d<sub>i</sub>): The latest time by which a job must finish execution. It may be hard (must be met) or soft (can be missed occasionally).
  - Relative deadline (D<sub>i</sub>): The maximum time allowed for a job to finish execution after its release time. It is equal to d<sub>i</sub> - r<sub>i</sub>.
  - Feasible interval [(r<sub>i</sub>, d<sub>i</sub>]: The time interval in which a job can be feasibly executed. It is equal to D<sub>i</sub>.
- The temporal parameters of a job determine its urgency, priority, and schedulability in a real time system. They also affect the performance metrics of the system, such as response time, utilization, and deadline miss ratio.