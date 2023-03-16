# Avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

- Avoidance is a technique to prevent deadlocks from occurring in a distributed system by ensuring that the system is always in a safe state.
- A safe state is a state where there is at least one sequence of resource allocation that does not lead to a deadlock.
- Avoidance requires the system to have some knowledge of the current and future resource requests and releases of each process.
- Avoidance can be implemented by using either a centralized or a decentralized approach.
- In the centralized approach, there is a single coordinator that maintains the global state of the system and decides whether to grant or deny a resource request based on the safe state criterion.
- In the decentralized approach, there is no coordinator and each process maintains its own local state and communicates with other processes to determine the safe state of the system.
- Some of the advantages of avoidance are:
  - It does not require the detection and recovery of deadlocks, which can be costly and complex.
  - It does not impose any restrictions on the resource requests and releases of the processes, unlike prevention.
  - It can achieve a higher degree of resource utilization and system throughput than prevention.
- Some of the disadvantages of avoidance are:
  - It requires the system to have accurate and complete information about the current and future resource demands of the processes, which may not be feasible or realistic in a distributed system.
  - It may incur a high overhead of maintaining and exchanging the state information among the processes or the coordinator.
  - It may result in a conservative resource allocation policy that may deny some requests that are actually safe, leading to a loss of concurrency and performance.