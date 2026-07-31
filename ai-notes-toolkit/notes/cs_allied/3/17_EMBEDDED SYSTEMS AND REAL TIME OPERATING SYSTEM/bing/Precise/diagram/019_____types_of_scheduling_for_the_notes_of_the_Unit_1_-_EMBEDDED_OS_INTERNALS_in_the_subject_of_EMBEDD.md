### Types of Scheduling for the Notes of the Unit 1 - Embedded OS Internals in the Subject of Embedded Systems and Real Time Operating System

Scheduling is the process of allocating system resources to different tasks or processes. In the context of an embedded operating system, scheduling is used to determine which task should be executed next. There are several types of scheduling algorithms that can be used in an embedded operating system, including:

1. **First-Come, First-Served (FCFS):** This is the simplest scheduling algorithm. Tasks are executed in the order in which they arrive in the ready queue. This algorithm is easy to implement but can result in long waiting times for tasks that arrive later in the queue.

2. **Shortest Job First (SJF):** This algorithm selects the task with the shortest estimated execution time to be executed next. This can result in shorter average waiting times, but it requires accurate estimates of execution times and can result in starvation for longer tasks.

3. **Priority Scheduling:** This algorithm assigns a priority to each task and selects the task with the highest priority to be executed next. Priorities can be assigned statically or dynamically, and can be based on various factors such as the importance of the task or its deadline.

4. **Round Robin:** This algorithm allocates a fixed time slice to each task in the ready queue and executes them in a cyclic order. This can result in fairer allocation of CPU time, but can also result in longer average waiting times if the time slice is not chosen appropriately.

5. **Rate Monotonic Scheduling (RMS):** This is a priority-based scheduling algorithm used in real-time systems. Tasks are assigned priorities based on their periods, with shorter periods being assigned higher priorities. This algorithm can provide guarantees on the schedulability of periodic tasks, but requires that all tasks have fixed periods and execution times.

6. **Earliest Deadline First (EDF):** This is another priority-based scheduling algorithm used in real-time systems. Tasks are assigned priorities based on their deadlines, with earlier deadlines being assigned higher priorities. This algorithm can provide guarantees on the schedulability of tasks with deadlines, but requires that all tasks have fixed deadlines and execution times.

These are some of the common scheduling algorithms used in embedded operating systems. The choice of scheduling algorithm depends on the specific requirements of the system, such as the need for real-time guarantees or fairness in resource allocation.