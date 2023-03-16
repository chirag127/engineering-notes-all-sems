# Deadlock Prevention for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process. Deadlocks can occur in distributed systems, where processes and resources are located on different machines connected by a network.

Deadlock prevention is a technique to avoid the occurrence of deadlocks by imposing some constraints on the resource allocation policies. There are two main methods of deadlock prevention in distributed systems:

- Ordered request: In this method, each resource type is assigned a certain level to maintain a resource request policy for a process. This is known as the resource allocation policy. A process can request resources only in an increasing order of levels. For example, if a process needs resources of type A, B, and C, and their levels are 1, 2, and 3 respectively, then the process must request A before B, and B before C. This prevents circular wait condition, which is one of the necessary conditions for deadlock.

- Collective request: In this method, a process must request all the resources it needs at the same time, before starting its execution. This is known as the atomic allocation policy. A process can either get all the resources it needs or none of them. This prevents hold and wait condition, which is another necessary condition for deadlock.

Both methods have some advantages and disadvantages. Ordered request method allows more concurrency and flexibility, but it may cause starvation and waste of resources. Collective request method avoids starvation and waste of resources, but it may cause blocking and reduced concurrency .

Some of the challenges and issues in implementing deadlock prevention in distributed systems are:

- How to assign levels to resources in a consistent and global way
- How to handle dynamic addition and deletion of resources and processes
- How to deal with communication delays and failures
- How to balance the trade-off between concurrency and deadlock prevention .