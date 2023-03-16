# Performance Metric for Distributed Mutual Exclusion Algorithms

Distributed mutual exclusion algorithms are algorithms that ensure that only one process at a time can access a shared resource in a distributed system. There are different types of distributed mutual exclusion algorithms, such as token-based, non-token-based, and quorum-based algorithms .

The performance of distributed mutual exclusion algorithms can be evaluated by the following four metrics :

- **Message complexity**: It is the number of messages that are required per critical section (CS) execution by a process. It measures the communication overhead of the algorithm. The lower the message complexity, the better the performance.
- **Synchronization delay**: It is the time elapsed between the moment when a process leaves the CS and the moment when the next process enters the CS. It measures the degree of concurrency of the algorithm. The lower the synchronization delay, the better the performance.
- **Response time**: It is the time elapsed between the moment when a process requests to enter the CS and the moment when it actually enters the CS. It measures the waiting time of the process. The lower the response time, the better the performance.
- **Throughput**: It is the number of CS executions per unit time in the system. It measures the efficiency of the algorithm. The higher the throughput, the better the performance.

Different algorithms may have different trade-offs among these metrics. For example, a token-based algorithm may have low message complexity but high synchronization delay, while a non-token-based algorithm may have high message complexity but low synchronization delay . Therefore, the choice of the best algorithm depends on the application requirements and the system characteristics.