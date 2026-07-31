### Deadlock Prevention for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process. In a distributed system, deadlocks are more difficult to detect and resolve than in a centralized system, because there is no global information or control.

Deadlock prevention is a technique that aims to ensure that at least one of the four necessary conditions for deadlock (mutual exclusion, hold and wait, no preemption, and circular wait) does not hold. There are two main methods of deadlock prevention in a distributed system:

- Ordered request: This method assigns a unique level to each resource type and requires that a process requests resources in increasing order of levels. This prevents circular wait, as there is a global ordering of resources.
- Collective request: This method requires that a process requests all the resources it needs at once, before starting its execution. This prevents hold and wait, as a process does not hold any resources while waiting for others.

Both methods have some drawbacks, such as reduced concurrency, increased overhead, and wasted resources. Therefore, deadlock prevention is not always feasible or desirable in a distributed system. Alternatively, deadlock detection and recovery can be used to deal with deadlocks after they occur.