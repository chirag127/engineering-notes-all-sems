### Common Approaches to Real Time Scheduling

Real-time scheduling is the process of allocating system resources to tasks in a way that ensures that all tasks meet their timing constraints. There are several common approaches to real-time scheduling, including:

1. **Rate Monotonic Scheduling (RMS):** This is a static priority scheduling algorithm where the priority of a task is inversely proportional to its period. The shorter the period of a task, the higher its priority.

2. **Earliest Deadline First (EDF):** This is a dynamic priority scheduling algorithm where the priority of a task is inversely proportional to its absolute deadline. The closer the deadline of a task, the higher its priority.

3. **Least Laxity First (LLF):** This is a dynamic priority scheduling algorithm where the priority of a task is inversely proportional to its laxity. The laxity of a task is the amount of time remaining until its deadline minus its remaining execution time. The smaller the laxity of a task, the higher its priority.

4. **Fixed Priority Scheduling (FPS):** This is a static priority scheduling algorithm where the priority of each task is assigned by the system designer and does not change during runtime.

These are some of the common approaches to real-time scheduling. Each approach has its advantages and disadvantages, and the choice of approach depends on the specific requirements of the system being designed.