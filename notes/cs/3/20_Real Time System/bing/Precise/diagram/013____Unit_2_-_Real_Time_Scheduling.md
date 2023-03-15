## Unit 2 - Real Time Scheduling

Real-time scheduling is the process of assigning system resources to tasks in a real-time system. The goal of real-time scheduling is to ensure that all tasks meet their deadlines while optimizing system performance.

1. **Hard Real-Time Systems**: In hard real-time systems, missing a deadline can result in catastrophic consequences. Therefore, the scheduling algorithm must guarantee that all tasks meet their deadlines.

2. **Soft Real-Time Systems**: In soft real-time systems, missing a deadline is undesirable but not catastrophic. The scheduling algorithm aims to minimize the number of missed deadlines.

3. **Rate Monotonic Scheduling (RMS)**: RMS is a priority-based scheduling algorithm for periodic tasks in hard real-time systems. The priority of a task is inversely proportional to its period, i.e., the shorter the period, the higher the priority.

4. **Earliest Deadline First (EDF)**: EDF is a dynamic scheduling algorithm for hard real-time systems. The priority of a task is inversely proportional to its absolute deadline, i.e., the closer the deadline, the higher the priority.

5. **Least Laxity First (LLF)**: LLF is a dynamic scheduling algorithm for hard real-time systems. The priority of a task is inversely proportional to its laxity, i.e., the difference between its deadline and its remaining computation time.

6. **Scheduling in Multiprocessor Systems**: In multiprocessor systems, tasks can be scheduled on multiple processors. There are two main approaches to scheduling in multiprocessor systems: partitioned scheduling and global scheduling.

7. **Partitioned Scheduling**: In partitioned scheduling, tasks are statically assigned to processors, and each processor runs its own scheduling algorithm.

8. **Global Scheduling**: In global scheduling, tasks are dynamically assigned to processors, and a single scheduling algorithm is used to schedule tasks on all processors.