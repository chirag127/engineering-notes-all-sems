# Optimality of Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) Algorithms

- EDF and LST are two dynamic priority scheduling algorithms for real-time systems that assign priorities to tasks based on their deadlines and slacks, respectively.
- A deadline is the time by which a task must finish its execution, and a slack is the difference between the deadline and the remaining execution time of a task.
- EDF assigns the highest priority to the task with the earliest deadline, and LST assigns the highest priority to the task with the least slack.
- EDF and LST are optimal only when they always produce a feasible schedule if one exists, that is, a schedule that meets all the deadlines of the tasks.
- EDF is optimal for preemptive scheduling of periodic and sporadic tasks with arbitrary deadlines, as well as for non-preemptive scheduling of periodic tasks with implicit deadlines (equal to their periods).
- LST is optimal for preemptive scheduling of periodic tasks with arbitrary deadlines and constrained deadlines (less than or equal to their periods), as well as for non-preemptive scheduling of periodic tasks with implicit deadlines.
- EDF and LST may not be optimal for other types of tasks, such as aperiodic tasks, tasks with precedence constraints, tasks with resource sharing, or tasks with variable execution times.
- EDF and LST may also have some drawbacks, such as high overhead, poor response time, low utilization, and deadline misses in overload scenarios.
- EDF and LST can be combined or modified to enhance their performance and overcome their limitations, such as using slack stealing, slack reclamation, or hybrid algorithms.