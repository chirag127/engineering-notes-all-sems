# Deadlock Prevention for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process. In a distributed system, deadlocks can occur across multiple nodes and resources, making them harder to detect and resolve.

Deadlock prevention is a technique to avoid the occurrence of deadlocks by imposing some constraints on how processes can request and acquire resources. There are two main methods of deadlock prevention in a distributed system:

- Ordered request: In this method, each resource type is assigned a certain level to maintain a resource request policy for a process. This is known as the resource allocation policy. A process can request resources only in an increasing order of levels. For example, if a process needs resources A, B, and C, and their levels are 1, 2, and 3 respectively, then the process must request A first, then B, and then C. This prevents circular wait condition, which is one of the necessary conditions for deadlock.

- Collective request: In this method, a process must request all the resources it needs at the same time before starting execution. This is known as the atomic allocation policy. A process can either get all the resources it needs or none of them. This prevents hold and wait condition, which is another necessary condition for deadlock.

Both methods have some advantages and disadvantages. Ordered request method allows more concurrency and flexibility, but it may cause resource starvation and waste. Collective request method avoids resource starvation and waste, but it may cause low resource utilization and long waiting time. Therefore, the choice of the method depends on the characteristics of the system and the application.