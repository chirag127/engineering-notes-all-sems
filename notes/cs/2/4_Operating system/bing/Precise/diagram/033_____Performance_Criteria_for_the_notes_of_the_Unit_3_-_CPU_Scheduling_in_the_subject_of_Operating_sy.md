### Performance Criteria for CPU Scheduling

CPU scheduling is the process of determining which process in the ready queue is to be allocated the CPU. There are several criteria to consider when evaluating the performance of a CPU scheduling algorithm:

1. **CPU utilization**: The percentage of time the CPU is busy executing processes. A high CPU utilization is desirable as it indicates that the CPU is being used efficiently.

2. **Throughput**: The number of processes completed per unit time. A high throughput is desirable as it indicates that the system is processing a large number of processes in a given time period.

3. **Turnaround time**: The time it takes for a process to complete, from the time it is submitted to the time it is completed. A low turnaround time is desirable as it indicates that processes are being completed quickly.

4. **Waiting time**: The time a process spends waiting in the ready queue. A low waiting time is desirable as it indicates that processes are not spending a long time waiting to be executed.

5. **Response time**: The time it takes for a process to start executing after it has been submitted. A low response time is desirable as it indicates that the system is responding quickly to user requests.

These performance criteria are often used to evaluate and compare different CPU scheduling algorithms. An effective CPU scheduling algorithm should aim to maximize CPU utilization and throughput while minimizing turnaround time, waiting time, and response time.