## Unit 3 - Distributed Deadlock Detection

In this unit, we will discuss the concept of distributed deadlock detection. Here are the key points to remember:

- **Deadlock**: A deadlock occurs in a distributed system when two or more processes are blocked, waiting for resources held by each other. This can cause the system to come to a standstill.

- **Distributed Deadlock**: A distributed deadlock occurs when a deadlock involves processes and resources that are distributed across different machines in a network.

- **Deadlock Detection**: Deadlock detection is the process of identifying whether a deadlock has occurred in a system. In a distributed system, deadlock detection becomes more complex because processes and resources are spread across different machines.

- **Centralized Deadlock Detection**: In centralized deadlock detection, a central monitor is responsible for detecting deadlocks in the system. However, this approach may not be suitable for large-scale distributed systems because it can become a bottleneck.

- **Distributed Deadlock Detection**: In distributed deadlock detection, each machine in the network monitors its own resources and communicates with other machines to detect deadlocks. This approach is more scalable than centralized deadlock detection, but it requires more communication overhead.

- **Chandy-Misra-Haas Algorithm**: The Chandy-Misra-Haas algorithm is a widely used algorithm for distributed deadlock detection. It works by constructing a wait-for graph that represents the dependencies between processes and resources in the system. The algorithm then checks for cycles in the graph, which indicate the presence of a deadlock.

- **Edge Chasing Algorithm**: The edge chasing algorithm is another approach to distributed deadlock detection. In this approach, each process periodically sends a probe message to its neighbors to check for deadlocks. If a process is detected as part of a deadlock, it will receive a request to release its resources.

- **Advantages of Distributed Deadlock Detection**: Distributed deadlock detection has several advantages. It is more scalable than centralized deadlock detection and can be used in large-scale distributed systems. It also allows for more efficient use of resources because processes can release resources as soon as they are no longer needed.

- **Disadvantages of Distributed Deadlock Detection**: Distributed deadlock detection also has some disadvantages. It requires more communication overhead than centralized deadlock detection, and it can be more complex to implement. It also requires each machine to have a complete view of the system, which may not always be possible in some distributed systems.