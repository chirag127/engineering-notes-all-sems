### Avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- Deadlock avoidance is a technique that prevents the occurrence of deadlocks by ensuring that the system is always in a safe state.
- A safe state is a state where there exists a sequence of resource allocations that can satisfy the requests of all processes without causing a deadlock.
- In a distributed system, deadlock avoidance is impractical because of the following problems:
  - The system is dynamic and unpredictable, as processes may join or leave, and resources may be added or removed at any time.
  - The system is decentralized and lacks global information, as processes may not know the status of other processes or resources in the system.
  - The system is heterogeneous and diverse, as processes may have different characteristics, requirements, and preferences for resources.
- Therefore, deadlock detection is preferred over deadlock avoidance in distributed systems, as it allows more concurrency and flexibility in resource allocation.
- Deadlock detection is a technique that identifies the existence of deadlocks by examining the state of the system periodically or on demand.
- Deadlock detection in distributed systems can be classified into four categories, based on the type of information and communication used:
  - Path-pushing algorithms: These algorithms propagate the information about the wait-for relations along the paths of the resource allocation graph, and detect cycles in the graph.
  - Edge-chasing algorithms: These algorithms send probe messages along the edges of the resource allocation graph, and detect cycles in the graph.
  - Diffusion computation algorithms: These algorithms initiate a computation at each node of the resource allocation graph, and collect the results of the computation to detect cycles in the graph.
  - Global state detection algorithms: These algorithms collect the global state of the system using snapshots or timestamps, and analyze the state to detect cycles in the graph.