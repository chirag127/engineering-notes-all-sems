### Edge Chasing Algorithms for the Notes of Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

In distributed systems, deadlock detection is a critical issue, and edge chasing algorithms are one of the methods that can be used to detect deadlocks. An edge in a distributed system represents a message sent between two processes.

Edge chasing algorithms are based on the idea of tracing circular chains of edges to detect deadlocks. In this method, every process maintains a wait-for graph, which represents the processes that are waiting for resources to be released. Each node in the wait-for graph represents a process, and each edge represents a request for a resource.

There are two types of edge chasing algorithms: diffusing computation and centralized computation.

#### Diffusing Computation Algorithm
In this algorithm, the detection process is distributed among the processes in the system. The idea is to propagate the detection of deadlocks through the wait-for graph until all processes are reached. This algorithm consists of the following steps:

1. Each process initiates the detection process by sending a probe message to all its neighbors in the wait-for graph.
2. When a process receives a probe message, it checks its wait-for graph to see if it has any cycles. If it does, it sends a probe message to its neighbors, and the process repeats.
3. If a process does not have any cycles in its wait-for graph, it sends an OK message to the process that sent the probe message.
4. When a process receives an OK message from all its neighbors, it knows that deadlock has not been detected.

#### Centralized Computation Algorithm
In this algorithm, there is a central process responsible for detecting deadlocks. The idea is to collect information from all processes in the system and check for cycles in the wait-for graph. This algorithm consists of the following steps:

1. Each process sends its wait-for graph to the central process.
2. The central process constructs a global wait-for graph by merging the wait-for graphs of all processes.
3. The central process checks for cycles in the global wait-for graph. If it finds a cycle, it sends a message to all processes involved in the cycle to release their resources.
4. Each process releases its resources and sends a message back to the central process to indicate that it has released its resources.
5. The central process checks again for cycles in the global wait-for graph. If it finds no cycles, it sends a message to all processes to resume normal operation.

#### Advantages of Edge Chasing Algorithms
- Edge chasing algorithms are simple and easy to implement.
- These algorithms are distributed, meaning that they do not require a centralized process to detect deadlocks.
- Edge chasing algorithms can be used in a variety of distributed systems.

#### Disadvantages of Edge Chasing Algorithms
- Edge chasing algorithms may produce false positives, which means that they may detect deadlocks when there are none.
- These algorithms can be slow, especially in large systems.

In conclusion, edge chasing algorithms are an effective method of detecting deadlocks in distributed systems. Both diffusing computation and centralized computation algorithms have their advantages and disadvantages, and the choice of algorithm depends on the specific requirements of the system.