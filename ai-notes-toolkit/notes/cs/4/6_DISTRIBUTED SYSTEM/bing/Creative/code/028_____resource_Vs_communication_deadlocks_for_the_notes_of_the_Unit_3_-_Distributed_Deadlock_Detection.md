### Resource Vs Communication Deadlocks

- A deadlock is a condition where a process cannot proceed because it needs to obtain a resource held by another process, and it itself is holding a resource that the other process needs.
- There are two types of deadlocks in distributed systems: resource deadlocks and communication deadlocks .
- Resource deadlocks occur when processes access resources, such as data objects in database systems and buffers in store and forward communication networks .
  - A process acquires a resource before accessing it and releases it after using it .
  - A resource deadlock can be modeled by a wait-for graph, where nodes represent processes and edges represent resource requests .
  - A cycle in the wait-for graph indicates a deadlock .
- Communication deadlocks occur when processes exchange messages, such as in message passing systems and distributed algorithms .
  - A process sends a message to another process and waits for a reply before continuing .
  - A communication deadlock can be modeled by a dependency graph, where nodes represent processes and edges represent message dependencies .
  - A cycle in the dependency graph indicates a deadlock .
- The main difference between resource deadlocks and communication deadlocks is that resource deadlocks involve contention for resources, while communication deadlocks involve loss or corruption of signals .
  - Resource deadlocks can be prevented by using resource allocation protocols, such as deadlock avoidance or deadlock detection and recovery .
  - Communication deadlocks can be prevented by using reliable communication protocols, such as timeouts, acknowledgments, or sequence numbers .