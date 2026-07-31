### Performance Criteria for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

CPU scheduling is the process of determining which process in the ready queue is to be allocated the CPU. There are several criteria to evaluate the performance of a CPU scheduling algorithm:

1. **CPU utilization**: The percentage of time the CPU is busy. The goal is to keep the CPU as busy as possible.
2. **Throughput**: The number of processes completed per unit time. The goal is to maximize the throughput.
3. **Turnaround time**: The time from the submission of a process to the completion of the process. The goal is to minimize the turnaround time.
4. **Waiting time**: The time a process spends waiting in the ready queue. The goal is to minimize the waiting time.
5. **Response time**: The time from the submission of a request until the first response is produced. The goal is to minimize the response time.

Different scheduling algorithms may prioritize different criteria, and the choice of algorithm depends on the specific needs of the system. For example, a real-time system may prioritize minimizing response time, while a batch processing system may prioritize maximizing throughput.