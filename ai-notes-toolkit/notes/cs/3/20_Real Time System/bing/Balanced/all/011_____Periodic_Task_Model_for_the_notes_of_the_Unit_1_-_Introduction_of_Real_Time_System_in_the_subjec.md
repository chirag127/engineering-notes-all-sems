# Periodic Task Model

The periodic task model is a well-known deterministic workload model for real-time systems. It is best suited for hard real-time applications, such as digital control, real-time monitoring, and constant bit-rate voice/video transmission .

A periodic task is one that repeats itself after a fixed time interval. A periodic task is denoted by four tuples: Ti = < Φi, Pi, ei, Di >

Where,

- Φi – is the phase of the task. It is the time at which the first job of the task is released.
- Pi – is the period of the task. It is the time interval between two consecutive job releases of the task.
- ei – is the worst-case execution time of the task. It is the maximum time required by any job of the task to complete its execution on the processor.
- Di – is the relative deadline of the task. It is the maximum time allowed for any job of the task to finish its execution after its release.

The periodic task model assumes that:

- All tasks are independent and do not share any resources.
- All tasks have fixed and known parameters.
- All tasks have implicit deadlines, i.e., Di = Pi for all tasks.
- All tasks have constrained deadlines, i.e., Di ≤ Pi for all tasks.
- All tasks have zero jitter, i.e., Ji = 0 for all tasks.

The periodic task model can be extended by adding more parameters, such as jitter, offset, precedence constraints, resource requirements, etc. to capture more realistic scenarios.
