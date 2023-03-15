# Scheduling Concepts for the notes of the Unit 3 - CPU Scheduling in the subject of Operating System

- Scheduling in operating system is the process of selecting a process from a ready queue and allotting CPU to this process for execution.
- The operating system schedules the processes in such a way that the CPU doesn’t sit idle and always has one process to execute. This reduces the CPU’s idle time and increases its utilization.
- The part of OS that allots the computer resources to the processes is termed as a scheduler.
- Schedulers are of three types: long-term scheduler, short-term scheduler and medium-term scheduler.
- Long-term scheduler (or job scheduler) selects the jobs to be submitted into the system from a pool of jobs. It controls the degree of multiprogramming, i.e., the number of processes in memory.
- Short-term scheduler (or CPU scheduler) selects the process to run from the ready queue and allocates the CPU to it. It is invoked frequently and makes fast decisions.
- Medium-term scheduler (or swap scheduler) swaps out some processes from the memory to the disk and swaps in some processes from the disk to the memory. It controls the degree of swapping, i.e., the number of processes in the swap space.
- CPU scheduling is the foundation or starting concept of multi-programmed operating systems. By switching the CPU among different processes, the operating system can make the computer and its processing power more productive.
- CPU scheduling is the action of assigning processors to perform tasks. The tasks may be threads, processes or data flows.
- CPU scheduling algorithms are the methods to decide which process should be allocated the CPU next. They are based on different criteria, such as arrival time, burst time, priority, etc.
- Some of the common CPU scheduling algorithms are: first come first serve (FCFS), shortest job first (SJF), priority scheduling, round robin (RR), multilevel queue scheduling, multilevel feedback queue scheduling, etc.
- CPU scheduling algorithms are evaluated based on different performance metrics, such as waiting time, turnaround time, response time, throughput, CPU utilization, etc.
- CPU scheduling algorithms can be classified into two categories: preemptive and non-preemptive. Preemptive algorithms can interrupt the execution of a process and switch to another process, while non-preemptive algorithms can only switch to another process when the current process finishes or requests for I/O.
- CPU scheduling algorithms can also be classified into two categories: static and dynamic. Static algorithms assign a fixed priority to each process, while dynamic algorithms can change the priority of a process based on its behavior or resource requirements.