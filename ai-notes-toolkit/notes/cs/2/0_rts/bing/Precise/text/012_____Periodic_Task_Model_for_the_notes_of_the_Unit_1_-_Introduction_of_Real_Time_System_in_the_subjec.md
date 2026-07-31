### Periodic Task Model

- A periodic task model is a model used in real-time systems to represent tasks that have a fixed period.
- In this model, tasks are released periodically at fixed intervals, and each task has a deadline by which it must be completed.
- The period of a task is the time interval between two consecutive releases of the task.
- The deadline of a task is the time by which the task must be completed after it is released.
- The execution time of a task is the time it takes for the task to complete its execution once it starts.
- The utilization of a task is the ratio of its execution time to its period.
- The schedulability of a set of periodic tasks is determined by whether all tasks can meet their deadlines under a given scheduling algorithm.
- Common scheduling algorithms for periodic tasks include Rate Monotonic Scheduling (RMS) and Earliest Deadline First (EDF) scheduling.
- In RMS, tasks are assigned priorities based on their periods, with shorter period tasks having higher priorities.
- In EDF, tasks are assigned priorities based on their deadlines, with earlier deadline tasks having higher priorities.
