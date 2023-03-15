### Performance Criteria for CPU Scheduling

- CPU scheduling is the process of selecting a process from the ready queue and allocating the CPU to it for execution.
- CPU scheduling aims to maximize the utilization of the CPU and the throughput of the system, while minimizing the turnaround time, waiting time, and response time of the processes.
- The performance criteria for CPU scheduling are as follows  :

  - **CPU utilization**: The percentage of time the CPU is busy executing processes. The higher the CPU utilization, the better the performance of the system. CPU utilization can range from 0% to 100%, but in a real system, it varies from 40% to 90% depending on the load on the system.
  - **Throughput**: The number of processes that complete their execution per unit of time. The higher the throughput, the more work is done by the system. Throughput can vary depending on the length and type of the processes.
  - **Turnaround time**: The amount of time it takes for a process to finish its execution, from the time it is submitted to the system until the time it is terminated. The turnaround time includes the waiting time, the CPU time, and the I/O time of the process. The lower the turnaround time, the faster the process is completed.
  - **Waiting time**: The amount of time a process spends in the ready queue, waiting for its turn to use the CPU. The waiting time does not include the I/O time or the CPU time of the process. The lower the waiting time, the less the process is delayed.
  - **Response time**: The amount of time it takes for a process to start its execution, from the time it is submitted to the system until the time it gets the first response from the CPU. The response time is important for interactive processes that require immediate feedback from the system. The lower the response time, the more responsive the system is.

- Different CPU scheduling algorithms may have different performance criteria, depending on the objectives and requirements of the system. For example, a real-time system may prioritize the response time and the deadline of the processes, while a batch system may prioritize the throughput and the CPU utilization of the system.