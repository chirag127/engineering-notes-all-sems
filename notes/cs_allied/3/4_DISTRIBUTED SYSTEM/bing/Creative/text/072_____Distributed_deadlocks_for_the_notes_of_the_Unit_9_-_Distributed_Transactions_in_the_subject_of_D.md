### Distributed Deadlocks

- A distributed deadlock is a situation where a set of processes in a distributed system are waiting for each other to release resources or messages, and none of them can proceed  .
- Distributed deadlocks can occur when distributed transactions or concurrency control are utilized in distributed systems .
- Distributed deadlocks are harder to detect, avoid, and prevent than deadlocks in centralized systems, because there is no single authority that can oversee resource allocation and monitor the state of the system.
- There are three main approaches to handle distributed deadlocks :
  - Prevention: This approach tries to prevent deadlocks from occurring by imposing some constraints on resource allocation, such as ordering the resources, granting requests only if they do not create cycles, or using timeouts.
  - Avoidance: This approach tries to avoid deadlocks by making dynamic decisions based on the current state of the system, such as using the banker's algorithm or the wait-die and wound-wait schemes.
  - Detection and resolution: This approach tries to detect deadlocks after they occur and then resolve them by aborting or restarting some of the processes involved in the deadlock.
- There are two main techniques for deadlock detection in distributed systems:
  - Global wait-for graph: This technique involves constructing a global wait-for graph (WFG) from local wait-for graphs at a deadlock detector, and then checking for cycles in the WFG. A WFG is a directed graph that represents the waiting relationships among processes and resources. A cycle in the WFG indicates a deadlock  .
  - Edge chasing: This technique involves sending probe messages along the edges of the local wait-for graphs, and then detecting cycles in the probe messages. A probe message contains the identity of the sender and the receiver, and the path of the message. A cycle in the probe messages indicates a deadlock .
- There are different types of distributed deadlocks, depending on the nature of the resources and the communication model:
  - Communication deadlocks: These are deadlocks that occur due to message passing among processes, where a process is waiting for a message from another process that is also waiting for a message from the first process or from a third process that is part of the cycle.
  - Resource deadlocks: These are deadlocks that occur due to shared resources among processes, where a process is waiting for a resource that is held by another process that is also waiting for a resource from the first process or from a third process that is part of the cycle.
  - Hybrid deadlocks: These are deadlocks that involve both communication and resource dependencies among processes.