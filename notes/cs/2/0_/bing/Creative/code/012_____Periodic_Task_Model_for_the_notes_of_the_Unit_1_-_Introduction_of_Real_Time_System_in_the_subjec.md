### Periodic Task Model

- The periodic task model is a well-known deterministic workload model that characterizes accurately many traditional hard real-time applications, such as digital control, real-time monitoring, and constant bit-rate voice/video transmission .
- A periodic task generates an infinite sequence of jobs (or called task instances) that are released at regular intervals. A periodic task repeats itself after a fixed time interval  .
- A periodic task is denoted by four or five tuples: Ti = < Φi, Pi, ei, Di > or Ti = < Φi, Pi, ei, Di, Ri >  where:
  - Φi is the phase of the task, which is the time of the first job release.
  - Pi is the period of the task, which is the time interval between two consecutive job releases.
  - ei is the worst-case execution time of the task, which is the maximum time required to execute a job on a given processor.
  - Di is the relative deadline of the task, which is the maximum time allowed for a job to complete after its release.
  - Ri is the resource requirement of the task, which is the amount of a shared resource (such as memory or bandwidth) needed by a job during its execution.
- A periodic task is said to be feasible if there exists a schedule that can meet all the deadlines of its jobs. A set of periodic tasks is said to be feasible if there exists a schedule that can meet all the deadlines of all the jobs of all the tasks.
- A periodic task is said to be implicit-deadline if Di = Pi, constrained-deadline if Di ≤ Pi, and arbitrary-deadline if Di can be any value.
- A periodic task is said to be harmonic if its period is an integer multiple of the periods of all the other tasks in the system.
- A periodic task is said to be sporadic if its period is the minimum separation time between two consecutive job releases, and aperiodic if its period is the maximum separation time between two consecutive job releases.