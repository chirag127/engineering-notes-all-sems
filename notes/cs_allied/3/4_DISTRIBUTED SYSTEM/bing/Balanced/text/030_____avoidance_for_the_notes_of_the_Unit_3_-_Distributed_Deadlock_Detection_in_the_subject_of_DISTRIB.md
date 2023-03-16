### Avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- Deadlock avoidance is a technique that prevents the occurrence of deadlocks by ensuring that the system is always in a safe state.
- A safe state is a state where there exists a safe sequence of processes that can finish their execution without causing a deadlock.
- In a distributed system, deadlock avoidance is impractical due to several problems, such as:
  - The lack of global information about the resource allocation and request of all processes in the system.
  - The dynamic and unpredictable nature of the system, where processes and resources may join or leave at any time.
  - The high communication and synchronization overhead involved in maintaining a global safe state.
- Therefore, deadlock detection is preferred over deadlock avoidance in distributed systems, as it allows more concurrency and flexibility in resource allocation and request.
- Deadlock detection is a technique that identifies the existence of a deadlock after it has occurred, and then takes some recovery actions to resolve it.
- Deadlock detection in distributed systems requires the following steps:
  - Collecting local information about the resource allocation and request of each process in the system.
  - Constructing a global wait-for graph that represents the dependency among processes and resources in the system.
  - Detecting a cycle in the wait-for graph, which indicates a deadlock condition.
  - Initiating a recovery procedure to break the cycle and release some resources.
- Deadlock detection algorithms in distributed systems can be classified into four categories, based on the way they construct and analyze the wait-for graph:
  - Path-pushing algorithms, which propagate the dependency information along the paths of the wait-for graph.
  - Edge-chasing algorithms, which send probe messages along the edges of the wait-for graph to detect cycles.
  - Diffusion computation algorithms, which perform a distributed computation to determine the deadlock status of each process.
  - Global state detection algorithms, which collect and examine the global state of the system to detect cycles.