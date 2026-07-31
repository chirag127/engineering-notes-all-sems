### Performance Metrics for Distributed Mutual Exclusion Algorithms

Distributed mutual exclusion algorithms are algorithms that ensure that only one process at a time can access a shared resource in a distributed system. The performance of these algorithms can be evaluated by using the following metrics :

- **Message complexity**: It is the number of messages that are required per critical section (CS) execution by a process. It indicates the communication overhead of the algorithm. A lower message complexity is desirable.
- **Synchronization delay**: It is the time elapsed between the moment when a process leaves the CS and the moment when the next process enters the CS. It indicates the degree of concurrency of the algorithm. A lower synchronization delay is desirable.
- **Response time**: It is the time elapsed between the moment when a process requests to enter the CS and the moment when it actually enters the CS. It indicates the waiting time of the process. A lower response time is desirable.
- **Throughput**: It is the number of CS executions per unit time in the system. It indicates the efficiency of the algorithm. A higher throughput is desirable.

The performance of different distributed mutual exclusion algorithms may vary depending on the system parameters, such as the number of processes, the network topology, the network delay, the CS execution time, and the inter-request time. Therefore, it is important to compare the algorithms under different scenarios and use appropriate statistical methods to analyze the results .

Some examples of distributed mutual exclusion algorithms are:

- **Central server algorithm**: In this algorithm, one process acts as the coordinator and grants access to the CS to other processes based on a FIFO queue. The message complexity is 3 messages per CS execution, the synchronization delay is one message transmission time, and the response time depends on the position of the requesting process in the queue.
- **Ricart-Agrawala algorithm**: In this algorithm, each process broadcasts its request to enter the CS to all other processes and waits for their replies. The process with the lowest timestamp has the highest priority to enter the CS. The message complexity is 2N messages per CS execution, where N is the number of processes, the synchronization delay is zero, and the response time depends on the network delay and the number of competing processes.
- **Lamport's algorithm**: In this algorithm, each process maintains a logical clock and a request queue. When a process wants to enter the CS, it sends its request with its clock value to all other processes and puts it in its own queue. The process with the lowest clock value has the highest priority to enter the CS. The message complexity is 3N-1 messages per CS execution, the synchronization delay is one message transmission time, and the response time depends on the network delay and the number of competing processes.