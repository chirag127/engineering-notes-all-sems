### Scheduling Concepts

Scheduling is the process of selecting a process from a ready queue and allotting CPU to this process for execution. The operating system schedules the processes in such a way that the CPU doesn’t sit idle and always has one process to execute . This reduces the CPU’s idle time and increases its utilization. The part of OS that allots the computer resources to the processes is termed as a scheduler.

There are different types of schedulers in operating systems, such as:

- **Long-term scheduler**: It is also called a job scheduler. It selects the jobs to be submitted into the system from a pool of jobs. It controls the degree of multiprogramming, i.e., the number of processes in memory. It runs less frequently and may use complex algorithms.
- **Short-term scheduler**: It is also called a CPU scheduler. It selects the process to run from the ready queue and allocates the CPU to it. It runs more frequently and may use simple algorithms. It affects the response time and throughput of the system.
- **Medium-term scheduler**: It is also called a swap scheduler. It swaps out some processes from the memory to the disk and swaps in some processes from the disk to the memory. It controls the degree of multiprogramming and the memory utilization. It runs occasionally and may use moderate algorithms.

There are different types of CPU scheduling algorithms, such as:

- **First Come First Serve (FCFS)**: It is the simplest of all operating system scheduling algorithms. It selects the process that arrives first in the ready queue and executes it until completion. It is non-preemptive, i.e., it cannot be interrupted by another process. It is easy to implement but may cause long waiting time and low CPU utilization.
- **Shortest Job First (SJF)**: It is a scheduling algorithm that selects the process that has the shortest burst time (the time required by the process to execute) in the ready queue and executes it until completion. It is optimal, i.e., it minimizes the average waiting time. It can be preemptive or non-preemptive. It is difficult to implement as the burst time of a process is not known in advance.
- **Round Robin (RR)**: It is a scheduling algorithm that selects the process from the ready queue in a circular order and executes it for a fixed time slice (also called quantum). It is preemptive, i.e., it can be interrupted by another process after the time slice expires. It is fair and easy to implement but may cause high context switching overhead and variable response time.
- **Priority Scheduling**: It is a scheduling algorithm that selects the process that has the highest priority in the ready queue and executes it until completion or preemption. The priority of a process can be static (assigned at the time of creation) or dynamic (changed during execution). It can be preemptive or non-preemptive. It may cause starvation, i.e., the low priority processes may never get the CPU.
- **Multilevel Queue Scheduling**: It is a scheduling algorithm that partitions the ready queue into several separate queues, each with its own scheduling algorithm. The processes are permanently assigned to one of the queues based on some criteria, such as memory size, process type, etc. The CPU is allocated to the processes from the queues according to some priority rules.
- **Multilevel Feedback Queue Scheduling**: It is a scheduling algorithm that allows the processes to move between different queues based on their behavior and characteristics. The queues have different priorities and different time slices. The processes that use more CPU time are moved to lower priority queues, while the processes that use less CPU time are moved to higher priority queues. It is flexible and adaptable but complex to implement.

: [Scheduling in Operating System - Binary Terms](https://binaryterms.com/scheduling-in-operating-system.html)
: [Operating System Scheduling Techniques - W3schools](https://www.w3schools.in/operating-system/scheduling-techniques)
: [Scheduling (computing) - Wikipedia](https://en.wikipedia.org/wiki/Scheduling_(computing))
: [CPU Scheduling in Operating Systems - GeeksforGeeks](https://www.geeksforgeeks.org/cpu-scheduling-in-operating-systems/)
: [Operating System - Process Scheduling - tutorialspoint.com](https://www.tutorialspoint.com/oper