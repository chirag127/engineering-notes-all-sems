### Deadlock Prevention for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

- A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
- Deadlock prevention is a technique to ensure that at least one of the necessary conditions for deadlock does not hold in a system.
- In a distributed system, deadlock prevention is more challenging than in a centralized system, because the processes and resources are distributed across multiple nodes, and there is no global information or control.
- There are two main approaches to deadlock prevention in a distributed system: ordered request and collective request.

#### Ordered Request
- In this approach, each resource type is assigned a unique level, and a process can request resources only in increasing order of levels.
- This ensures that no circular wait can occur, as a process cannot request a resource that is already held by a lower-level resource.
- For example, if there are three resource types A, B, and C, with levels 1, 2, and 3 respectively, a process can request A, then B, then C, but not C, then A, then B.
- This approach requires a global agreement on the resource levels, and may impose unnecessary restrictions on the resource requests.

#### Collective Request
- In this approach, a process must request all the resources it needs at once, before starting its execution.
- This ensures that no hold and wait can occur, as a process cannot hold a resource while waiting for another resource.
- For example, if a process needs resources A, B, and C, it must request them all together, and not request A, then B, then C.
- This approach requires a global knowledge of the resource needs, and may cause underutilization of resources.