# Periodic Task Model

- The periodic task model is a well-known deterministic workload model that characterizes accurately many traditional hard real-time applications, such as digital control, real-time monitoring, and constant bit-rate voice/video transmission .
- A periodic task is one that repeats itself after a fixed time interval, called the period.
- A periodic task is denoted by four tuples: Ti = < Φi, Pi, ei, Di > Where, Φi – is the phase of the task, Pi – is the period of the task, ei – is the worst-case execution time of the task, and Di – is the relative deadline of the task.
- The phase of a task is the time difference between the start of the first job and the start of the hyperperiod, which is the least common multiple of all the periods.
- The relative deadline of a task is the maximum allowable time between the release of a job and its completion.
- The utilization of a periodic task is defined as the ratio of its execution time to its period: Ui = ei / Pi.
- The utilization of a set of periodic tasks is the sum of their individual utilizations: U = Σ Ui.
- The periodic task model can be extended by adding a jitter Ji for each task τi, to allow the flexibility that the actual release time of a job may be at most Ji time units earlier or later than the exact start time of the period.
- The periodic task model can also be extended by adding a deadline slack Si for each task τi, to allow the flexibility that the actual deadline of a job may be at most Si time units earlier or later than the relative deadline of the task.
- The periodic task model can be used to analyze the schedulability of a set of tasks under different scheduling algorithms, such as rate-monotonic, earliest deadline first, or least laxity first .