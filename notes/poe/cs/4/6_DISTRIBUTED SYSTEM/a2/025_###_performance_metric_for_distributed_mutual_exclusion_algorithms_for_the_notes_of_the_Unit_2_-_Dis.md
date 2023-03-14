 Here is the content in markdown format:

### Performance Metric for Distributed Mutual Exclusion Algorithms

For distributed mutual exclusion algorithms, the following performance metrics are used to evaluate and compare different algorithms:

1. **Message Complexity**: The number of messages exchanged between processes to achieve mutual exclusion. Less message passing leads to better performance.
2. **Time Complexity**: The number of rounds or units of time required to achieve mutual exclusion. Less time leads to better performance.
3. **Processor Utilization**: The percentage of time processors are engaged in useful computation rather than coordination activities. Higher utilization leads to better performance.
4. **Scalability**: The ability of an algorithm to efficiently handle increase in the number of processes. Algorithms that can handle large number of processes with little degradation in performance are considered scalable.

Some mnemonics to remember the performance metrics:

* Messages pass, time laps, util ups, scale adapt
* Less message, less time, more use, more scale

Detailed diagrams and examples can be included if required. The advantages and disadvantages of different algorithms can also be discussed with respect to these performance metrics. For example, token-based algorithms generally have low message complexity but suffer from poor scalability. Distributed queue-based algorithms have good scalability but higher message complexity. There is always a trade-off between these metrics for different algorithms.