### Scheduling Concepts

Scheduling is the process of selecting a process from a ready queue and allotting CPU to this process for execution. The operating system schedules the processes in such a way that the CPU doesn’t sit idle and always has one process to execute . This reduces the CPU’s idle time and increases its utilization. The part of OS that allots the computer resources to the processes is termed as a scheduler.

Scheduling can be done at different levels of the system, such as:

- **Long-term scheduling**: It is also called a job scheduler. It decides which processes are admitted to the system for execution. It controls the degree of multiprogramming, i.e., the number of processes in memory.
- **Medium-term scheduling**: It is also called a swapping scheduler. It decides which processes are to be swapped in or out of the memory. It is used for memory management and to balance the mix of CPU-bound and I/O-bound processes.
- **Short-term scheduling**: It is also called a CPU scheduler. It decides which process is to be executed next by the CPU. It is invoked frequently and must be fast. It aims to increase CPU performance and process response time.

Scheduling can also be classified based on the different criteria or objectives, such as:

- **Preemptive vs non-preemptive scheduling**: Preemptive scheduling allows the CPU to be taken away from a process if a higher priority process arrives or a certain time quantum expires. Non-preemptive scheduling does not allow the CPU to be taken away from a process until it completes or requests I/O.
- **Deterministic vs probabilistic scheduling**: Deterministic scheduling guarantees that a process will get the CPU at a fixed time interval. Probabilistic scheduling does not guarantee that a process will get the CPU at a fixed time interval, but rather assigns a probability of getting the CPU.
- **Static vs dynamic scheduling**: Static scheduling assigns a fixed priority to each process before execution. Dynamic scheduling changes the priority of each process during execution based on some factors, such as CPU burst time, waiting time, etc.

Some of the common CPU scheduling algorithms are:

- **First Come First Serve (FCFS)**: It is the simplest of all operating system scheduling algorithms. It selects the process that arrives first in the ready queue and executes it until completion or I/O request. It is non-preemptive, deterministic and static.
- **Shortest Job First (SJF)**: It is a scheduling algorithm that selects the process that has the shortest CPU burst time in the ready queue and executes it until completion or I/O request. It can be preemptive or non-preemptive, probabilistic and dynamic.
- **Priority Scheduling**: It is a scheduling algorithm that selects the process that has the highest priority in the ready queue and executes it until completion or I/O request. It can be preemptive or non-preemptive, deterministic or probabilistic, and static or dynamic.
- **Round Robin (RR)**: It is a scheduling algorithm that selects the process that arrives first in the ready queue and executes it for a fixed time quantum or slice. If the process does not finish within the time quantum, it is preempted and moved to the end of the ready queue. It is preemptive, deterministic and static.
- **Multilevel Queue (MLQ)**: It is a scheduling algorithm that divides the ready queue into several separate queues, each with its own scheduling algorithm. The processes are permanently assigned to one of the queues based on some criteria, such as memory size, process type, etc. A higher-level scheduler decides which queue to serve next.
- **Multilevel Feedback Queue (MLFQ)**: It is a scheduling algorithm that divides the ready queue into several separate queues, each with its own scheduling algorithm. The processes can move between the queues based on some criteria, such as CPU burst time, priority, etc. A higher-level scheduler decides which queue to serve next.