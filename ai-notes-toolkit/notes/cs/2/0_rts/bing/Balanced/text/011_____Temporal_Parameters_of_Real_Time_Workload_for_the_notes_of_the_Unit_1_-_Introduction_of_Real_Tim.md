### Temporal Parameters of Real Time Workload

- Temporal parameters are the time-related attributes of a real time job or task that define its timing constraints and requirements.
- The temporal parameters of a job are  :
  - Release time (ri): The earliest time at which a job can start execution. It may be known exactly or within a range [r-, r+] (jitter).
  - Absolute deadline (di): The latest time by which a job must finish execution. It may be hard (must be met) or soft (can be missed occasionally).
  - Relative deadline (Di): The maximum time allowed for a job to finish execution after its release time. It is equal to di - ri.
  - Feasible interval [(ri, di)]: The time interval in which a job can be feasibly scheduled and executed. It is equal to Di.
- The temporal parameters of a job depend on the characteristics of the real time system, such as the workload, the scheduling algorithm, the resource availability, and the performance metrics.
- The temporal parameters of a job can be used to analyze and verify the temporal behavior and correctness of a real time system, such as the schedulability, the response time, the utilization, and the deadline miss ratio.