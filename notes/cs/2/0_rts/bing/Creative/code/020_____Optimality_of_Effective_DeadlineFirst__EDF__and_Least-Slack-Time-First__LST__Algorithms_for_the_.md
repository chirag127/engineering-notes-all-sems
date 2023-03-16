### Optimality of Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) Algorithms

- EDF and LST are two dynamic priority scheduling algorithms used in real-time systems.
- EDF assigns priorities to tasks according to their absolute deadlines. The task with the earliest deadline has the highest priority and is executed first.
- LST assigns priorities to tasks according to their slacks. The slack of a task is the difference between its deadline and its remaining execution time. The task with the least slack has the highest priority and is executed first.
- Both EDF and LST are optimal for preemptive scheduling of periodic tasks with implicit deadlines, meaning that the deadline of each task is equal to its period.
- EDF is also optimal for preemptive scheduling of periodic tasks with arbitrary deadlines, meaning that the deadline of each task can be less than or equal to its period.
- LST is not optimal for preemptive scheduling of periodic tasks with arbitrary deadlines, as it may under-utilize the CPU and miss some deadlines.
- EDF and LST are not optimal for non-preemptive scheduling of periodic tasks, as they may cause unnecessary blocking and context switching.
- EDF and LST can also be used for scheduling aperiodic tasks, which have no fixed period or deadline. However, they may not be optimal or feasible in some cases, depending on the arrival time, execution time, and deadline of each aperiodic task.