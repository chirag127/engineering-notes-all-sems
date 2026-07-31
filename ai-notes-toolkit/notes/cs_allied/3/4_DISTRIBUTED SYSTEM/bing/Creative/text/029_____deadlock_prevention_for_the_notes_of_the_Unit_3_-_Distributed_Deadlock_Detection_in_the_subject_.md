### Deadlock Prevention for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

- A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
- Deadlock prevention is a technique to ensure that at least one of the necessary conditions for deadlock does not hold in a system.
- In a distributed system, deadlock prevention is more challenging than in a centralized system, because the processes and resources may be located in different nodes and there is no global information or control.
- There are two main approaches to deadlock prevention in a distributed system: ordered request and collective request.
- Ordered request: In this approach, each resource type is assigned a unique level and each process must request resources in increasing order of levels. This prevents circular wait condition and hence deadlock.
- Collective request: In this approach, each process must request all the resources it needs at once, before starting its execution. This prevents hold and wait condition and hence deadlock.
- Both approaches have some drawbacks, such as reduced concurrency, increased overhead, and wasted resources.
- Therefore, deadlock prevention is not widely used in distributed systems, and deadlock detection and recovery are preferred.