### Distributed Deadlocks

- A distributed deadlock is a situation where a set of processes in a distributed system are waiting for each other to release resources or messages, and none of them can proceed.
- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems .
- Distributed deadlocks are harder to detect, avoid, and prevent than deadlocks in centralized systems, because there is no single authority that can oversee resource allocation and dependency graphs.
- There are three main approaches to handle distributed deadlocks :
  - Prevention: This approach tries to ensure that deadlocks never occur by imposing some constraints on resource allocation, such as ordering, preemption, or timeouts.
  - Avoidance: This approach tries to avoid deadlocks by dynamically analyzing the resource requests and granting them only if they do not lead to a potential deadlock, such as using the Banker's algorithm or timestamps.
  - Detection and recovery: This approach tries to detect deadlocks after they occur and then recover from them by aborting or restarting some processes, or by breaking cycles in the dependency graph.
- There are two main techniques to detect distributed deadlocks :
  - Global wait-for graph: This technique involves constructing a global graph of processes and resources from local graphs at each node, and then finding cycles in the global graph. This technique requires a centralized or distributed coordinator that can collect and analyze the local graphs.
  - Edge chasing: This technique involves sending probe messages along the edges of the local wait-for graphs, and detecting cycles when a probe returns to its originator. This technique does not require a coordinator, but it may generate a lot of messages and false positives.