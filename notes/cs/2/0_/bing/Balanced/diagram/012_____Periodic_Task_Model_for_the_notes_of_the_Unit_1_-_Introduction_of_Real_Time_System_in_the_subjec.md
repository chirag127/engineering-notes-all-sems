### Periodic Task Model

- A periodic task is a task that repeats itself after a fixed time interval, called the period.
- A periodic task is characterized by four parameters: phase, period, execution time, and deadline.
- Phase is the time at which the first instance of the task is released.
- Period is the time interval between two consecutive releases of the task.
- Execution time is the worst-case time required by the task to complete its execution.
- Deadline is the time by which the task must finish its execution.
- A periodic task can be represented by a tuple: T = <Φ, P, e, D> where Φ is the phase, P is the period, e is the execution time, and D is the deadline.
- A periodic task can also be represented by a timeline diagram, as shown below:

![Periodic task timeline diagram](https://www.skedsoft.com/books/real-time-systems/periodic-task-model/periodic-task-model.png)

- The periodic task model is a deterministic workload model that can accurately characterize many traditional hard real-time applications, such as digital control, real-time monitoring, and constant bit-rate voice/video transmission.
- The periodic task model can be extended by adding a jitter parameter, which allows the flexibility that the actual release time of a task may be at most J time units earlier or later than the exact start time of the period.
- The periodic task model can also be extended by adding a sporadic task model, which allows the tasks to have variable inter-arrival times, as long as they are bounded by a minimum separation time.
