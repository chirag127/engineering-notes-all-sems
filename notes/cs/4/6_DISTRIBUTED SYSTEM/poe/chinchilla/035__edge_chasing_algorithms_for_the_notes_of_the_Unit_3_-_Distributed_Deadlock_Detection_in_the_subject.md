### Edge Chasing Algorithms for the Notes of Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

In the distributed system, deadlock can occur when multiple processes are waiting for each other to release resources. To detect deadlock in a distributed system, we use distributed deadlock detection algorithms. One of the types of distributed deadlock detection algorithms is the edge chasing algorithm. In this note, we will discuss the edge chasing algorithms for distributed deadlock detection.

#### Definition

Edge chasing algorithms are distributed deadlock detection algorithms that use a message-based approach to detect deadlock. In these algorithms, each process periodically sends probe messages to its neighbors to check for cycles in the resource allocation graph. When a process receives a probe message, it adds its own resource allocation information to the message and forwards it to its neighbors. If a cycle is detected in the resource allocation graph, it means that a deadlock has occurred.

#### Basic Edge Chasing Algorithm

The basic edge chasing algorithm consists of the following steps:

1. Each process sends a probe message to its neighbors.
2. When a process receives a probe message, it checks if the message contains its own resource allocation information. If it does, it means that a cycle has been detected and the process can initiate a deadlock resolution algorithm.
3. If the message does not contain the process's own resource allocation information, the process adds its own information to the message and forwards it to its neighbors.

#### Optimized Edge Chasing Algorithm

The optimized edge chasing algorithm improves the performance of the basic edge chasing algorithm by reducing the number of messages sent between processes. The algorithm consists of the following steps:

1. Each process sends a probe message to its neighbors.
2. When a process receives a probe message, it checks if the message contains its own resource allocation information. If it does, it means that a cycle has been detected and the process can initiate a deadlock resolution algorithm.
3. If the message does not contain the process's own resource allocation information, the process adds its own information to the message and forwards it to its neighbors, but only if the message has not already been forwarded by the process.
4. Each process maintains a table of all the messages it has forwarded to its neighbors. This table is used to avoid forwarding duplicate messages.

#### Advantages and Disadvantages

Edge chasing algorithms have the following advantages and disadvantages:

##### Advantages

- Edge chasing algorithms can detect deadlocks in a distributed system.
- Edge chasing algorithms are message-based and do not require a centralized component.
- Edge chasing algorithms are scalable and can handle a large number of processes and resources.

##### Disadvantages

- Edge chasing algorithms can generate a large number of messages, which can impact network performance.
- Edge chasing algorithms may not be suitable for systems with a high degree of resource sharing.

#### Conclusion

Edge chasing algorithms are distributed deadlock detection algorithms that use a message-based approach to detect deadlock in a distributed system. The basic edge chasing algorithm and the optimized edge chasing algorithm are two types of edge chasing algorithms. These algorithms have advantages and disadvantages and can be used in different types of distributed systems depending on their characteristics.