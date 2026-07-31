# Distributed Deadlocks

- A **distributed deadlock** is a situation where a set of processes in a distributed system are waiting for each other to release resources, and none of them can proceed .
- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems .
- Distributed deadlocks are harder to detect, avoid, and prevent than deadlocks in centralized systems, because there is no single authority that can oversee resource allocation and process states.
- There are three main approaches to handle distributed deadlocks :
  - **Prevention**: This approach tries to ensure that deadlocks never occur by imposing some constraints on resource allocation, such as ordering, preemption, or timeouts.
  - **Avoidance**: This approach tries to avoid deadlocks by making careful decisions on resource requests, based on the current and future resource availability and process requirements, such as using the Banker's algorithm.
  - **Detection and recovery**: This approach tries to detect deadlocks after they occur and then recover from them by aborting or restarting some processes, or by releasing some resources.
- There are two main techniques to detect distributed deadlocks :
  - **Global wait-for graph**: This technique involves constructing a global graph that represents the waiting relationships among processes and resources in the system, and then checking for cycles in the graph. A cycle indicates a deadlock. The global graph can be constructed from local graphs at each node, or by a centralized coordinator that collects information from all nodes.
  - **Edge chasing**: This technique involves sending probe messages along the edges of the local wait-for graphs, and detecting cycles when a probe message returns to its originator. This technique is also known as the Chandy-Misra-Haas algorithm or the path-pushing algorithm.