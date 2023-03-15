### Prevention for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

- CPU scheduling is the process of deciding which process will own the CPU for execution while another process is on hold .
- CPU scheduling aims to maximize CPU utilization, throughput, and turnaround time, while minimizing waiting time and response time .
- CPU scheduling can be classified into two types: preemptive and non-preemptive .
- Preemptive scheduling allows the CPU to be taken away from a process if a higher priority process arrives in the ready queue .
- Non-preemptive scheduling does not allow the CPU to be taken away from a process until it finishes its execution or voluntarily releases the CPU.
- CPU scheduling algorithms can be evaluated based on different criteria, such as average waiting time, average turnaround time, average response time, number of context switches, and CPU utilization .
- Some of the common CPU scheduling algorithms are: first-come first-served (FCFS), shortest job first (SJF), shortest remaining time first (SRTF), priority scheduling, round robin (RR), and multilevel queue scheduling .
- CPU scheduling can face some challenges, such as starvation, deadlock, and convoy effect  .
- Starvation occurs when a low-priority process is indefinitely postponed by a stream of higher-priority processes.
- Deadlock occurs when a set of processes are waiting for each other to release some resources, and none of them can proceed.
- Convoy effect occurs when a long process holds the CPU and blocks the execution of other processes, resulting in low CPU and device utilization.
- CPU scheduling can prevent these challenges by using some techniques, such as aging, resource allocation, and time quantum  .
- Aging is a technique that gradually increases the priority of a process that waits in the system for a long time.
- Resource allocation is a technique that ensures that a process can get all the resources it needs before starting its execution, or that it can release all the resources it holds if it is blocked.
- Time quantum is a technique that limits the maximum amount of time a process can use the CPU in one burst, and forces the process to relinquish the CPU if it exceeds the quantum.