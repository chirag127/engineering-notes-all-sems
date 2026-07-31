### Avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- Deadlock avoidance is a technique that prevents the occurrence of deadlocks by ensuring that the system is always in a safe state.
- A safe state is a state where there exists a safe sequence of processes that can finish their execution without causing a deadlock.
- In a distributed system, deadlock avoidance is impractical due to several problems, such as:
  - The lack of global information about the resource allocation and requests of all processes.
  - The dynamic and unpredictable nature of the system, where processes and resources may join or leave at any time.
  - The high communication and synchronization overhead involved in maintaining a global safe state.
- Therefore, deadlock detection is preferred over deadlock avoidance in distributed systems, as it allows more concurrency and flexibility in resource allocation.
- Deadlock detection is a technique that identifies the existence of a deadlock after it has occurred, and then takes some recovery actions to resolve it.
- Deadlock detection in distributed systems can be classified into four classes, based on the type of information and algorithm used:
  - Path-pushing: This class of algorithms propagates the information about the wait-for relations along the paths of the wait-for graph, until a cycle is detected or the information reaches a designated coordinator.
  - Edge-chasing: This class of algorithms sends probe messages along the edges of the wait-for graph, until a cycle is detected or the probe returns to the sender.
  - Diffusion computation: This class of algorithms initiates a distributed computation at each node of the wait-for graph, where each node exchanges information with its neighbors and decides whether it is part of a deadlock or not.
  - Global state detection: This class of algorithms collects the global state of the system using techniques such as snapshot algorithms or vector clocks, and then analyzes the global state for the presence of a deadlock.