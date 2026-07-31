### Deadlock Prevention for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process. Deadlocks can occur in distributed systems, where processes and resources are located on different machines connected by a network.

Deadlock prevention is a technique to avoid the occurrence of deadlocks by imposing some constraints on the resource allocation policies. There are two main methods of deadlock prevention in distributed systems:

- Ordered request: In this method, each resource type is assigned a unique level, and a process can request a resource only if its level is lower than the level of the resource it currently holds. This ensures that there is a global ordering of resource requests, and no circular wait can occur. For example, if there are three resource types A, B, and C, with levels 1, 2, and 3 respectively, then a process can request A only if it does not hold any resource, B only if it holds A, and C only if it holds B. This method is simple and easy to implement, but it may result in low resource utilization and reduced concurrency. 

- Collective request: In this method, a process must request all the resources it needs at the same time, and either get them all or none. This ensures that there is no hold and wait condition, and no process can block another process by holding a resource. For example, if a process needs resources A and B, it must request them together, and not request A first and then B. This method is more flexible and efficient than ordered request, but it may result in deadlock if there are not enough resources available to satisfy a request. 

Both methods of deadlock prevention require global knowledge of the resource allocation state and the resource request patterns of the processes, which may be difficult or costly to obtain in a distributed system. Therefore, deadlock prevention may not be suitable for all distributed systems, and other techniques such as deadlock detection and avoidance may be preferred.   

: https://www.geeksforgeeks.org/deadlock-prevention-policies-in-distributed-system/
: https://www.javatpoint.com/deadlock-detection-in-distributed-systems
: https://www.tutorialspoint.com/distributed_dbms/distributed_dbms_deadlock_handling.htm
: https://www.cse.scu.edu/~m1wang/projects/DeadLock_prevention_14s.pdf