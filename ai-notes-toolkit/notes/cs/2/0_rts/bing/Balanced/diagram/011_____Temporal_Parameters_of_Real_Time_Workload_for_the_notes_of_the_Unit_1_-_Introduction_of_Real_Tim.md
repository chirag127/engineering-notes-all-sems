### Temporal Parameters of Real Time Workload

- Temporal parameters are the time-related attributes of a real time job or task that specify its timing constraints and requirements.
- The temporal parameters of a job are :
  - Release time (r<sub>i</sub>): The earliest time at which a job can start execution. It may be known exactly or within a range [r<sub>i</sub><sup>-</sup>, r<sub>i</sub><sup>+</sup>] (jitter).
  - Absolute deadline (d<sub>i</sub>): The latest time by which a job must finish execution. It may be hard (must be met) or soft (can be missed occasionally).
  - Relative deadline (D<sub>i</sub>): The maximum time allowed for a job to finish execution after its release time. It is equal to d<sub>i</sub> - r<sub>i</sub>.
  - Feasible interval [(r<sub>i</sub>, d<sub>i</sub>]: The time interval in which a job can be feasibly executed. It is the difference between the release time and the absolute deadline.
- The temporal parameters of a job can be represented graphically as follows:

```
|<----------------- D_i ----------------->|
|<----- r_i ----->|<------ C_i ------->|<----- d_i ----->|
|-----------------|--------------------|-----------------|
0                 r_i                  d_i               t
```

- Where C<sub>i</sub> is the worst-case execution time of the job, and t is the time axis.
- The temporal parameters of a job can be used to determine its schedulability, priority, and performance metrics.