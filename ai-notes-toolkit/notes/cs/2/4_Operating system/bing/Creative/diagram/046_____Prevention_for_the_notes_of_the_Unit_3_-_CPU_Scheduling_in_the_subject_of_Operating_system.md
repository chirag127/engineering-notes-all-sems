### Prevention for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

- CPU scheduling is the process of deciding which process will own the CPU for execution while another process is on hold .
- CPU scheduling aims to maximize CPU utilization, throughput, and turnaround time, and minimize waiting time and response time .
- CPU scheduling can be classified into two types: preemptive and non-preemptive  .
  - Preemptive scheduling allows the CPU to be taken away from a process if a higher priority process arrives in the ready queue .
  - Non-preemptive scheduling does not allow the CPU to be taken away from a process until it finishes its execution or voluntarily releases the CPU .
- CPU scheduling algorithms are the methods to decide which process should be allocated the CPU based on some criteria .
  - Some of the common CPU scheduling algorithms are: first come first serve (FCFS), shortest job first (SJF), priority scheduling, round robin (RR), and multilevel queue scheduling .
- CPU scheduling can face some challenges such as starvation, aging, and deadlock  .
  - Starvation is the situation where a process waits indefinitely for the CPU because of the interference of other processes with higher priority .
  - Aging is the technique to prevent starvation by gradually increasing the priority of a process that waits for a long time in the ready queue .
  - Deadlock is the situation where a set of processes are blocked because each process is holding a resource and waiting for another resource held by another process .
- CPU scheduling can prevent some of these challenges by applying some strategies such as  :
  - Eliminating mutual exclusion, which means allowing multiple processes to share the same resource simultaneously.
  - Eliminating hold and wait, which means requiring a process to request and be allocated all its resources before execution or release all its resources before requesting a new one.
  - Eliminating no preemption, which means allowing the system to forcibly take a resource from a process and give it to another process.
  - Eliminating circular wait, which means imposing a total ordering on all resource types and requiring each process to request resources in an increasing order of enumeration.
  - Implementing a priority aging scheme, which means increasing the priority of a process as it waits longer in the ready queue .
  - Implementing a feedback mechanism, which means adjusting the priority of a process based on its behavior and resource requirements.