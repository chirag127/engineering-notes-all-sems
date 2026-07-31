### Prevention for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

- CPU scheduling is the process of deciding which process will own the CPU to use while another process is suspended.
- CPU scheduling aims to maximize CPU utilization, throughput, and responsiveness, and minimize turnaround time, waiting time, and response time.
- CPU scheduling can face some challenges, such as starvation, aging, and deadlock, which can affect the performance and fairness of the system.
- Starvation is a phenomenon associated with the priority scheduling algorithms, in which a process ready for the CPU can wait indefinitely because of low priority .
- Aging is a technique to prevent starvation by gradually increasing the priority of processes that wait in the system for a long time .
- Deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
- Deadlock prevention is a method to ensure that at least one of the necessary conditions for deadlock does not hold in the system.
- Some of the deadlock prevention strategies are:
  - Eliminate mutual exclusion by allowing multiple processes to access the same resource simultaneously.
  - Eliminate hold and wait by requiring processes to request all the resources they need before execution or to release the resources they hold before requesting new ones.
  - Eliminate no preemption by allowing the system to forcibly take a resource from a process and give it to another process that requests it.
  - Eliminate circular wait by imposing a total ordering on the resources and requiring processes to request them in increasing order.