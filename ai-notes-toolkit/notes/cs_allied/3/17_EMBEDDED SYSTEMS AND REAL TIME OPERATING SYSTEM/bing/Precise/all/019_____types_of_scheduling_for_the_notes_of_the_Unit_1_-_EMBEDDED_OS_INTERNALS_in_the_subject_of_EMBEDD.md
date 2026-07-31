# Types of Scheduling for the Notes of the Unit 1 - Embedded OS Internals in the Subject of Embedded Systems and Real Time Operating System

Scheduling is the process of allocating system resources to different tasks or processes. In the context of an embedded operating system, scheduling is used to determine which task should be executed at a given time. There are several types of scheduling algorithms that can be used in an embedded operating system, including:

1. **First-Come, First-Served (FCFS):** This is the simplest scheduling algorithm, where tasks are executed in the order in which they arrive in the ready queue. This algorithm is easy to implement but can result in long waiting times for tasks that arrive later in the queue.

2. **Shortest Job First (SJF):** This algorithm schedules tasks based on their execution time, with the shortest task being executed first. This can result in shorter average waiting times, but can also lead to starvation for longer tasks.

3. **Priority Scheduling:** This algorithm schedules tasks based on their priority, with higher priority tasks being executed before lower priority tasks. This can be useful in real-time systems where certain tasks have strict timing requirements.

4. **Round Robin:** This algorithm allocates a fixed time slice to each task in the ready queue, and tasks are executed in a cyclic order. This can provide fairness and prevent starvation, but can also result in longer waiting times for tasks with longer execution times.

5. **Rate Monotonic Scheduling (RMS):** This is a priority-based scheduling algorithm used in real-time systems, where tasks are assigned priorities based on their period (the time between successive executions). Tasks with shorter periods are assigned higher priorities.

6. **Earliest Deadline First (EDF):** This is another scheduling algorithm used in real-time systems, where tasks are scheduled based on their deadlines. Tasks with earlier deadlines are executed before tasks with later deadlines.

These are some of the common scheduling algorithms used in embedded operating systems. The choice of scheduling algorithm depends on the specific requirements of the system, such as timing constraints, fairness, and resource utilization.