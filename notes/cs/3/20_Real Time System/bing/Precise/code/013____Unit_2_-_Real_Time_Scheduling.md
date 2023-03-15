## Unit 2 - Real Time Scheduling

Real-time scheduling is the process of assigning system resources to tasks in a real-time system. The goal of real-time scheduling is to ensure that all tasks meet their deadlines while optimizing system performance.

1. **Hard Real-Time Systems**: In hard real-time systems, missing a deadline can result in catastrophic consequences. Therefore, the scheduling algorithm must guarantee that all tasks meet their deadlines.
2. **Soft Real-Time Systems**: In soft real-time systems, missing a deadline can result in degraded system performance, but not catastrophic consequences. Therefore, the scheduling algorithm should try to ensure that all tasks meet their deadlines, but it is not a strict requirement.
3. **Rate Monotonic Scheduling (RMS)**: RMS is a priority-based scheduling algorithm for periodic tasks in hard real-time systems. The priority of a task is inversely proportional to its period, i.e., the shorter the period, the higher the priority.
4. **Earliest Deadline First (EDF)**: EDF is a dynamic priority scheduling algorithm for hard real-time systems. The priority of a task is inversely proportional to its absolute deadline, i.e., the closer the deadline, the higher the priority.
5. **Least Laxity First (LLF)**: LLF is a dynamic priority scheduling algorithm for hard real-time systems. The priority of a task is inversely proportional to its laxity, i.e., the difference between its deadline and its remaining computation time.
