# Periodic Task Model

- A periodic task model is a deterministic workload model that describes many hard real-time applications .
- A periodic task is one that repeats itself after a fixed time interval.
- A periodic task is denoted by four tuples: Ti = < Φi, Pi, ei, Di > where:
  - Φi is the phase of the task, which is the time between the start of the system and the release of the first job of the task.
  - Pi is the period of the task, which is the time between two consecutive releases of the task's jobs.
  - ei is the worst-case execution time of the task, which is the maximum time required by any job of the task to complete on a given processor.
  - Di is the relative deadline of the task, which is the maximum time allowed for any job of the task to finish after its release.
- A periodic task is said to be feasible if there exists a schedule that meets all the deadlines of the task's jobs.
- A periodic task is said to be synchronous if all the tasks have zero phase, i.e., Φi = 0 for all i.
- A periodic task is said to be asynchronous if at least one task has a nonzero phase, i.e., Φi > 0 for some i.
- A periodic task model can be extended by adding a jitter Ji for each task Ti, which is the maximum deviation of the actual release time of a job from the exact start time of the period.
- A periodic task model can also be extended by adding a deadline monotonic priority Pi for each task Ti, which is a fixed priority assigned to the task based on its deadline, i.e., the shorter the deadline, the higher the priority.