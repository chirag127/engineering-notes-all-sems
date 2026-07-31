## Unit 3 - Distributed Deadlock Detection

Distributed deadlock detection is the process of detecting deadlocks in a distributed system. A deadlock occurs when two or more processes are blocked and unable to proceed because they are waiting for resources held by other processes. In a distributed system, deadlocks can occur across multiple nodes, making them more difficult to detect and resolve.

There are several approaches to distributed deadlock detection, including:

1. **Centralized approach:** In this approach, a single node is designated as the deadlock detector and is responsible for detecting deadlocks in the entire system. This approach can be efficient, but it introduces a single point of failure and can become a bottleneck as the system grows.

2. **Hierarchical approach:** In this approach, the system is organized into a hierarchy of nodes, with each node responsible for detecting deadlocks within its subtree. This approach can reduce the load on individual nodes, but it can be more complex to implement.

3. **Distributed approach:** In this approach, each node is responsible for detecting deadlocks within its local environment and communicating with other nodes to detect global deadlocks. This approach can be more scalable, but it can also be more complex to implement and can require more communication overhead.

Distributed deadlock detection algorithms can be based on various techniques, including graph-based algorithms, probe-based algorithms, and timestamp-based algorithms. Each technique has its own advantages and disadvantages, and the choice of technique will depend on the specific requirements of the system.