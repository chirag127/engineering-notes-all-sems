### Prevention for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

- CPU scheduling is the process of deciding which process will own the CPU to use while another process is suspended.
- CPU scheduling algorithms can be classified into two modes: pre-emptive and non pre-emptive.
- Pre-emptive scheduling allows the CPU to switch from one process to another before the current process finishes its execution.
- Non pre-emptive scheduling does not allow the CPU to switch from one process to another until the current process finishes its execution.
- CPU scheduling algorithms aim to optimize various criteria, such as CPU utilization, throughput, turnaround time, waiting time, and response time.
- CPU scheduling algorithms may face some challenges, such as starvation, aging, and deadlock.
- Starvation is a phenomenon associated with the priority scheduling algorithms, in which a low-priority process can wait indefinitely for the CPU because of a steady stream of higher-priority processes .
- Aging is a technique to prevent starvation by gradually increasing the priority of a waiting process over time .
- Deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
- Deadlock prevention is a method to avoid deadlock by ensuring that at least one of the four necessary conditions for deadlock does not hold.
- The four necessary conditions for deadlock are: mutual exclusion, hold and wait, no preemption, and circular wait.
- Deadlock prevention can be achieved by using one of the following strategies:
  - Eliminate mutual exclusion: This is not possible for some resources, such as printers and tape drives, that are inherently non-shareable.
  - Eliminate hold and wait: This can be done by requiring a process to request all the resources it needs before starting execution, or by releasing all the resources it holds before requesting a new one.
  - Eliminate no preemption: This can be done by allowing the system to preempt a resource from a process if another process with higher priority needs it.
  - Eliminate circular wait: This can be done by imposing a total ordering on the resources and requiring a process to request resources in increasing order of the ordering.