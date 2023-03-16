### Deadlock Prevention for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process. In a distributed system, deadlocks are more difficult to detect and resolve because the processes and resources may be physically dispersed across different nodes.

Deadlock prevention is a technique to ensure that at least one of the necessary conditions for deadlock does not hold in the system. There are two main methods of deadlock prevention in a distributed system:

- Ordered request: In this method, each resource type is assigned a unique level, and a process can request resources only in increasing order of levels. This prevents circular wait condition, as no process can hold a resource of higher level and wait for a resource of lower level. For example, if there are three resource types A, B, and C with levels 1, 2, and 3 respectively, then a process can request A, then B, then C, but not C, then A, then B.
- Collective request: In this method, a process must request all the resources it needs at the same time, and either get all of them or none of them. This prevents hold and wait condition, as no process can hold some resources and wait for others. For example, if a process needs resources A, B, and C, then it must request them together, and not request A, then wait for B, then request C.

Both methods have some drawbacks, such as reduced concurrency, increased overhead, and wasted resources. Therefore, deadlock prevention may not be suitable for all distributed systems, and other techniques such as deadlock avoidance or deadlock detection and recovery may be preferred.