### Unit 3 - Distributed Deadlock Detection

#### Detection & Resolution

- **Distributed Deadlock Detection**: In a distributed system, a deadlock can occur when two or more processes are waiting for resources held by each other. Detecting deadlocks in a distributed system is more complex than in a centralized system due to the lack of global information about the state of the system.

- **Detection Algorithms**: There are several algorithms for detecting deadlocks in distributed systems, including the Chandy-Misra-Haas algorithm, the Path Pushing algorithm, and the Edge Chasing algorithm. These algorithms use different techniques to detect cycles in the resource allocation graph, which indicate the presence of a deadlock.

- **Resolution**: Once a deadlock is detected, it must be resolved to allow the system to continue functioning. Common methods for resolving deadlocks include preemption, rollback, and killing one or more of the deadlocked processes. The choice of resolution method depends on the specific requirements of the system and the nature of the deadlock.

- **Prevention**: In addition to detection and resolution, it is also possible to prevent deadlocks from occurring in the first place. This can be achieved through careful resource allocation and the use of techniques such as timeouts and deadlock avoidance algorithms.