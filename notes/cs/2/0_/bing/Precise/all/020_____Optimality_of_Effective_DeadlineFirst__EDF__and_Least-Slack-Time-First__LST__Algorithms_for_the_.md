# Optimality of Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) Algorithms

Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) are two scheduling algorithms used in real-time systems. These algorithms are used to schedule tasks in a way that ensures that all tasks meet their deadlines.

- **Effective-Deadline-First (EDF)**: This algorithm schedules tasks based on their absolute deadlines. The task with the earliest absolute deadline is scheduled first. EDF is an optimal algorithm for scheduling tasks on a single processor, meaning that if a feasible schedule exists, EDF will find it.

- **Least-Slack-Time-First (LST)**: This algorithm schedules tasks based on their slack time, which is the amount of time left until the task's deadline minus the task's remaining execution time. The task with the least slack time is scheduled first. LST is also an optimal algorithm for scheduling tasks on a single processor.

In summary, both EDF and LST are optimal algorithms for scheduling tasks on a single processor in real-time systems. They ensure that all tasks meet their deadlines if a feasible schedule exists.