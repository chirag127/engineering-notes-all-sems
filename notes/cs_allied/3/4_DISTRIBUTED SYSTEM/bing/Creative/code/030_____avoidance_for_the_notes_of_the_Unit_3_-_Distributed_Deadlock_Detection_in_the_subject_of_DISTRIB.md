### Avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- Deadlock avoidance is a technique that prevents the occurrence of deadlocks by ensuring that the system is always in a safe state.
- A safe state is a state where there exists a safe sequence of processes that can finish their execution without causing a deadlock.
- In a distributed system, deadlock avoidance is impractical because of the following reasons :
  - The system is dynamic and unpredictable, making it hard to know the current and future resource requests and releases of each process.
  - The system is decentralized and autonomous, making it hard to coordinate and synchronize the resource allocation decisions of each site.
  - The system is heterogeneous and complex, making it hard to define and enforce a global ordering of resources and processes.
- Therefore, deadlock detection is preferred over deadlock avoidance in distributed systems. Deadlock detection involves finding and resolving the existing deadlocks in the system.
- Deadlock detection in distributed systems can be classified into four categories :
  - Path-pushing algorithms: These algorithms propagate the information about the wait-for relations along the dependency paths in the system. A deadlock is detected when a cycle is formed in the wait-for graph.
  - Edge-chasing algorithms: These algorithms send probe messages along the dependency paths in the system. A deadlock is detected when a probe message returns to its originator.
  - Diffusion computation algorithms: These algorithms initiate a distributed computation at each site that detects a potential deadlock. A deadlock is confirmed when all the sites involved in the computation agree on the existence of a cycle.
  - Global state detection algorithms: These algorithms collect the local state information of each site and construct a global state of the system. A deadlock is detected when the global state contains a cycle in the wait-for graph.