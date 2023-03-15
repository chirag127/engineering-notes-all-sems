# Optimality of Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) Algorithms

- EDF and LST are two dynamic priority scheduling algorithms for real-time systems that assign priorities to tasks based on their deadlines and slacks, respectively.
- A deadline is the time by which a task must finish its execution, and a slack is the difference between the deadline and the remaining execution time of a task.
- EDF assigns the highest priority to the task with the earliest deadline, and LST assigns the highest priority to the task with the least slack.
- EDF and LST are optimal only when they always produce a feasible schedule if one exists, meaning that they can meet all the deadlines of the tasks in the system.
- EDF is optimal for preemptive scheduling of periodic and sporadic tasks with arbitrary deadlines, as long as the total utilization of the system is less than or equal to one.
- LST is optimal for preemptive scheduling of periodic and sporadic tasks with constrained deadlines, meaning that the deadline of each task is less than or equal to its period.
- EDF and LST may not be optimal for non-preemptive scheduling, aperiodic tasks, tasks with shared resources, or tasks with precedence constraints.
- EDF and LST may also under-utilize the CPU, meaning that they may leave some idle time when some tasks are not ready or have finished their execution.
- EDF and LST can be combined to enhance the performance of real-time task scheduling by switching between them according to the system load or the slack distribution of the tasks  .