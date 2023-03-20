 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Optimality of Effective-Deadline-First (EDF) and Least-Slack-Time-First (LSTF) Algorithms

- EDF is an optimal preemptive scheduling algorithm for real-time systems. It can meet all deadlines if the system is feasible.
- EDF sorts tasks in increasing order of their deadlines and allocates the CPU to the task with the earliest deadline.
- LSTF is also an optimal preemptive algorithm. It sorts tasks in increasing order of slack time, where slack time is the difference between deadline and completion time. The task with least slack time is executed first.
- Both EDF and LSTF are optimal as they can meet all deadlines if the system is feasible. However, EDF has lower scheduling overhead as task priorities don't change with time and only sorting is required. LSTF requires recomputation of slack times and resorting at every preemption leading to higher overhead.
- For periodic real-time tasks with implicit deadlines, where deadline = period, EDF and LSTF are equivalent. The tasks can be sorted in decreasing order of periods to get EDF or in increasing order of slack times to get LSTF.
- To summarize, EDF and LSTF are two optimal preemptive real-time scheduling algorithms. EDF has lower overhead compared to LSTF making it more suitable for real-time systems with large number of tasks. For periodic tasks with implicit deadlines, EDF and LSTF are equivalent.