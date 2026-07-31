### Periodic Task Model

- A periodic task is a task that is executed repeatedly at regular intervals.
- The interval between two consecutive executions of a periodic task is called the period of the task.
- The period of a task is usually specified as a fixed value, but it can also be specified as a range of values.
- The execution time of a periodic task is the time it takes for the task to complete one execution.
- The deadline of a periodic task is the time by which the task must complete its execution.
- The utilization of a periodic task is the ratio of its execution time to its period.
- A set of periodic tasks is said to be schedulable if there exists a scheduling algorithm that can schedule the tasks such that all their deadlines are met.
- The utilization bound of a set of periodic tasks is the maximum utilization that the set of tasks can have and still be schedulable.
- The rate-monotonic scheduling algorithm is a commonly used algorithm for scheduling periodic tasks. It assigns priorities to tasks based on their periods, with shorter periods having higher priorities.
- The earliest deadline first scheduling algorithm is another commonly used algorithm for scheduling periodic tasks. It assigns priorities to tasks based on their deadlines, with earlier deadlines having higher priorities.
