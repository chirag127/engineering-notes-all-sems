## Unit 3 - CPU Scheduling

CPU scheduling is a crucial part of the operating system that helps in deciding which process should be executed first. Here are some key points that you need to know about CPU scheduling:

- CPU scheduling is the process of allocating CPU time to different processes that are ready to execute in the system.
- The main objective of CPU scheduling is to increase the efficiency of the system by minimizing the waiting time of the processes and maximizing CPU utilization.
- There are different scheduling algorithms that are used in the operating system, such as First Come First Serve (FCFS), Shortest Job First (SJF), Round Robin (RR), Priority Scheduling, and Multilevel Queue Scheduling.
- FCFS is the simplest scheduling algorithm that allocates CPU time to the processes in the order they arrive in the ready queue.
- SJF is a preemptive or non-preemptive scheduling algorithm that allocates CPU time to the process with the shortest burst time.
- RR is a time-sharing algorithm that allocates CPU time to the processes in a round-robin fashion, where each process is given a fixed quantum of time to execute.
- Priority Scheduling is a scheduling algorithm that allocates CPU time to the processes based on their priority level.
- Multilevel Queue Scheduling is a scheduling algorithm that divides the ready queue into multiple queues based on the process characteristics, such as priority, CPU burst time, and I/O burst time.
- There are different metrics that are used to evaluate the performance of the scheduling algorithms, such as average waiting time, average turnaround time, and CPU utilization.
- The choice of scheduling algorithm depends on the system requirements, such as response time, throughput, and fairness.

In summary, CPU scheduling is an important aspect of the operating system that helps in managing the CPU time of the processes efficiently. Understanding the different scheduling algorithms and their performance metrics is crucial for designing and implementing an efficient scheduling policy in the system.