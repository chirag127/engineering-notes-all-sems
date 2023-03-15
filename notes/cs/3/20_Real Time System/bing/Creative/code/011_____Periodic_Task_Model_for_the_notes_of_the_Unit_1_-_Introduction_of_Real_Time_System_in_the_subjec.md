### Periodic Task Model

- The periodic task model is a well-known deterministic workload model that characterizes accurately many traditional hard real-time applications, such as digital control, real-time monitoring, and constant bit-rate voice/video transmission .
- A periodic task is one that repeats itself after a fixed time interval, called the period.
- A periodic task is denoted by four tuples: Ti = < Φi, Pi, ei, Di > Where, Φi – is the phase of the task, Pi – is the period of the task, ei – is the worst-case execution time of the task, and Di – is the relative deadline of the task.
- The phase of a task is the time difference between the start of the first job and the start of the hyperperiod. The hyperperiod is the least common multiple of the periods of all the tasks.
- The relative deadline of a task is the maximum allowable time between the release of a job and its completion. The absolute deadline of a job is the sum of its release time and its relative deadline.
- A periodic task is said to be feasible if there exists a schedule that meets all the deadlines of the task. A set of periodic tasks is said to be feasible if there exists a schedule that meets all the deadlines of all the tasks.
- The periodic task model can be extended by adding a jitter Ji for each task τi, to allow the flexibility that the actual release time of a job may be at most Ji time units earlier or later than the exact start time of the period.
- The periodic task model can also be extended by adding a deadline monotonic priority Pi for each task τi, to indicate the relative urgency of the task. A higher priority means a higher urgency.
- The periodic task model can be used to analyze the schedulability of real-time systems using various scheduling algorithms, such as rate monotonic, earliest deadline first, and fixed priority  .
- The periodic task model can also be used to design real-time systems using various techniques, such as harmonic periods, utilization bounds, and response time analysis  .