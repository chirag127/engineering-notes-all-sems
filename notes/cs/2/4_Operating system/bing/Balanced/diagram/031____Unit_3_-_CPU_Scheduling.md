## Unit 3 - CPU Scheduling

CPU scheduling is the process of allocating the CPU to different processes in a multiprogramming system. The objective of CPU scheduling is to maximize the CPU utilization and throughput, and minimize the waiting time and response time of the processes.

Some of the topics covered in this unit are:

- **CPU Scheduling Criteria**: The criteria used to evaluate the performance of different CPU scheduling algorithms, such as average waiting time, average turnaround time, average response time, CPU utilization, and throughput.
- **CPU Scheduling Algorithms**: The algorithms used to select the next process to run on the CPU, such as first-come first-served (FCFS), shortest job first (SJF), shortest remaining time first (SRTF), priority scheduling, round robin (RR), and multilevel queue scheduling.
- **Preemptive and Non-preemptive Scheduling**: The difference between preemptive and non-preemptive scheduling is that in preemptive scheduling, the CPU can be taken away from a running process before it finishes its burst, while in non-preemptive scheduling, the CPU cannot be taken away from a running process until it finishes its burst or requests I/O.
- **Process Synchronization**: The concept of ensuring that multiple processes can access shared resources without causing inconsistency or deadlock. Some of the techniques used for process synchronization are mutual exclusion, semaphores, monitors, and message passing.
- **Deadlocks**: The situation where a set of processes are waiting for each other to release some resources, and none of them can proceed. Some of the methods to deal with deadlocks are deadlock prevention, deadlock avoidance, deadlock detection, and deadlock recovery.