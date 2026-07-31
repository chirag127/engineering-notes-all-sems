### System Model for Distributed Deadlock Detection

Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

1. A distributed system consists of a collection of autonomous processes that are interconnected by a computer network.
2. Each process has its own local resources and can request resources from other processes in the system.
3. A deadlock occurs when a set of processes are blocked, waiting for resources held by other processes in the set.
4. Distributed deadlock detection algorithms aim to detect deadlocks in a distributed system and resolve them by aborting one or more processes or by preempting resources.
5. There are several approaches to distributed deadlock detection, including centralized, hierarchical, and distributed algorithms.
6. The choice of algorithm depends on factors such as the size and topology of the system, the frequency of resource requests, and the desired level of fault tolerance.
7. In a centralized approach, a single process is responsible for deadlock detection and resolution.
8. In a hierarchical approach, the system is divided into clusters, with each cluster having a coordinator responsible for deadlock detection within the cluster.
9. In a distributed approach, each process participates in deadlock detection and resolution.
10. Distributed deadlock detection algorithms can be further classified into path-pushing, edge-chasing, and diffusing computation algorithms.
