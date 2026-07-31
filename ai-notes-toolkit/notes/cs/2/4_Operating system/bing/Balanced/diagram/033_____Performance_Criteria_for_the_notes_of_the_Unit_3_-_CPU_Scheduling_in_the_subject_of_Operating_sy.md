### Performance Criteria for CPU Scheduling

- CPU scheduling is the process of selecting a process from the ready queue and allocating the CPU to it.
- CPU scheduling aims to optimize the performance of the system by maximizing CPU utilization, throughput, and responsiveness, and minimizing turnaround time, waiting time, and context switching overhead.
- Some of the performance criteria for CPU scheduling are:

  - **CPU utilization**: The percentage of time the CPU is busy executing processes. Higher CPU utilization means better use of the system resources and lower idle time.
  - **Throughput**: The number of processes that are completed per unit time. Higher throughput means higher productivity and efficiency of the system.
  - **Turnaround time**: The total time a process spends in the system, from its arrival to its completion. It includes the waiting time, the CPU time, and the I/O time. Lower turnaround time means faster service and better user satisfaction.
  - **Waiting time**: The total time a process spends in the ready queue, waiting for its turn to execute on the CPU. Lower waiting time means less wasted time and better user satisfaction.
  - **Response time**: The time from the submission of a request until the first response is produced. It is applicable for interactive processes that require frequent user interaction. Lower response time means better interactivity and user satisfaction.
  - **Context switch time**: The time required to save the state of the current process and load the state of the next process on the CPU. It is an overhead that reduces the effective CPU time available for the processes. Lower context switch time means less overhead and better performance.