### Performance metric for distributed mutual exclusion algorithms

Distributed mutual exclusion algorithms are algorithms that ensure that only one process at a time can access a shared resource in a distributed system. The performance of these algorithms can be evaluated by the following metrics :

- **Message complexity**: It is the number of messages that are required per critical section (CS) execution by a process. It measures the communication overhead of the algorithm. A lower message complexity is desirable.
- **Synchronization delay**: It is the time elapsed between the departure of a process from the CS and the entry of the next process into the CS. It measures the degree of concurrency achieved by the algorithm. A lower synchronization delay is desirable.
- **Response time**: It is the time interval between the request of a process to enter the CS and the end of its CS execution. It measures the waiting time of the process. A lower response time is desirable.
- **Throughput**: It is the number of CS executions per unit time in the system. It measures the efficiency of the algorithm. A higher throughput is desirable.

Different algorithms may have different trade-offs among these metrics. For example, a token-based algorithm may have low message complexity but high synchronization delay, while a non-token-based algorithm may have high message complexity but low synchronization delay. A quorum-based algorithm may have lower message complexity and synchronization delay than both token-based and non-token-based algorithms, but it may require more knowledge of the system state. Therefore, the choice of the algorithm depends on the application requirements and the system characteristics.