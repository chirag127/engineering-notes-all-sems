
### Schedulers for the Notes of Unit 3 - CPU Scheduling in Operating Systems

1. First-Come, First-Served (FCFS) Scheduling: This is the simplest scheduling algorithm, which assigns the CPU to the process that arrives first in the ready queue. It is an non-preemptive algorithm, meaning that once a process is allocated the CPU, it will run until completion.

2. Shortest-Job-First (SJF) Scheduling: This scheduling algorithm assigns the CPU to the process with the shortest burst time. It is a preemptive algorithm, meaning that once a process is allocated the CPU, it may be preempted if a process with a shorter burst time is waiting in the ready queue.

3. Priority Scheduling: This scheduling algorithm assigns the CPU to the process with the highest priority. It is a preemptive algorithm, meaning that once a process is allocated the CPU, it may be preempted if a process with a higher priority is waiting in the ready queue.

4. Round-Robin (RR) Scheduling: This scheduling algorithm assigns the CPU to each process in the ready queue in turn. It is a preemptive algorithm, meaning that once a process is allocated the CPU, it may be preempted if another process is waiting in the ready queue. The time quantum is the amount of time used for each process before the CPU is allocated to the next process in the ready queue.