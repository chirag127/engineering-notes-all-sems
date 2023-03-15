```
### Scheduling Algorithms

A scheduling algorithm is the algorithm that defines how much CPU time must be allotted to which process and when. Scheduling algorithms are important for the efficient utilization of the CPU and the satisfaction of the users. There are two types of scheduling algorithms:

- Non-preemptive scheduling algorithms: For these algorithms, once a process starts running, they are not stopped until completion. The processes are executed in the order of their arrival or priority. Examples of non-preemptive scheduling algorithms are First-Come, First-Served (FCFS), Shortest-Job-Next (SJN), and Priority Scheduling.

- Preemptive scheduling algorithms: For these algorithms, a running process can be interrupted by the arrival of a higher priority process or by the expiration of a time quantum. The interrupted process is moved to the ready queue and resumes execution when it gets the CPU again. Examples of preemptive scheduling algorithms are Shortest Remaining Time (SRT), Round Robin (RR), and Multiple-Level Queues Scheduling.

Some of the criteria for evaluating the performance of scheduling algorithms are:

- CPU utilization: The percentage of time the CPU is busy executing processes.
- Throughput: The number of processes completed per unit time.
- Turnaround time: The time interval from the submission of a process to its completion.
- Waiting time: The time interval a process spends in the ready queue waiting for the CPU.
- Response time: The time interval from the submission of a request to the first response by a process.

Different scheduling algorithms may have different advantages and disadvantages depending on the characteristics of the processes and the system requirements. There is no universal "best" scheduling algorithm, and many operating systems use extended or combinations of the scheduling algorithms above.
```