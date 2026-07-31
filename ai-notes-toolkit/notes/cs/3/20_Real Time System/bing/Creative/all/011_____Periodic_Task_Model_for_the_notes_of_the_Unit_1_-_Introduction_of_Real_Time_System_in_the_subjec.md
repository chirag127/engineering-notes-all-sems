# Periodic Task Model

- The periodic task model is a well-known deterministic workload model that characterizes accurately many traditional hard real-time applications, such as digital control, real-time monitoring, and constant bit-rate voice/video transmission .
- A periodic task is one that repeats itself after a fixed time interval, called the period.
- A periodic task is denoted by four tuples: Ti = < Φi, Pi, ei, Di > Where, 
  - Φi – is the phase of the task, which is the time instant when the first job of the task is released.
  - Pi – is the period of the task, which is the time interval between two consecutive job releases of the task.
  - ei – is the worst-case execution time of the task, which is the maximum time required by any job of the task to complete its execution on a given processor.
  - Di – is the relative deadline of the task, which is the maximum time allowed for any job of the task to finish its execution after its release.
- The periodic task model can be extended by adding a jitter Ji for each task τi, to allow the flexibility that the actual release time of a job may be at most Ji time units earlier or later than the exact start time of the period.
- The periodic task model can also be extended by adding a priority Pi for each task τi, to specify the order of execution of the tasks in case of resource contention.
- The periodic task model can be used to analyze the schedulability of a set of tasks on a single processor or a multiprocessor system, using various scheduling algorithms, such as rate-monotonic, earliest-deadline-first, or fixed-priority  .