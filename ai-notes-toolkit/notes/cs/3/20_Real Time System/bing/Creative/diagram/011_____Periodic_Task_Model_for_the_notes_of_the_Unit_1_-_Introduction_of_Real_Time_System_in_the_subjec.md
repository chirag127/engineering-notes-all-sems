### Periodic Task Model

- A periodic task is a task that repeats itself after a fixed time interval, called the period.
- A periodic task is denoted by four tuples: Ti = < Φi, Pi, ei, Di > Where, 
  - Φi – is the phase of the task, which is the time difference between the start of the first job and the start of the hyperperiod.
  - Pi – is the period of the task, which is the time interval between two consecutive job releases.
  - ei – is the worst-case execution time of the task, which is the maximum time required by any job of the task to complete on a given processor.
  - Di – is the relative deadline of the task, which is the maximum time allowed for any job of the task to finish after its release.
- The periodic task model is a well-known deterministic workload model that characterizes accurately many traditional hard real-time applications, such as digital control, real-time monitoring, and constant bit-rate voice/video transmission .
- The periodic task model can be extended by adding a jitter Ji for each task τi, to allow the flexibility that the actual release time of a job may be at most Ji time units earlier or later than the exact start time of the period.
- The periodic task model can be represented by a task graph, where each node is a task and each edge is a precedence constraint between tasks.
- The periodic task model can be analyzed by using various scheduling algorithms, such as rate-monotonic, earliest deadline first, or fixed priority, to determine the feasibility and schedulability of the task set.