# Performance Metric for Distributed Mutual Exclusion Algorithms

Distributed mutual exclusion algorithms are algorithms that ensure that only one process at a time can access a shared resource in a distributed system. There are different types of distributed mutual exclusion algorithms, such as token-based, non-token-based, and quorum-based algorithms .

The performance of distributed mutual exclusion algorithms can be evaluated by the following four metrics :

- **Message complexity**: It is the number of messages that are required per critical section (CS) execution by a process. It measures the communication overhead of the algorithm. The lower the message complexity, the better the performance.
- **Synchronization delay**: It is the time elapsed between the moment when a process leaves the CS and the moment when the next process enters the CS. It measures the responsiveness of the algorithm. The lower the synchronization delay, the better the performance.
- **Response time**: It is the time elapsed between the moment when a process requests to enter the CS and the moment when it actually enters the CS. It measures the waiting time of the process. The lower the response time, the better the performance.
- **Throughput**: It is the number of CS executions per unit time in the system. It measures the efficiency of the algorithm. The higher the throughput, the better the performance.

The performance metrics of distributed mutual exclusion algorithms may vary depending on the best case and the worst case scenarios. For example, the best case scenario for message complexity is when the process that requests the CS already has the token or the permission, and the worst case scenario is when the process has to wait for the token or the permission from all other processes. The performance metrics may also depend on the system parameters, such as the number of processes, the network topology, the network delay, and the CS execution time. Therefore, it is important to compare the performance of different algorithms under the same system settings and assumptions.