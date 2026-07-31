# Prevention for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

- CPU scheduling is the process of deciding which process will own the CPU for execution while another process is on hold .
- The main goal of CPU scheduling is to maximize the CPU utilization and minimize the waiting time, response time, and turnaround time of the processes .
- CPU scheduling can be classified into two types: preemptive and non-preemptive .
- Preemptive scheduling allows the CPU to be taken away from a process if a higher priority process arrives in the ready queue .
- Non-preemptive scheduling does not allow the CPU to be taken away from a process until it finishes its execution or voluntarily releases the CPU.
- Some of the common CPU scheduling algorithms are: first come first serve (FCFS), shortest job first (SJF), priority scheduling, round robin (RR), and multilevel queue scheduling .
- CPU scheduling can face some challenges such as starvation, deadlock, and convoy effect  .
- Starvation occurs when a low priority process is indefinitely postponed by a stream of higher priority processes.
- Deadlock occurs when a set of processes are waiting for each other to release some resources, and none of them can proceed.
- Convoy effect occurs when a long process holds the CPU and blocks the execution of other shorter processes in the ready queue.
- To prevent these problems, some techniques can be applied, such as:
  - Aging: increasing the priority of a process as it waits longer in the ready queue.
  - Eliminating one of the four necessary conditions for deadlock: mutual exclusion, hold and wait, no preemption, and circular wait.
  - Using a short time quantum for round robin scheduling to reduce the waiting time of short processes.