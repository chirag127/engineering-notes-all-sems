### Deadlock Prevention for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of Distributed System

A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process. In a distributed system, deadlocks are more difficult to detect and resolve because the processes and resources may be physically dispersed across multiple nodes.

Deadlock prevention is a technique to avoid the occurrence of deadlocks by ensuring that at least one of the four necessary conditions for deadlock (mutual exclusion, hold and wait, no preemption, and circular wait) is never met. There are two main methods of deadlock prevention in a distributed system:

- Ordered request: In this method, each resource type is assigned a unique number or level, and a process can request resources only in an increasing order of levels. This prevents circular wait condition, as there is a total ordering of resources.
- Collective request: In this method, a process must request all the resources it needs in one single message, and wait for the grant of all of them before proceeding. This prevents hold and wait condition, as a process does not hold any resource while waiting for another.

Both methods have some drawbacks, such as reduced concurrency, increased overhead, and wasted resources. Therefore, deadlock prevention is not always feasible or desirable in a distributed system. Alternatively, deadlock detection and recovery can be used to deal with deadlocks after they occur.