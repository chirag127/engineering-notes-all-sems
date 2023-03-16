### Deadlock Prevention for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

- A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
- A distributed deadlock is a deadlock that involves processes and resources located on different machines connected by a network.
- Deadlock prevention is a technique to ensure that at least one of the necessary conditions for deadlock does not hold in a system.
- There are two main ways to prevent deadlock in a distributed system: ordered request and collective request.
- Ordered request is a method where each resource type is assigned a certain level and a process can only request resources in increasing order of levels. This prevents circular wait condition.
- Collective request is a method where a process must request all the resources it needs at the same time before starting execution. This prevents hold and wait condition.
- Both methods have some drawbacks, such as reduced concurrency, increased overhead, and increased complexity.