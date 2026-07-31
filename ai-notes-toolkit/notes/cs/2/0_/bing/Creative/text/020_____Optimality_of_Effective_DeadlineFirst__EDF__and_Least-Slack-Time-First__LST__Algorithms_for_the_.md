### Optimality of Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) Algorithms

- EDF and LST are two dynamic priority scheduling algorithms for real-time systems that assign priorities to tasks based on their deadlines and slacks, respectively.
- A task's deadline is the time by which it must finish its execution, and its slack is the difference between its deadline and its remaining execution time.
- EDF assigns the highest priority to the task with the earliest deadline, and LST assigns the highest priority to the task with the least slack.
- EDF and LST are optimal only when they always produce a feasible schedule if one exists, that is, a schedule that meets all the deadlines of the tasks.
- EDF is optimal for preemptive scheduling of periodic and sporadic tasks with arbitrary deadlines, as well as for non-preemptive scheduling of periodic tasks with implicit deadlines (equal to their periods).
- LST is optimal for preemptive scheduling of periodic tasks with arbitrary deadlines and constrained deadlines (less than or equal to their periods), as well as for non-preemptive scheduling of periodic tasks with implicit deadlines.
- EDF and LST may not be optimal for other types of tasks, such as aperiodic tasks, tasks with precedence constraints, tasks with resource sharing, or tasks with variable execution times.
- EDF and LST may also under-utilize the CPU, that is, leave some idle time when some tasks are ready to execute, especially in the overload scenario where the CPU load is greater than one.
- EDF and LST can be combined to enhance the performance of real-time task scheduling, by switching between them according to the CPU load or the slack distribution of the tasks.