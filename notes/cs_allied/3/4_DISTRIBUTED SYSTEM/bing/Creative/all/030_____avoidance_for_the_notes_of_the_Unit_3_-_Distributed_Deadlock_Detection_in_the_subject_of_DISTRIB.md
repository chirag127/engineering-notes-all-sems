# Avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- Avoidance is a technique to prevent deadlocks from occurring in a distributed system by ensuring that the system is always in a safe state.
- A safe state is a state where there is at least one sequence of resource allocation that does not lead to a deadlock.
- Avoidance requires the system to have some knowledge of the current and future resource requests and releases of each process.
- Avoidance can be implemented by using either a centralized or a decentralized approach.
- In a centralized approach, there is a single coordinator that maintains the global state of the system and decides whether to grant or deny a resource request based on a safety algorithm.
- In a decentralized approach, each site maintains its own local state and communicates with other sites to exchange information and reach a consensus on resource allocation.
- Some of the advantages of avoidance are:
  - It does not require the detection and recovery of deadlocks, which can be costly and complex.
  - It can reduce the resource utilization and the waiting time of processes by avoiding unnecessary blocking.
  - It can improve the performance and reliability of the system by avoiding deadlock situations.
- Some of the disadvantages of avoidance are:
  - It requires the system to have accurate and complete information about the resource requests and releases of each process, which may not be feasible or realistic in a distributed system.
  - It may impose a high overhead on the system due to the communication and computation involved in the safety algorithm.
  - It may be too conservative and deny some resource requests that would not actually cause a deadlock, thus reducing the concurrency and throughput of the system.