# Scheduling Concepts for the notes of the Unit 3 - CPU Scheduling in the subject of Operating System

- Scheduling in operating system is the process of selecting a process from a ready queue and allotting CPU to this process for execution.
- The operating system schedules the processes in such a way that the CPU doesn’t sit idle and always has one process to execute. This reduces the CPU’s idle time and increases its utilization.
- The part of OS that allots the computer resources to the processes is termed as a scheduler.
- Schedulers are of three types: long-term scheduler, short-term scheduler and medium-term scheduler.
- Long-term scheduler (or job scheduler) selects the jobs to be submitted into the system from a pool of jobs. It controls the degree of multiprogramming, i.e., the number of processes in memory.
- Short-term scheduler (or CPU scheduler) selects the process to run from the ready queue and allocates the CPU to it. It is invoked frequently and makes fast decisions.
- Medium-term scheduler (or swap scheduler) removes the processes from memory (swapping or suspension) and later restores them for execution. It controls the degree of swapping, i.e., the number of processes swapped in or out of memory.
- CPU scheduling is the foundation or starting concept of multi-programmed operating systems. By switching the CPU among different processes, the operating system can make the computer and its processing power more productive.
- CPU scheduling is the action of assigning processors to perform tasks. The tasks may be threads, processes or data flows.
- CPU scheduling algorithms are the methods to decide which process should be allocated the CPU next. They are based on different criteria, such as arrival time, burst time, priority, etc.
- Some of the common CPU scheduling algorithms are: first come first serve (FCFS), shortest job first (SJF), priority scheduling, round robin (RR), multilevel queue scheduling, multilevel feedback queue scheduling, etc.
- CPU scheduling algorithms are evaluated based on different performance metrics, such as CPU utilization, throughput, turnaround time, waiting time, response time, etc.