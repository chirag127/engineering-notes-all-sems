### Avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- Deadlock avoidance is a technique that prevents the occurrence of deadlocks by ensuring that the system is always in a safe state.
- A safe state is one where there exists a sequence of processes that can finish their execution without causing a deadlock.
- In a distributed system, deadlock avoidance is impractical due to several problems, such as:
  - Lack of global information about the resource allocation and requests of all processes.
  - High communication and synchronization overhead for maintaining and updating the global state.
  - Dynamic and unpredictable nature of the distributed system, where processes and resources may join or leave at any time.
- Therefore, deadlock detection is preferred over deadlock avoidance in distributed systems, as it allows more concurrency and flexibility.
- Deadlock detection involves examining the status of the process-resource interactions for the presence of cyclic wait, which indicates a deadlock.
- Deadlock detection in distributed systems can be classified into four categories, based on the type of information and algorithm used:
  - Path-pushing: Each process maintains a wait-for graph that represents the dependencies among processes, and periodically sends it to a coordinator node. The coordinator node merges the graphs and checks for cycles.
  - Edge-chasing: Each process sends a probe message to the process it is waiting for, and the message is forwarded along the dependency chain until it reaches a deadlocked process or returns to the sender. A cycle in the probe messages indicates a deadlock.
  - Diffusion computation: Each process initiates a computation to detect a deadlock involving itself, and propagates the computation to its neighbors. The computation terminates when all processes involved in the deadlock are identified or when no deadlock exists.
  - Global state detection: Each process periodically records its local state and sends it to a coordinator node. The coordinator node constructs a global state of the system and checks for deadlocks using a global wait-for graph or a global resource allocation graph.