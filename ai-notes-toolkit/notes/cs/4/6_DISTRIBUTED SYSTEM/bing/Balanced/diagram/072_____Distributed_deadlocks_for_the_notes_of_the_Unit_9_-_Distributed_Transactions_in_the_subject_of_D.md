### Distributed Deadlocks

- A distributed deadlock is a situation where a set of processes in a distributed system are waiting for each other to release resources or messages, and none of them can proceed .
- Distributed deadlocks are similar to deadlocks in centralized systems, but they are harder to detect, avoid, and prevent, because there is no single authority that can oversee resource allocation and monitor the state of the system.
- There are different types of distributed deadlocks, depending on the nature of the resources or messages involved:
  - Communication deadlocks: occur when processes are waiting for messages from each other that will never arrive.
  - Resource deadlocks: occur when processes are holding local resources and requesting remote resources that are held by other processes.
  - Hybrid deadlocks: occur when both communication and resource deadlocks are present in the system.
- There are different approaches to handle distributed deadlocks, such as :
  - Prevention: use a global ordering of resources or messages and ensure that processes request them in that order, avoiding circular waits.
  - Avoidance: use a global state information of the system and ensure that processes only request resources or messages that will not lead to unsafe states.
  - Detection: use a global or distributed algorithm to detect cycles in the wait-for graph of the system and resolve them by aborting or restarting some processes.
  - Ignorance: do not attempt to handle distributed deadlocks and rely on timeouts or user intervention to recover from them.