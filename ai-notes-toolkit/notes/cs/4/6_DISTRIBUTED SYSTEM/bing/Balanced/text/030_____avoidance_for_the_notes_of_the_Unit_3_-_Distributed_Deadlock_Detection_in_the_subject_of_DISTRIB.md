### Avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- Deadlock avoidance is a technique that prevents a system from entering a deadlock state by ensuring that the system is always in a safe state.
- A safe state is a state where there exists a sequence of resource allocations that can satisfy the requests of all processes without causing a deadlock.
- In a distributed system, deadlock avoidance is impractical due to several problems, such as:
  - The lack of global information about the resource allocation and requests of all processes.
  - The dynamic and unpredictable nature of the processes and resources in a distributed system.
  - The high communication and synchronization overhead involved in maintaining a global safe state.
- Therefore, deadlock detection is preferred over deadlock avoidance in distributed systems.
- Deadlock detection is a technique that identifies the existence of a deadlock in a system after it has occurred and takes appropriate actions to recover from it.
- Deadlock detection in distributed systems requires the following steps:
  - Collecting local information about the resource allocation and requests of each process and sending it to a coordinator or a set of coordinators.
  - Constructing a global wait-for graph that represents the dependencies among the processes and resources in the system.
  - Detecting a cycle in the global wait-for graph, which indicates a deadlock.
  - Initiating a recovery procedure to break the cycle and resolve the deadlock.