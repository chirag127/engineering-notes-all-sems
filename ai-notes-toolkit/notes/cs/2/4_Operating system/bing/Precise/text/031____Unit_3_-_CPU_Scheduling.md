## Unit 3 - CPU Scheduling

CPU scheduling is the process of determining which process in the ready queue is to be allocated the CPU. The objective of CPU scheduling is to maximize CPU utilization and throughput while minimizing turnaround time, waiting time, and response time.

There are several CPU scheduling algorithms, including:

1. **First-Come, First-Served (FCFS):** Processes are executed in the order they arrive in the ready queue.
2. **Shortest-Job-First (SJF):** The process with the shortest estimated CPU burst time is selected for execution next.
3. **Priority Scheduling:** Processes are assigned a priority and the process with the highest priority is selected for execution next.
4. **Round Robin (RR):** Each process is assigned a time quantum and the processes are executed in a circular order.
5. **Multilevel Queue Scheduling:** The ready queue is partitioned into several separate queues, each with its own scheduling algorithm.

Each scheduling algorithm has its own advantages and disadvantages, and the choice of algorithm depends on the specific requirements of the system.