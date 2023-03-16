### Deadlock Prevention for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process. In a distributed system, deadlocks can occur across multiple nodes and resources, making them harder to detect and resolve.

Deadlock prevention is a technique that aims to avoid the occurrence of deadlocks by imposing some constraints on how processes can request and acquire resources. There are two main methods of deadlock prevention in distributed systems:

- Ordered request: This method assigns a unique level to each resource type and requires that a process requests resources in increasing order of levels. This prevents circular wait, one of the necessary conditions for deadlock. For example, if there are three resource types A, B, and C with levels 1, 2, and 3 respectively, a process can request A, then B, then C, but not C, then A, then B. 
- Collective request: This method requires that a process requests all the resources it needs at once, before starting its execution. This prevents hold and wait, another necessary condition for deadlock. For example, if a process needs resources A, B, and C, it must request them all together, rather than requesting A, then B, then C.  

Both methods have some drawbacks, such as reducing concurrency, increasing overhead, and requiring prior knowledge of resource requirements. Therefore, deadlock prevention may not be suitable for all distributed systems and applications.