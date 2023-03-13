### Deadlock prevention for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process. Deadlock is a common problem in distributed systems, where processes may compete for resources located in different nodes.

Deadlock prevention is a technique to ensure that at least one of the four necessary conditions for deadlock (mutual exclusion, hold and wait, no preemption, and circular wait) does not hold. There are two main methods of deadlock prevention in distributed systems: ordered request and collective request.

- Ordered request: In this method, each resource type is assigned a certain level to maintain a resource request policy for a process. This is known as the resource allocation policy. A process can request resources only in an increasing order of levels. This prevents circular wait condition, as there is a global ordering of resources. For example, if there are three resource types A, B, and C with levels 1, 2, and 3 respectively, a process can request A, then B, then C, but not C, then A, then B. This method is simple and easy to implement, but it may cause low resource utilization and starvation.

- Collective request: In this method, a process must request all the resources it needs at once, before starting its execution. This prevents hold and wait condition, as a process does not hold any resource while waiting for others. For example, if a process needs resources A, B, and C, it must request them all together, and not request A, then wait for B, then wait for C. This method is more flexible and efficient than ordered request, but it may cause high overhead and deadlock due to communication failures.

Some advantages of deadlock prevention in distributed systems are:

- It avoids the need for deadlock detection and recovery, which can be costly and complex in distributed systems.
- It ensures that processes can proceed without waiting indefinitely for resources.
- It reduces the chances of system failures due to deadlock.

Some disadvantages of deadlock prevention in distributed systems are:

- It may impose restrictions on the resource allocation and request policies, which can limit the concurrency and performance of the system.
- It may cause wastage of resources, as some resources may remain unused or underutilized.
- It may not be feasible or practical to implement in some scenarios, such as when the resource types or levels are not known in advance, or when the resource requests are dynamic or unpredictable.