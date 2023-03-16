### Common Approaches to Real Time Scheduling

Real-time scheduling is the process of assigning priorities to tasks in a real-time system to ensure that they meet their deadlines. There are several common approaches to real-time scheduling, including:

1. **Rate Monotonic Scheduling (RMS):** This is a static priority scheduling algorithm where the priority of a task is inversely proportional to its period. The shorter the period, the higher the priority.

2. **Earliest Deadline First (EDF):** This is a dynamic priority scheduling algorithm where the priority of a task is inversely proportional to its absolute deadline. The closer the deadline, the higher the priority.

3. **Least Laxity First (LLF):** This is a dynamic priority scheduling algorithm where the priority of a task is inversely proportional to its laxity. The laxity of a task is the difference between its deadline and its remaining computation time. The smaller the laxity, the higher the priority.

4. **Fixed Priority Scheduling (FPS):** This is a static priority scheduling algorithm where the priorities of tasks are assigned based on their importance or criticality. The more important or critical the task, the higher the priority.

These are some of the common approaches to real-time scheduling. Each approach has its advantages and disadvantages, and the choice of approach depends on the specific requirements of the real-time system.