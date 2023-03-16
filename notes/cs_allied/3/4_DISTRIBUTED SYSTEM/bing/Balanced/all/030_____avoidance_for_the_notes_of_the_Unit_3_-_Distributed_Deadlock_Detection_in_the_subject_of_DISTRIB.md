# Avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- Avoidance is a technique to prevent deadlocks from occurring in a distributed system by ensuring that the system is always in a safe state.
- A safe state is a state where there is at least one sequence of resource allocation that does not lead to a deadlock.
- Avoidance requires the system to have some knowledge of the current and future resource requests and releases of each process.
- Avoidance is impractical in distributed systems due to several problems, such as:
  - The lack of global information and synchronization among processes and sites.
  - The uncertainty and unpredictability of resource requests and releases in a dynamic and heterogeneous environment.
  - The high overhead and complexity of maintaining and updating the global state of the system.
- Therefore, avoidance is rarely used in distributed systems, and deadlock detection is preferred as a more feasible and realistic approach.