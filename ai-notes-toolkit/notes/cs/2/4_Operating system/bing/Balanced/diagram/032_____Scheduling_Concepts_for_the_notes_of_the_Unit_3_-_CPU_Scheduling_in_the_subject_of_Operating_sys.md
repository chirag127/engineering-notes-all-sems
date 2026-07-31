### Scheduling Concepts

- Scheduling is the process of selecting a process from a ready queue and allotting CPU to this process for execution.
- Scheduling aims to maximize CPU utilization and minimize waiting time, response time, and turnaround time of the processes.
- Scheduling is performed by a part of the operating system called the scheduler.
- There are three types of schedulers in the operating system :
  - Long-term scheduler: It decides which jobs to admit into the system and which to reject. It controls the degree of multiprogramming, i.e., the number of processes in memory.
  - Short-term scheduler: It decides which process to run next from the ready queue. It is invoked frequently and must be fast. It implements the CPU scheduling algorithm, such as FCFS, SJF, RR, etc.
  - Medium-term scheduler: It decides which processes to swap out from memory and which to swap in. It controls the degree of swapping, i.e., the number of processes in the swap space.
- Scheduling criteria are the measures used to evaluate the performance of a scheduling algorithm. Some common criteria are:
  - CPU utilization: The percentage of time the CPU is busy executing processes.
  - Throughput: The number of processes completed per unit time.
  - Waiting time: The amount of time a process spends in the ready queue before getting the CPU.
  - Response time: The amount of time from the submission of a request until the first response is produced.
  - Turnaround time: The amount of time from the submission of a process until its completion.