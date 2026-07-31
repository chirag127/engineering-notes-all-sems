### Common Approaches to Real Time Scheduling

Real-time scheduling is the process of allocating system resources to tasks in a way that ensures that all tasks meet their timing constraints. There are several common approaches to real-time scheduling, including:

1. **Rate Monotonic Scheduling (RMS):** This is a static priority scheduling algorithm where the priority of a task is inversely proportional to its period. Tasks with shorter periods are assigned higher priorities.

2. **Earliest Deadline First (EDF):** This is a dynamic priority scheduling algorithm where the priority of a task is inversely proportional to its absolute deadline. Tasks with earlier deadlines are assigned higher priorities.

3. **Least Laxity First (LLF):** This is a dynamic priority scheduling algorithm where the priority of a task is inversely proportional to its laxity. Laxity is defined as the difference between the task's deadline and its remaining computation time. Tasks with smaller laxity are assigned higher priorities.

4. **Fixed Priority Scheduling (FPS):** This is a static priority scheduling algorithm where the priority of a task is assigned by the system designer and does not change during runtime.

These are some of the common approaches to real-time scheduling. Each approach has its own advantages and disadvantages, and the choice of approach depends on the specific requirements of the system.