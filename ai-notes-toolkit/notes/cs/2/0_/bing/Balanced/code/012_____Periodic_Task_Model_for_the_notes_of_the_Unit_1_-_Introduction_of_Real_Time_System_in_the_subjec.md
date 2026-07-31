### Periodic Task Model

- A periodic task is a task that repeats itself after a fixed time interval, called the period.
- A periodic task is characterized by four parameters: phase, period, execution time, and deadline .
- Phase is the time at which the first instance of the task is released.
- Period is the time interval between two consecutive releases of the task.
- Execution time is the worst-case time required by the task to complete its execution.
- Deadline is the time by which the task must finish its execution.
- The periodic task model is a deterministic workload model that accurately represents many hard real-time applications, such as digital control, real-time monitoring, and constant bit-rate voice/video transmission .
- The periodic task model can be extended by adding a jitter parameter, which allows the flexibility that the actual release time of a task may vary within a certain range from the exact start time of the period.
