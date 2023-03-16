### Rate Monotonic Algorithm

Rate Monotonic Algorithm (RMA) is a priority assignment algorithm used in real-time scheduling. It is a static priority scheduling algorithm, which means that the priorities of tasks are assigned before the system starts running and do not change during execution.

Here are some key points to remember about the Rate Monotonic Algorithm:

1. RMA assigns priorities to tasks based on their periods. The shorter the period of a task, the higher its priority.
2. RMA is an optimal algorithm for scheduling periodic tasks on a uniprocessor system. This means that if a set of periodic tasks can be scheduled by any static priority algorithm, it can also be scheduled by RMA.
3. RMA is a preemptive algorithm, which means that a higher priority task can interrupt a lower priority task that is currently executing.
4. The schedulability of a set of tasks under RMA can be determined using the Liu and Layland utilization bound or the hyperbolic bound.
5. RMA is not suitable for scheduling tasks with deadlines that are different from their periods or for scheduling aperiodic or sporadic tasks.
