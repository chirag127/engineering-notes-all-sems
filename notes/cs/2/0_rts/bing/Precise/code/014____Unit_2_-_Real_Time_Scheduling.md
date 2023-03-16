## Unit 2 - Real Time Scheduling

Real-time scheduling is the process of assigning CPU time to tasks in a real-time system. The goal of real-time scheduling is to ensure that all tasks meet their deadlines, while also maximizing system performance.

There are several types of real-time scheduling algorithms, including:

1. **Rate Monotonic Scheduling (RMS)**: This is a static priority scheduling algorithm where tasks are assigned priorities based on their periods. The shorter the period, the higher the priority.

2. **Earliest Deadline First (EDF)**: This is a dynamic priority scheduling algorithm where tasks are assigned priorities based on their deadlines. The closer the deadline, the higher the priority.

3. **Least Laxity First (LLF)**: This is a dynamic priority scheduling algorithm where tasks are assigned priorities based on their laxity. The laxity of a task is the amount of time remaining until its deadline minus its remaining execution time. The smaller the laxity, the higher the priority.

Real-time scheduling algorithms can be either preemptive or non-preemptive. In preemptive scheduling, a higher priority task can interrupt a lower priority task, while in non-preemptive scheduling, a task must complete before another task can be scheduled.

Real-time scheduling is a complex and challenging problem, and there is ongoing research in this area to develop new algorithms and improve existing ones. It is an important topic in the field of real-time systems and is essential for ensuring the correct and timely operation of these systems.