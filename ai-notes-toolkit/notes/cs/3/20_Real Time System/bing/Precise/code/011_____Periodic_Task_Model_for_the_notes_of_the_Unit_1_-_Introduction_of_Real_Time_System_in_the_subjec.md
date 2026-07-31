### Periodic Task Model

- In real-time systems, a periodic task model is a commonly used model for representing recurring tasks.
- A periodic task is characterized by a fixed period, which is the time interval between consecutive releases of the task.
- Each release of the task is called a job, and the task must complete its execution before the next release.
- The worst-case execution time (WCET) of a task is the maximum time it takes for the task to complete its execution.
- The utilization of a task is defined as the ratio of its WCET to its period.
- The schedulability of a set of periodic tasks can be determined by analyzing their utilization and deadlines.
- Common scheduling algorithms for periodic tasks include Rate Monotonic Scheduling (RMS) and Earliest Deadline First (EDF) scheduling.
- In RMS, tasks are assigned priorities based on their periods, with shorter period tasks having higher priorities.
- In EDF, tasks are assigned priorities based on their deadlines, with earlier deadline tasks having higher priorities.
- The utilization bound for RMS is given by `U <= n(2^(1/n) - 1)`, where `n` is the number of tasks and `U` is the total utilization of all tasks.
- The utilization bound for EDF is `U <= 1`, meaning that a set of tasks is schedulable under EDF if their total utilization is less than or equal to 1.