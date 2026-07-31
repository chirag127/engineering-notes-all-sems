### Common Approaches to Real Time Scheduling

Real-time scheduling is the process of allocating system resources to tasks in a way that ensures that all tasks meet their timing constraints. There are several common approaches to real-time scheduling, including:

1. **Rate Monotonic Scheduling (RMS):** This is a static priority scheduling algorithm where the priority of a task is inversely proportional to its period. The shorter the period, the higher the priority.

2. **Earliest Deadline First (EDF):** This is a dynamic priority scheduling algorithm where the priority of a task is inversely proportional to its absolute deadline. The closer the deadline, the higher the priority.

3. **Least Laxity First (LLF):** This is a dynamic priority scheduling algorithm where the priority of a task is inversely proportional to its laxity. The laxity of a task is the difference between its deadline and its remaining computation time. The smaller the laxity, the higher the priority.

4. **Fixed Priority Scheduling (FPS):** This is a static priority scheduling algorithm where the priority of each task is fixed and does not change during the execution of the system.

These are some of the common approaches to real-time scheduling. Each approach has its own advantages and disadvantages, and the choice of approach depends on the specific requirements of the system being designed.