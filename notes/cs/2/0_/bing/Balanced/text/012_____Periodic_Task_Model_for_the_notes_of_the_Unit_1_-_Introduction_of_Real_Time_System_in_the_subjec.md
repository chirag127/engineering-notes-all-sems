### Periodic Task Model

- A periodic task is a task that repeats itself after a fixed time interval, called the period.
- A periodic task is characterized by four parameters: phase, period, execution time, and deadline.
- Phase is the time at which the first job of the task is released.
- Period is the time interval between two consecutive job releases.
- Execution time is the worst-case time required to complete a job.
- Deadline is the time by which a job must finish.
- A periodic task model is a deterministic workload model that accurately represents many hard real-time applications, such as digital control, real-time monitoring, and constant bit-rate voice/video transmission .
- A periodic task model can be extended by adding a jitter parameter, which allows the flexibility that the actual release time of a job may be at most jitter time units earlier or later than the exact start time of the period.
- A periodic task model can be analyzed using various scheduling algorithms, such as rate-monotonic, earliest deadline first, and fixed priority .