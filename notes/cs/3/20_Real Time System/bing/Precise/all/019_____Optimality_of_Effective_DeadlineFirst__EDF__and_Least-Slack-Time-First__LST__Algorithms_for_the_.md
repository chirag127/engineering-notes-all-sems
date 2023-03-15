# Optimality of Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) Algorithms

Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) are two scheduling algorithms used in real-time systems. These algorithms are used to schedule tasks with deadlines in a way that ensures that all tasks meet their deadlines.

1. **Effective-Deadline-First (EDF)**: This algorithm schedules tasks based on their absolute deadlines. The task with the earliest absolute deadline is scheduled first. EDF is an optimal algorithm for scheduling tasks with deadlines on a single processor. This means that if there is a feasible schedule for a set of tasks with deadlines, EDF will always find it.

2. **Least-Slack-Time-First (LST)**: This algorithm schedules tasks based on their slack time. The slack time of a task is the amount of time left until its deadline minus the amount of time the task still needs to execute. The task with the least slack time is scheduled first. LST is also an optimal algorithm for scheduling tasks with deadlines on a single processor.

In summary, both EDF and LST are optimal algorithms for scheduling tasks with deadlines on a single processor. They ensure that all tasks meet their deadlines if a feasible schedule exists. These algorithms are commonly used in real-time systems to ensure that all tasks are completed on time.