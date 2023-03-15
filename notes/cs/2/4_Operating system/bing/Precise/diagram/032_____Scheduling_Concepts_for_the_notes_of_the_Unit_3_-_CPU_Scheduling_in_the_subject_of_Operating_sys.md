### Scheduling Concepts

CPU scheduling is a process that allows the operating system to allocate CPU time to various processes in a fair and efficient manner. Here are some key concepts related to CPU scheduling:

1. **CPU Burst**: The time period for which a process executes on the CPU before it is interrupted by the operating system.
2. **I/O Burst**: The time period for which a process performs I/O operations before it is ready to execute on the CPU again.
3. **Preemptive Scheduling**: A scheduling algorithm that allows the operating system to interrupt a process that is currently executing on the CPU and allocate the CPU to another process.
4. **Non-Preemptive Scheduling**: A scheduling algorithm that does not allow the operating system to interrupt a process that is currently executing on the CPU. The process must voluntarily release the CPU before another process can be scheduled.
5. **Context Switch**: The process of saving the state of the currently executing process and restoring the state of the next process to be executed on the CPU.
6. **Scheduling Criteria**: The criteria used by the operating system to determine which process should be allocated the CPU next. Common scheduling criteria include CPU utilization, throughput, turnaround time, waiting time, and response time.
7. **Scheduling Algorithms**: The algorithms used by the operating system to determine which process should be allocated the CPU next. Common scheduling algorithms include First-Come, First-Served (FCFS), Shortest Job First (SJF), Priority Scheduling, and Round Robin (RR).

These are some of the key concepts related to CPU scheduling in operating systems. Understanding these concepts is essential for understanding how the operating system manages the allocation of CPU time to various processes.