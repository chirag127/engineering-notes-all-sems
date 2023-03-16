### Periodic Task Model

- The periodic task model is a well-known deterministic workload model that characterizes accurately many traditional hard real-time applications, such as digital control, real-time monitoring, and constant bit-rate voice/video transmission .
- A periodic task is one that repeats itself after a fixed time interval, called the period.
- A periodic task is denoted by four tuples: Ti = < Φi, Pi, ei, Di > Where, Φi – is the phase of the task, Pi – is the period of the task, ei – is the worst-case execution time of the task, and Di – is the relative deadline of the task.
- The phase of a task is the time difference between the start of the first job and the start of the hyperperiod. The hyperperiod is the least common multiple of the periods of all the tasks in the system.
- The relative deadline of a task is the maximum allowable time between the release of a job and its completion. The absolute deadline of a job is the sum of its release time and its relative deadline.
- A periodic task is said to be feasible if there exists a scheduling algorithm that can guarantee that all the jobs of the task meet their deadlines.
- A set of periodic tasks is said to be feasible if there exists a scheduling algorithm that can guarantee that all the jobs of all the tasks meet their deadlines.
- The periodic task model can be extended by adding a jitter Ji for each task τi, to allow the flexibility that the actual release time of a job may be at most Ji time units earlier or later than the exact start time of the period.
- The periodic task model can also be extended by adding a deadline slack Si for each task τi, to allow the flexibility that the actual deadline of a job may be at most Si time units earlier or later than the exact end time of the period.
- The periodic task model can be further extended by adding a priority Pi for each task τi, to specify the relative importance of the task in the system. A higher priority task can preempt a lower priority task if they are ready to execute at the same time.