### Scheduling Algorithms

Scheduling algorithms are the algorithms that determine how the CPU allocates its time to the processes that are ready to execute. Scheduling algorithms can be classified into two categories: preemptive and non-preemptive.

- Preemptive scheduling algorithms allow the CPU to interrupt a running process and switch to another process, based on some criteria. This can improve the responsiveness and fairness of the system, but also introduce overhead and complexity.
- Non-preemptive scheduling algorithms do not interrupt a running process until it completes or requests an I/O operation. This can reduce the overhead and complexity of the system, but also cause starvation and poor utilization of the CPU.

Some of the common scheduling algorithms are:

- First-Come, First-Served (FCFS): This algorithm assigns the CPU to the process that arrives first in the ready queue. It is simple and easy to implement, but it can cause long waiting times and low CPU utilization.
- Shortest-Job-Next (SJN): This algorithm assigns the CPU to the process that has the shortest estimated burst time (the time required to complete the process). It can minimize the average waiting time and turnaround time, but it requires prior knowledge of the burst times and can cause starvation for long processes.
- Priority Scheduling: This algorithm assigns the CPU to the process that has the highest priority. The priority can be static (assigned by the system or the user) or dynamic (based on some factors such as age or I/O frequency). It can improve the importance and urgency of the processes, but it can also cause starvation for low-priority processes.
- Shortest Remaining Time (SRT): This algorithm is a preemptive version of SJN. It assigns the CPU to the process that has the shortest remaining burst time (the time required to complete the remaining portion of the process). It can also minimize the average waiting time and turnaround time, but it requires frequent preemption and prior knowledge of the burst times.
- Round Robin (RR): This algorithm assigns the CPU to the processes in the ready queue in a circular order, with a fixed time quantum (the maximum time a process can use the CPU in one cycle). It is simple and fair, but it can cause high context switching overhead and poor performance for processes with varying burst times.
- Multiple-Level Queues Scheduling: This algorithm divides the processes into different queues based on some criteria, such as priority, memory size, or CPU-boundness. Each queue has its own scheduling algorithm, and the CPU is assigned to the processes from the highest-level queue to the lowest-level queue. It can accommodate different types of processes, but it can also cause starvation and complexity.