### Temporal Parameters of Real Time Workload

- Temporal parameters are the time-related attributes of a real time job or task that specify its timing constraints and requirements.
- Some common temporal parameters are :
  - Release time (r<sub>i</sub>): The earliest time at which a job or task can start its execution.
  - Absolute deadline (d<sub>i</sub>): The latest time by which a job or task must finish its execution.
  - Relative deadline (D<sub>i</sub>): The maximum time allowed for a job or task to complete its execution after its release time. It is equal to d<sub>i</sub> - r<sub>i</sub>.
  - Feasible interval ([r<sub>i</sub>, d<sub>i</sub>]): The time interval in which a job or task can be feasibly executed. It is equal to D<sub>i</sub>.
- Temporal parameters are important for defining the performance and correctness of a real time system. They are used to determine the schedulability and feasibility of a real time workload, and to design appropriate scheduling algorithms and policies.
- Temporal parameters may be known in advance (static), or may vary depending on the system state and environment (dynamic). They may also be deterministic (fixed) or stochastic (random).
- Temporal parameters may have different levels of criticality, depending on the consequences of missing them. For example, a hard real time system may have strict temporal parameters that must be met at all times, while a soft real time system may have flexible temporal parameters that can tolerate some degree of deviation.