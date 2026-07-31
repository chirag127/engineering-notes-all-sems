### Weighted Round Robin Approach

The Weighted Round Robin (WRR) approach is a scheduling algorithm used in Real Time Systems for scheduling processes. It is a modification of the Round Robin algorithm, where processes are executed in a cyclic manner.

The WRR algorithm assigns a weight to each process, which represents its priority. Processes with higher weights get executed more frequently than processes with lower weights.

The following are the key features of the WRR algorithm:

- The WRR algorithm is a preemptive scheduling algorithm, which means that a process can be interrupted and replaced by another process with a higher priority.
- The algorithm assigns a weight to each process, which determines its priority. Processes with higher weights get more CPU time than processes with lower weights.
- The WRR algorithm uses a cyclic approach to execute processes. Each process gets a fixed time slice, and the CPU moves to the next process in the queue after the time slice expires.
- The algorithm allows for dynamic adjustment of weights based on the system load. Processes with higher weights get more CPU time when the system is heavily loaded, and processes with lower weights get more CPU time when the system is lightly loaded.

The WRR algorithm is widely used in Real Time Systems because of its ability to handle dynamic loads and prioritize processes based on their importance. It is an efficient and fair scheduling algorithm that ensures that all processes get a fair share of the CPU time.