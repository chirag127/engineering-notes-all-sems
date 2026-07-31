# Scheduling Algorithms for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

- A scheduling algorithm in OS is the algorithm that defines how much CPU time must be allotted to which process and when.
- CPU scheduling is the process which determines the process which will own the CPU for execution while other processes are in the queue.
- CPU scheduling algorithms are either preemptive or non-preemptive.
  - Preemptive scheduling algorithms allow the CPU to be taken away from a process if a higher priority process arrives in the queue.
  - Non-preemptive scheduling algorithms do not stop a process until it completes or voluntarily relinquishes the CPU.
- There are six popular process scheduling algorithms:
  - First-Come, First-Served (FCFS) Scheduling: The process that arrives first in the queue is executed first by the CPU.
  - Shortest-Job-Next (SJN) Scheduling: The process that has the shortest burst time (the time required to complete the execution) is executed first by the CPU.
  - Priority Scheduling: The process that has the highest priority (a predefined value assigned to each process) is executed first by the CPU.
  - Shortest Remaining Time (SRT) Scheduling: The process that has the shortest remaining burst time is executed first by the CPU. This is a preemptive version of SJN scheduling.
  - Round Robin (RR) Scheduling: The processes are executed in a circular order by the CPU, with each process getting a fixed time slice (quantum) of CPU time.
  - Multiple-Level Queues Scheduling: The processes are divided into different queues based on their characteristics, such as foreground or background, interactive or batch, etc. Each queue has its own scheduling algorithm and priority.
- There is no universal "best" scheduling algorithm, and many operating systems use extended or combinations of the scheduling algorithms above.
- The performance of a scheduling algorithm depends on various factors, such as CPU utilization, throughput, turnaround time, waiting time, response time, etc.